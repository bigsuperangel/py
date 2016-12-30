#! /usr/bin/env python
# -*- coding: utf-8 -*-
# python print功能不能完全打印utf-8字符，需要重置sys

import requests
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8') #改变标准输出的默认编码
s = requests.Session()

headers = {
  'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
  'Accept-Encoding':'gzip, deflate, sdch, br',
  'Accept-Language':'zh-CN,zh;q=0.8',
  'Cache-Control':'max-age=0',
  'Connection':'keep-alive',
  'Host': 'www.zhihu.com',
  'Cookie' : '_za=abec5d64-111b-45ec-8997-8e804c15cc41; udid="ACDA_VsrlQmPTp0CcpmkIg9Z58GM_zcDixg=|1457510641"; _zap=e9265990-043b-4ecd-9952-fb8d64056446; d_c0="AEDAOxkfpwmPTmoKCLa9moqhuT8wx4twEHI=|1461296061"; _ga=GA1.2.1900552140.1469693292; q_c1=9d20821f42ae48e9993d3aefecbcfb45|1482399085000|1451891208000; _xsrf=22ae4be86f34642bffc7c3371ae2c8e6; l_cap_id="ZWIzMDQ5MTg3NjY2NGNjNDgzNzE1NTVlMjVkOWVkZDA=|1483083272|4faf69c2ccb2bdca4b604281faa0d194c0f709ff"; cap_id="OTk1N2I2N2RiZmFlNDE1ZDhmZGM4ZTJmYTlkZTcwMTU=|1483083272|1ca2d345a14a803356a55223317f6c3f5cec238b"; r_cap_id="YmY4ZDg0ZjQ0MmFhNGFjMDk2NmNjYmI4NjJhMmEwY2E=|1483083273|b16aa08abf9b0e89d946ab51530f9c7869928174"; __utmt=1; login="MDdkY2IyZjc4MWMxNDU5NjgyZDMxNzZlOTk1ZmZiNDc=|1483083291|bf6f35d7e5bab15b9abcc699740ea107023d6b0d"; n_c=1; z_c0=Mi4wQUFCQWljQVlBQUFBUU1BN0dSLW5DUmNBQUFCaEFsVk5ZcHVOV0FCdzE0cG02VXRpV0xwWUpXaWdiemM2YzdqQmNn|1483083365|698eed476ae56c808c9ebb1e7e630985eb1a97a3; __utma=51854390.1900552140.1469693292.1483068948.1483083272.12; __utmb=51854390.4.10.1483083272; __utmc=51854390; __utmz=51854390.1483068948.11.10.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); __utmv=51854390.100-1|2=registration_date=20111101=1^3=entry_date=20111101=1',
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s.headers.update(headers)

r = s.get('https://www.zhihu.com')
# r = s.get('https://www.zhihu.com/lives/797770174366371840')
print(r.encoding)
print(r.text)
