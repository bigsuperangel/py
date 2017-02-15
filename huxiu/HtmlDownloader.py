#coding:utf-8

import os
import requests
import random
import config

class Html_Downloader(object):
    def __init__(self):
        self.list_url = 'https://www.huxiu.com/chuangye/ajax_home'

    def download(self,values):
        headers = config.HEADERS.copy()
        headers["Host"] = 'www.huxiu.com'

        r = requests.post(self.list_url, timeout=5 ,headers=headers,params=values)
        r.encoding = 'utf-8'
        return r.json()

    def download_detail(self,url):
        headers = config.HEADERS.copy()
        headers["Host"] = 'www.huxiu.com'
        r = requests.get(url, timeout=5 ,headers=headers)
        r.encoding = 'utf-8'
        return r.content

    def download_pic(self,url):
        r = requests.get(url)
        return r
