#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 mapleray <zhiwuliao#gmail.com>
#
# Distributed under terms of the MIT license.
import asyncio

async def hello():
    print("Hello world!")
    # 异步调用asyncio.sleep(1):
    r = await asyncio.sleep(1)
    print("Hello again!")



def url():
  url = 'http://192.168.0.114:8000/?types=%d&count=%d' %(1,40)
  print(url)

if __name__=='__main__':
    # 获取EventLoop:
    loop = asyncio.get_event_loop()
    # 执行coroutine
    loop.run_until_complete(hello())
    loop.close()

