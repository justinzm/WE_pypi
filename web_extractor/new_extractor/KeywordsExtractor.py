#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 12:16
# @Author  : justin.郑 3907721@qq.com
# @File    : KeywordsExtractor.py
# @Desc    : 新闻关键词信息抽取

import re
from lxml.html import HtmlElement
from web_extractor.cons import KEYWORDS_META, KEYWORDS_PATTERN
from web_extractor.new_extractor.new_utils import config


class KeywordsExtractor:
    def extract(self, element: HtmlElement, keywords_xpath: str = '') -> str:
        keywords_xpath = keywords_xpath or config.get('keywords', {}).get('xpath')
        keywords = (self.extract_from_user_xpath(keywords_xpath, element)  # 用户指定的 Xpath 是第一优先级
                        or self.extract_from_meta(element)   # 第二优先级从 Meta 中提取
                        or self.extract_from_text(element))  # 最坏的情况从正文中提取
        return keywords

    def extract_from_user_xpath(self, keywords_xpath: str, element: HtmlElement) -> str:
        # 用户指定的 Xpath 是第一优先级
        if keywords_xpath:
            keywords = ''.join(element.xpath(keywords_xpath))
            return keywords
        return ''

    def extract_from_meta(self, element: HtmlElement) -> str:
        """
        一些很规范的新闻网站，会把关键词放在 META 中，因此应该优先检查 META 数据
        """
        for xpath in KEYWORDS_META:
            keywords = element.xpath(xpath)
            if keywords:
                return ''.join(keywords)
        return ''

    def extract_from_text(self, element: HtmlElement) -> str:
        text = ''.join(element.xpath('.//text()'))
        for dt in KEYWORDS_PATTERN:
            dt_obj = re.search(dt, text)
            if dt_obj:
                return dt_obj.group(1)
        else:
            return ''


