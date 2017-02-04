#!/usr/bin/env python3
# -*- coding: utf-8 -*-

########## prepare ##########

# install mysql-connector-python:
# pip3 install mysql-connector-python --allow-external mysql-connector-python

import mysql.connector

class MysqlDb(object):
    def __init__(self):
        self.conn = mysql.connector.connect(host = "192.168.0.114",user='root', password='login', database='fund')
        self.cursor = self.conn.cursor()

    def initTable(self):
        # 创建user表:
        self.cursor.execute('create table user (id varchar(20) primary key, name varchar(20))')
    def insertTable(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('INSERT INTO tb_manager_detail (pid,info, managerName, managerNameE, groupNo, registerCapital, realCapital, enterpriseNature, paidProportion, category, otherCategory, EmployeeCount, url, lawStatus,lawOffice,lawName,legalRepresentative,qualification,obtainWay ,lastUpdate,tip) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s , %s ) ', data)
        print('tb_manager_detail,rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()

    def insertResume(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('INSERT INTO tb_resume (ctime, unit, POSITION, pid) VALUES (%s, %s,%s,%s) ', data)
        print('tb_resume,rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()

    def insertSituation(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('INSERT INTO tb_situation ( hname, POSITION, isQualifications, pid ) VALUES (%s, %s,%s,%s) ', data)
        print('tb_situation,rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()

    def insertMP(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('INSERT INTO tb_manager_product ( productName, url, pid,TYPE)  VALUES (%s, %s,%s,%s) ', data)
        print('tb_manager_product,rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()

    def replaceMP(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('replace INTO tb_manager_product ( productName, url, pid,TYPE)  VALUES (%s, %s,%s,%s) ', data)
        print('tb_manager_product,rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()


    def insertFund(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('INSERT INTO tb_fund ( id, fundName, fundNo, establishDate, recordDate, step, fundType, currency, managerName,managerId, managerType, hostName, fundAreas, status, lastUpdate, tip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ', data)
        print('tb_fund,rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()

    def replaceFund(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('replace INTO tb_fund ( id, fundName, fundNo, establishDate, recordDate, step, fundType, currency, managerName,managerId, managerType, hostName, fundAreas, status, lastUpdate, tip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ', data)
        print('tb_fund,rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()

    def selectFund(self,data):
        # 运行查询:
        self.cursor.execute('select * from tb_fund where id = %s and managerId= %s', data)
        values = self.cursor.fetchall()
        return values

    def selectAllMP(self,data):
        # 运行查询:
        self.cursor.execute('select productName,url,pid from tb_manager_product limit %s,%s', data)
        values = self.cursor.fetchall()
        return values

    def test(self,data):
        self.cursor.execute('INSERT INTO tb_manager_detail (pid) values (%s)',data)
        print('rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()
    def select(self):
        # 运行查询:
        self.cursor.execute('select * from tb_manager_detail where id = %s', (1,))
        values = self.cursor.fetchall()
        print(values)

    def selectManager(self,data):
        # 运行查询:
        self.cursor.execute('select * from tb_manager_detail where pid = %s', data)
        values = self.cursor.fetchall()
        return values

    def selectIsMp(self,data):
        # 运行查询:
        self.cursor.execute('select * from tb_manager_product where pid = %s', data)
        values = self.cursor.fetchall()
        return values

    def close(self):
        self.cursor.close()
        self.conn.close()

    def insertFund2(self,data):
        # 插入一行记录，注意MySQL的占位符是%s:
        self.cursor.execute('INSERT INTO tb_fund2 ( id, fundName, fundNo, establishDate, recordDate, step, fundType, currency, managerName,managerId, managerType, hostName, fundAreas, status, lastUpdate, tip) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) ', data)
        print('tb_fund,rowcount =', self.cursor.rowcount)
        # 提交事务:
        self.conn.commit()

if __name__=='__main__':
    mysqlDb = MysqlDb()
    # mysqlDb.initTable()
    # data = [12 ,'managerName', 'managerNameE', 'groupNo', 'registerCapital', 'realCapital', 'enterpriseNature', 'paidProportion', 'category', 'otherCategory', 5, 'url', 'advise']
    # data = ['510727', '汉云-清和泉优选1期私募证券投资基金', 'SM5769', '2016-10-31', '2016-11-25', '暂行办法实施后成立的基金', '证券投资基金', '人民币现钞', '厦门汉云投资管理有限公司', '23308', '受托管理', '', '现金类资产', '正在运作', '2016-11-22', '']
    # mysqlDb.insertFund(data)
    print(mysqlDb.selectAllMP((0,10)))
    mysqlDb.close()
