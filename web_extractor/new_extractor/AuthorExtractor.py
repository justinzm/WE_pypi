#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 12:16
# @Author  : justin.郑 3907721@qq.com
# @File    : AuthorExtractor.py
# @Desc    : 新闻作者信息抽取

import re
from lxml.html import HtmlElement
from web_extractor.cons import AUTHOR_PATTERN, TITLE_SPLIT_CHAR_PATTERN
from web_extractor.new_extractor.new_utils import config


class AuthorExtractor:
    def extract(self, element: HtmlElement, author_xpath=''):
        author_xpath = author_xpath or config.get('author', {}).get('xpath')
        author = self.extract_from_xpath(element, author_xpath) \
                or self.extract_from_htag(element)
        return author.strip()

    def extract_from_xpath(self, element, author_xpath):
        if author_xpath:
            author_list = element.xpath(author_xpath)
            if author_list:
                return author_list[0]
            else:
                return ''
        return ''

    def extract_from_htag(self, element):
        text = ''.join(element.xpath('.//text()'))
        for pattern in AUTHOR_PATTERN:
            author_obj = re.search(pattern, text)
            if author_obj:
                return author_obj.group(1)
        return ''

