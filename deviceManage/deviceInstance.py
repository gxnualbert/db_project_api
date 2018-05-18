#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: deviceType.py
@time: 2018/05/14/12:00
"""

import json
import time

import requests
from util.paraMeterValue import DeviceManageParamsValue as dmpv
from util.requestURL import projectUrls as pu


class deviceInstance():


    @staticmethod
    def centerControl_addInstance():
        payload=dmpv.centerControl_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        rsp = json.loads(r.text)
        print r.status_code

    @staticmethod
    def centerControl_updateInstance():
        payload=dmpv.centerControl_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def centerControl_deleteInstance():
        payload = dmpv.centerControl_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code

    @staticmethod
    def lock_addInstance_0():
        payload=dmpv.lock_addInstance("普通")
        reqUrl=pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def lock_addInstance_1():
        payload = dmpv.lock_addInstance("网络")
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code

    @staticmethod
    def lock_addInstance_2():
        payload = dmpv.lock_addInstance("其他")
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code

    @staticmethod
    def lock_updateInstance():
        payload = dmpv.lock_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code

    @staticmethod
    def lock_deleteInstance():
        payload = dmpv.lock_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def water_addInstance():
        payload=dmpv.waterMeter_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def water_updateInstance():
        payload=dmpv.waterMeter_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def water_deleteInstance():
        payload = dmpv.waterMeter_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def electric_addInstance():
        payload = dmpv.electric_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def electric_updateInstance():
        payload = dmpv.electric_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def electric_deleteInstance():
        payload = dmpv.electric_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code

    @staticmethod
    def caiji_addInstance():
        payload = dmpv.caiji_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def caiji_updateInstance():
        payload = dmpv.caiji_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def caiji_deleteInstance():
        payload = dmpv.caiji_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def menji_addInstance():
        print "请参考bug 933"

    @staticmethod
    def yangan_addInstance():
        payload = dmpv.yangan_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def yangan_updateInstance():
        payload = dmpv.yangan_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code

    @staticmethod
    def yangan_deleteInstance():
        payload = dmpv.yangan_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def zhognji_addInstance():
        payload = dmpv.zhongji_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code
    @staticmethod
    def zhongji_updateInstance():
        payload = dmpv.zhongji_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code

    @staticmethod
    def zhongji_deleteInstance():
        payload = dmpv.zhongji_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)
        print r.status_code




a = deviceInstance()
# a.centerControl_addInstance()
# time.sleep(10)
# a.centerControl_updateInstance()
# time.sleep(10)
# a.centerControl_deleteInstance()

# a.lock_addInstance_2()
# time.sleep(10)
# a.lock_updateInstance()
# time.sleep(10)
# a.lock_deleteInstance()
# a.water_addInstance()
# time.sleep(7)
# a.water_updateInstance()
# time.sleep(10)
# # a.water_deleteInstance()
a.zhognji_addInstance()
time.sleep(5)
a.zhongji_updateInstance()
time.sleep(4)
a.zhongji_deleteInstance()