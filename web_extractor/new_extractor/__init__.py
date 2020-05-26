#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 21:49
# @Author  : justin.郑 3907721@qq.com
# @File    : __init__.py.py
# @Desc    : 新闻类站点自动化抽取类

import chardet
import requests
from web_extractor.new_extractor.AuthorExtractor import AuthorExtractor
from web_extractor.new_extractor.ContentExtractor import ContentExtractor
from web_extractor.new_extractor.DescriptionExtractor import DescriptionExtractor
from web_extractor.new_extractor.KeywordsExtractor import KeywordsExtractor
from web_extractor.new_extractor.TimeExtractor import TimeExtractor
from web_extractor.new_extractor.TitleExtractor import TitleExtractor
from web_extractor.utils import html2element, pre_parse, remove_noise_node
from web_extractor.new_extractor.new_utils import config


class NewsExtractor:
    def extract(self,
                url='',
                html=None,
                title_xpath='',
                author_xpath='',
                publish_time_xpath='',
                keywords_xpath='',
                description_xpath='',
                host='',
                noise_node_list=None,
                with_body_html=False):
        """
        新闻类站点自动化抽取
        :param url:                 新闻页面网址
        :param html:                新闻页面源代码
        :param title_xpath:         新闻标题xpath
        :param author_xpath:        作者xpath
        :param publish_time_xpath:  发布时间xpath
        :param keywords_xpath:      新闻关键词xpath
        :param description_xpath:   新闻简介xpath
        :param host:                站点网址
        :param noise_node_list:     去除多余list内容
        :param with_body_html:
        :return:    输出json
        """
        if url is not None and len(url) > 0:
            html = self.getHtml(url=url)

        element = html2element(html)

        title = TitleExtractor().extract(element, title_xpath=title_xpath)
        publish_time = TimeExtractor().extract(element, publish_time_xpath=publish_time_xpath)
        author = AuthorExtractor().extract(element, author_xpath=author_xpath)
        keywords = KeywordsExtractor().extract(element, keywords_xpath=keywords_xpath)
        description = DescriptionExtractor().extract(element, description_xpath=description_xpath)

        element = pre_parse(element)
        remove_noise_node(element, noise_node_list)
        content = ContentExtractor().extract(element, host, with_body_html)
        result = {'title': title,
                  'author': author,
                  'publish_time': publish_time,
                  'keywords': keywords,
                  'description': description,
                  'content': content[0][1]['text'],
                  'images': content[0][1]['images']}
        if with_body_html or config.get('with_body_html', False):
            result['body_html'] = content[0][1]['body_html']
        return result

    def getHtml(self, url: str) -> str:
        headers = {
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
        }
        response = requests.get(url, headers=headers)
        encode_info = chardet.detect(response.content)
        response.encoding = encode_info['encoding'] if encode_info['confidence'] > 0.5 else 'utf-8'
        return response.text