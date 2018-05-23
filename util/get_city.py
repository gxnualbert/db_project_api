#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: getCity.py
@time: 2018/05/18/8:48
"""

import json
import os
import random


class GetCity():

    @staticmethod
    def get_house_addr():
        city_file_prefix_path = os.getcwd().split("db_project_api")[0]
        city_file = city_file_prefix_path + "db_project_api\\util\\city.txt"
        with open(city_file, "r", encoding='UTF-8') as f:
            city = f.read()
        china = json.loads(city)
        province_id = random.randint(0, (len(china) - 1))
        province_name = china[province_id][1]
        detail_addr = {}
        # 判断是否有市
        if china[province_id][2]:
            city_list = china[province_id][2]
            city_id = random.randint(0, (len(city_list) - 1))
            city_name = city_list[city_id][1]
            # 判断是否有县区
            if city_list[city_id][2]:
                section_list = city_list[city_id][2]
                section_id = random.randint(0, (len(section_list) - 1))
                section_name = section_list[section_id][1]
                # print  sectionList[sectionID][0],provinceName,cityName,sectionName
                detail_addr["address_code"] = section_list[section_id][0]
                detail_addr["province"] = province_name
                detail_addr["city_name"] = city_name
                detail_addr["section_name"] = section_name
                return detail_addr
            else:
                # print cityList[cityId][0],provinceName,cityName
                detail_addr["address_code"] = city_list[city_id][0]
                detail_addr["province_name"] = province_name
                detail_addr["city_name"] = city_name
                return detail_addr
        else:

            detail_addr["province_name"] = province_name
            return detail_addr
