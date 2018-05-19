#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: roleManage.py
@time: 2018/05/19/11:34
"""
import json
import time
import requests
from util.paraMeterValue import SystemManageParamsValue as smpv
from util.danbayDatabase import DB_database as db
from util.requestURL import projectUrls as pu

class RoleManage():



    @staticmethod
    def addUserInfo():
        payload = smpv.addUserInfo()
        reqUrl = pu.SystemManageUrls()["addUserInfoUrl"]
        r = requests.post(reqUrl, data=(payload))
        rsp = json.loads(r.text)
        print r.status_code
    @staticmethod
    def updateUserInfo():
        payload = smpv.updateUserInfo()
        reqUrl = pu.SystemManageUrls()["updateUserInfoUrl"]
        r = requests.post(reqUrl, data=(payload))
        rsp = json.loads(r.text)
        print r.status_code
    @staticmethod
    def deleteUserInfo():
        payload = smpv.updateUserInfo()
        reqUrl = pu.SystemManageUrls()["updateUserInfoUrl"]
        r = requests.post(reqUrl, data=(payload))
        rsp = json.loads(r.text)
        print r.status_code

a=RoleManage()
a.addUserInfo()
# time.sleep(10)
a.updateUserInfo()