#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 10:32
# @Author  : justin.郑 3907721@qq.com
# @File    : new_utils.py
# @Desc    : 新闻类信息抽取工具


def read_config():
    return {
        "title": {
            "xpath": "//title/text()"
        }
    }


config = read_config()


