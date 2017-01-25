#coding:utf-8
import sys
from Mysqldb import MysqlDb

mysqldb = MysqlDb()

def store_data(queue):

    while True:
      if not queue.empty():

        data = queue.get(timeout=5)
        sys.stdout.write(data+"\r")
        sys.stdout.flush()
        mysqldb.insertFund2(data)
