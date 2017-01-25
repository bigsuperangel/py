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


# types   int 0: 高匿代理, 1 透明
# protocol    int 0: http, 1 https
# count   int 数量
# country str 国家
# area    str 地区
def urls():
    url = 'http://192.168.0.114:8000/?types=0&count=40'
    # url = 'http://104.224.145.43:8000/?types=0&count=40'
    with request.urlopen(url) as f:
        data = f.read()
        ip_ports = json.loads(data.decode('utf-8'))
        return ip_ports

if __name__=='__main__':
    print(urls())

