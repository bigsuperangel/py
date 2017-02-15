#coding:utf-8

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
        cont = self.downloader.download_detail('https://www.huxiu.com/chuangye/product/58987/'+quote('会计乐'))
        f = open('detail2', 'wb')
        pickle.dump(cont, f)
        f.close()

    def craw_pic(self):
        arrs = SqlHelper.queryPic()
        for d in arrs:
            res = self.downloader.download_pic(d['imgUrl'])
            if res.status_code == 200:
                d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")+ str(random.randrange(1000,9999)) + ".jpg"
                open(d, 'wb').write(res.content)
            break



if __name__=='__main__':
    craw = Craw()
    ###### 爬列表页
    # craw.craw_list()

    ####　爬图片
    # craw.craw_pic()

    craw.craw_detail()




