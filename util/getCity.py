#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: getCity.py
@time: 2018/05/18/8:48
"""

import json
import random
import os
class getCity():
    @staticmethod
    def getHouseAddr():
        cityFilePrePath=os.getcwd().split("db_project_api")[0]
        cityFile=cityFilePrePath+"db_project_api\\util\\city.txt"
        with open(cityFile, "r") as f:
            city = f.read()
        china=json.loads(city)
        provinceId=random.randint(0,(len(china)-1))
        provinceName=china[provinceId][1]
        detailAddr = {}
        #判断是否有市
        if china[provinceId][2]:
            cityList=china[provinceId][2]
            cityId=random.randint(0,(len(cityList)-1))
            cityName = cityList[cityId][1]
            #判断是否有县区
            if cityList[cityId][2]:
                sectionList=cityList[cityId][2]
                sectionID=random.randint(0,(len(sectionList)-1))
                sectionName=sectionList[sectionID][1]
                # print  sectionList[sectionID][0],provinceName,cityName,sectionName
                detailAddr["addrcode"]=sectionList[sectionID][0]
                detailAddr["province"]=provinceName
                detailAddr["cityName"]=cityName
                detailAddr["sectionName"]=sectionName
                return detailAddr
            else:
                # print cityList[cityId][0],provinceName,cityName
                detailAddr["addrcode"] = cityList[cityId][0]
                detailAddr["provinceName"]=provinceName
                detailAddr["cityName"]=cityName
                return detailAddr
        else:
            # print provinceName

            # detailAddr["provinceName"]=provinceName
            detailAddr["provinceName"]=provinceName
            return detailAddr

