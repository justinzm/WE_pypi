#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/2 21:58
# @Author  : justin.郑 3907721@qq.com
# @File    : utils.py.py
# @Desc    : 工具集

import re
from urllib.parse import urlparse, urljoin
from lxml.html import fromstring, HtmlElement
from lxml.html import etree
from web_extractor.cons import USELESS_TAG, TAGS_CAN_BE_REMOVE_IF_EMPTY, USELESS_ATTR, HIGH_WEIGHT_ARRT_KEYWORD


def normalize_node(element: HtmlElement):
    # 去除etree中的某个子节点
    etree.strip_elements(element, *USELESS_TAG)
    for node in iter_node(element):
        # inspired by readability.
        if node.tag.lower() in TAGS_CAN_BE_REMOVE_IF_EMPTY and is_empty_element(node):
            remove_node(node)

        # 参数中的标签从源element中删除，并且把里面的标签文本给合并进来
        if node.tag.lower() == 'p':
            etree.strip_tags(node, 'span')
            etree.strip_tags(node, 'strong')

        # 如果div标记不包含任何子节点，则可以将其转换为p节点。
        if node.tag.lower() == 'div' and not node.getchildren():
            node.tag = 'p'

        if node.tag.lower() == 'span' and not node.getchildren():
            node.tag = 'p'

        # remove empty p tag
        if node.tag.lower() == 'p' and not node.xpath('.//img'):
            if not (node.text and node.text.strip()):
                drop_tag(node)

        class_name = node.get('class')
        if class_name:
            for attribute in USELESS_ATTR:
                if attribute in class_name:
                    remove_node(node)
                    break


def html2element(html):
    html = re.sub('</?br.*?>', '', html)
    # 将字符串转换为Element对象，解析树的根节点度。
    element = fromstring(html)
    return element


def pre_parse(element):
    normalize_node(element)
    return element


def remove_noise_node(element, noise_xpath_list):
    noise_node_list = [
        '//div[@class=\"comment-list\"]',
        '//*[@style=\"display:none\"]',
        '//*[@class="contheight"]'
    ]
    noise_xpath_list = noise_xpath_list or noise_node_list
    # noise_xpath_list = noise_xpath_list or config.get('noise_node_list')
    if not noise_xpath_list:
        return
    for noise_xpath in noise_xpath_list:
        nodes = element.xpath(noise_xpath)
        for node in nodes:
            remove_node(node)
    return element


def iter_node(element: HtmlElement):
    yield element
    for sub_element in element:
        if isinstance(sub_element, HtmlElement):
            yield from iter_node(sub_element)


def remove_node(node: HtmlElement):
    """
    移除指定标签
    """
    # 获得父标签
    parent = node.getparent()
    if parent is not None:
        parent.remove(node)


def drop_tag(node: HtmlElement):
    """
    只删除标记，但将其文本合并到父标记。
    """
    parent = node.getparent()
    if parent is not None:
        node.drop_tag()


def is_empty_element(node: HtmlElement):
    """ 判断是否为空element """
    return not node.getchildren() and not node.text


def pad_host_for_images(host, url):
    """
    网站上的图片可能有如下几种格式：
    完整的绝对路径：https://xxx.com/1.jpg
    完全不含 host 的相对路径： /1.jpg
    含 host 但是不含 scheme:  xxx.com/1.jpg 或者  ://xxx.com/1.jpg
    :param host:
    :param url:
    :return:
    """
    if url.startswith('http'):
        return url
    parsed_uri = urlparse(host)
    scheme = parsed_uri.scheme
    if url.startswith(':'):
        return f'{scheme}{url}'
    if url.startswith('//'):
        return f'{scheme}:{url}'
    return urljoin(host, url)


def get_high_weight_keyword_pattern():
    return re.compile('|'.join(HIGH_WEIGHT_ARRT_KEYWORD), flags=re.I)


if __name__ == "__main__":
    html = ''' 

     '''
    tmp = html2element(html)
