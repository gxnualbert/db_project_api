#!usr/bin/env python
# -*- coding:utf-8 _*-
"""
@author:albert.chen
@file: txt_info.py
@time: 2018/05/22/12:07
"""


class TextUtil(object):

    # 命名规则为：包-模块-类-函数-文字
    # 或：包-模块-类-函数-变量

    @staticmethod
    def common_text():
        common_text_dict = dict()
        common_text_dict["status_not_200"] = "返回状态码不为200!"
        common_text_dict["compare_not_equal"] = "数据库存储的{info}跟实际比对的不一致!"

        return common_text_dict

    @staticmethod
    def text_center_control():
        text_center_control_dict = {}
        text_center_control_dict[""]
        base_text = ""
