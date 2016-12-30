#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

str = '''
<html><head><meta http-equiv="Content-Type" content="text/html; charset=gb2312" /><meta http-equiv="pragma" content="no-cache" /><meta http-equiv="cache-control" content="no-store" /><meta http-equiv="Connection" content="Close" /><script>function JumpSelf(){ self.location="/thread-2147-1-1.html?WebShieldSessionVerify=yzjwGCaN3PJciacAEmdP";}</script><script>setTimeout("JumpSelf()",700);</script></head><body></body></html>
'''
pattern = re.compile('<html>.*?self.location=(.*?);.*?',re.S)
items = re.findall(pattern, str)
print(items[0])
