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
result = extractor.extract(html)
print(result)
```

