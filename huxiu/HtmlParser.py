#coding:utf-8

import os
from pyquery import PyQuery as pq
from lxml import etree
import pickle
import SqlHelper
import re


class Html_Parser(object):

    def parse_list(self,response):
        '''
        获取私募基金公示信息
        '''
        d = pq(response)

        L = []

        for box in d(".cy-cp-box").items():
            dic = {}
            img = box(".cy-cp-img a img").attr("src")
            name = box(".cy-cp-name").text()
            info = box('.cy-cp-info').text()
            url = box(".cy-cp-name").parent('a').attr('href')
            m = re.match(r'/chuangye/product/(\d+)/.*?', url)
            id = m.group(1)
            dic['title']=name
            dic['imgUrl']=img
            dic['href'] = url
            dic['intro'] = info
            dic['id']=id

            cols = ['industry','city','step']
            for i, item in enumerate(box(".cy-cp-tag ul").children().items()):
                dic[cols[i]]=item.text().split('：')[1]

            L.append(dic)

        return L

    def parse_detail(self):
        f = open('detail', 'rb')
        cont = pickle.load(f)
        f.close()
        d = pq(cont)

        # 处理公司信息
        # companys = []
        # for item in d(".box-moder ul").children('li').items():
        #     result = item.text()
        #     dic = {}
        #     print(result)
        #     if result.find('创始人')> -1:
        #         print(result.split('：')[1])
        #         dic['initiator']=result.split('：')[1]
        #     if result.find('网址')> -1:
        #         print(result.split('：')[1])
        #         dic['companyUrl']=result.split('：')[1]
        #     if result.find('融资')> -1:
        #         print(result.split('：')[1])
        #         dic['step']=result.split('：')[1]
        #     if result.find('地址')> -1:
        #         print(result.split('：')[1])
        #         dic['address']=result.split('：')[1]
        #     if result.find('员工')> -1:
        #         print(result.split('：')[1])
        #         dic['employeeCount']=result.split('：')[1]
        #     if result.find('公司')> -1:
        #         print(result.split('：')[1])
        #         dic['companyName']=result.split('：')[1]
        #     if result.find('法定代表')> -1:
        #         print(result.split('：')[1])
        #         dic['legal']=result.split('：')[1]
        #     if result.find('公司类型')> -1:
        #         print(result.split('：')[1])
        #         dic['companyType']=result.split('：')[1]
        #     if result.find('成立时间')> -1:
        #         print(result.split('：')[1])
        #         dic['establishDate']=result.split('：')[1]

        #     if result.find('注册资本')> -1:
        #         print(result.split('：')[1])
        #         dic['regCapital']=result.split('：')[1]
        #     if result.find('注册时间')> -1:
        #         print(result.split('：')[1])
        #         dic['regDate']=result.split('：')[1]
        #     if result.find('当前股东人数')> -1:
        #         print(result.split('：')[1])
        #         dic['stockholderCount']=result.split('：')[1]
        #     if result.find('办公地点')> -1:
        #         print(result.split(':')[1])
        #         dic['officeAddress']=result.split('：')[1]
        #     if result.find('联系电话')> -1:
        #         print(result.split('：')[1])
        #         dic['phone']=result.split('：')[1]
        #     if result.find('电子邮箱')> -1:
        #         print(result.split('：')[1])
        #         dic['email']=result.split('：')[1]
        #     companys.append(dic)

        product = {}
        imgs = []
        type = 1
        for x in d(".cy-cp-nav ul").children().items():
            if x.text().find('经营范围')>-1:
                type = 2
                break

        product['logo'] = d(".cy-icon-box img").attr("src")
        product['cpName'] = d(".cy-cp-name").text()
        for item in d(".gallery-img-box").children().items():
            imgs.append(item.find('img').attr("src"))
        print(imgs)

        if type == 2 :
            product['publishDate'] = d(".cy-xq-time").text().split('：')[1]
            product['cpIntroInfo'] = d(".cy-cp-intro-info").text()
            product['bizScope'] = d("#business").parent().find(".cy-cp-advantage").text()
            product['shareholders'] = d("#shareholders").parent().find(".cy-cp-advantage").text()
            product['type'] = 2
            # product['changeRecord'] = d("#change").parent().find(".cy-cp-advantage").html()

        if type == 1 :
            product['advantage'] = d("#advantage").parent().find(".cy-cp-advantage").text()
            product['results'] = d("#results").parent().find(".cy-cp-advantage").text()

        print(product)

    def parse(self):
        f = open('huxiu.txt', 'rb')
        cont = pickle.load(f)
        f.close()

        return self.parse_list(cont)

if __name__=='__main__':
    p = Html_Parser()
    # rows = p.parse()
    p.parse_detail()
