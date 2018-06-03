#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: common_util.py
@time: 2018/06/02/17:52
"""
import requests

from util.read_conf import ReadConfigFile
from util.request_url import ProjectUrls as pu


class Util(object):
    rcf = ReadConfigFile()
    username = rcf.get_basic_conf()["username"]
    password = rcf.get_basic_conf()["password"]

    @staticmethod
    def get_cookies():
        # 该方法中，如果从parameter_value 中引用payload，会产生环形引用错误，因此在这里写payload
        login_url = pu.login_url()
        payload = {"userName": Util.username, "password": Util.password}
        r = requests.post(login_url, json=payload)
        return r.cookies
    @staticmethod
    def base_message(info):
        return "数据库存储的{info}跟实际传入的不一致".format(info=info)