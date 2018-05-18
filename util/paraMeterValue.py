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

from util.danbayDatabase import DB_database as db
from util.getCity import getCity as gc
from util.requestURL import projectUrls as pu


class DeviceManageParamsValue():
    # 中控
    globalsCenterControlName = "auto中控" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    globalsCenterControlId = ""
    # 门锁
    globalsLockName = "auto门锁" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    globalsLocklId = ""
    # 水表
    globalsWaterMeterName = "auto水表" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    globalsWaterMeterId = ""
    # 电表
    globalsElectricName = "auto电表" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    globalsElectricId = ""
    # 电表采集器
    globalCaiJiName = "auto电采" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    globalCaiJiId = ""
    # 烟感
    globalYanGanName = "auto烟感" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    globalYanGanId = ""
    # 中继
    globalZhongJiName = "auto中继" + time.strftime('%m%d%H%M', time.localtime(time.time()))
    globalZhongJiId = ""

    @staticmethod
    def getDeviceType(typeID, type=0):
        if typeID == 0:
            return "门锁"
        elif typeID == "1":
            if type == 0:
                return "zhongkong"
            elif type == 1:
                return "hauwei"

        elif typeID == "2":
            if type == 0:
                return "lengshui"
            elif type == 1:
                return "rehsui"

        elif typeID == "3":
            return "rehsui"
        elif typeID == "4":
            return "rehsui"
        elif typeID == "5":
            return "rehsui"
        elif typeID == "6":
            return "rehsui"
        elif typeID == "7":
            return "rehsui"

    @staticmethod
    def addInstance(img, name, types, model, cost, net, correspond, wire, typeId):
        img = DeviceManageParamsValue.getImgPath(img)
        addInstancePayload = {"name": name,
                              "types": types,
                              "model": model,
                              "cost": cost,
                              "net": net,
                              "correspond": correspond,
                              "wire": wire,
                              "typeId": typeId,
                              "images": img
                              }
        return addInstancePayload

    @staticmethod
    def updateInstance(img, name, types, model, cost, net, correspond, wire, id):
        img = DeviceManageParamsValue.getImgPath(img)

        updataeInstancePayload = {"name": name,
                                  "types": types,
                                  "cost": cost,
                                  "correspond": correspond,
                                  "wire": wire,
                                  "model": model,
                                  "net": net,
                                  "images": img,
                                  "id": id
                                  }
        return updataeInstancePayload

    @staticmethod
    def deleteInstance(id):
        deleteInstance_Payload = {}
        deleteInstance_Payload["id"] = id
        return deleteInstance_Payload

    @staticmethod
    def uploadImage(imgPath):
        uploadUrl = pu.deviceUrls()["uploadImageUrl"]
        with open(imgPath, "rb") as image_file:
            encodedImg = base64.b64encode(image_file.read())
        r = requests.post(uploadUrl, data={"base64": "data:image/png;base64," + encodedImg})
        rsp = json.loads(r.text)
        img = rsp['image']
        return img

    @staticmethod
    def getImgPath(imgName):
        imgPath = os.getcwd()
        if "db_project_api" in imgPath:
            imgPathPrefix = imgPath.split("db_project_api")[0]
            imgPath = imgPathPrefix + "\\db_project_api\\util\\img\\" + imgName
            img = DeviceManageParamsValue.uploadImage(imgPath)
            return img
        else:
            print "获取图片路径出错，退出！！！"
            sys.exit()

    @staticmethod
    def deviceValue_deviceCenter():
        # 对应设备管理页面

        deviceValues = {}
        deviceValues["中控"] = "中控"
        deviceValues["门锁"] = "门锁"
        deviceValues["水表"] = "水表"
        deviceValues["采集器"] = "采集器"
        deviceValues["门禁"] = "门禁"
        deviceValues["烟感"] = "烟感"
        deviceValues["中继器"] = "中继器"

        return deviceValues

    @staticmethod
    def centerControl_addInstance():

        # 添加中控
        centerControl_addInstance_name = DeviceManageParamsValue.globalsCenterControlName  # 页面提示不能超过15个字符
        centerControl_addInstance_model = "GW_auto" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        centerControl_addInstance_net = "1"
        centerControl_addInstance_typeId = "1"

        centerControl_addInstancePayload = DeviceManageParamsValue.addInstance("des.png",
                                                                               centerControl_addInstance_name, "",
                                                                               centerControl_addInstance_model, "",
                                                                               centerControl_addInstance_net, "", "",
                                                                               centerControl_addInstance_typeId)
        return centerControl_addInstancePayload

    @staticmethod
    def centerControl_updateInstance():
        centerControl_updateInstance_name = "upda中控" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        centerControl_updateInstance_model = "upda中控" + time.strftime('%m%d%H%M', time.localtime(time.time()))

        idAndModel = db.deviceSql("getProdutIdAndModel", DeviceManageParamsValue.globalsCenterControlName)

        DeviceManageParamsValue.globalsCenterControlId = idAndModel[0]
        centerControl_updateInstancePayload = DeviceManageParamsValue.updateInstance("upda.png",
                                                                                     centerControl_updateInstance_name,
                                                                                     "",
                                                                                     centerControl_updateInstance_model,
                                                                                     "",
                                                                                     "1", "", "",
                                                                                     idAndModel[0])

        return centerControl_updateInstancePayload

    @staticmethod
    def centerControl_deleteInstance():

        return DeviceManageParamsValue.deleteInstance(DeviceManageParamsValue.globalsCenterControlId)

    @staticmethod
    def lock_addInstance(lockNetType):
        lock_addInstance_name = DeviceManageParamsValue.globalsLockName
        lock_addInstance_model = "lk_auto" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        if lockNetType == "普通":
            lock_addInstance_net = "0"
        elif lockNetType == "网络":
            lock_addInstance_net = "1"
        elif lockNetType == "其他":
            lock_addInstance_net = "2"
        img = DeviceManageParamsValue.getImgPath("lock.png")
        payload_lock_addInstance = {"name": lock_addInstance_name,
                                    "types": "",
                                    "model": lock_addInstance_model,
                                    "cost": "",
                                    "net": lock_addInstance_net,
                                    "correspond": "",
                                    "wire": "",
                                    "typeId": "2",
                                    "images": img
                                    }
        return payload_lock_addInstance

    @staticmethod
    def lock_updateInstance():
        lock_updateInstance_name = "upda门锁" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        lock_updateInstance_model = "upda门锁" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        idAndModel = db.deviceSql("getProdutIdAndModel", DeviceManageParamsValue.globalsLockName)

        return DeviceManageParamsValue.updateInstance("lockUpdate.png", lock_updateInstance_name, "",
                                                      lock_updateInstance_model, "", "1", "", "", idAndModel[0])

    @staticmethod
    def lock_deleteInstance():

        return DeviceManageParamsValue.deleteInstance(DeviceManageParamsValue.globalsLocklId)

    @staticmethod
    def waterMeter_addInstance():
        waterMeter_addInstance_name = DeviceManageParamsValue.globalsWaterMeterName
        waterMeter_addInstance_model = "wm_auto" + time.strftime('%m%d%H%M', time.localtime(time.time()))

        return DeviceManageParamsValue.addInstance("wm1.png", waterMeter_addInstance_name, "0",
                                                   waterMeter_addInstance_model,
                                                   "1", "0", "0", "1", "3")

    @staticmethod
    def waterMeter_updateInstance():
        water_updateInstanceName = "WM_hot" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        water_updateInstance_model = "WM_hot" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        idAndModel = db.deviceSql("getProdutIdAndModel", DeviceManageParamsValue.globalsWaterMeterName)
        DeviceManageParamsValue.globalsLocklId = idAndModel[0]
        return DeviceManageParamsValue.updateInstance("wmhot.png", water_updateInstanceName, "",
                                                      water_updateInstance_model,
                                                      "", "1", "", "",
                                                      idAndModel[0])

    @staticmethod
    def waterMeter_deleteInstance():
        return DeviceManageParamsValue.deleteInstance(DeviceManageParamsValue.globalsLocklId)

    @staticmethod
    def electric_addInstance():
        electric_addInstance_name = DeviceManageParamsValue.globalsElectricName
        electric_addInstance_model = "em_auto" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        return DeviceManageParamsValue.addInstance("electric.png", electric_addInstance_name, "0",
                                                   electric_addInstance_model,
                                                   "0", "0", "0", "0", "4")

    @staticmethod
    def electric_updateInstance():
        electric_updateInstance_name = "emupda" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        electric_updateInstance_model = "emupda" + time.strftime('%m%d%H%M', time.localtime(time.time()))
        idAndModel = db.deviceSql("getProdutIdAndModel", DeviceManageParamsValue.globalsElectricName)
        DeviceManageParamsValue.globalsElectricId = idAndModel[0]
        return DeviceManageParamsValue.updateInstance("eleupdate.png", electric_updateInstance_name, "1",
                                                      electric_updateInstance_model, "0",
                                                      "1", "2", "1", idAndModel[0])

    @staticmethod
    def electric_deleteInstance():
        return DeviceManageParamsValue.deleteInstance(DeviceManageParamsValue.globalsElectricId)

    @staticmethod
    def caiji_addInstance():
        diancai_addInstance_name = DeviceManageParamsValue.globalCaiJiName
        diancai_addInstance_model = "电采_auto" + time.strftime('%H%M', time.localtime(time.time()))
        return DeviceManageParamsValue.addInstance("diancai.png", diancai_addInstance_name, "0",
                                                   diancai_addInstance_model,
                                                   "", "", "0", "0", "6")

    @staticmethod
    def caiji_updateInstance():
        caijii_updateInstance_name = "水采Update" + time.strftime('%H%M', time.localtime(time.time()))
        caiji_updateInstance_model = "水采Update" + time.strftime('%H%M', time.localtime(time.time()))
        idAndModel = db.deviceSql("getProdutIdAndModel", DeviceManageParamsValue.globalCaiJiName)
        DeviceManageParamsValue.globalCaiJiId = idAndModel[0]
        return DeviceManageParamsValue.updateInstance("diancaiupdate.png", caijii_updateInstance_name, "1",
                                                      caiji_updateInstance_model, "",
                                                      "", "1", "1", idAndModel[0])

    @staticmethod
    def caiji_deleteInstance():
        return DeviceManageParamsValue.deleteInstance(DeviceManageParamsValue.globalCaiJiId)

    @staticmethod
    def yangan_addInstance():
        yangan_addInstance_name = DeviceManageParamsValue.globalYanGanName
        yangan_addInstance_model = "烟感_auto" + time.strftime('%H%M', time.localtime(time.time()))
        return DeviceManageParamsValue.addInstance("yangan1.png", yangan_addInstance_name, "", yangan_addInstance_model,
                                                   "", "0", "0", "0", "8")

    @staticmethod
    def yangan_updateInstance():
        yangan_updateInstance_name = "烟感Update" + time.strftime('%H%M', time.localtime(time.time()))
        yangan_updateInstance_model = "烟感Update" + time.strftime('%H%M', time.localtime(time.time()))
        idAndModel = db.deviceSql("getProdutIdAndModel", DeviceManageParamsValue.globalYanGanName)
        DeviceManageParamsValue.globalYanGanId = idAndModel[0]
        return DeviceManageParamsValue.updateInstance("yanganUpdate.png", yangan_updateInstance_name, "1",
                                                      yangan_updateInstance_model, "",
                                                      "1", "1", "1", idAndModel[0])

    @staticmethod
    def yangan_deleteInstance():
        return DeviceManageParamsValue.deleteInstance(DeviceManageParamsValue.globalYanGanId)

    @staticmethod
    def zhongji_addInstance():
        zhongji_addInstance_name = DeviceManageParamsValue.globalZhongJiName
        zhongji_addInstance_model = "中继_auto" + time.strftime('%H%M', time.localtime(time.time()))
        return DeviceManageParamsValue.addInstance("zhongji.png", zhongji_addInstance_name, "",
                                                   zhongji_addInstance_model,
                                                   "", "", "", "", "62")

    @staticmethod
    def zhongji_updateInstance():
        zhongji_updateInstance_name = "中继Update" + time.strftime('%H%M', time.localtime(time.time()))
        zhongji_updateInstance_model = "中继Update" + time.strftime('%H%M', time.localtime(time.time()))
        idAndModel = db.deviceSql("getProdutIdAndModel", DeviceManageParamsValue.globalZhongJiName)
        DeviceManageParamsValue.globalZhongJiId = idAndModel[0]
        return DeviceManageParamsValue.updateInstance("zhognjiupdate.png", zhongji_updateInstance_name, "1",
                                                      zhongji_updateInstance_model, "",
                                                      "1", "1", "1", idAndModel[0])

    @staticmethod
    def zhongji_deleteInstance():
        return DeviceManageParamsValue.deleteInstance(DeviceManageParamsValue.globalZhongJiId)


