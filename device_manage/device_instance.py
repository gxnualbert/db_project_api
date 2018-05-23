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
    status_not_200 = "返回状态码不为200!"

    def base_message(self, info):
        return "数据库存储的{info}跟实际传入的不一致".format(info=info)

    def test_center_control_add_instance(self):
        payload = dmpv.center_control_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.status_code_API_return(time.strftime("%Y-%m-%d %H:%M:%S"), str(r.status_code) + rsp["message"])
            center_control_properties = db_wc.device_manage_web_check("add_dev_url", payload["name"])
            # 校验类型，名字 name,model,net
            log.log("中控名字:{cc_name}；中控类型:{cc_type}；中控网络属性:{cc_net}".format(
                cc_name=center_control_properties[0],
                cc_type=center_control_properties[1],
                cc_net=center_control_properties[2]))
            self.assertEquals(center_control_properties[0], payload["name"], msg=self.base_message("中控名字"))
            self.assertEquals(center_control_properties[1], payload["model"], msg=self.base_message("中控类型"))
            self.assertEquals(center_control_properties[2], int(payload["net"]), msg=self.base_message("中控网络属性"))
        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code)

    def center_control_update_instance(self):
        payload = dmpv.center_control_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload)

        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.status_code_API_return(time.strftime("%Y-%m-%d %H:%M:%S"), str(r.status_code) + rsp["message"])
            center_control_properties = db_wc.device_manage_web_check("get_center_control_properties_by_name", payload["name"])
            # 校验类型，名字 name,model,net
            log.log("中控名字:{cc_name}；中控类型:{cc_type}；中控网络属性:{cc_net}".format(cc_name=center_control_properties[0],
                                                                           cc_type=center_control_properties[1],
                                                                           cc_net=center_control_properties[2]))
            self.assertEquals(center_control_properties[0], payload["name"], msg=self.base_message("中控名字"))
            self.assertEquals(center_control_properties[1], payload["model"], msg=self.base_message("中控类型"))
            self.assertEquals(center_control_properties[2], int(payload["net"]), msg=self.base_message("中控网络属性"))
        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code)

    def center_control_delete_instance(self):
        payload = dmpv.center_control_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload)

        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.status_code_API_return(time.strftime("%Y-%m-%d %H:%M:%S"), str(r.status_code) + rsp["message"])
            # 检查字段是否标识为删除状态
            center_control_properties = db_wc.device_manage_web_check("get_center_control_properties_by_id", payload["id"])
            self.assertEquals(center_control_properties[3], 1, msg=self.base_message("中控删除状态"))  # 1表示删除，0表示没删除
        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code)

    def lock_add_instance_common(self):
        payload = dmpv.lock_add_instance(u"普通")
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.status_code_API_return(time.strftime("%Y-%m-%d %H:%M:%S"), str(r.status_code) + rsp["message"])
            db_wc.device_manage_web_check("get_center_control_properties_by_id", payload["id"])
        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code)

    @staticmethod
    def lock_add_instance_net():
        payload = dmpv.lock_add_instance(u"网络")
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def lock_add_instance_other():
        payload = dmpv.lock_add_instance(u"其他")
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def lock_update_instance():
        payload = dmpv.lock_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def lock_delete_instance():
        payload = dmpv.lock_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def water_add_instance():
        payload = dmpv.water_meter_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def water_update_instance():
        payload = dmpv.water_meter_update_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def water_delete_instance():
        payload = dmpv.water_meter_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def electric_add_instance():
        payload = dmpv.electric_meter_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def electric_update_instance():
        payload = dmpv.electric_meter_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def electric_delete_instance():
        payload = dmpv.electric_meter_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def collector_add_instance():
        payload = dmpv.collector_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def collector_update_instance():
        payload = dmpv.collector_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def collector_delete_instance():
        payload = dmpv.collector_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def door_access_add_instance():
        print(u"请参考bug 933")

    @staticmethod
    def smoke_detector_add_instance():
        payload = dmpv.smoke_detector_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def smoke_detector_update_instance():
        payload = dmpv.smoke_detector_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def smoke_detector_delete_instance():
        payload = dmpv.smoke_detector_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def repeater_add_instance():
        payload = dmpv.repeater_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def repeater_update_instance():
        payload = dmpv.repeater_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload)

    @staticmethod
    def repeater_delete_instance():
        payload = dmpv.repeater_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload)
