#coding:utf-8

import os
from pyquery import PyQuery as pq
from lxml import etree


class Html_Parser(object):


    def parseManager(self,href,response):
        '''
        获取基金介绍页
        '''

        d = pq(response)
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
        return L,resumes,situations,productA,productB


    def parseFund(self,href,response):
        '''
        获取私募基金公示信息
        '''
        d = pq(response)

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
        return L
