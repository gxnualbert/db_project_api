#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: projectMain.py
@time: 2018/05/14/11:12
"""
import datetime
import time
import unittest

from device_manage.device_instance import DeviceInstance as di
from house_manage.customer_manage import CustomerManage as cm
from system_manage.role_manage import RoleManage as rm
from system_manage.user_manage import UserManage as um
from util.check_report_dir import CheckReportPath as checkDir
from util.HTMLTestRunner import HTMLTestRunner


suite = unittest.TestSuite()

# 设备相关开始
# suite.addTest(di("center_control_add_instance"))#pass
# suite.addTest(di("center_control_update_instance"))#pass
# suite.addTest(di("center_control_delete_instance"))#pass
# suite.addTest(di("lock_add_instance_common"))#pass
# suite.addTest(di("lock_add_instance_net"))#pass
# suite.addTest(di("lock_add_instance_other"))#pass
# suite.addTest(di("lock_update_instance"))#pass
# suite.addTest(di("lock_delete_instance"))#pass
# suite.addTest(di("water_add_instance"))#pass
# suite.addTest(di("water_update_instance"))#pass
# suite.addTest(di("water_delete_instance"))#pass
# suite.addTest(di("electric_add_instance"))#pass
# suite.addTest(di("electric_update_instance"))#pass
# suite.addTest(di("electric_delete_instance"))#pass
# suite.addTest(di("collector_add_instance"))#pass
# suite.addTest(di("collector_update_instance"))#pass
# suite.addTest(di("collector_delete_instance"))#pass
# suite.addTest(di("door_access_add_instance"))#pass
# suite.addTest(di("smoke_detector_add_instance"))#pass
# suite.addTest(di("smoke_detector_update_instance"))#pass
# suite.addTest(di("smoke_detector_delete_instance"))#pass
# suite.addTest(di("repeater_add_instance"))#pass
# suite.addTest(di("repeater_update_instance"))#pass
# suite.addTest(di("repeater_delete_instance"))#pass
# suite.addTest(cm("add_home_provider"))#pass
# suite.addTest(cm("add_house_source"))#pass
# suite.addTest(cm("update_house_source"))#pass
# suite.addTest(cm("add_space"))#pass
# suite.addTest(cm("update_space"))#pass
# suite.addTest(cm("delete_space"))#pass
# suite.addTest(cm("delete_house_source"))#pass
# suite.addTest(cm("delete_home_provider"))#pass
# # 设备相关结束
##用户相关
suite.addTest(um("add_user_info"))#pass
suite.addTest(um("update_user_info"))#pass
suite.addTest(um("delete_user_info"))#pass
suite.addTest(rm("add_user_group"))#pass
suite.addTest(rm("update_user_group"))#pass
suite.addTest(rm("delete_user_group"))#pass

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    startTime = datetime.datetime.now()
    print(u"开始时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
    reportPath = checkDir.get_report_path()
    filename = "蛋贝工程管理系统接口测试报告" + now + ".html"
    reportFile = reportPath + "\\\\" + filename
    fp = open(reportFile, "wb")
    runner = HTMLTestRunner(stream=fp, title=u"蛋贝工程管理系统接口测试报告", description=u"蛋贝工程管理系统接口测试报告")
    runner.run(suite)
    fp.close()

    end = time.strftime("%Y-%m-%d %H:%M:%S")
    endtime = datetime.datetime.now()
    print("\n")
    print(u"结束时间：", end)
    print(u"总共花费时间为: %s" % (endtime - startTime))
