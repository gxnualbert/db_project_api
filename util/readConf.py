#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: readConf.py
@time: 2018/05/14/11:45
"""
import ConfigParser
import os


class ReadConfigFile():
    aa=os.path.abspath(os.path.join(os.getcwd(), ".."))
    confPath=aa+"\\conf.cfg"
    # confPath=os.getcwd()+"\\conf.cfg"
    cf = ConfigParser.ConfigParser()
    cf.read(confPath)

    def getBasicConf(self):
        host=self.cf.get("BasicConf", "host")
        username=self.cf.get("BasicConf", "username")
        password=self.cf.get("BasicConf", "password")
        projectUrlprefix="http://"+host+":8001"
        confinfo={}
        confinfo["host"]=host
        confinfo["username"]=username
        confinfo["password"]=password
        confinfo["projectUrlprefix"]=projectUrlprefix

        return confinfo


class ResTestQ():

    aa="eeee"
    @staticmethod
    def albertggg():
        gte={}
        gte["hhh"]="kkkkkkkkk"


        return gte

