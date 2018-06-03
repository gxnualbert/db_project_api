#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: user_manage.py
@time: 2018/06/03/16:22
"""
import datetime
import unittest

import requests

from util.common_util import Util
from util.danbay_database import DataBaseValidateWebResult as db_wc
from util.log_tool import AddLog as log
from util.parameter_value import SystemManageParamsValue as smpv
from util.request_url import ProjectUrls as pu


class UserManage(unittest.TestCase):
    ck = Util.get_cookies()
    status_not_200 = "返回状态码不为200!接口返回状态码为："

    # 系统管理--用户管理
    log_username = "用户名："
    log_nickname = "昵称:"
    log_phone = "手机号:"
    log_group_id = "所属用户组id:"
    log_company_name = "企业名称:"
    log_del = "是否删除(1-删除,0-正常)："
    log_states = "状态:(0-启用,1-禁用)："

    def result_check(self, r, operate_time, payload, query_args, **kwargs):
        if r.status_code == 200:
            log.status_code_API_return(operate_time, str(r.status_code))
            for k, v in kwargs.items():
                if v == "get_user_info":
                    user_query_result = db_wc.system_manager_web_check(v, query_args)
                    if user_query_result:
                        log.log((
                                self.log_username + "{log_username}；" +
                                self.log_nickname + "{log_nickname}；" +
                                self.log_phone + "{log_phone}；" +
                                self.log_group_id + "{log_group_id}；" +
                                self.log_company_name + "{log_company_name}；" +
                                self.log_del + "{log_del}；" +
                                self.log_states + "{log_states}；"
                        ).format(
                            log_username=user_query_result[1],
                            log_nickname=user_query_result[2],
                            log_phone=user_query_result[6],
                            log_group_id=user_query_result[0],
                            log_company_name=user_query_result[3],
                            log_del=user_query_result[4],
                            log_states=user_query_result[5],
                        ))
                        if v == "get_user_info_by_id":
                            self.assertEquals(1, user_query_result[4],
                                              msg=Util.base_message("删除状态"))
                        else:
                            self.assertEquals(payload["userName"], user_query_result[1],
                                              msg=Util.base_message(payload["userName"]))
                            self.assertEquals(payload["phone"], user_query_result[6],
                                              msg=Util.base_message(payload["phone"]))
                            self.assertEquals(payload["nickName"], user_query_result[2],
                                              msg=Util.base_message(payload["nickName"]))
                            self.assertEquals(payload["groupId"], user_query_result[0],
                                              msg=Util.base_message(payload["groupId"]))
                            self.assertEquals(payload["states"], str(user_query_result[5]),
                                              msg=Util.base_message(payload["states"]))
                            self.assertEquals(payload["companyName"], user_query_result[3],
                                              msg=Util.base_message(payload["companyName"]))
                    else:
                        log.log("查询数据库时，返回空值！！！！")
        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code + "。报错信息为：" + r.text)

    def add_user_info(self):
        payload = smpv.add_user_info()
        req_url = pu.system_manage_urls()["add_user_info_url"]
        r = requests.post(req_url, json=payload, cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, ("userName", payload["userName"]), query_type="get_user_info")

    def update_user_info(self):
        payload = smpv.update_user_info()
        req_url = pu.system_manage_urls()["update_user_info_url"]
        r = requests.post(req_url, json=payload, cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, ("userName", payload["userName"]), query_type="get_user_info")

    def delete_user_info(self):
        payload = smpv.delete_user_info()
        req_url = pu.system_manage_urls()["delete_user_info_url"]
        r = requests.post(req_url, data=payload, cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, ("id", payload["userId"]), query_type="get_user_info_by_id")
