#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: requestURL.py
@time: 2018/05/13/7:53
"""
from util.read_conf import ReadConfigFile


class ProjectUrls(object):
    rcf = ReadConfigFile()
    project_url_prefix = rcf.get_basic_conf()["project_url_prefix"]

    @staticmethod
    def device_urls():
        device_type = "/project-service/device/type/"
        add_device_model_url = device_type + "addRecord"
        del_device_model_url = device_type + "deleteById"
        update_device_model_url = device_type + "updateById"
        upload_image_url = "/project-service/image/uploadImage"
        device_urls = dict()
        device_urls["add_device_model_url"] = ProjectUrls.project_url_prefix + add_device_model_url
        device_urls["del_device_model_url"] = ProjectUrls.project_url_prefix + del_device_model_url
        device_urls["update_device_model_url"] = ProjectUrls.project_url_prefix + update_device_model_url
        device_urls["upload_image_url"] = ProjectUrls.project_url_prefix + upload_image_url
        return device_urls

    @staticmethod
    def devices_instance_urls():
        # 所有类型（中控，门锁，水表，电表，采集器，烟感等）的设备，新增，修改，删除请求的都是同一个URL
        device_info = "/project-service/device/info/"
        add_dev_url = device_info + "addRecord"
        update_dev_url = device_info + "updateById"
        delete_dev_url = device_info + "deleteById"

        dev_instance_urls = dict()
        dev_instance_urls["add_dev_url"] = ProjectUrls.project_url_prefix + add_dev_url
        dev_instance_urls["update_dev_url"] = ProjectUrls.project_url_prefix + update_dev_url
        dev_instance_urls["delete_dev_url"] = ProjectUrls.project_url_prefix + delete_dev_url

        return dev_instance_urls

    @staticmethod
    def house_manage_urls():
        # 添加客户信息
        home_source_provider = "/project-service/homeSourceProvider/"
        add_home_source_provider_url = home_source_provider + "insertRecord"

        # 房源相关
        add_home_source_url = "/project-service/homeSource/insertRecord"
        update_home_source_url = "/project-service/homeSource/updateRecord"
        delete_home_source_url = "/project-service/homeSource/"

        # 添加空间类型
        space_manage = "/project-service/homeList/"
        add_space_url = space_manage + "insertRecord"
        update_space_url = space_manage + "updateRecord"

        house_manage_urls = dict()
        house_manage_urls["home_source_provider"] = ProjectUrls.project_url_prefix + home_source_provider
        house_manage_urls["delete_home_source_provider"] = ProjectUrls.project_url_prefix + home_source_provider
        house_manage_urls[
            "add_home_source_provider_url"] = ProjectUrls.project_url_prefix + add_home_source_provider_url

        # 添加房源
        house_manage_urls["add_home_source_url"] = ProjectUrls.project_url_prefix + add_home_source_url
        house_manage_urls["update_home_source_url"] = ProjectUrls.project_url_prefix + update_home_source_url
        house_manage_urls["delete_home_source_url"] = ProjectUrls.project_url_prefix + delete_home_source_url

        # 添加空间类型
        house_manage_urls["add_space_url"] = ProjectUrls.project_url_prefix + add_space_url
        house_manage_urls["update_space_url"] = ProjectUrls.project_url_prefix + update_space_url
        house_manage_urls["delete_space_url"] = ProjectUrls.project_url_prefix + space_manage

        return house_manage_urls

    @staticmethod
    def system_manage_urls():
        system_manage_urls = dict()

        user_base_urls = "/project-service/user/"

        add_user_info_url = user_base_urls + "info/addUserInfo"
        update_user_info_url = user_base_urls + "info/updateUserInfo"
        delete_user_info_url = user_base_urls + "info/delUserById"

        user_group_base_url = "/project-service/user/group/"

        add_user_group_url = user_group_base_url + "addUserGroup"
        update_user_group_url = user_group_base_url + "updateUserGroup"
        delete_user_group_url = user_group_base_url + "delUserGroup"

        system_manage_urls["add_user_info_url"] = ProjectUrls.project_url_prefix + add_user_info_url
        system_manage_urls["update_user_info_url"] = ProjectUrls.project_url_prefix + update_user_info_url
        system_manage_urls["delete_user_info_url"] = ProjectUrls.project_url_prefix + delete_user_info_url
        system_manage_urls["add_user_group_url"] = ProjectUrls.project_url_prefix + add_user_group_url
        system_manage_urls["update_user_group_url"] = ProjectUrls.project_url_prefix + update_user_group_url
        system_manage_urls["delete_user_group_url"] = ProjectUrls.project_url_prefix + delete_user_group_url

        return system_manage_urls
