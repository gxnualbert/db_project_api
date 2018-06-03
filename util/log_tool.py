#!usr/bin/env python
#-*- coding:utf-8 _*-
"""
@author:albert.chen
@file: logTool.py
@time: 2018/04/27/22:19
"""


import logging
import logging.handlers


import logging

# 参考文章https://www.cnblogs.com/dkblog/archive/2011/08/26/2155018.html
class AddLog(object):
    def __init__(self):
        pass
    @staticmethod
    def log(log_message):

        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename="",
                            filemode='w')
        #################################################################################################
        # 定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
        console = logging.StreamHandler()
        # console = logging.FileHandler(LOG_FILE)  # 写到文件中，不会写到HTML里面
        console.setLevel(logging.INFO)
        formatter = logging.Formatter('%(name)s: %(levelname)s %(message)s')
        console.setFormatter(formatter)
        logging.getLogger('').addHandler(console)
        #################################################################################################
        logging.info(log_message)

    @staticmethod
    def status_code_API_return(opt_time, API_status_code):
        AddLog.log("{optTime}返回的状态码:{apiStatusCode}".format(optTime=opt_time, apiStatusCode=API_status_code))
