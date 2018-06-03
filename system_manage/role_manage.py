#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: role_manage.py
@time: 2018/05/19/11:34
"""
import datetime
import unittest

import requests

from util.common_util import Util
from util.danbay_database import DataBaseValidateWebResult as db_wc
from util.log_tool import AddLog as log
from util.parameter_value import SystemManageParamsValue as smpv
from util.request_url import ProjectUrls as pu


class RoleManage(unittest.TestCase):
    ck = Util.get_cookies()
    status_not_200 = "返回状态码不为200!接口返回状态码为："

    # 系统管理--角色管理
    log_id = "角色id："
    log_name = "角色名称："
    log_ext = "角色描述信息："
    log_del = "角色是否删除(1-删除,0-正常):"
    log_group_type = "角色类型（1-超级管理员,2-管理员,3-一般用户）："

    def result_check(self, r, operate_time, payload, query_args, **kwargs):

        if r.status_code == 200:
            log.status_code_API_return(operate_time, str(r.status_code))
            for k, v in kwargs.items():
                if v == "get_user_group":
                    # id,name,ext,del,groupType
                    group_query_result = db_wc.system_manager_web_check(v, query_args)
                    if group_query_result:
                        log.log((
                                self.log_id + "{log_id}；" +
                                self.log_name + "{log_name}；" +
                                self.log_ext + "{log_ext}；" +
                                self.log_del + "{log_del}；" +
                                self.log_group_type + "{log_group_type}；"

                        ).format(
                            log_id=group_query_result[0],
                            log_name=group_query_result[1],
                            log_ext=group_query_result[2],
                            log_del=group_query_result[3],
                            log_group_type=group_query_result[4],
                        ))
                        if query_args[0] == "id":
                            self.assertEquals(payload["groupId"], group_query_result[0],
                                              msg=Util.base_message("角色状态"))
                        else:
                            self.assertEquals(payload[query_args[0]], group_query_result[1],
                                              msg=Util.base_message(payload["name"]))

                    else:
                        log.log("查询数据库时，返回空值！！！！")

        else:
            self.assertEquals(True, False, msg=self.status_not_200 + "%s" % r.status_code + "。报错信息为：" + r.text)

    def add_user_group(self):
        payload = smpv.add_user_group()
        req_url = pu.system_manage_urls()["add_user_group_url"]
        r = requests.post(req_url, json=payload, cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, ("name", payload["name"]), query_type="get_user_group")

    def update_user_group(self):
        payload = smpv.update_user_group()
        req_url = pu.system_manage_urls()["update_user_group_url"]
        r = requests.post(req_url, json=payload, cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, ("name", payload["name"]), query_type="get_user_group")

        # 更新权限设置

    def update_user_group_setting(self):
        payload = smpv.update_user_group()

    def delete_user_group(self):
        payload = smpv.delete_user_group()
        req_url = pu.system_manage_urls()["delete_user_group_url"]
        r = requests.post(req_url, data=payload, cookies=self.ck)
        operate_time = datetime.datetime.now().strftime("%H:%M:%S.%f")
        self.result_check(r, operate_time, payload, ("id", payload["groupId"]), query_type="get_user_group")
