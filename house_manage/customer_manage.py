#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: customerManage.py
@time: 2018/05/17/9:13
"""
import datetime
import json
import time
import unittest

import requests

from util.danbay_database import DataBase as db
from util.danbay_database import DataBaseValidateWebResult as db_wc
from util.log_tool import AddLog as log
from util.parameter_value import HouseManageParamsValue as hmpv
from util.request_url import ProjectUrls as pu
from util.common_util import Util

class CustomerManage(unittest.TestCase):
    # 全局变量
    home_provider_name = ""
    home_source_name = ""
    home_source_id = ""
    provider_id = ""
    home_no = ""
    space_id = ""
    status_not_200 = "返回状态码不为200!接口返回状态码为："
    # 日志记录部分，不能与上面全局变量部分冲突
    log_enterpriser_name = "企业账号"
    log_home_provider_name = "房源提供者"
    log_provider_record_id = "房源提供者标致ID"
    log_provider_del_status = "房源提供者记录删除状态"

    log_home_source_addr = "房源地址"
    log_home_source_type = "房源类型"
    log_home_source_recorde_id = "房源地址标致ID"
    log_home_source_type = "房源类型"
    log_home_source_del_status = "房源删除状态"

    log_space_id = "空间id"
    log_space_home_no = "房间编号"
    log_space_floor_num = "楼层编号"
    log_space_del_status = "空间删除状态"
    log_space_is_public = "空间类型"  # 是否为公共空间:0-不是,1-是
    log_home_type = "房间类型"  # 房间类型:主卧、次卧、客厅、走廊等
    ck=Util.get_cookies()

    def base_message(self, info):
        return "数据库存储的{info}跟实际传入的不一致".format(info=info)

    def add_home_provider_serials(self):
        # 批量添加房源信息，空间信息
        payload = hmpv.add_house_provider()
        home_provider_name = hmpv.add_house_provider()["providerName"]
        req_url = pu.house_manage_urls()["add_home_source_provider_url"]
        r = requests.post(req_url, json=payload)
        rsp = json.loads(r.text)
        # 添加房源信息
        if r.status_code == 200:
            provider_id = db.house_source_sql("get_provider_name_and_id", home_provider_name)
            payload = hmpv.add_house_source()
            payload["providerId"] = provider_id
            req_url = pu.house_manage_urls()["add_home_source_url"]
            r = requests.post(req_url, json=payload)
            home_source_name = payload["homeSourceName"]

            if r.status_code:
                # 添加空间信息
                payload = hmpv.add_space()
                payload["homeSourceId"] = db.house_source_sql("get_home_source_id", home_source_name)
                req_url = pu.house_manage_urls()["add_space_url"]
                r = requests.post(req_url, json=payload)
            else:
                pass
        else:
            pass

    def result_check(self, r, operate_time, payload, query_args, **kwargs):
        if r.status_code == 200:
            rsp = json.loads(r.text)
            log.status_code_API_return(operate_time, str(r.status_code))
            for k, v in kwargs.items():
                if v == "get_home_provider_info":
                    query_result = db_wc.house_manage_web_check(v, query_args)
                    # 检查provider name，删除状态，id  id,providerName,del,enterpriseAccountId
                    if query_result:
                        log.log((self.log_enterpriser_name + "：{enterpriseAccountId}，" +
                                 self.log_home_provider_name + "：{home_provider}，" +
                                 self.log_provider_record_id + "：{id}," +
                                 self.log_provider_del_status + ":{del_status}").format(
                            enterpriseAccountId=query_result[3],
                            home_provider=query_result[1],
                            id=query_result[0],
                            del_status=query_result[2]
                        ))
                        self.assertEquals(payload["providerName"], query_result[1],
                                          msg=self.base_message(self.log_enterpriser_name))

                        if k == "del_home_source":
                            self.assertEquals(payload["del_status"], query_result[2],
                                              msg=self.base_message(self.log_space_del_status))
                            self.assertEquals(payload["id"],query_result[6],msg=self.base_message(self.log_provider_record_id))
                    else:
                        self.assertIsNotNone(query_result,
                                             msg=time.strftime("%Y-%m-%d %H:%M:%S") + '查询数据库是，返回空值，没有该条记录')
                elif v == "get_home_source_info":
                    query_result = db_wc.house_manage_web_check(v, query_args)
                    # check database 检查 homeSourceName, providerId,id,types,删除状态
                    # 检查 id,types,providerId,homeSourceName,del 删除状态
                    # id,types,providerId,homeSourceName,del
                    if query_result:
                        log.log((
                                self.log_home_source_addr + "：{log_home_source_addr}," +
                                self.log_provider_record_id + ":{log_provider_record_id}" +
                                self.log_home_source_recorde_id + ":{log_home_source_recorde_id}" +
                                self.log_home_source_type + ":{log_home_source_type}" +
                                 self.log_home_source_del_status + ":{log_home_source_del_status}"
                        ).format(
                            log_home_source_addr=query_result[3],
                            log_provider_record_id=query_result[2],
                            log_home_source_recorde_id=query_result[0],
                            log_home_source_type=query_result[1],
                            log_home_source_del_status=query_result[4]
                        ))
                        self.assertEquals(payload["homeSourceName"], query_result[3],
                                          msg=self.base_message(self.log_home_source_addr))
                        self.assertEquals(int(payload["providerId"]), query_result[2],
                                          msg=self.base_message(self.log_provider_record_id))
                        self.assertEquals(int(payload["types"]), query_result[1],
                                          msg=self.base_message(self.log_home_source_type))
                        if k == "del_home_source":
                            self.assertEquals(payload["del_status"], query_result[4],
                                              msg=self.base_message(self.log_home_source_del_status))
                    else:
                        self.assertIsNotNone(query_result,
                                             msg=time.strftime("%Y-%m-%d %H:%M:%S") + '查询数据库是，返回空值，没有该条记录')
                elif v == "get_space_info":
                    query_result = db_wc.house_manage_web_check(v, query_args)
                    if query_result:
                        # id,homeSourceId,homeNo,isPublic,floorNum,homeType,del
                        log.log(
                            (
                                    self.log_space_id + "：{log_space_id};" +
                                    self.log_home_source_recorde_id + "：{log_home_source_recorde_id};" +
                                    self.log_space_home_no + "：{log_space_home_no};" +
                                    self.log_space_is_public + ":{log_space_is_public};" +
                                    self.log_space_floor_num + "：{log_space_floor_num};" +
                                    self.log_home_type + ":{log_home_type};" +
                                    self.log_space_del_status + "：{log_space_del_status};"
                            ).format
                                (
                                log_space_id=query_result[0],
                                log_home_source_recorde_id=query_result[1],
                                log_space_home_no=query_result[2],
                                log_space_is_public=query_result[3],
                                log_space_floor_num=query_result[4],
                                log_home_type=query_result[5],
                                log_space_del_status=query_result[6]
                            )
                        )
                        self.assertEquals(payload["floorNum"], query_result[4],
                                          msg=self.base_message(self.log_space_floor_num))
                        self.assertEquals(payload["homeNo"], query_result[2],
                                          msg=self.base_message(self.log_space_home_no))
                        self.assertEquals(payload["homeSourceId"], query_result[1],
                                          msg=self.base_message(self.log_home_source_recorde_id))
                        if k == "del_space":
                            self.assertEquals(payload["del_status"], query_result[6],
                                              msg=self.base_message(self.log_space_del_status))
                    else:
                        self.assertIsNotNone(query_result,
                                             msg=time.strftime("%Y-%m-%d %H:%M:%S") + '查询数据库是，返回空值，没有该条记录')
        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code + "。报错信息为：" + r.text)

    def add_home_provider(self):
        payload = hmpv.add_house_provider()
        CustomerManage.home_provider_name = payload["providerName"]
        req_url = pu.house_manage_urls()["add_home_source_provider_url"]
        aa=self.ck
        r = requests.post(req_url, json=payload,cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        # 检查provider name
        self.result_check(r, operate_time, payload, payload["providerName"], query_type="get_home_provider_info")

    def batch_delete_home_provider(self):
        pass

    def add_house_source(self):

        payload = hmpv.add_house_source()
        payload["providerId"] = db.house_source_sql("get_provider_name_and_id", CustomerManage.home_provider_name)

        req_url = pu.house_manage_urls()["add_home_source_url"]
        r = requests.post(req_url, json=payload,cookies=self.ck)
        CustomerManage.home_source_name = payload["homeSourceName"]
        CustomerManage.addrCode = payload["addrCode"]
        CustomerManage.provider_id = payload["providerId"]
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, payload["homeSourceName"], query_type="get_home_source_info")

    def update_house_source(self):

        payload = hmpv.update_house_source()
        payload["id"] = db.house_source_sql("get_home_source_id", CustomerManage.home_source_name)
        payload["providerId"] = str(CustomerManage.provider_id)
        req_url = pu.house_manage_urls()["update_home_source_url"]
        r = requests.post(req_url, json=payload,cookies=self.ck)

        # 检查 homeSourceName, providerId,id,types,删除状态
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        CustomerManage.home_source_name = payload["homeSourceName"]
        self.result_check(r, operate_time, payload, payload["homeSourceName"], query_type="get_home_source_info")

    # 添加空间
    def add_space(self):
        payload = hmpv.add_space()
        payload["homeSourceId"] = db.house_source_sql("get_home_source_id", CustomerManage.home_source_name)
        req_url = pu.house_manage_urls()["add_space_url"]
        r = requests.post(req_url, json=payload,cookies=self.ck)
        CustomerManage.home_source_id = payload["homeSourceId"]
        CustomerManage.home_no = payload["homeNo"]
        # homelist 检查id，homeSourceId，homeNo,floorNum,del
        # 通过homeSourceId，homeNo确定space 的id
        CustomerManage.space_id = db_wc.house_manage_web_check("get_space_id", payload["homeSourceId"],
                                                               payload["homeNo"])
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, CustomerManage.space_id, query_type="get_space_info")

    def update_space(self):
        payload = hmpv.update_space()
        payload["homeSourceId"] = CustomerManage.home_source_id
        payload["id"] = db.house_source_sql("get_space_id", CustomerManage.home_no)
        req_url = pu.house_manage_urls()["update_space_url"]
        r = requests.post(req_url, json=payload,cookies=self.ck)
        CustomerManage.home_source_id = payload["homeSourceId"]
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, CustomerManage.space_id, query_type="get_space_info")

    def delete_space(self):
        space_id = hmpv.delete_space()
        req_url = pu.house_manage_urls()["delete_space_url"] + str(space_id) + "/deleteRecordById"
        r = requests.get(req_url,cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        # 获取删除后的信息
        payload = dict()
        query_result = db_wc.house_manage_web_check("get_space_info", space_id)
        # id,homeSourceId,homeNo,isPublic,floorNum,homeType,del
        payload["floorNum"] = query_result[4]
        payload["homeNo"] = query_result[2]
        payload["homeSourceId"] = query_result[1]
        payload["del_status"] = query_result[6]
        self.result_check(r, operate_time, payload, CustomerManage.space_id, query_type="get_space_info",
                          del_space=True)

    def delete_house_source(self):
        house_source_id = hmpv.delete_house_source()
        req_url = pu.house_manage_urls()["delete_home_source_url"] + str(house_source_id) + "/deleteRecordById"
        r = requests.get(req_url,cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        # id,types,providerId,homeSourceName,del
        query_result = db_wc.house_manage_web_check("get_home_source_info", CustomerManage.home_source_name)
        payload = dict()
        payload["homeSourceName"] = query_result[3]
        payload["providerId"] = query_result[2]
        payload["types"] = query_result[1]
        payload["del"] = query_result[4]
        self.result_check(r, operate_time, payload, CustomerManage.home_source_name, query_type="get_home_source_info",
                          del_home_source=True)

    def delete_home_provider(self):
        home_provide_id = hmpv.delete_house_provider()
        req_url = pu.house_manage_urls()["delete_home_source_provider"] + str(home_provide_id) + "/deleteRecordById"
        r = requests.get(req_url,cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        query_result = db_wc.house_manage_web_check("get_home_provider_info", CustomerManage.home_provider_name)
        # id,providerName,del,enterpriseAccountId
        payload = dict()

        payload["del_status"]=query_result[2]
        payload["id"]=query_result[0]
        self.result_check(r, operate_time, payload, CustomerManage.home_source_name, query_type="get_home_provider_info",
                          del_home_source=True)
