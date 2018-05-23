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

class RoleManage(object):


    @staticmethod
    def add_user_info():
        payload = smpv.addUserInfo()
        req_url = pu.SystemManageUrls()["addUserInfoUrl"]
        r = requests.post(req_url, data=(payload))
        rsp = json.loads(r.text)
        # print r.status_code
    @staticmethod
    def update_user_info():
        payload = smpv.updateUserInfo()
        req_url = pu.SystemManageUrls()["updateUserInfoUrl"]
        r = requests.post(req_url, data=(payload))
        rsp = json.loads(r.text)
        # print r.status_code
    @staticmethod
    def delete_user_info():
        payload = smpv.deleteUserInfo()
        req_url = pu.SystemManageUrls()["deleteUserInfoUrl"]
        r = requests.post(req_url, data=(payload))
        rsp = json.loads(r.text)
        # print r.status_code

    @staticmethod
    def add_user_group():
        payload = smpv.addUserGroup()
        req_url = pu.SystemManageUrls()["addUserGroupUrl"]
        r = requests.post(req_url, data=(payload))
        rsp = json.loads(r.text)
        # print r.status_code
    @staticmethod
    def update_user_group():
        payload = smpv.updateUserGroup()
        req_url = pu.SystemManageUrls()["updateUserGroupUrl"]
        r = requests.post(req_url, data=(payload))
        rsp = json.loads(r.text)
        # print r.status_code

    @staticmethod
    def delete_user_group():
        payload = smpv.deleteUserGroup()
        req_url = pu.SystemManageUrls()["deleteUserGroupUrl"]
        r = requests.post(req_url, data=(payload))
        rsp = json.loads(r.text)
        # print r.status_code


# a=RoleManage()
# # a.addUserInfo()
# # # time.sleep(10)
# # a.updateUserInfo()
# # time.sleep(10)
# # a.deleteUserInfo()
# a.addUserGroup()
# time.sleep(10)
# a.updateUserGroup()
# time.sleep(15)
# a.deleteUserGroup()

