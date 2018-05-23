#!usr/bin/env python
#-*- coding:utf-8 -*-
"""
@author:albert.chen
@file: CheckReportDir.py
@time: 2017/12/11/17:42
"""
import sys

import os,time

class CheckReportPath():


    @staticmethod
    def get_report_path():
        cwd = os.getcwd()
        # parentpath = os.path.abspath(os.path.join(s, ".."))
        folder_path = cwd + "\\api_test_report\\\\" + time.strftime("%Y-%m-%d")

        if os.path.exists(folder_path):
            return folder_path
        else:
            os.makedirs(folder_path)
            return folder_path
