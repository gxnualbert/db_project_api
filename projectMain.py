#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: projectMain.py
@time: 2018/05/14/11:12
"""
import time,datetime
from util.CheckReportDir import CheckReportPath as checkDir
from util.HTMLTestRunner import HTMLTestRunner
import unittest
suite = unittest.TestSuite()






if __name__=="__main__":

    now=time.strftime("%Y-%m-%d %H_%M_%S")
    startTime = datetime.datetime.now()
    print u"开始时间：",time.strftime("%Y-%m-%d %H:%M:%S")
    reportPath=checkDir.CheckReportPath.getReportPath()
    filename="蛋贝云端智能服务系统接口测试报告"+now+".html"
    reportFile=reportPath+"\\\\"+filename
    fp=open(reportFile.decode('utf-8'), "wb")
    runner=HTMLTestRunner(stream=fp,title="蛋贝云端智能服务系统接口测试报告",description="蛋贝云端智能服务系统接口测试报告")
    runner.run(suite)
    fp.close()

    end=time.strftime("%Y-%m-%d %H:%M:%S")
    endtime  = datetime.datetime.now()
    print "\n"
    print u"结束时间：",end

    print u"总共花费时间为: %s" % (endtime - startTime)
