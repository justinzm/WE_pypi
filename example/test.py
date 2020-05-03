#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 21:20
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py.py
# @Desc    :

from web_extractor import NewsExtractor


def test(html):
    extractor = NewsExtractor()
    result = extractor.extract(html)
    print(result)


if __name__ == "__main__":
    html = ''' 

 '''
    test(html)