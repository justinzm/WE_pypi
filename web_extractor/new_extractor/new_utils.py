#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 10:32
# @Author  : justin.郑 3907721@qq.com
# @File    : new_utils.py
# @Desc    : 新闻类信息抽取工具

import os
import yaml


def read_config():
    if os.path.exists('.new_config'):
        with open('.new_config', encoding='utf-8') as f:
            config_text = f.read()
        config = yaml.safe_load(config_text)
        return config
    return {}


config = read_config()

