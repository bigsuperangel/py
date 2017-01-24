#coding:utf-8

import os
import random
from multiprocessing import Queue, Process, Value,Pool
from Mysqldb import MysqlDb
from HtmlDownloader import Html_Downloader
from HtmlParser import Html_Parser

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
                print(e)

    def crawFund(self,urls):
        for url in urls :
            print("产品请求%s"%url)
            try:
                url,content = self.downloader.download(url)
                data = self.parser.parseFund(url,content)
                self.queue.put(data)
                print(data)
            except Exception as e:
                print(e)


def run(queue, urls):
    craw = AmacCraw2(queue)
    return craw.crawFund(urls)

if __name__=='__main__':

    print('Parent process %s.' % os.getpid())
    q1 = Queue()
    mysqlDb = MysqlDb()
    records = mysqlDb.selectAllMP((0,5))
    urls = set()
    for r in records:
        print(r)
        urls.add(r[1])

    p1 = Process(target=run,args=(q1,urls))
    p1.start()

    # for i in range(5):
    #     p.map(craw.crawFund,urls)
    #     # p.apply_async(run, args=(q1,urls))
    # print('Waiting for all subprocesses done...')
    # p.close()
    # p.join()
    # print('All subprocesses done.')

