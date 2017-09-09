# coding:utf-8

from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://movie.douban.com')

bsObj = BeautifulSoup(html, 'lxml')

liList = bsObj.findAll('li', {'class': 'ui-slide-item'})

for li in liList:
    ul = li.children
    for child in ul: #由于children是个孩子集合，所以下面要迭代进行查看
        print(child)
