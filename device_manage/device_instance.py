#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: deviceType.py
@time: 2018/05/14/12:00
"""

import json
import time
import unittest

import requests

from util.danbay_database import DataBaseValidateWebResult as db_wc
from util.log_tool import AddLog as log
from util.parameter_value import DeviceManageParamsValue as dmpv
from util.request_url import ProjectUrls as pu


class DeviceInstance(unittest.TestCase):

    status_not_200="返回状态码不为200!"

    def base_message(self,info):
        return "数据库存储的{info}跟实际传入的不一致".format(info=info)

    def test_center_control_add_instance(self):
        payload = dmpv.center_control_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.status_code_API_return(time.strftime("%Y-%m-%d %H:%M:%S"), str(r.status_code) + rsp["message"])
            ccProperties = db_wc.device_manage_web_check("add_dev_url", payload["name"])
            # 校验类型，名字 name,model,net
            log.log("中控名字:{cc_name}；中控类型:{cc_type}；中控网络属性:{cc_net}".format(cc_name=ccProperties[0],
                                                                           cc_type=ccProperties[1],
                                                                           cc_net=ccProperties[2]))
            self.assertEquals(ccProperties[0], payload["name"], msg=self.base_message("中控名字"))
            self.assertEquals(ccProperties[1], payload["model"], msg=self.base_message("中控类型"))
            self.assertEquals(ccProperties[2], int(payload["net"]), msg=self.base_message("中控网络属性"))
        else:
            self.assertEquals(True, False, msg=self.status_not_200+"%s" % r.status_code)

    def center_control_update_instance(self):
        payload = dmpv.center_control_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload)

        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.status_code_API_return(time.strftime("%Y-%m-%d %H:%M:%S"), str(r.status_code) + rsp["message"])
            ccProperties = db_wc.device_manage_web_check("get_center_control_properties", payload["name"])
            # 校验类型，名字 name,model,net
            log.Log("中控名字:{cc_name}；中控类型:{cc_type}；中控网络属性:{cc_net}".format(cc_name=ccProperties[0],
                                                                           cc_type=ccProperties[1],
                                                                           cc_net=ccProperties[2]))
            self.assertEquals(ccProperties[0], payload["name"], msg=self.base_message("中控名字"))
            self.assertEquals(ccProperties[1], payload["model"], msg=self.base_message("中控类型"))
            self.assertEquals(ccProperties[2], int(payload["net"]), msg=self.base_message("中控网络属性"))
        else:
            self.assertEquals(True, False, msg=self.status_not_200+"%s" % r.status_code)

    def center_control_delete_instance(self):
        payload = dmpv.centerControl_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)

        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.statusCodeAPIReturn(time.strftime("%Y-%m-%d %H:%M:%S"), str(r.status_code) + rsp["message"])
            # 检查字段是否标识为删除状态
            ccProperties = db_wc.deviceManageWebCheck("get_center_control_properties_by_id", payload["id"])
            self.assertEquals(ccProperties[3], 1, msg=self.base_message("中控删除状态")) # 1表示删除，0表示没删除
        else:
            self.assertEquals(True, False, msg=self.status_not_200+"%s" % r.status_code)

    def lock_add_instance_common(self):
        payload = dmpv.lock_addInstance(u"普通")
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)

        if r.status_code==200:
            rsp = json.loads(r.text)
            log.statusCodeAPIReturn(time.strftime("%Y-%m-%d %H:%M:%S"), str(r.status_code) + rsp["message"])
            db_wc.deviceManageWebCheck("get_center_control_properties_by_id", payload["id"])
        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code)


    @staticmethod
    def lock_add_instance_net():
        payload = dmpv.lock_addInstance(u"网络")
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def lock_add_instance_other():
        payload = dmpv.lock_addInstance(u"其他")
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def lock_updateInstance():
        payload = dmpv.lock_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def lock_deleteInstance():
        payload = dmpv.lock_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def water_add_instance():
        payload = dmpv.waterMeter_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def water_update_instance():
        payload = dmpv.waterMeter_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def water_delete_instance():
        payload = dmpv.waterMeter_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def electric_add_instance():
        payload = dmpv.electric_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def electric_update_instance():
        payload = dmpv.electric_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def electric_delete_instance():
        payload = dmpv.electric_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def caiji_add_instance():
        payload = dmpv.caiji_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def caiji_update_instance():
        payload = dmpv.caiji_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def caiji_delete_instance():
        payload = dmpv.caiji_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def menji_add_instance():
        print(u"请参考bug 933")

    @staticmethod
    def yangan_add_instance():
        payload = dmpv.yangan_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def yangan_update_instance():
        payload = dmpv.yangan_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def yangan_delete_instance():
        payload = dmpv.yangan_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def zhognji_add_instance():
        payload = dmpv.zhongji_addInstance()
        reqUrl = pu.devicesInstanceUrls()["addDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def zhongji_update_instance():
        payload = dmpv.zhongji_updateInstance()
        reqUrl = pu.devicesInstanceUrls()["updateDevUrl"]
        r = requests.post(reqUrl, data=payload)

    @staticmethod
    def zhongji_delete_instance():
        payload = dmpv.zhongji_deleteInstance()
        reqUrl = pu.devicesInstanceUrls()["deleteDevUrl"]
        r = requests.post(reqUrl, data=payload)

# a = deviceInstance()
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
# a.zhognji_addInstance()
# time.sleep(5)
# a.zhongji_updateInstance()
# time.sleep(4)
# a.zhongji_deleteInstance()
