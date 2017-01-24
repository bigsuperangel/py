#coding:utf-8

import os
import json
import requests
import re
import datetime
import time
import random
from pyquery import PyQuery as pq
from lxml import etree
from Mysqldb import MysqlDb
from SqlHelper import SqlHelper
import multiprocessing

class AmacCraw(object):
    def __init__(self):
        self.list_url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/manager'
        self.fund_url = 'http://gs.amac.org.cn/amac-infodisc/res/pof/fund/'
        self.manager_url = 'http://gs.amac.org.cn/amac-infodisc/res/pof/manager/'
        self.mysqlDb = MysqlDb()

    def urls(self,p):
        '''
        获取列表页json
        '''

        user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        values = {
        'rand' : 0.9533140078801254,
        'page' : p,
        'size' : 50
        }
        headers = { 'User-Agent' : user_agent ,'content-type':'application/json'}
        payload = {'registerProvince': '福建省'}
        r = requests.post(self.list_url,headers=headers,params=values,json=payload)
        print(r.status_code)
        return r.json()

    def managerUrl(self,href):
        '''
        获取基金介绍页
        '''
        headers = {'Host':'gs.amac.org.cn','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','Connection':'keep-alive','Accept-Language':'zh-CN,zh;q=0.8'}
        d = pq(url=os.path.join(self.manager_url,href),encoding="utf-8",headers=headers)
        L = []

        pid = os.path.splitext(href)[0]
        L.append(pid)

        #### 诚信信息
        cflag = False
        for i in d('td.td-title').items():
            if i.text() == '机构诚信信息:':
                cflag = True
                result = i.next().find('td').text()
                L.append(result)
        if not cflag:
            L.append('')

        # ### 基本资料
        for i in d('td.td-title').items():
            if i.text() == '基金管理人全称(中文):':
                complaint = i.next().find('div#complaint1').text()
                L.append(''.join(complaint.replace('&nbsp','').split(' ')))
            if i.text() == '基金管理人全称(英文):':
                L.append(i.next().text())
            if i.text() == '组织机构代码:':
                L.append(i.next().text())
            if i.text() == '注册资本(万元)(人民币):':
                L.append(i.next().text())
            if i.text() == '实缴资本(万元)(人民币):':
                L.append(i.next().text())
            if i.text() == '企业性质:':
                L.append(i.next().text())
            if i.text() == '注册资本实缴比例:':
                L.append(i.next().text())
            if i.text() == '管理基金主要类别:':
                L.append(i.next().text())
            if i.text() == '申请的其他业务类型:':
                L.append(i.next().text())
            if i.text() == '员工人数:':
                L.append(i.next().text())
            if i.text() == '机构网址:':
                L.append(i.next().text())


        # ### 法律意见
        for i in d('td.td-title').items():
            if i.text() == '法律意见书状态:':
                L.append(i.next().text())

        oflag = False
        for i in d('td.td-title').items():
            if i.text() == '律师事务所名称:':
                oflag = True
                L.append(i.next().text())
        if not oflag:
            L.append('')

        nflag = False
        for i in d('td.td-title').items():
            if i.text() == '律师姓名:':
                nflag = True
                L.append(i.next().text())
        if not nflag:
            L.append('')

        # ### 高管介绍
        for i in d('td.td-title').items():
            if i.text() == '法定代表人/执行事务合伙人(委派代表)姓名:':
                L.append(i.next().text())
            if i.text() == '是否有从业资格:':
                L.append(i.next().text())
            if i.text() == '资格取得方式:':
                L.append(i.next().text())
            if i.text() == '机构信息最后更新时间:':
                L.append(i.next().text())
            if i.text() == '特别提示信息:':
                L.append(i.next().text())

        ### 工作履历
        resumes = []
        for i in d('td.td-title').items():
            if i.text() == '法定代表人/执行事务合伙人(委派代表)工作履历:':
                resume = i.next().children('.table-center')('tbody tr')
                for my_div in resume.items():
                    item = []
                    item.append(''.join(my_div('td').eq(0).text().replace('\r\n','').split(' ')))
                    item.append(my_div('td').eq(1).text())
                    item.append(my_div('td').eq(2).text())
                    item.append(pid)
                    resumes.append(item)

        ####高管情况:
        situations = []
        for i in d('td.td-title').items():
            if i.text() == '高管情况:':
                situation = i.next().children('.table-center')('tbody tr')
                for my_div in situation.items():
                    item = []
                    item.append(''.join(my_div('td').eq(0).text().replace('\r\n','').split(' ')))
                    item.append(my_div('td').eq(1).text())
                    item.append(my_div('td').eq(2).text())
                    item.append(pid)
                    situations.append(item)

        productA = []
        productB = []
        for i in d('td.td-title').items():
            if i.text() == '暂行办法实施前成立的基金:':
                for pb in i.parent().find('a').items():
                    item = []
                    item.append(pb.text())
                    item.append(os.path.split(pb.attr('href'))[1])
                    item.append(pid)
                    item.append(1)
                    productA.append(item)
            if i.text() == '暂行办法实施后成立的基金:':
                for pb in i.parent().find('a').items():
                    item = []
                    item.append(pb.text())
                    item.append(os.path.split(pb.attr('href'))[1])
                    item.append(pid)
                    item.append(2)
                    productB.append(item)
        print(L)
        return L,resumes,situations,productA,productB

    def craw_one(self,url):
        L,resumes,situations,productA,productB = self.managerUrl(url)


        ## 存储基金介绍数据
        self.mysqlDb.insertTable(L)

        for rec in resumes:
            self.mysqlDb.insertResume(rec)
        for rec in situations:
            self.mysqlDb.insertSituation(rec)
        for rec in productA:
            self.mysqlDb.insertMP(rec)
        for rec in productB:
            self.mysqlDb.insertMP(rec)

        time.sleep(7+random.randint(1,5))

    def fundUrl(self,href):
        '''
        获取私募基金公示信息
        '''
        headers = {
            'Host':"gs.amac.org.cn",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive",
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:39.0) Gecko/20100101 Firefox/39.0"
        }

        # d = pq(url=os.path.join(self.fund_url,href),encoding="utf-8",headers=headers)
        proxies = {
          "http": "http://127.0.0.1:1080",
          "https": "http://127.0.0.1:1080",
        }

        r = requests.get(os.path.join(self.fund_url,href), timeout=5 ,headers=headers, proxies=proxies)
        r.encoding = 'utf-8'
        d = pq(r.content)

        L = []

        id = os.path.splitext(href)[0]
        L.append(id)

        for i in d('td.td-title').items():
            if i.text() == '基金名称:':
                L.append(i.next().text())
            if i.text() == '基金编号:':
                L.append(i.next().text())
            if i.text() == '成立时间:':
                L.append(i.next().text())
            if i.text() == '备案时间:':
                L.append(i.next().text())
            if i.text() == '基金备案阶段:':
                L.append(i.next().text())
            if i.text() == '基金类型:':
                L.append(i.next().text())
            if i.text() == '币种:':
                L.append(i.next().text())
            if i.text() == '基金管理人名称:':
                L.append(i.next().text())
                L.append(os.path.splitext(os.path.split(i.next().find('a').attr('href'))[1])[0])
            if i.text() == '管理类型:':
                L.append(i.next().text())
            if i.text() == '托管人名称:':
                L.append(i.next().text())
            if i.text() == '主要投资领域:':
                L.append(i.next().text())
            if i.text() == '运作状态:':
                L.append(i.next().text())
            if i.text() == '基金信息最后更新时间:':
                L.append(i.next().text())
            if i.text() == '基金协会特别提示（针对基金）:':
                L.append(i.next().text())
        print(L)
        return L


    def isExistManager(self,pid):
        result = self.mysqlDb.selectManager((pid,))
        print(result)
        return result

    def isExistMp(self,pid):
        result = self.mysqlDb.selectIsMp((pid,))
        return result

    def craw(self):
        sqlhelper = SqlHelper()
        record = sqlhelper.select(count=68)
        for r in record:

            print("请求%s"%r[0])
            result = self.isExistManager(r[0])  ####判断是否请求过
            if len(result)>0:
                continue
            else:
                self.craw_one(r[1])

    def crawFund(self,href,mid):
        print("产品请求%s"%href)
        fid = os.path.splitext(href)[0]
        result = self.mysqlDb.selectFund((fid,mid))
        if len(result) == 0 :
            data = self.fundUrl(href)
            self.mysqlDb.insertFund(data)
            time.sleep(15+random.randint(1,5))

    def crawFunds(self,data):
        print(data)
        records = self.findAllMp(data)
        try:
          for r in records :
            self.crawFund(r[1],r[2])
        except Exception as e:
          print('except:', e)

    def findAllMp(self,data):
        return self.mysqlDb.selectAllMP(data)


def run(cls_instance, data):
    return cls_instance.crawFunds(data)

if __name__=='__main__':

    craw = AmacCraw()
    craw.crawFunds((0,1000))
    # print('Parent process %s.' % os.getpid())
    # p = multiprocessing.Pool(multiprocessing.cpu_count())
    # p = Pool(4)

    # for i in range(3):
    #     # p.map(craw.crawFunds,[0,10])
    #     p.apply_async(run, (craw, i*100,100))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done.')

