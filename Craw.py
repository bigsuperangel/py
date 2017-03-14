# -*- coding: utf-8 -*-

import time
import codecs
import sys
import logging
from os import system
import importlib
import requests
import lxml.html
importlib.reload(sys)

# 设置日志级别
if sys.version_info[:3] < (2, 7, 9):
    logging.captureWarnings(True)

# 获取数据


def getData():
    header = {
        'Host': 'a.ishadow.tech',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36'
    }
    res = requests.get('https://a.ishadow.tech/', headers=header)
    content = res.content
    doc = lxml.html.fromstring(content)
    pwdA = doc.xpath(
        "//*[@id='free']/div/div[2]/div[1]/h4[3]")[0].text_content().split(":")[1]
    hostA = doc.xpath(
        "//*[@id='free']/div/div[2]/div[1]/h4[1]")[0].text_content().split(":")[1]
    methodA = doc.xpath(
        "//*[@id='free']/div/div[2]/div[1]/h4[4]")[0].text_content().split(":")[1]
    portA = doc.xpath(
        "//*[@id='free']/div/div[2]/div[1]/h4[2]")[0].text_content().split(":")[1]

    pwdB = doc.xpath(
        "//*[@id='free']/div/div[2]/div[2]/h4[3]")[0].text_content()
    pwdB = pwdB.split(":")[1]
    portB = doc.xpath(
        "//*[@id='free']/div/div[2]/div[2]/h4[2]")[0].text_content()
    portB = portB.split(":")[1]

    pwdC = doc.xpath(
        "//*[@id='free']/div/div[2]/div[3]/h4[3]")[0].text_content()
    pwdC = pwdC.split(":")[1]
    portC = doc.xpath(
        "//*[@id='free']/div/div[2]/div[3]/h4[2]")[0].text_content()
    portC = portC.split(":")[1]

    file = codecs.open('/home/linyu/ss.json', 'w+', 'utf-8')
    line = '''{
  "server":"hostA",
  "server_port":portA,
  "local_port":1080,
  "password":"pwdA",
  "timeout":300,
  "method":"methodA"
}
'''
    str = line.replace('pwdA', pwdA).replace('hostA', hostA).replace(
        'portA', portA).replace('methodA', methodA)
    file.write(str)
    file.close()

if __name__ == '__main__':
    getData()
    # time.sleep(1)
    # system('sslocal -c ss.json -d stop')
    # system('sslocal -c ss.json -d start')
