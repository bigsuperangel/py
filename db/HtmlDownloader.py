#coding:utf-8

import os
import requests
import random
import proxy
import config

class Html_Downloader(object):
    def __init__(self):
        self.list_url = 'http://gs.amac.org.cn/amac-infodisc/api/pof/manager'
        self.fund_url = 'http://gs.amac.org.cn/amac-infodisc/res/pof/fund/'
        self.manager_url = 'http://gs.amac.org.cn/amac-infodisc/res/pof/manager/'
        self.proxyUrl = proxy.urls()[random.randint(1,10)]

    async def download(self,url):
        headers = config.HEADERS.copy()
        headers["Host"] = 'gs.amac.org.cn'

        proxies = {
          "http": "http://%s:%s"%(self.proxyUrl[0],self.proxyUrl[1]),
          "https": "http://%s:%s"%(self.proxyUrl[0],self.proxyUrl[1]),
        }

        r = requests.get(os.path.join(self.fund_url,url), timeout=5 ,headers=headers, proxies=proxies)
        r.encoding = 'utf-8'
        return url,r.content
