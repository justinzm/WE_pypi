#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 12:16
# @Author  : justin.郑 3907721@qq.com
# @File    : __init__.py.py
# @Desc    : AuthorExtractor.py

import re
from lxml.html import HtmlElement
from web_extractor.cons import AUTHOR_PATTERN
from web_extractor.new_extractor.new_utils import config


class AuthorExtractor:
    def __init__(self):
        self.author_pattern = AUTHOR_PATTERN

    def extractor(self, element: HtmlElement, author_xpath=''):
        author_xpath = author_xpath or config.get('author', {}).get('xpath')
        if author_xpath:
            author = ''.join(element.xpath(author_xpath))
            return author
        text = ''.join(element.xpath('.//text()'))
        for pattern in self.author_pattern:
            author_obj = re.search(pattern, text)
            if author_obj:
                return author_obj.group(1)
        return ''
