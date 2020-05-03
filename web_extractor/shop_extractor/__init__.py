#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 11:05
# @Author  : justin.郑 3907721@qq.com
# @File    : __init__.py.py
# @Desc    : 电商类站点页面自动化抽取类
from web_extractor.shop_extractor.KeywordsExtractor import KeywordsExtractor
from web_extractor.shop_extractor.TitleExtractor import TitleExtractor
from web_extractor.utils import html2element


class ShopExtractor:
    def extract(self,
                html,
                keywords_xpath='',
                shop_name_xpath='',
                host='',
                noise_node_list=None,
                with_body_html=False):
        """
        新闻类站点自动化抽取
        :param html:                新闻页面源代码
        :param title_xpath:         新闻标题xpath
        :param author_xpath:        作者xpath
        :param publish_time_xpath:  发布时间xpath
        :param keywords_xpath:      新闻关键词xpath
        :param host:                站点网址
        :param noise_node_list:     去除多余list内容
        :param with_body_html:
        :return:    输出json
        """
        element = html2element(html)

        shop_name = TitleExtractor().extract(element, title_xpath=shop_name_xpath)
        keywords = KeywordsExtractor().extract(element, keywords_xpath=keywords_xpath)

        result = {'shop_name': shop_name,
                  'keywords': keywords
                  }

        return result
