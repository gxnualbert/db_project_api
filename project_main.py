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
from util.check_report_dir import CheckReportPath as checkDir
from util.HTMLTestRunner import HTMLTestRunner


suite = unittest.TestSuite()
suite.addTest(di("test_center_control_add_instance"))
suite.addTest(di("center_control_update_instance"))
suite.addTest(di("center_control_delete_instance"))
# suite.addTest(getLockApi("test_0001deviceInfo_getLockInfo"))#pass
# suite.addTest(getLockApi("test_0002deviceInfo_getLockPwdList"))
# suite.addTest(getLockApi("test_0003deviceCtrl_lockPwd_addPwd_zuke"))


if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    startTime = datetime.datetime.now()
    print(u"开始时间：", time.strftime("%Y-%m-%d %H:%M:%S"))
    reportPath = checkDir.getReportPath()
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
