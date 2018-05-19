#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: requestURL.py
@time: 2018/05/13/7:53
"""



from readConf import ReadConfigFile as rcf



class projectUrls():
    rcf = rcf()
    projectUrlprefix = rcf.getBasicConf()["projectUrlprefix"]



    @staticmethod
    def deviceUrls():
        deviceType = "/project-service/device/type/"
        addDeviceModelUrl = deviceType + "addRecord"
        delDeviceModelUrl = deviceType + "deleteById"
        updateDeviceModelUrl = deviceType + "updateById"
        uploadImageUrl = "/project-service/image/uploadImage"
        deviceUrls = {}
        deviceUrls["addDeviceModelUrl"] = projectUrls.projectUrlprefix + addDeviceModelUrl
        deviceUrls["delDeviceModelUrl"] = projectUrls.projectUrlprefix + delDeviceModelUrl
        deviceUrls["updateDeviceModelUrl"] = projectUrls.projectUrlprefix + updateDeviceModelUrl
        deviceUrls["uploadImageUrl"] = projectUrls.projectUrlprefix + uploadImageUrl
        return deviceUrls

    @staticmethod
    def devicesInstanceUrls():
        # 所有类型（中控，门锁，水表，电表，采集器，烟感等）的设备，新增，修改，删除请求的都是同一个URL
        deviceInfo = "/project-service/device/info/"
        addDevUrl = deviceInfo + "addRecord"
        updateDevUrl = deviceInfo + "updateById"
        deleteDevUrl = deviceInfo + "deleteById"

        devInstanceUrls = {}
        devInstanceUrls["addDevUrl"] = projectUrls.projectUrlprefix + addDevUrl
        devInstanceUrls["updateDevUrl"] = projectUrls.projectUrlprefix + updateDevUrl
        devInstanceUrls["deleteDevUrl"] = projectUrls.projectUrlprefix + deleteDevUrl

        return devInstanceUrls

    @staticmethod
    def HouseManageUrls():
        house_manage_urls = {}

        homeSourceProvider="/project-service/homeSourceProvider/"
        addhomeSourceProviderUrl=homeSourceProvider+"insertRecord"


        # 房源相关
        addHomeSourceUrl="/project-service/homeSource/insertRecord"
        updateHomeSourceUrl="/project-service/homeSource/updateRecord"
        deleteHomeSourceUrl="/project-service/homeSource/"

        # 添加空间类型
        spaceManage = "/project-service/homeList/"
        addSpaceUrl = spaceManage + "insertRecord"
        updateSpaceUrl = spaceManage + "updateRecord"

        house_manage_urls["homeSourceProvider"]=projectUrls.projectUrlprefix+homeSourceProvider
        house_manage_urls["deleteHomeSourceProvider"]=projectUrls.projectUrlprefix+homeSourceProvider
        house_manage_urls["addhomeSourceProviderUrl"]=projectUrls.projectUrlprefix+addhomeSourceProviderUrl

        #添加房源
        house_manage_urls["addHomeSourceUrl"] = projectUrls.projectUrlprefix + addHomeSourceUrl
        house_manage_urls["updateHomeSourceUrl"] = projectUrls.projectUrlprefix + updateHomeSourceUrl
        house_manage_urls["deleteHomeSourceUrl"] = projectUrls.projectUrlprefix + deleteHomeSourceUrl

        # 添加空间类型
        house_manage_urls["addSpaceUrl"] = projectUrls.projectUrlprefix + addSpaceUrl
        house_manage_urls["updateSpaceUrl"] = projectUrls.projectUrlprefix + updateSpaceUrl
        house_manage_urls["deleteSpaceUrl"] = projectUrls.projectUrlprefix + spaceManage


        return house_manage_urls

    @staticmethod
    def SystemManageUrls():
        system_manage_urls={}
        userBaseUrls="/project-service/user/"

        addUserInfoUrl=userBaseUrls+"info/addUserInfo"
        updateUserInfoUrl=userBaseUrls+"info/updateUserInfo"



        system_manage_urls["addUserInfoUrl"]=projectUrls.projectUrlprefix+addUserInfoUrl
        system_manage_urls["updateUserInfoUrl"]=projectUrls.projectUrlprefix+updateUserInfoUrl

        return system_manage_urls
