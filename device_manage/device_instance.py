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
from util.common_util import Util

class DeviceInstance(unittest.TestCase):
    status_not_200 = "返回状态码不为200!接口返回状态码为："
    # 中控
    cc_name = "中控名字"
    cc_model = "中控型号"
    cc_net_type = "中控网络类型"
    cc_id = "中控id"
    # 门锁
    lock_name = "门锁名字"
    lock_model = "门锁型号"
    lock_net_type = "门锁网络类型"
    lock_id = "门锁id"
    # 水表
    water_name = "水表名字"
    water_model = "水表型号"
    water_net_type = "水表网络类型"
    water_id = "水表id"
    # 电表
    electric_name = "电表名字"
    electric_model = "电表型号"
    electric_net_type = "电表网络类型"
    electric_id = "电表id"
    # 采集器
    collector_name = "采集器名字"
    collector_model = "采集器型号"
    collector_net_type = "采集器网络类型"
    collector_id = "采集器id"
    # 烟感
    smoke_detector_name = "烟感名字"
    smoke_detector_model = "烟感型号"
    smoke_detector_net_type = "烟感网络类型"
    smoke_detector_id = "烟感id"
    # 中继器
    repeater_name = "中继器名字"
    repeater_model = "中继器型号"
    repeater_net_type = "中继器网络类型"
    repeater_id = "中继器id"
    ck = Util.get_cookies()
    def base_message(self, info):
        return "数据库存储的{info}跟实际传入的不一致".format(info=info)

    def result_check(self, r, operate_time, payload, sql_type, sql_para, device_name, device_model, device_net_type,
                     device_id, is_del_check=False):
        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.status_code_API_return(operate_time, str(r.status_code) + rsp["message"])
            query_result = db_wc.device_manage_web_check(sql_type, sql_para)
            # 校验类型，名字 name,model,net
            if is_del_check:
                log.log("数据库中该设备状态为：%s. (1表示删除，0表示没删除) 设备id为：%s" % (query_result[3], query_result[4]))
                self.assertEquals(query_result[3], 1, msg=self.base_message("中控删除状态"))  # 1表示删除，0表示没删除
            else:
                log.log((device_name + ":{device_name}；" + device_model + ":{device_model}；" + device_net_type
                         + ":{device_net_type}；" + device_id + ":{device_id}").format(
                    device_name=query_result[0],
                    device_model=query_result[1],
                    device_net_type=query_result[2],
                    device_id=query_result[4]))
                self.assertEquals(query_result[0], payload["name"], msg=self.base_message(device_name))
                self.assertEquals(query_result[1], payload["model"], msg=self.base_message(device_model))
                if query_result[2]:  # 有时候部分设备（如中继器）的网络类型是空的，只有不为空的时候，才做比较
                    self.assertEquals(str(query_result[2]), payload["net"], msg=self.base_message(device_net_type))
        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code)

    def center_control_add_instance(self):
        payload = dmpv.center_control_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"], self.cc_name,
                          self.cc_model,
                          self.cc_net_type, self.cc_id)

    def center_control_update_instance(self):
        payload = dmpv.center_control_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.cc_name, self.cc_model,
                          self.cc_net_type, self.cc_id)

    def center_control_delete_instance(self):
        payload = dmpv.center_control_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)

        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_id", payload["id"], "", "", "",
                          self.cc_id, True)

    def lock_add_instance_common(self):
        payload = dmpv.lock_add_instance(u"普通")
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)

        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"], self.lock_name,
                          self.lock_model, self.lock_net_type, self.lock_id)

    def lock_add_instance_net(self):
        payload = dmpv.lock_add_instance(u"网络")
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)

        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"], self.lock_name,
                          self.lock_model, self.lock_net_type, self.lock_id)

    def lock_add_instance_other(self):
        payload = dmpv.lock_add_instance(u"其他")
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"], self.lock_name,
                          self.lock_model, self.lock_net_type, self.lock_id)

    def lock_update_instance(self):
        payload = dmpv.lock_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"], self.lock_name,
                          self.lock_model, self.lock_net_type, self.lock_id)

    def lock_delete_instance(self):
        payload = dmpv.lock_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_id", payload["id"], "", "", "",
                          self.lock_id, True)

    def water_add_instance(self):
        payload = dmpv.water_meter_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"], self.water_name,
                          self.water_model, self.water_net_type, self.water_id)

    def water_update_instance(self):
        payload = dmpv.water_meter_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"], self.water_name,
                          self.water_model, self.water_net_type, self.water_id)

    def water_delete_instance(self):
        payload = dmpv.water_meter_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_id", payload["id"], "", "", "",
                          self.water_id, True)

    def electric_add_instance(self):
        payload = dmpv.electric_meter_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.electric_name,
                          self.electric_model, self.electric_net_type, self.electric_id)

    def electric_update_instance(self):
        payload = dmpv.electric_meter_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.electric_name,
                          self.electric_model, self.electric_net_type, self.electric_id)

    def electric_delete_instance(self):
        payload = dmpv.electric_meter_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_id", payload["id"], "", "", "",
                          self.electric_id, True)

    def collector_add_instance(self):
        payload = dmpv.collector_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.collector_name,
                          self.collector_model, self.collector_net_type, self.collector_id)

    def collector_update_instance(self):
        payload = dmpv.collector_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.collector_name,
                          self.collector_model, self.collector_net_type, self.collector_id)

    def collector_delete_instance(self):
        payload = dmpv.collector_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_id", payload["id"], "", "", "",
                          self.collector_id, True)

    def door_access_add_instance(self):
        self.assertEquals(True,False,msg="请参考bug 933")

    def smoke_detector_add_instance(self):
        payload = dmpv.smoke_detector_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.smoke_detector_name,
                          self.smoke_detector_model, self.smoke_detector_net_type, self.smoke_detector_id)

    def smoke_detector_update_instance(self):
        payload = dmpv.smoke_detector_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.smoke_detector_name,
                          self.smoke_detector_model, self.smoke_detector_net_type, self.smoke_detector_id)

    def smoke_detector_delete_instance(self):
        payload = dmpv.smoke_detector_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_id", payload["id"], "", "", "",
                          self.smoke_detector_id, True)

    def repeater_add_instance(self):
        payload = dmpv.repeater_add_instance()
        req_url = pu.devices_instance_urls()["add_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.repeater_name,
                          self.repeater_model, "", self.repeater_id)

    def repeater_update_instance(self):
        payload = dmpv.repeater_update_instance()
        req_url = pu.devices_instance_urls()["update_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_name", payload["name"],
                          self.repeater_name,
                          self.repeater_model, self.repeater_net_type, self.repeater_id)

    def repeater_delete_instance(self):
        payload = dmpv.repeater_delete_instance()
        req_url = pu.devices_instance_urls()["delete_dev_url"]
        r = requests.post(req_url, data=payload,cookies=self.ck)
        operate_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.result_check(r, operate_time, payload, "get_device_properties_by_id", payload["id"], "", "", "",
                          self.repeater_id, True)
