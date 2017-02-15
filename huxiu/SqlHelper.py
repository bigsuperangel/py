#! -*- coding: utf-8 -*-
from __future__ import absolute_import
import logging
from traceback import format_exc
import pymysql
from hare import Hare, Model

# 创建一个Hare对象, 作为数据源
# 会使用默认的logger来记录执行的sql
haredb = Hare(
    host='192.168.0.114', user='root',
    password='login', db='night',
    charset='utf8')

# 将user表和User类绑定
@haredb.table('tb_project')
class Project(Model):
    pass

def saveProject(**kw):
    pro = Project()
    pro.set_many(**kw).save()

def batchSavePro(rows):
    dbi = haredb.dbi
    dbi.modify_many(u'INSERT INTO tb_project(imgUrl, intro, href, industry, id, step, city, title) VALUES(%(imgUrl)s, %(intro)s, %(href)s, %(industry)s, %(id)s, %(step)s, %(city)s, %(title)s)', rows)

def queryPic():
    dbi = haredb.dbi
    return dbi.select_many(u'SELECT id,imgUrl FROM tb_project')
