#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: customerManage.py
@time: 2018/05/17/9:13
"""
import json
import time
import requests
from util.paraMeterValue import HouseManageParamsValue as hmpv
from util.danbayDatabase import DB_database as db
from util.requestURL import projectUrls as pu


class CustomerManage():

    #全局变量
    homeProviderName=""
    homeSourceName=""
    homeSourceId=""
    providerId=""
    homeNo=""



    @staticmethod
    def addHomeProviderSerials():

        payload=hmpv.addHouseProvider()
        homeProviderName=hmpv.addHouseProvider()["providerName"]
        reqUrl=pu.HouseManageUrls()["addhomeSourceProviderUrl"]
        r = requests.post(reqUrl, json=(payload))
        rsp = json.loads(r.text)
        print r.status_code
        #添加房源信息
        if r.status_code==200:
            providerId=db.houseSourceSql("getProviderNameID", homeProviderName)
            payload = hmpv.addHouseSource()
            payload["providerId"]=providerId
            reqUrl = pu.HouseManageUrls()["addHomeSourceUrl"]
            r = requests.post(reqUrl, json=payload)
            homeSourceName=payload["homeSourceName"]

            print(r.status_code)
            if r.status_code:
                #添加空间信息
                payload = hmpv.addSpace()
                payload["homeSourceId"]= db.houseSourceSql("getHomeSourceId", homeSourceName)
                reqUrl = pu.HouseManageUrls()["addSpaceUrl"]
                r = requests.post(reqUrl, json=payload)
                print(r.status_code)
            else:
                print "添加房源信息失败"
        else:
            print "添加房源提供者信息失败"

    @staticmethod
    def addHomeProvider():
        payload = hmpv.addHouseProvider()
        CustomerManage.homeProviderName = hmpv.addHouseProvider()["providerName"] #write to txt

        reqUrl = pu.HouseManageUrls()["addhomeSourceProviderUrl"]
        r = requests.post(reqUrl, json=(payload))
        rsp = json.loads(r.text)
        print r.status_code

    @staticmethod
    def batchDeleteHomeProvider():
        pass

    @staticmethod
    def addHouseSource():

        payload=hmpv.addHouseSource()
        payload["providerId"] = db.houseSourceSql("getProviderNameID", CustomerManage.homeProviderName)

        reqUrl=pu.HouseManageUrls()["addHomeSourceUrl"]
        r = requests.post(reqUrl, json=payload)
        CustomerManage.homeSourceName = payload["homeSourceName"]
        CustomerManage.addrCode=payload["addrCode"]
        CustomerManage.providerId=payload["providerId"]

        print(r.status_code)

    @staticmethod
    def updateHouseSource():

        payload=hmpv.updateHouseSource()
        payload["id"] = db.houseSourceSql("getHomeSourceId", CustomerManage.homeSourceName)
        payload["providerId"] = CustomerManage.providerId
        reqUrl = pu.HouseManageUrls()["updateHomeSourceUrl"]
        r = requests.post(reqUrl, json=payload)
        print r.status_code

    # 添加空间
    @staticmethod
    def addSpace():
        payload = hmpv.addSpace()
        payload["homeSourceId"] = db.houseSourceSql("getHomeSourceId", CustomerManage.homeSourceName)
        reqUrl = pu.HouseManageUrls()["addSpaceUrl"]
        r = requests.post(reqUrl, json=payload)
        CustomerManage.homeSourceId=payload["homeSourceId"]
        CustomerManage.homeNo=payload["homeNo"]
        print(r.status_code)

    @staticmethod
    def updateSpace():
        payload = hmpv.updateSpace()
        payload["homeSourceId"]=CustomerManage.homeSourceId
        payload["id"]=db.houseSourceSql("getSpaceId", CustomerManage.homeNo)
        reqUrl = pu.HouseManageUrls()["updateSpaceUrl"]
        r = requests.post(reqUrl, json=payload)
        CustomerManage.homeSourceId = payload["homeSourceId"]
        print(r.status_code)

    @staticmethod
    def deleteSpace():
        spaceID = hmpv.deleteSpace()
        reqUrl = pu.HouseManageUrls()["deleteSpaceUrl"] + str(spaceID) + "/deleteRecordById"
        r = requests.get(reqUrl)
        print r.status_code

    @staticmethod
    def deleteHouseSource():
        houseSourceID = hmpv.deleteHouseSource()
        reqUrl = pu.HouseManageUrls()["deleteHomeSourceUrl"] + str(houseSourceID) + "/deleteRecordById"
        r = requests.get(reqUrl)
        print r.status_code

    @staticmethod
    def deleteHomeProvider():
        homeProvideID=hmpv.deleteHouseProvider()
        reqUrl=pu.HouseManageUrls()["deleteHomeSourceProvider"]+str(homeProvideID)+"/deleteRecordById"
        r=requests.get(reqUrl)
        print r.status_code





a=CustomerManage()

a.addHomeProvider() #添加客户
a.addHouseSource()#添加房源信息
a.addSpace() #添加空间信息
# time.sleep(19)
a.updateSpace()
# time.sleep(10)
a.deleteSpace()
# time.sleep(10)
a.updateHouseSource()
a.deleteHouseSource()
time.sleep(10)
a.deleteHomeProvider()


#批量添加房源信息
# a.deleteHomeProvider()
# for i in range(1000):
#     a = CustomerManage()
#     a.addHouseSource()
#     # time.sleep(1)
