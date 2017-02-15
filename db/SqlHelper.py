#coding:utf-8
import datetime
from sqlalchemy import Column, Integer, String, DateTime, BigInteger,Boolean, Numeric, create_engine, VARCHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from config import DB_CONFIG
from ISqlHelper import ISqlHelper
import os
import pymysql

DB_CONFIG={

    'DB_CONNECT_TYPE':'sqlalchemy',#'pymongo'sqlalchemy
    # 'DB_CONNECT_STRING':'mongodb://localhost:27017/'
    # 'DB_CONNECT_STRING':'sqlite:///'+os.path.dirname(__file__)+'/data/proxy.db'
    'DB_CONNECT_STRING' : 'mysql+mysqlconnector://root:login@192.168.0.114/fund?charset=utf8'
    # 'DB_CONNECT_STRING' : 'mysql+mysqlconnector://howetop:howetop888@rdsz5k34ap6zt113nd46public.mysql.rds.aliyuncs.com/fjsimu?charset=utf8'
}

BaseModel = declarative_base()
class Proxy(BaseModel):
    __tablename__='tb_manager'
    id = Column(Integer, primary_key=True)
    establishDate = Column(BigInteger,default=0)
    fundCount = Column(Integer,default=0)
    fundScale = Column(Integer,default=0)
    hasCreditTips = Column(Boolean)
    hasSpecialTips = Column(Boolean)
    inBlacklist = Column(Boolean)
    managerHasProduct = Column(Boolean)
    managerName = Column(VARCHAR(100))
    officeAddress = Column(VARCHAR(100))
    officeCoordinate = Column(VARCHAR(100))
    officeProvince = Column(VARCHAR(100))
    paidInCapital = Column(Numeric(7,2))
    primaryInvestType = Column(VARCHAR(100))
    regAdrAgg = Column(VARCHAR(100))
    regCoordinate = Column(VARCHAR(100))
    registerAddress = Column(VARCHAR(100))
    registerCity = Column(VARCHAR(100))
    registerDate = Column(BigInteger,default=0)
    registerNo = Column(VARCHAR(100))
    registerProvince = Column(VARCHAR(100))
    subscribedCapital = Column(Numeric(7,2))
    url = Column(VARCHAR(100))


