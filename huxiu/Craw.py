# -*- coding: utf-8 -*-

import os
import random
from HtmlDownloader import Html_Downloader
import traceback
import pickle
from HtmlParser import Html_Parser
import SqlHelper
import time
import datetime
from requests.utils import quote

class Craw(object):
    def __init__(self):
        self.downloader = Html_Downloader()
        self.parser = Html_Parser()

    def craw_list(self):
        try:
            for i in range(1,5):
                params = {
                    'is_ajax':1,
                    'huxiu_hash_code':'d212535ab8661f8533d724fe76db9554',
                    'city':13,
                    'page':i
                }
                ret = self.downloader.download(params)
                if ret['result'] ==1 :
                    f = open('huxiu%s.txt'%i, 'wb')
                    pickle.dump(ret['data'], f)
                    f.close()
                    rows = self.parser.parse_list(ret['data'])
                    SqlHelper.batchSavePro(rows)

                time.sleep(3)
        except Exception as e:
            exstr = traceback.format_exc()
            print(exstr)

    def craw_detail(self):
        arrs = SqlHelper.queryPic()
        errs = []

        for x in arrs:
            s = x['href']
            index = s.rindex("/")
            url = "https://www.huxiu.com"+s[:index+1]+quote(s[index+1:])
            try:
                cont = self.downloader.download_detail(url)
                type,teams,company,imgs,product = self.parser.parse_detail(cont)
                # SqlHelper.saveCompany(**company)
                # SqlHelper.batchSaveImgs(imgs)
                SqlHelper.saveProDetail(**product)
                # if type==1 :
                #     SqlHelper.batchSaveTeams(teams)
                # if type==2 :
                #     SqlHelper.batchSaveChanges(teams)
                # time.sleep(random.randrange(3,6))
            except Exception as e:
                print("err:%s"%url)
                errs.append(url)
                exstr = traceback.format_exc()
                print(exstr)
                continue

        f = open('errs.txt', 'wb')
        pickle.dump(errs, f)
        f.close()

    def craw_pic(self):
        arrs = SqlHelper.queryPic()
        for d in arrs:
            res = self.downloader.download_pic(d['imgUrl'])
            if res.status_code == 200:
                d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+ str(random.randrange(1000,9999)) + ".jpg"
                open(d, 'wb').write(res.content)
            break

    def craw_one(self):
        s = "/chuangye/product/59810/IronBot"
        index = s.rindex("/")
        url = "https://www.huxiu.com"+s[:index+1]+quote(s[index+1:])
        print(url)
        try:
            cont = self.downloader.download_detail(url)
            # f = open('3063.txt', 'wb')
            # pickle.dump(cont, f)
            # f.close()
            type,teams,company,imgs,product = self.parser.parse_detail(cont)
            SqlHelper.saveCompany(**company)
            # SqlHelper.batchSaveImgs(imgs)
            # SqlHelper.saveProDetail(**product)
            # if type==1 :
            #     SqlHelper.batchSaveTeams(teams)
            # if type==2 :
            #     SqlHelper.batchSaveChanges(teams)
        except Exception as e:
            exstr = traceback.format_exc()
            print(exstr)



if __name__=='__main__':
    craw = Craw()
    ###### 爬列表页
    # craw.craw_list()

    ####　爬图片
    # craw.craw_pic()

    craw.craw_detail()




