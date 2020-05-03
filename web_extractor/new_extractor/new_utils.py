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
        },
        "host": "",
        "noise_node_list": [
            '//div[@class=\"comment-list\"]',
            '//*[@style=\"display:none\"]',
            '//*[@class="contheight"]'
        ],
        "with_body_html": False,
        "author": {
            "xpath": '//meta[@name="author"]/@content'
        },
        "publish_time": {
            "xpath": '//em[@id="publish_time"]/text()'
        },
    }


# host: https://www.xxx.com
# noise_node_list:
#     - //div[@class=\"comment-list\"]
#     - //*[@style=\"display:none\"]
#     - //*[@class="contheight"]
# with_body_html: false
# author:
#     xpath: //meta[@name="author"]/@content
# publish_time:
#     xpath: //em[@id="publish_time"]/text()

config = read_config()

