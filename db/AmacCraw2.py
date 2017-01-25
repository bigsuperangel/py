#coding:utf-8

import os
import random
from multiprocessing import Queue, Process, Value,Pool,Manager
from Mysqldb import MysqlDb
from HtmlDownloader import Html_Downloader
from HtmlParser import Html_Parser
from DataStore import store_data
import asyncio
import traceback

class AmacCraw2(object):
    def __init__(self,queue):
        self.queue = queue
        self.parser = Html_Parser()
        self.downloader = Html_Downloader()

    def crawManager(self,urls):

        for url in urls:
            print("基金请求%s"%url)
            try:
                url,content = self.downloader.download(url)
                L,resumes,situations,productA,productB = self.parser.parseManager(url,content)
                print(L)
            except Exception as e:
                exstr = traceback.format_exc()
                print(exstr)

    def crawFund(self,urls):
        for url in urls :
            print("产品请求%s"%url)
            try:
                url,content = self.downloader.download(url)
                data = self.parser.parseFund(url,content)
                self.queue.put(data)
                # print(data)
            except Exception as e:
                exstr = traceback.format_exc()
                print(exstr)

    async def craw(self,url):
        print("产品请求%s"%url)
        try:
            url,content = await self.downloader.download(url)
            data = self.parser.parseFund(url,content)
            self.queue.put(data)
            print(data)
        except Exception as e:
            exstr = traceback.format_exc()
            print(exstr)


def run(queue, urls):
    craw = AmacCraw2(queue)
    return craw.crawFund(urls)

def doCraw(queue,urls):
    craw = AmacCraw2(queue)
    loop = asyncio.get_event_loop()
    tasks = [craw.craw(host) for host in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()

if __name__=='__main__':



    # print('Parent process %s.' % os.getpid())
    # manager = Manager()
    # q1 = manager.Queue()
    q1 = Queue()
    mysqlDb = MysqlDb()
    records = mysqlDb.selectAllMP((0,3))
    urls = []
    for r in records:
        urls.append(r[1])

    p1 = Process(target=doCraw,args=(q1,urls))
    p2 = Process(target=store_data,args=(q1,))
    p1.start()
    p2.start()

    # with Pool(processes=4) as pool:
    #     multiple_results = [pool.apply_async(run, args=(q1,urls)) for i in range(4)]
    #     print([res.get(timeout=1) for res in multiple_results])

    # with Pool(processes=4) as p:
    #     for i in range(4):
    #         p.map(run,args=(q1,urls)
    #         # p.apply_async(run, args=(q1,urls))

    #     print('Waiting for all subprocesses done...')
    #     p.close()
    #     p.join()
    #     print('All subprocesses done.')



