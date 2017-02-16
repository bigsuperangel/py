#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re
import os
import pickle
import datetime
import random
from requests.utils import quote


# str = '''
# <html><head><meta http-equiv="Content-Type" content="text/html; charset=gb2312" /><meta http-equiv="pragma" content="no-cache" /><meta http-equiv="cache-control" content="no-store" /><meta http-equiv="Connection" content="Close" /><script>function JumpSelf(){ self.location="/thread-2147-1-1.html?WebShieldSessionVerify=yzjwGCaN3PJciacAEmdP";}</script><script>setTimeout("JumpSelf()",700);</script></head><body></body></html>
# '''
# pattern = re.compile('<html>.*?self.location=(.*?);.*?',re.S)
# items = re.findall(pattern, str)
# print(items[0])

# m = re.match(r'.*?product/(\d+)/.*?', '/chuangye/product/59810/IronBot')
# print(m.group(1))

# str = '../fund/11.html'
# print(os.path.splitext(str))
# print(os.path.splitext(os.path.split(str)[1])[0])

# t = []
# t.append((1,2,3))
# t.append((1,2,3))
# t.append((1,2,3))
# t.append((1,2,3))
# f = open('dump.txt', 'wb')
# pickle.dump(t, f)
# f.close()

# f = open('dump.txt', 'rb')
# d = pickle.load(f)
# f.close()
# print(d)

# d = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
# print(d + str(random.randrange(1000,9999)))

s = "/chuangye/product/3049/形象家"
index = s.rindex("/")
print(s[:index+1]+quote(s[index+1:]))

print(random.randrange(3,6))
