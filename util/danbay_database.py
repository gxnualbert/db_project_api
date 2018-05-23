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
            home_source_id = DataBase.excuteSql(home_source_id_sql, db="db_project")[0][0]
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

    @staticmethod
    def device_manage_web_check(*param):

        if param[0] == "get_device_type_and_id":
            model_id_sql = "SELECT id from tb_project_device_type WHERE `name` LIKE '%" + param[1] + "%'"
            model_id = DataBase.excute_sql(model_id_sql, db="db_project")[0][0]
            return model_id

        if param[0] == "add_dev_url":
            center_control_properties_sql = "SELECT name,model,net,del from tb_project_device_info WHERE name='" + \
                                            param[
                                                1] + "'"
            center_control_properties = DataBase.excute_sql(center_control_properties_sql, db="db_project")[0]
            return center_control_properties
        if param[0] == "get_center_control_properties_by_id":
            center_control_properties_sql = "SELECT name,model,net,del from tb_project_device_info WHERE id='" + \
                                            str(param[1]) + "'"
            center_control_properties = DataBase.excute_sql(center_control_properties_sql, db="db_project")[0]
            return center_control_properties
        if param[0] == "get_lock_properties":
            lock_properties_sql = ""
