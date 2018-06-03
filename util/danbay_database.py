#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: danbayDatabase.py
@time: 2018/05/14/11:02
"""
import sys

import pymysql


class DataBase(object):

    @staticmethod
    def excute_sql(sql, db='danbay_device'):
        conn = pymysql.connect(
            host='120.77.236.177',
            port=3307,
            user='root',
            passwd='LoveDanbayWrite!',
            db=db,
            charset="utf8"
        )
        cur = conn.cursor()
        cur.execute(sql)
        results = cur.fetchall()
        cur.close()
        conn.commit()
        conn.close()
        return results

    @staticmethod
    def system_sql(*param):
        if param[0] == "get_group_id_and_name":
            group_id_and_name_sql = "SELECT id,NAME from tb_project_user_group"
            group_id_and_name = DataBase.excute_sql(group_id_and_name_sql, db="db_project")
            return group_id_and_name
        if param[0] == "get_group_id":
            group_id_sql = "SELECT id FROM tb_project_user WHERE userName='" + param[1] + "'"
            group_id = DataBase.excute_sql(group_id_sql, db="db_project")
            return group_id
        if param[0] == "get_group_id_with_group_name":
            group_id_sql = "SELECT id FROM tb_project_user_group WHERE name='" + param[1] + "'"
            group_id = DataBase.excute_sql(group_id_sql, db="db_project")
            return group_id

    @staticmethod
    def house_source_sql(*param):

        if param[0] == "get_customer_id":
            # 根据用户名获取账号ID
            customer_id_sql = "SELECT ID FROM mc_user WHERE NICK_NAME LIKE '%" + param[1] + "%'"
            customer_id = DataBase.excute_sql(customer_id_sql, db="danbay_device")[0][0]
            return customer_id
        if param[0] == "get_provider_name_and_id":
            customer_id_sql = "SELECT ID FROM tb_project_homeprovider WHERE providerName LIKE '%" + param[1] + "%'"
            customer_id = DataBase.excute_sql(customer_id_sql, db="db_project")[0][0]
            return customer_id
        if param[0] == "get_home_source_id":
            home_source_id_sql = "SELECT id FROM tb_project_homesource WHERE homeSourceName LIKE  '%" + param[1] + "%'"
            home_source_id = DataBase.excute_sql(home_source_id_sql, db="db_project")[0][0]
            return home_source_id
        if param[0] == "get_space_id":
            space_id_sql = "SELECT id FROM tb_project_homelist WHERE homeNo LIKE  '%" + param[1] + "%'"
            space_id = DataBase.excute_sql(space_id_sql, db="db_project")[0][0]
            return space_id

    @staticmethod
    def device_sql(*param):
        # 第一个是类型，第二个是参数值，
        if param[0] == "get_device_type_id":
            model_id_sql = "SELECT id from tb_project_device_type WHERE `name` LIKE '%" + param[1] + "%'"
            model_id = DataBase.excute_sql(model_id_sql, db="db_project")[0][0]
            return model_id

        # 中控类目下添加产品
        if param[0] == "get_product_id_and_model":
            product_id_and_model_sql = "SELECT id,model FROM tb_project_device_info WHERE `name` LIKE '%" + param[
                1] + "%'"

            product_id_and_model = DataBase.excute_sql(product_id_and_model_sql, db="db_project")
            if product_id_and_model:
                return product_id_and_model[0]
            else:
                print("数据库返回空值！%s" % product_id_and_model_sql)
                sys.exit()

    @staticmethod
    def project_sql():
        pass


class DataBaseValidateWebResult(object):

    # 设备管理页面Sql 语句检查
    @staticmethod
    def device_manage_web_check(*param):

        if param[0] == "get_device_properties_by_id":
            device_properties_sql = "SELECT name,model,net,del,id from tb_project_device_info WHERE id='" + \
                                    str(param[1]) + "'"
            device_properties = DataBase.excute_sql(device_properties_sql, db="db_project")[0]
            return device_properties
        if param[0] == "get_device_properties_by_name":
            device_properties_sql = "SELECT name,model,net,del,id from tb_project_device_info WHERE name='" + \
                                    str(param[1]) + "'"
            device_properties = DataBase.excute_sql(device_properties_sql, db="db_project")[0]
            return device_properties

    # 房源管理页面sql检查
    @staticmethod
    def house_manage_web_check(*param):
        # 房源管理相关
        if param[0] == "get_home_provider_info":
            home_provider_sql = "SELECT id,providerName,del,enterpriseAccountId FROM tb_project_homeprovider WHERE providerName='" + \
                                param[1] + "'"
            home_provider_info = DataBase.excute_sql(home_provider_sql, db="db_project")
            home_provider_info = home_provider_info[0]
            return home_provider_info
        if param[0] == "get_home_source_info":
            home_source_sql = "SELECT id,types,providerId,homeSourceName,del FROM tb_project_homesource WHERE homeSourceName='" + str(
                param[1]) + "'"
            home_source_info = DataBase.excute_sql(home_source_sql, db="db_project")[0]
            return home_source_info

        if param[0] == "get_space_info":
            space_sql = "SELECT id,homeSourceId,homeNo,isPublic,floorNum,homeType,del from tb_project_homelist WHERE id='" + \
                        param[
                            1] + "'"
            space_info = DataBase.excute_sql(space_sql, db="db_project")[0]
            return space_info
        if param[0] == "get_space_id":
            space_id_sql = "SELECT id FROM tb_project_homelist WHERE homeSourceId='" + param[1] + "'  AND homeNo='" + \
                           param[2] + "'"
            space_id = DataBase.excute_sql(space_id_sql, db="db_project")[0][0]
            return space_id

    # 系统管理页面sql检查
    @staticmethod
    def system_manager_web_check(*param):
        # 用户管理相关
        if param[0] == "get_user_info":
            user_sql = "SELECT groupId,userName,nickName,companyName,del,states,phone " \
                       "FROM tb_project_user WHERE " + param[1][0] + "='" + str(param[1][1]) + "'"
            user_info = DataBase.excute_sql(user_sql, db="db_project")[0]
            return user_info
        if param[0] == "get_user_group":
            user_group_sql = "SELECT id,name,ext,del,groupType FROM tb_project_user_group WHERE " + param[1][
                0] + "='" + str(param[1][1]) + "'"
            user_group = DataBase.excute_sql(user_group_sql, db="db_project")[0]
            return user_group


















