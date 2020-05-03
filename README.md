## Web-Extractor (python3)

Web-Extractor 支持Python 3.6+，旨在更方便更智能提取Html中所需内容。

#### 建议安装方法
    pip install web-extractor

#### 升级方法
    pip install web-extractor --upgrade

#### 使用方法

```buildoutcfg
from web_extractor import NewsExtractor

extractor = NewsExtractor()
result = extractor.extract(html, title_xpath='//title/text()')
print(result)
```

#### 各个参数的意义如下：

html(str): 目标网站的源代码

title_xpath(str): 新闻标题的 XPath，用于定向提取标题

host(str): 图片所在的域名，例如``https://www.sina.com``, 那么，当从新闻网站提取到图片的相对连接``/images/123.png``时，会把 host 拼接上去，变成``https://www.sina.com/images/123.png``

noise_node_list(List[str]): 一个包含 XPath 的列表。这个列表中的 XPath 对应的标签，会在预处理时被直接删除掉，从而避免他们影响新闻正文的提取

author_xpath(str): 文章作者的 XPath，用于定向提取文章作者

keywords_xpath(str): 文章关键词的 XPath，用于定向提取文章关键词

description_xpath(str): 文章简介的 XPath，用于定向提取文章简介

publish_time_xpath(str): 文章发布时间的 XPath，用于定向提取文章发布时间

with_body_html(bool): 默认为 False，此时，返回的提取结果不含新闻正文所在标签的 HTML 源代码。当把它设置为 True 时，返回的结果会包含字段 body_html，内容是新闻正文所在标签的 HTML 源代码