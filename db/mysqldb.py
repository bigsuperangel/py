#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

class MysqlDb(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host = "192.168.0.114",user='root', password='login', database='night')
        self.cursor = self.conn.cursor()

    def initTable(self):
        # 创建user表:
        self.cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    def insertTable(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('INSERT INTO manager (pid, managerName, managerNameE, groupNo, registerCapital, realCapital, enterpriseNature, paidProportion, category, otherCategory, EmployeeCount, url, advise ) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) ', data)
        print('rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()

    def test(self,data):
        self.cursor.execute('INSERT INTO manager (pid) values (%s)',data)
        print('rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()
    def select(self):
        # 运行查询:
        self.cursor.execute('select * from manager where id = %s', (1,))
        values = self.cursor.fetchall()
        print(values)

    def close(self):
        self.cursor.close()
        self.conn.close()



if __name__=='__main__':
    mysqlDb = MysqlDb()
    # mysqlDb.initTable()
    # data = [12 ,'managerName', 'managerNameE', 'groupNo', 'registerCapital', 'realCapital', 'enterpriseNature', 'paidProportion', 'category', 'otherCategory', 5, 'url', 'advise']
    data = [12]
    mysqlDb.test(data)
    mysqlDb.select()
    mysqlDb.close()
