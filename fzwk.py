#! /usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import re
from time import sleep

headers = {
  'Host': 'www.fzwankaw.com',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
  # 'Cookie' : 'Y4DJ_2132_saltkey=H5cWm4g1; Y4DJ_2132_lastvisit=1480643220; Y4DJ_2132_nofavfid=1; Y4DJ_2132_auth=ae03TWqaFImlaPyJ4SyCm2nLxZLxiKlqb8KK7rAF89z5KHgPS5MgaJxoJPnsXeS1a6ttzmUEl6IX8Zk7nPRSAif9yA; Y4DJ_2132_lastcheckfeed=52492%7C1482912483; Y4DJ_2132_security_cookiereport=52fa703Q3SXKSiXLkAIdG58H4rcbIsNBI3%2FRdzVqCP4K6lBM%2F%2FSw; Y4DJ_2132_ulastactivity=a3baBRlvCnFZSM1XLxyzzIhKcYESqexSaDjKvqZn5tuSOPR9EKuK; safedog-flow-item=DA6EB8EB851F13F0FF325082E5D96D29; Y4DJ_2132_forum_lastvisit=D_44_1482978853D_72_1482992829D_54_1482992840D_52_1483064987D_53_1483065601; Y4DJ_2132_editormode_e=1; Y4DJ_2132_visitedfid=44D53D52D54D72D2; Y4DJ_2132_smile=1D1; Y4DJ_2132_lip=112.5.238.85%2C1483065873; Y4DJ_2132_sid=aHl3cC; CNZZDATA1259949930=2006372445-1477301032-http%253A%252F%252Fwww.fzwankaw.com%252F%7C1483079428; Y4DJ_2132_sendmail=1; Y4DJ_2132_lastact=1483080937%09home.php%09spacecp; Y4DJ_2132_checkpm=1'
}

s = requests.Session()
s.headers.update(headers)
r = s.get('http://www.fzwankaw.com/thread-14520-1-1.html')
str = r.text
print(str)
pattern = re.compile('<html>.*?self.location="(.*?)";.*?',re.S)
items = re.findall(pattern, str)
r = s.get('http://www.fzwankaw.com%s'%items[0])
print(r.text)

