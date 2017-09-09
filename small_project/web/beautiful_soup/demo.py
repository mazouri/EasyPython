# coding:utf-8

from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://tieba.baidu.com/')

bsObj = BeautifulSoup(html, 'lxml')  # 在这里讲html对象转化为BeautifulSoup对象.

print(bsObj.title)  # <title>百度贴吧——全球最大的中文社区</title>
# print(bsObj.__str__)  # 会发现bsObj对象的内容 是网页的源代码；任意节点信息都可以被提取出来

print(bsObj.title.text)  # 百度贴吧——全球最大的中文社区

