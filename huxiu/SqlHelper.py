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
    password='login', db='huxiu',
    charset='utf8')

# 将user表和User类绑定
@haredb.table('tb_project')
class Project(Model):
    pass

@haredb.table('tb_company')
class Company(Model):
    pass

@haredb.table('tb_product_detail')
class ProductDetail(Model):
    pass

@haredb.table('tb_product_imgs')
class ProductImgs(Model):
    pass

@haredb.table('tb_changes')
class Changes(Model):
    pass

@haredb.table('tb_teams')
class Teams(Model):
    pass


def saveProject(**kw):
    pro = Project()
    pro.set_many(**kw).save()

def batchSavePro(rows):
    dbi = haredb.dbi
    dbi.modify_many(u'INSERT INTO tb_project(imgUrl, intro, href, industry, id, step, city, title) VALUES(%(imgUrl)s, %(intro)s, %(href)s, %(industry)s, %(id)s, %(step)s, %(city)s, %(title)s)', rows)

def queryPic():
    dbi = haredb.dbi
    return dbi.select_many(u'SELECT id,href,imgUrl FROM tb_project')

def saveCompany(**kw):
    # INSERT INTO `tb_company`(legal, regDate, phone, pid, officeAddress, stockholderCount, email, establishDate, regCapital) VALUES(%(legal)s, %(regDate)s, %(phone)s, %(pid)s, %(officeAddress)s, %(stockholderCount)s, %(email)s, %(establishDate)s, %(regCapital)s) ;
    pro = Company()
    pro.set_many(**kw).save()

def saveProDetail(**kw):
    # INSERT INTO `tb_product_detail`(shareholders, id, cpIntroInfo, type, logo, bizScope, cpName, tags, publishDate) VALUES(%(shareholders)s, %(id)s, %(cpIntroInfo)s, %(type)s, %(logo)s, %(bizScope)s, %(cpName)s, %(tags)s, %(publishDate)s) ;
    pro = ProductDetail()
    pro.set_many(**kw).save()

def saveProImgs(**kw):
    pro = ProductImgs()
    pro.set_many(**kw).save()

def saveChange(**kw):
    # INSERT INTO `tb_changes`(pid, changeDate, beforeChange, changeItems, sort, afterChange) VALUES(%(pid)s, %(changeDate)s, %(beforeChange)s, %(changeItems)s, %(sort)s, %(afterChange)s) ;
    pro = Changes()
    pro.set_many(**kw).save()

def batchSaveChanges(rows):
    dbi = haredb.dbi
    dbi.modify_many(u'INSERT INTO `tb_changes`(pid, changeDate, beforeChange, changeItems, sort, afterChange) VALUES(%(pid)s, %(changeDate)s, %(beforeChange)s, %(changeItems)s, %(sort)s, %(afterChange)s) ', rows)

def batchSaveImgs(rows):
    dbi = haredb.dbi
    dbi.modify_many(u'INSERT INTO `tb_product_imgs`(url, pid) VALUES(%(url)s, %(pid)s) ', rows)


def saveTeam(**kw):
    pro = Teams()
    pro.set_many(**kw).save()

def batchSaveTeams(rows):
    dbi = haredb.dbi
    dbi.modify_many(u'INSERT INTO `tb_teams`(personIntro, personName, pid, personPosition) VALUES(%(personIntro)s, %(personName)s, %(pid)s, %(personPosition)s)', rows)