class SqlHelper(ISqlHelper):
    params =  {'id':Proxy.id,'establishDate':Proxy.establishDate,
    'fundCount':Proxy.fundCount,'fundScale':Proxy.fundScale,
    'hasCreditTips':Proxy.hasCreditTips,'hasSpecialTips':Proxy.hasSpecialTips,
    'inBlacklist':Proxy.inBlacklist,'managerHasProduct':Proxy.managerHasProduct,
    'managerName':Proxy.managerName,'officeAddress':Proxy.officeAddress,
    'officeCoordinate':Proxy.officeCoordinate,'officeProvince':Proxy.officeProvince,
    'paidInCapital':Proxy.paidInCapital,'primaryInvestType':Proxy.primaryInvestType,
    'regAdrAgg':Proxy.regAdrAgg,'regCoordinate':Proxy.regCoordinate,
    'registerAddress':Proxy.registerAddress,'registerCity':Proxy.registerCity,
    'registerDate':Proxy.registerDate,'registerNo':Proxy.registerNo,
    'registerProvince':Proxy.registerProvince,'subscribedCapital':Proxy.subscribedCapital,
    'url':Proxy.url}
    def __init__(self):
        if 'sqlite' in DB_CONFIG['DB_CONNECT_STRING']:
            connect_args={'check_same_thread':False}
            self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'],echo=False,connect_args=connect_args)
        else:
            self.engine = create_engine(DB_CONFIG['DB_CONNECT_STRING'],echo=False)
        DB_Session = sessionmaker(bind=self.engine)
        self.session = DB_Session()

    def init_db(self):
         BaseModel.metadata.create_all(self.engine)
    def drop_db(self):
         BaseModel.metadata.drop_all(self.engine)


    def insert(self,value):
        proxy = Proxy(id=value['id'],
            establishDate=value['establishDate'],
            fundCount=value['fundCount'],fundScale=value['fundScale'],
            hasCreditTips = value['hasCreditTips'],hasSpecialTips=value['hasSpecialTips'],
            inBlacklist=value['inBlacklist'],managerHasProduct=value['managerHasProduct'],
            managerName=value['managerName'],officeAddress=value['officeAddress'],
            officeCoordinate=value['officeCoordinate'],officeProvince=value['officeProvince'],
            paidInCapital=value['paidInCapital'],primaryInvestType=value['primaryInvestType'],
            regAdrAgg=value['regAdrAgg'],regCoordinate=value['regCoordinate'],
            registerAddress=value['registerAddress'],registerCity=value['registerCity'],
            registerDate=value['registerDate'],registerNo=value['registerNo'],
            registerProvince=value['registerProvince'],subscribedCapital=value['subscribedCapital'],
            url=value['url']
            )
        self.session.add(proxy)
        # self.session.commit()
    def commit(self):
        self.session.commit()

    def delete(self, conditions=None):
        if conditions:
            conditon_list = []
            for key in list(conditions.keys()):
                if self.params.get(key,None):
                    conditon_list.append(self.params.get(key)==conditions.get(key))
            conditions = conditon_list
            query = self.session.query(Proxy)
            for condition in conditions:
                query = query.filter(condition)
            deleteNum = query.delete()
            self.session.commit()
        else:
            deleteNum = 0
        return ('deleteNum',deleteNum)


    def update(self, conditions=None,value=None):
        '''
        conditions的格式是个字典。类似self.params
        :param conditions:
        :param value:也是个字典：{'ip':192.168.0.1}
        :return:
        '''
        if conditions and value:
            conditon_list = []
            for key in list(conditions.keys()):
                if self.params.get(key,None):
                    conditon_list.append(self.params.get(key)==conditions.get(key))
            conditions = conditon_list
            query = self.session.query(Proxy)
            for condition in conditions:
                query = query.filter(condition)
            updatevalue = {}
            for key in list(value.keys()):
                if self.params.get(key,None):
                    updatevalue[self.params.get(key,None)]=value.get(key)
            updateNum = query.update(updatevalue)
            self.session.commit()
        else:
            updateNum=0
        return {'updateNum':updateNum}


    def select(self, count=None,conditions=None):
        '''
        conditions的格式是个字典。类似self.params
        :param count:
        :param conditions:
        :return:
        '''
        if conditions:
            conditon_list = []
            for key in list(conditions.keys()):
                if self.params.get(key,None):
                    conditon_list.append(self.params.get(key)==conditions.get(key))
            conditions = conditon_list
        else:
            conditions=[]

        query = self.session.query(Proxy.id,Proxy.url,Proxy.managerName,Proxy.fundCount)
        if len(conditions)>0 and count:
            for condition in conditions:
                query = query.filter(condition)
            return query.order_by(Proxy.id.asc()).limit(count).all()
        elif count:
            return query.order_by(Proxy.id.asc()).limit(count).all()
        elif len(conditions)>0:
            for condition in conditions:
                query = query.filter(condition)
            return query.order_by(Proxy.id.asc()).all()
        else:
            return query.order_by(Proxy.id.asc()).all()

    def select2(self, conditions):
        return self.session.query(Proxy.id,Proxy.url,Proxy.managerName,Proxy.fundCount).filter(conditions).all()

    def close(self):
        pass

if __name__=='__main__':

    sqlhelper = SqlHelper()
    # result = sqlhelper.select(conditions={'registerDate>:registerDate':'registerDate=1484611200000'})
    # result = sqlhelper.select2('registerDate>1484611200000')
    result = sqlhelper.update({'id':'1609080127100152'},{'fundCount':1})
    print(result)
    # sqlhelper.init_db()

    #### 测试插入数据
    # proxy = {"id":"445","managerName":"厦门瑞泰和投资管理有限公司","artificialPersonName":"余万贵","registerNo":"P1001025","establishDate":1312329600000,"managerHasProduct":"false","url":"445.html","registerDate":1398124800000,"registerAddress":"福建省厦门市厦禾路302号2307室","registerProvince":"福建省","registerCity":"厦门市","regAdrAgg":"厦门市","fundCount":0,"fundScale":0,"paidInCapital":12433.7500,"subscribedCapital":12433.7500,"hasSpecialTips":"true","inBlacklist":"false","hasCreditTips":"true","regCoordinate":"24.466320743,118.086399644","officeCoordinate":"24.466320743,118.086399644","officeAddress":"福建省厦门市思明区厦禾路302号2307室","officeProvince":"福建省","officeCity":"厦门市","primaryInvestType":"证券投资基金"}
    # sqlhelper.insert(proxy)

    ##### 批量拉取列表页
    # pages = [x for x in range(8)]
    # for i in pages:
    #     for x in urls(i)['content']:
    #         sqlhelper.insert(x)
    #     sqlhelper.commit()





