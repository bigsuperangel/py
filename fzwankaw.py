#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 mapleray <zhiwuliao#gmail.com>
#
# Distributed under terms of the MIT license.
from urllib import request
import json
from urllib.parse import quote
import time
from selenium import webdriver



def urls():
    url = 'http://192.168.0.114:8000/?types=0&count=40'
    with request.urlopen(url) as f:
        data = f.read()
        ip_ports = json.loads(data.decode('utf-8'))
        return ip_ports

def post(ip,port):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    # proxy ip
    PROXY = ip+":"+ str(port)
    print(PROXY)

    chrome_options.add_argument('--proxy-server=%s' % PROXY)
    #mobile_emulation = {"deviceName": "Google Nexus 5"}
    #chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome('F:\\chromedriver.exe', chrome_options=chrome_options)
    driver.get("http://www.fzwankaw.com/?fromuser=nimabibi163")
    time.sleep(10)
    driver.quit()


def doPost(ip_ports):
    for i in range(40):
        ip = ip_ports[40-i-1][0]
        port = ip_ports[40-i-1][1]
        post(ip, port)

if __name__=='__main__':
    print(doPost(urls()))

