# coding:utf-8

from urllib.request import urlopen

from bs4 import BeautifulSoup

html = urlopen('http://movie.douban.com')

bsObj = BeautifulSoup(html, 'lxml')

liList = bsObj.find_all('li', {'class': 'title'})  # 通过标签的名称和属性来查找标签

for li in liList:
    print(li.a.get_text())  # 获取标签<a>中的文字

