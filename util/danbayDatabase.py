#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: danbayDatabase.py
@time: 2018/05/14/11:02
"""
import MySQLdb
import sys

class DB_database():
    @staticmethod
    def excuteSql(sql,db='danbay_device'):
        conn = MySQLdb.connect(
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
    def systemSql():
        pass

    @staticmethod
    def houseSourceSql(*param):

        if param[0]=="getCustomerID":
            # 根据用户名获取账号ID
            customerIDSql="SELECT ID FROM mc_user WHERE NICK_NAME LIKE '%"+param[1]+"%'"
            customerID=DB_database.excuteSql(customerIDSql, db="danbay_device")[0][0]
            return customerID

        if param[0]=="getProviderNameID":
            customerIDSql = "SELECT ID FROM tb_project_homeprovider WHERE providerName LIKE '%" + param[1] + "%'"
            customerID = DB_database.excuteSql(customerIDSql, db="db_project")[0][0]
            return customerID
        if param[0]=="getHomeSourceId":
            homeSourceIDSql = "SELECT id FROM tb_project_homesource WHERE homeSourceName LIKE  '%" + param[1] + "%'"
            homeSourceID = DB_database.excuteSql(homeSourceIDSql, db="db_project")[0][0]
            return homeSourceID
        if param[0]=="getSpaceId":
            spaceIDSql = "SELECT id FROM tb_project_homelist WHERE homeNo LIKE  '%" + param[1] + "%'"
            spaceID = DB_database.excuteSql(spaceIDSql, db="db_project")[0][0]
            return spaceID






    @staticmethod
    def deviceSql(*param):
        #第一个是类型，第二个是参数值，
        if param[0]=="getDeviceTypeId":
            modelId = "SELECT id from tb_project_device_type WHERE `name` LIKE '%"+param[1]+"%'"
            modelId=DB_database.excuteSql(modelId,db="db_project")[0][0]
            return modelId

        #中控类目下添加产品
        if param[0]=="getProdutIdAndModel":
            produIdAndModelSql="SELECT id,model FROM tb_project_device_info WHERE `name` LIKE '%"+param[1]+"%'"

            produIdAndModel=DB_database.excuteSql(produIdAndModelSql,db="db_project")
            if produIdAndModel:
                return produIdAndModel[0]
            else:
                print "数据库返回空值！%s"%produIdAndModelSql
                sys.exit()

    @staticmethod
    def projectSql():
        pass