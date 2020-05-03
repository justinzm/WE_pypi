#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/3 14:17
# @Author  : justin.郑 3907721@qq.com
# @File    : TitleExtractor.py
# @Desc    : 电商 商品标题抽取

import re
from lxml.html import HtmlElement
from web_extractor.cons import TITLE_SPLIT_CHAR_PATTERN, TITLE_HTAG_XPATH
from web_extractor.shop_extractor.shop_utils import config


class TitleExtractor:
    def extract(self, element: HtmlElement, title_xpath: str = ''):
        title_xpath = title_xpath or config.get('title', {}).get('xpath')
        title = self.extract_from_xpath(element, title_xpath) \
                or self.extract_from_title(element) \
                or self.extract_from_htag(element)
        return title.strip()

    def extract_from_xpath(self, element, title_xpath):
        if title_xpath:
            title_list = element.xpath(title_xpath)
            if title_list:
                title = re.split(TITLE_SPLIT_CHAR_PATTERN, title_list[0])
                return title[0]
            else:
                return ''
        return ''

    def extract_from_title(self, element):
        title_list = element.xpath('//title/text()')
        if not title_list:
            return ''
        title = re.split(TITLE_SPLIT_CHAR_PATTERN, title_list[0])
        if title:
            return title[0]
        else:
            return ''

    def extract_from_htag(self, element):
        title_list = element.xpath(TITLE_HTAG_XPATH)
        if not title_list:
            return ''
        return title_list[0]