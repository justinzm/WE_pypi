#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 21:20
# @Author  : justin.郑 3907721@qq.com
# @File    : test.py.py
# @Desc    :

from web_extractor import NewsExtractor


def test(url):
    extractor = NewsExtractor()
    result = extractor.extract(url=url)
    print(result)


if __name__ == "__main__":
    url = '''https://timesofindia.indiatimes.com/business/india-business/raghuram-rajan-clears-the-air-on-how-to-fund-stimulus/articleshow/75639335.cms'''
    test(url=url)

