#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: readConf.py
@time: 2018/05/14/11:45
"""
import configparser
import os


class ReadConfigFile(object):
    aa = os.path.abspath(os.path.join(os.getcwd(), ".."))
    # confPath=aa+"\\conf.cfg"
    conf_path = aa + "\\db_project_api\\conf.cfg"
    # confPath=os.getcwd()+"\\conf.cfg"
    cf = configparser.ConfigParser()
    cf.read(conf_path, encoding='UTF-8')

    def get_basic_conf(self):
        host = self.cf.get("BasicConf", "host")
        username = self.cf.get("BasicConf", "username")
        password = self.cf.get("BasicConf", "password")
        project_url_prefix = "http://" + host + ":8001"
        conf_info = dict()
        conf_info["host"] = host
        conf_info["username"] = username
        conf_info["password"] = password
        conf_info["project_url_prefix"] = project_url_prefix

        return conf_info