class HouseManageParamsValue():
    # 对应设备管理系统中的企业昵称
    customerName = "自动化测试"

    # 工程管理系统中房源提供商名字
    houseProviderName = "auto房源提供商" + time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time()))
    houseProviderId = ""
    deleteHomeProviderName = "特实打实的"

    # 添加房源
    homeSourceName = "auto_自动化_回民街_" + time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())) + "_" + str(
        random.randint(0, 10000))
    updateHomeSourceName="auto_自动化_更新的回民街_" + time.strftime('%Y%m%d_%H%M%S', time.localtime(time.time())) + "_" + str(
        random.randint(0, 10000))
    deleteHouseSouceName = ""
    addrcode=gc.getHouseAddr()["addrcode"]

    # 添加空间类型
    floorNum = str( random.randint(0, 99))
    homeNo =floorNum+ str( random.randint(0, 99))
    homeType = "0"
    isPublic = "0"
    #更新空间类型
    updateFloorNum = str( random.randint(0, 99))
    updatHomeNo = updateFloorNum+ str( random.randint(0, 99))
    updateHomeType = "1"
    updateIsPublic = "0"



    # 空间信息
    deleteSpaceName = ""





    ###客户管理部分开始
    @staticmethod
    def addHouseProvider():
        customerID = db.houseSourceSql("getCustomerID", HouseManageParamsValue.customerName)
        addHouseProviderPayload = {"enterpriseAccountId": str(customerID),
                                   "providerName": HouseManageParamsValue.houseProviderName}
        return addHouseProviderPayload

    # 房源提供者没有修改的功能
    # @staticmethod
    # def updateHouseProvider():
    #     print u""
    # 房源提供者没有修改的功能

    @staticmethod
    def deleteHouseProvider():
        houseProviderID = db.houseSourceSql("getProviderNameID", HouseManageParamsValue.houseProviderName)
        return houseProviderID

    @staticmethod
    def batchDeleteHouseProvider():
        pass

    ###客户管理部分结束

    @staticmethod
    def addHouseSource():
        addHouseSourcePayload = {
            "addrCode": HouseManageParamsValue.addrcode,
            "homeSourceName": HouseManageParamsValue.homeSourceName,
            "providerId": "",
            "types": "0"
        }
        return addHouseSourcePayload

    @staticmethod
    def updateHouseSource():
        updateHouseSourcePayload = {
            "addrCode": gc.getHouseAddr()["addrcode"],
            "homeSourceName": HouseManageParamsValue.updateHomeSourceName,
            "id": "",
            "providerId": "",
            "types": "1" #0 集中式  1 分散式
        }
        return updateHouseSourcePayload
    @staticmethod
    def deleteHouseSource():
        houseSourceID = db.houseSourceSql("getHouseSourceID", HouseManageParamsValue.deleteHouseSouceName)
        return houseSourceID

    @staticmethod
    def batchAddHouseSource():
        addHouseSourcePayload = {
            "addrCode": gc.getHouseAddr()["addrcode"],
            "homeSourceName": "auto_自动化_回民街_" + time.strftime('%y%m%d%H%M%S',
                                                              time.localtime(time.time())) + "_" + str(
                random.randint(0, 10000)),
            "providerId": "33",
            "types": "0"
        }
        print HouseManageParamsValue.homeSourceName
        return addHouseSourcePayload

    @staticmethod
    def addSpace():
        addSpacePayload = {"floorNum": HouseManageParamsValue.floorNum,
                           "homeNo": HouseManageParamsValue.homeNo,
                           "homeSourceId": "",
                           "homeType": HouseManageParamsValue.homeType,
                           "isPublic": HouseManageParamsValue.isPublic
                           }
        return addSpacePayload

    @staticmethod
    def updateSpace():
        updateSpacePayload = {"floorNum": HouseManageParamsValue.updateFloorNum,
                              "homeNo": HouseManageParamsValue.updatHomeNo,
                              "homeSourceId": "",
                              "homeType": HouseManageParamsValue.updateHomeType,
                              "isPublic": HouseManageParamsValue.updateIsPublic,
                              "id": ""
                              }
        return updateSpacePayload
    @staticmethod
    def deleteSpace():
        spaceID = db.houseSourceSql("getSpaceId", HouseManageParamsValue.updatHomeNo)
        return spaceID