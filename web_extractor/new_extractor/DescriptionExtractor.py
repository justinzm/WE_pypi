#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 12:16
# @Author  : justin.郑 3907721@qq.com
# @File    : DescriptionExtractor.py
# @Desc    : 新闻文章简介信息抽取

from lxml.html import HtmlElement
from web_extractor.cons import DESCRIPTION_META
from web_extractor.new_extractor.new_utils import config


class DescriptionExtractor:
    def extract(self, element: HtmlElement, description_xpath: str = '') -> str:
        description_xpath = description_xpath or config.get('description', {}).get('xpath')
        description = (self.extract_from_user_xpath(description_xpath, element)  # 用户指定的 Xpath 是第一优先级
                        or self.extract_from_meta(element))
        return description

    def extract_from_user_xpath(self, description_xpath: str, element: HtmlElement) -> str:
        # 用户指定的 Xpath 是第一优先级
        if description_xpath:
            keywords = ''.join(element.xpath(description_xpath))
            return keywords
        return ''

    def extract_from_meta(self, element: HtmlElement) -> str:
        for xpath in DESCRIPTION_META:
            keywords = element.xpath(xpath)
            if keywords:
                return ''.join(keywords)
        return ''


