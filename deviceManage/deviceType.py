#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: deviceModel.py
@time: 2018/05/14/12:00
"""
from util.paraMeterValue import projectMeterValue as pmv
from util.requestURL import projectUrls as pu
from util.danbayDatabase import DB_database as db
import requests
import json
import base64
import time

class deviceModel():

    projectUrls = pu()
    pmv = pmv()
    name=pmv.deviceValue_deviceCenter()["中控"]

    #根据周思芸反馈，设备中心模块，设备类型基本确定，一般都是中控，门锁，水表，电表，采集器，门禁，烟感，中继器
    #当里面有具体设备是，大模块的设备不能删除，比如说，中控这个类目，如果里面有小圆盒或者华为网关，那么中控不可删除
    #因此，本人觉得该模块不适合做自动化测试。可以选择大类目里面的小类目做自动化测试
    @staticmethod
    def addDeviceModel():

        uploadUrl =deviceModel.projectUrls.deviceUrls()["uploadImageUrl"]
        with open("des.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        r = requests.post(uploadUrl, data={"base64":"data:image/png;base64,"+encoded_string})
        rsp=json.loads(r.text)
        img=rsp['image']
        payload = {"name": deviceModel.name,
                   "images":img,
                   "ext": deviceModel.pmv.deviceValue_deviceCenter()["中控"]}
        reqUrl = deviceModel.projectUrls.deviceUrls()["addDeviceModelUrl"]

        r = requests.post(reqUrl, data=payload)
        rsp = json.loads(r.text)

        print r.status_code

    @staticmethod
    def updateDegiceModel():
        uploadUrl = deviceModel.projectUrls.deviceUrls()["uploadImageUrl"]
        with open("upda.png", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        r = requests.post(uploadUrl, data={"base64": "data:image/png;base64,"+encoded_string})
        rsp = json.loads(r.text)
        img = rsp['image']

        updateId = db.deviceSql("getDeviceTypeId", deviceModel.name)
        payload = {"name": deviceModel.pmv.deviceValue_deviceCenter()["updateName"],
                   "images": img,
                   "ext": "",
                   "id":updateId}
        reqUrl = deviceModel.projectUrls.deviceUrls()["updateDeviceModelUrl"]

        r = requests.post(reqUrl, data=payload)
        rsp = json.loads(r.text)
        reqUrl=deviceModel.projectUrls.deviceUrls()["updateDeviceModelUrl"]
        print r.status_code

    @staticmethod
    def delDeviceModel():
        reqUrl=deviceModel.projectUrls.deviceUrls()["delDeviceModelUrl"]
        delId=db.deviceSql("getDeviceTypeId","testTu")
        payload={"id":delId}
        r = requests.post(reqUrl, data=payload)
        print r.status_code
        rsp = json.loads(r.text)



a = deviceModel()
a.addDeviceModel()
time.sleep(40)
a.updateDegiceModel()
