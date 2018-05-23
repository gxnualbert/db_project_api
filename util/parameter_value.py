#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: paraMeterValue.py
@time: 2018/05/14/18:24
"""
import base64
import json
import os
import random
import sys
import time

import requests

from util.danbay_database import DataBase as db
from util.get_city import GetCity as gc
from util.request_url import ProjectUrls as pu


class DeviceManageParamsValue(object):
    # 中控
    ceter_control_name = u"auto中控" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    center_control_id = ""
    center_control_model = "GW_auto" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    # 更新中控
    update_center_control_name = u"更新中控名字" + time.strftime('%H%M', time.localtime(time.time()))
    update_center_control_model = u"upda中控" + time.strftime('%m%d%H%M', time.localtime(time.time()))

    # 门锁
    lock_name = u"auto门锁" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    lock_id= ""
    lock_model = "lk_auto" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    # 更新门锁
    update_lock_name = u"upda门锁" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    # LOCK_UPDATE_INSTANCE_NAME = u"upda门锁" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    update_lock_model = u"upda门锁" + time.strftime('%m%d%H%M', time.localtime(time.time()))

    # 水表
    water_meter_name = u"auto水表" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    water_meter_id = ""
    water_meter_model = "wm_auto" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    # 更新水表
    update_water_meter_name = "WM_hot" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    update_water_meter_model = "WM_hot" + time.strftime('%m%d%H%M', time.localtime(time.time()))

    # 电表
    electric_meter_name = u"auto电表" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    electric_meter_id = ""
    electric_meter_model = "em_auto" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    # 更新电表
    update_electric_name = "emupda" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    update_electric_model = "emupda" + time.strftime('%m%d%H%M', time.localtime(time.time()))

    # 采集器
    collector_name = u"auto电采" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    collector_id = ""
    collector_model = u"电采_auto" + time.strftime('%H%M', time.localtime(time.time()))
    # 更新采集器
    update_collector_name = u"水采Update" + time.strftime('%H%M', time.localtime(time.time()))
    update_collector_model = u"水采Update" + time.strftime('%H%M', time.localtime(time.time()))

    # 烟感
    smoke_detector_name = u"auto烟感" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    smoke_detector_id = ""
    smoke_detector_model = u"烟感_auto" + time.strftime('%H%M', time.localtime(time.time()))
    # 更新烟感
    update_smoke_detector_name = u"烟感Update" + time.strftime('%H%M', time.localtime(time.time()))
    update_smoke_detector_model = u"烟感Update" + time.strftime('%H%M', time.localtime(time.time()))

    # 中继
    repeater_name = u"auto中继" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    repeater_id = ""
    repeater_model = u"中继_auto" + time.strftime('%H%M', time.localtime(time.time()))

    # 更新中继
    update_repeater_name = u"中继Update" + time.strftime('%H%M', time.localtime(time.time()))
    update_repeater_model = u"中继Update" + time.strftime('%H%M', time.localtime(time.time()))

    # 更新设备属性

    @staticmethod
    def add_instance(img, name, types, model, cost, net, correspond, wire, type_id):
        img = DeviceManageParamsValue.get_img_path(img)
        add_instance_payload = {"name": name,
                                "types": types,
                                "model": model,
                                "cost": cost,
                                "net": net,
                                "correspond": correspond,
                                "wire": wire,
                                "typeId": type_id,
                                "images": img
                                }
        return add_instance_payload

    @staticmethod
    def update_instance(img, name, types, model, cost, net, correspond, wire, id):
        img = DeviceManageParamsValue.get_img_path(img)

        update_instance_payload = {"name": name,
                                   "types": types,
                                   "cost": cost,
                                   "correspond": correspond,
                                   "wire": wire,
                                   "model": model,
                                   "net": net,
                                   "images": img,
                                   "id": id
                                   }
        return update_instance_payload

    @staticmethod
    def delete_instance(id):
        delete_instance_payload = dict()
        delete_instance_payload["id"] = id
        return delete_instance_payload

    @staticmethod
    def upload_image(img_path):
        upload_url = pu.device_urls()["upload_image_url"]
        with open(img_path, "rb") as image_file:
            encoded_img = base64.b64encode(image_file.read())

        r = requests.post(upload_url, data={"base64": "data:image/png;base64," + encoded_img.decode("utf-8")})
        rsp = json.loads(r.text)
        img = rsp['image']
        return img

    @staticmethod
    def get_img_path(img_name):
        img_path = os.getcwd()
        if "db_project_api" in img_path:
            img_path_prefix = img_path.split("db_project_api")[0]
            imgPath = img_path_prefix + "\\db_project_api\\util\\img\\" + img_name
            img = DeviceManageParamsValue.upload_image(imgPath)
            return img
        else:
            print(u"获取图片路径出错，退出！！！")
            sys.exit()

    @staticmethod
    def device_value_device_center():
        # 对应设备管理页面

        device_values = dict()
        device_values[u"中控"] = u"中控"
        device_values[u"门锁"] = u"门锁"
        device_values[u"水表"] = u"水表"
        device_values[u"采集器"] = u"采集器"
        device_values[u"门禁"] = u"门禁"
        device_values[u"烟感"] = u"烟感"
        device_values[u"中继器"] = u"中继器"

        return device_values

    @staticmethod
    def center_control_add_instance():

        # 添加中控
        center_control_add_instance_name = DeviceManageParamsValue.ceter_control_name  # 页面提示不能超过15个字符
        center_control_add_instance_model = DeviceManageParamsValue.center_control_model
        center_control_add_instance_net = "1"
        center_control_add_instance_type_id = "1"

        center_control_add_instance_payload = DeviceManageParamsValue.add_instance("des.png",
                                                                                   center_control_add_instance_name, "",
                                                                                   center_control_add_instance_model,
                                                                                   "",
                                                                                   center_control_add_instance_net, "",
                                                                                   "",
                                                                                   center_control_add_instance_type_id)
        return center_control_add_instance_payload

    @staticmethod
    def center_control_update_instance():

        id_and_model = db.device_sql("get_product_id_and_model", DeviceManageParamsValue.ceter_control_name)

        DeviceManageParamsValue.center_control_id = id_and_model[0]
        center_control_update_instance_payload = DeviceManageParamsValue.update_instance("upda.png",
                                                                                         DeviceManageParamsValue.update_center_control_name,
                                                                                         "",
                                                                                         DeviceManageParamsValue.update_center_control_model,
                                                                                         "",
                                                                                         "0",
                                                                                         "",
                                                                                         "",
                                                                                         id_and_model[0])

        return center_control_update_instance_payload

    @staticmethod
    def center_control_delete_instance():

        return DeviceManageParamsValue.delete_instance(DeviceManageParamsValue.center_control_id)

    @staticmethod
    def lock_add_instance(lock_net_type):
        lock_add_instance_name = DeviceManageParamsValue.lock_name
        lock_add_instance_model = DeviceManageParamsValue.lock_model
        if lock_net_type == u"普通":
            lock_add_instance_net = "0"
        elif lock_net_type == u"网络":
            lock_add_instance_net = "1"
        elif lock_net_type == u"其他":
            lock_add_instance_net = "2"

        img = DeviceManageParamsValue.get_img_path("lock.png")
        lock_add_instance_payload = {"name": lock_add_instance_name,
                                     "types": "",
                                     "model": lock_add_instance_model,
                                     "cost": "",
                                     "net": lock_add_instance_net,
                                     "correspond": "",
                                     "wire": "",
                                     "typeId": "2",
                                     "images": img
                                     }
        return lock_add_instance_payload

    @staticmethod
    def lock_update_instance():
        lock_update_instance_name = DeviceManageParamsValue.update_lock_name
        lock_update_instance_model = DeviceManageParamsValue.update_lock_model
        id_and_model = db.device_sql("get_product_id_and_model", DeviceManageParamsValue.lock_name)

        return DeviceManageParamsValue.update_instance("lockUpdate.png", lock_update_instance_name, "",
                                                       lock_update_instance_model, "", "1", "", "", id_and_model[0])

    @staticmethod
    def lock_delete_instance():

        return DeviceManageParamsValue.delete_instance(DeviceManageParamsValue.lock_id)

    @staticmethod
    def water_meter_add_instance():
        water_meter_add_instance_name = DeviceManageParamsValue.water_meter_name
        water_meter_add_instance_model = DeviceManageParamsValue.water_meter_model

        return DeviceManageParamsValue.add_instance("wm1.png",
                                                    water_meter_add_instance_name,
                                                    "0",
                                                    water_meter_add_instance_model,
                                                    "1",
                                                    "0",
                                                    "0",
                                                    "1",
                                                    "3")

    @staticmethod
    def water_meter_update_instance():
        water_update_instance_name = DeviceManageParamsValue.update_water_meter_name
        water_update_instance_model = DeviceManageParamsValue.update_water_meter_model
        id_and_model = db.device_sql("get_product_id_and_model", DeviceManageParamsValue.water_meter_name)
        DeviceManageParamsValue.water_meter_id = id_and_model[0]
        return DeviceManageParamsValue.update_instance("wmhot.png",
                                                       water_update_instance_name,
                                                       "",
                                                       water_update_instance_model,
                                                       "",
                                                       "1",
                                                       "",
                                                       "",
                                                       id_and_model[0])

    @staticmethod
    def water_meter_delete_instance():
        return DeviceManageParamsValue.delete_instance(DeviceManageParamsValue.water_meter_id)

    @staticmethod
    def electric_meter_add_instance():
        electric_add_instance_name = DeviceManageParamsValue.electric_meter_name
        electric_add_instance_model = DeviceManageParamsValue.electric_meter_model
        return DeviceManageParamsValue.add_instance("electric.png",
                                                    electric_add_instance_name,
                                                    "0",
                                                    electric_add_instance_model,
                                                    "0",
                                                    "0",
                                                    "0",
                                                    "0",
                                                    "4")

    @staticmethod
    def electric_meter_update_instance():
        electric_update_instance_name = DeviceManageParamsValue.update_electric_name
        electric_update_instance_model = DeviceManageParamsValue.update_electric_model
        id_and_model = db.device_sql("get_product_id_and_model", DeviceManageParamsValue.electric_meter_name)
        DeviceManageParamsValue.electric_meter_id = id_and_model[0]
        return DeviceManageParamsValue.update_instance("eleupdate.png",
                                                       electric_update_instance_name,
                                                       "1",
                                                       electric_update_instance_model,
                                                       "0",
                                                       "1",
                                                       "2",
                                                       "1",
                                                       id_and_model[0])

    @staticmethod
    def electric_meter_delete_instance():
        return DeviceManageParamsValue.delete_instance(DeviceManageParamsValue.electric_meter_id)

    @staticmethod
    def collector_add_instance():
        collector_add_instance_name = DeviceManageParamsValue.collector_name
        collector_add_instance_model = DeviceManageParamsValue.collector_model
        return DeviceManageParamsValue.add_instance("diancai.png",
                                                    collector_add_instance_name,
                                                    "0",
                                                    collector_add_instance_model,
                                                    "",
                                                    "",
                                                    "0",
                                                    "0",
                                                    "6")

    @staticmethod
    def collector_update_instance():
        collector_update_instance_name = DeviceManageParamsValue.update_collector_name
        collector_update_instance_model = DeviceManageParamsValue.update_collector_model
        id_and_model = db.device_sql("get_product_id_and_model", DeviceManageParamsValue.collector_name)
        DeviceManageParamsValue.collector_id = id_and_model[0]
        return DeviceManageParamsValue.update_instance("diancaiupdate.png",
                                                       collector_update_instance_name,
                                                       "1",
                                                       collector_update_instance_model,
                                                       "",
                                                       "",
                                                       "1",
                                                       "1",
                                                       id_and_model[0])

    @staticmethod
    def collector_delete_instance():
        return DeviceManageParamsValue.delete_instance(DeviceManageParamsValue.collector_id)

    @staticmethod
    def smoke_detector_add_instance():

        smoke_detector_add_instance_name = DeviceManageParamsValue.smoke_detector_name
        smoke_detector_add_instance_model = DeviceManageParamsValue.smoke_detector_model
        return DeviceManageParamsValue.add_instance("yangan1.png",
                                                    smoke_detector_add_instance_name,
                                                    "",
                                                    smoke_detector_add_instance_model,
                                                    "",
                                                    "0",
                                                    "0",
                                                    "0",
                                                    "8")

    @staticmethod
    def smoke_detector_update_instance():
        smoke_detector_update_instance_name = DeviceManageParamsValue.update_smoke_detector_name
        smoke_detector_update_instance_model = DeviceManageParamsValue.update_smoke_detector_model
        id_and_model = db.device_sql("get_product_id_and_model", DeviceManageParamsValue.smoke_detector_name)
        DeviceManageParamsValue.smoke_detector_id = id_and_model[0]
        return DeviceManageParamsValue.update_instance("yanganUpdate.png",
                                                       smoke_detector_update_instance_name,
                                                       "1",
                                                       smoke_detector_update_instance_model,
                                                       "",
                                                       "1",
                                                       "1",
                                                       "1",
                                                       id_and_model[0])

    @staticmethod
    def smoke_detector_delete_instance():
        return DeviceManageParamsValue.delete_instance(DeviceManageParamsValue.smoke_detector_id)

    @staticmethod
    def repeater_add_instance():
        repeater_name = DeviceManageParamsValue.repeater_name
        repeater_model = DeviceManageParamsValue.repeater_model
        return DeviceManageParamsValue.add_instance("zhongji.png",
                                                    repeater_name,
                                                    "",
                                                    repeater_model,
                                                    "",
                                                    "",
                                                    "",
                                                    "",
                                                    "62")

    @staticmethod
    def repeater_update_instance():
        repeater_update_name = DeviceManageParamsValue.update_repeater_name
        repeater_update_model = DeviceManageParamsValue.update_repeater_model
        id_and_model = db.device_sql("get_product_id_and_model", DeviceManageParamsValue.repeater_name)
        DeviceManageParamsValue.repeater_id = id_and_model[0]
        return DeviceManageParamsValue.update_instance("zhognjiupdate.png",
                                                       repeater_update_name,
                                                       "1",
                                                       repeater_update_model,
                                                       "",
                                                       "1",
                                                       "1",
                                                       "1",
                                                       id_and_model[0])

    @staticmethod
    def repeater_delete_instance():
        return DeviceManageParamsValue.delete_instance(DeviceManageParamsValue.repeater_id)


class HouseManageParamsValue():
    # 对应设备管理系统中的企业昵称
    # customer_name = u"自动化测试"
    customer_name = u"自动化测试"

    # 工程管理系统中房源提供商名字
    house_provider_name = u"auto房源提供商" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    house_provider_id = ""

    # 添加房源
    home_source_name = u"auto_自动化_回民街_" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time())) + "_" + str(
        random.randint(0, 10000))
    update_home_source_name = u"auto_自动化_更新的回民街_" + time.strftime('%Y-%m-%d_%H:%M:%S',
                                                                  time.localtime(time.time())) + "_" + str(
        random.randint(0, 10000))
    delete_house_source_name = ""

    # 添加空间类型
    floor_num = str(random.randint(0, 99))
    home_num = floor_num + str(random.randint(0, 99))
    home_type = "0"
    is_public = "0"

    # 更新空间类型
    update_floor_num = str(random.randint(0, 99))
    update_home_num = update_floor_num + str(random.randint(0, 99))
    update_home_type = "1"
    update_is_public = "0"

    # 空间信息
    delete_space_name = ""

    ###客户管理部分开始
    @staticmethod
    def add_house_provider():
        customer_id = db.house_source_sql("get_customer_id", HouseManageParamsValue.customer_name)
        add_house_provider_payload = {"enterpriseAccountId": str(customer_id),
                                      "providerName": HouseManageParamsValue.house_provider_name}
        return add_house_provider_payload

    # 房源提供者没有修改的功能
    # @staticmethod
    # def updateHouseProvider():
    #     print u""
    # 房源提供者没有修改的功能

    @staticmethod
    def delete_house_provider():
        house_provider_id = db.house_source_sql("get_provider_name_and_id", HouseManageParamsValue.house_provider_name)
        return house_provider_id

    @staticmethod
    def batch_delete_house_provider():
        pass

    ###客户管理部分结束

    @staticmethod
    def add_house_source():
        add_house_source_payload = {
            "addrCode": gc.get_house_addr()["address_code"],
            "homeSourceName": HouseManageParamsValue.home_source_name,
            "providerId": "",
            "types": "0"
        }
        return add_house_source_payload

    @staticmethod
    def update_house_source():
        update_house_source_payload = {
            "addrCode": gc.get_house_addr()["address_code"],
            "homeSourceName": HouseManageParamsValue.update_home_source_name,
            "id": "",
            "providerId": "",
            "types": "1"  # 0 集中式  1 分散式
        }
        return update_house_source_payload

    @staticmethod
    def delete_house_source():
        house_source_id = db.house_source_sql("get_home_source_id", HouseManageParamsValue.update_home_source_name)
        return house_source_id

    @staticmethod
    def batch_add_house_source():
        add_house_source_payload = {
            "addrCode": gc.get_house_addr()["address_code"],
            "homeSourceName": u"auto_自动化_回民街_" + time.strftime('%y%m%d%H%M%S',
                                                               time.localtime(time.time())) + "_" + str(
                random.randint(0, 10000)),
            "providerId": "33",
            "types": "0"
        }
        print(HouseManageParamsValue.home_source_name)
        return add_house_source_payload

    @staticmethod
    def add_space():
        add_space_payload = {"floorNum": HouseManageParamsValue.floor_num,
                             "homeNo": HouseManageParamsValue.home_num,
                             "homeSourceId": "",
                             "homeType": HouseManageParamsValue.home_type,
                             "isPublic": HouseManageParamsValue.is_public
                             }
        return add_space_payload

    @staticmethod
    def update_space():
        update_space_payload = {"floorNum": HouseManageParamsValue.update_floor_num,
                                "homeNo": HouseManageParamsValue.update_home_num,
                                "homeSourceId": "",
                                "homeType": HouseManageParamsValue.update_home_type,
                                "isPublic": HouseManageParamsValue.update_is_public,
                                "id": ""
                                }
        return update_space_payload

    @staticmethod
    def delete_space():
        space_id = db.house_source_sql("get_space_id", HouseManageParamsValue.update_home_num)
        return space_id


class SystemManageParamsValue(object):
    # 角色管理--新增角色
    user_group_name = u"自动化组" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    user_group_description = u"这是自动化测试使用角色描述。这里有很多时间戳" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    # 角色管理--更新角色
    update_user_group_name = u"更新！！更新！！自动化组" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    update_user_group_description = u"更新！！！！更新！！！更新！！！！这是自动化测试使用角色描述。这里有很多时间戳" + time.strftime('%Y-%m-%d_%H:%M:%S',
                                                                                               time.localtime(
                                                                                                   time.time()))

    # 用户管理--添加账户
    phone_prefix_list = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151",
                         "152", "153",
                         "155", "156", "157", "158", "159", "186", "187", "188"]
    first_name = ['张', '金', '李', '王', '赵', '陈', '郭', '宋', '周', '秦', '何', '刘']
    middle_name = ['玉', '明', '龙', '芳', '军', '玲', '才', '伟', '娜', '敏', '静', '杰']
    last_name = ['', '立', '玲', '', '国', '', '玉', '', '秀', '', '桂', '勇']
    username = "auto自动化测试账号" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    phone = random.choice(phone_prefix_list) + "".join(random.choice("0123456789") for i in range(8))
    nickname = random.choice(first_name) + random.choice(middle_name) + random.choice(
        last_name) + time.strftime('%Y-%m-%d_%H:%M:%S',
                                   time.localtime(
                                       time.time()))
    group_name_and_id = db.system_sql("get_group_id_and_name")
    group_name = group_name_and_id[random.randint(0, len(group_name_and_id) - 1)][1]
    group_id = group_name_and_id[random.randint(0, len(group_name_and_id) - 1)][0]
    states = "0"
    company_name = "auto自动化公司" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))

    # 用户管理--更新账户
    update_username = "更新auto自动化测试账号" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    update_phone = random.choice(phone_prefix_list) + "".join(random.choice("0123456789") for i in range(8))
    update_nickname = "更新" + random.choice(first_name) + random.choice(middle_name) + random.choice(
        last_name) + time.strftime(
        '%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))
    update_group_name_and_id = db.system_sql("get_group_id_and_name")
    update_group_name = update_group_name_and_id[random.randint(0, len(update_group_name_and_id) - 1)][1]
    update_group_id = update_group_name_and_id[random.randint(0, len(update_group_name_and_id) - 1)][0]
    update_states = "1"
    update_company_name = "更新auto自动化公司" + time.strftime('%Y-%m-%d_%H:%M:%S', time.localtime(time.time()))

    @staticmethod
    def add_user_info():
        add_user_info_payload = {
            "userName": SystemManageParamsValue.username,
            "phone": SystemManageParamsValue.phone,
            "nickName": SystemManageParamsValue.nickname,
            "groupId": SystemManageParamsValue.group_id,
            "states": SystemManageParamsValue.states,
            "companyName": SystemManageParamsValue.company_name
        }
        return add_user_info_payload

    @staticmethod
    def update_user_info():
        update_user_info_payload = {
            "userName": SystemManageParamsValue.update_username,
            "phone": SystemManageParamsValue.update_phone,
            "nickName": SystemManageParamsValue.update_nickname,
            "groupId": SystemManageParamsValue.update_group_id,
            "states": SystemManageParamsValue.update_states,
            "companyName": SystemManageParamsValue.update_company_name,
            "id": db.system_sql("get_group_id", SystemManageParamsValue.username)[0][0]
        }
        return update_user_info_payload

    @staticmethod
    def delete_user_info():
        delete_user_info_payload = {
            "userId": db.system_sql("get_group_id", SystemManageParamsValue.update_username)[0][0]
        }
        return delete_user_info_payload

    @staticmethod
    def add_user_group():
        add_user_group_payload = {
            "name": SystemManageParamsValue.group_name,
            "ext": SystemManageParamsValue.user_group_description
        }
        return add_user_group_payload

    @staticmethod
    def update_user_group():
        update_user_group_payload = {
            "name": SystemManageParamsValue.update_user_group_name,
            "ext": SystemManageParamsValue.update_user_group_description,
            "groupId": db.system_sql("get_group_id_with_group_name", SystemManageParamsValue.user_group_name)[0][0]
        }
        return update_user_group_payload

    @staticmethod
    def delete_user_group():
        delete_user_group_payload = {
            "groupId": db.system_sql("get_group_id_with_group_name", SystemManageParamsValue.update_group_name)[0][0]
        }
        return delete_user_group_payload
