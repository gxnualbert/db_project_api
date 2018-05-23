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
from util.parameter_value import HouseManageParamsValue as hmpv
from util.danbay_database import DataBase as db
from util.request_url import ProjectUrls as pu


class CustomerManage(object):

    #全局变量
    home_provider_name=""
    home_source_name=""
    home_source_id=""
    provider_id=""
    home_no=""



    @staticmethod
    def add_home_provider_serials():

        payload=hmpv.add_house_provider()
        home_provider_name=hmpv.add_house_provider()["providerName"]
        req_url=pu.house_manage_urls()["add_home_source_provider_url"]
        r = requests.post(req_url, json=payload)
        rsp = json.loads(r.text)
        #添加房源信息
        if r.status_code==200:
            provider_id=db.house_source_sql("get_provider_name_and_id", home_provider_name)
            payload = hmpv.add_house_source()
            payload["providerId"]=provider_id
            req_url = pu.house_manage_urls()["add_home_source_url"]
            r = requests.post(req_url, json=payload)
            home_source_name=payload["homeSourceName"]

            if r.status_code:
                #添加空间信息
                payload = hmpv.add_space()
                payload["homeSourceId"]= db.house_source_sql("get_home_source_id", home_source_name)
                req_url = pu.house_manage_urls()["add_space_url"]
                r = requests.post(req_url, json=payload)
            else:
                pass
        else:
            pass

    @staticmethod
    def add_home_provider():
        payload = hmpv.add_house_provider()
        CustomerManage.homeProviderName = hmpv.add_house_provider()["providerName"] #write to txt

        req_url = pu.house_manage_urls()["add_home_source_provider_url"]
        r = requests.post(req_url, json=payload)
        rsp = json.loads(r.text)

    @staticmethod
    def batch_delete_home_provider():
        pass

    @staticmethod
    def add_house_source():

        payload=hmpv.add_house_source()
        payload["providerId"] = db.house_source_sql("get_provider_name_and_id", CustomerManage.home_provider_name)

        req_url=pu.house_manage_urls()["add_home_source_url"]
        r = requests.post(req_url, json=payload)
        CustomerManage.homeSourceName = payload["homeSourceName"]
        CustomerManage.addrCode=payload["addrCode"]
        CustomerManage.providerId=payload["providerId"]


    @staticmethod
    def update_house_source():

        payload=hmpv.update_house_source()
        payload["id"] = db.house_source_sql("get_home_source_id", CustomerManage.home_source_name)
        payload["providerId"] = CustomerManage.provider_id
        req_url = pu.house_manage_urls()["update_home_source_url"]
        r = requests.post(req_url, json=payload)

    # 添加空间
    @staticmethod
    def add_space():
        payload = hmpv.add_space()
        payload["homeSourceId"] = db.house_source_sql("get_home_source_id", CustomerManage.home_source_name)
        req_url = pu.house_manage_urls()["add_space_url"]
        r = requests.post(req_url, json=payload)
        CustomerManage.homeSourceId=payload["homeSourceId"]
        CustomerManage.homeNo=payload["homeNo"]

    @staticmethod
    def update_space():
        payload = hmpv.update_space()
        payload["homeSourceId"]=CustomerManage.home_source_id
        payload["id"]=db.house_source_sql("get_space_id", CustomerManage.home_no)
        req_url = pu.house_manage_urls()["update_space_url"]
        r = requests.post(req_url, json=payload)
        CustomerManage.homeSourceId = payload["homeSourceId"]

    @staticmethod
    def delete_space():
        space_id = hmpv.delete_space()
        req_url = pu.house_manage_urls()["delete_space_url"] + str(space_id) + "/deleteRecordById"
        r = requests.get(req_url)

    @staticmethod
    def delete_house_source():
        house_source_id = hmpv.delete_house_source()
        req_url = pu.house_manage_urls()["delete_home_source_url"] + str(house_source_id) + "/deleteRecordById"
        r = requests.get(req_url)

    @staticmethod
    def delete_home_provider():
        home_provide_id=hmpv.delete_house_provider()
        req_url=pu.house_manage_urls()["delete_home_source_provider"]+str(home_provide_id)+"/deleteRecordById"
        r=requests.get(req_url)





# a=CustomerManage()
#
# a.addHomeProvider() #添加客户
# a.addHouseSource()#添加房源信息
# a.addSpace() #添加空间信息
# # time.sleep(19)
# a.updateSpace()
# # time.sleep(10)
# a.deleteSpace()
# # time.sleep(10)
# a.updateHouseSource()
# a.deleteHouseSource()
# time.sleep(10)
# a.deleteHomeProvider()


#批量添加房源信息
# a.deleteHomeProvider()
# for i in range(1000):
#     a = CustomerManage()
#     a.addHouseSource()
#     # time.sleep(1)
