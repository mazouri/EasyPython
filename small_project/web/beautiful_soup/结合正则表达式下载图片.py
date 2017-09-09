# coding:utf-8
import random
import re
from urllib.request import urlopen, Request, urlretrieve

from bs4 import BeautifulSoup


def get_html(url, headers):
    """
    用于抓取返回403禁止访问的网页
    :param url:
    :param headers:
    :return:
    """
    random_header = random.choice(headers)

    req = Request(url)
    req.add_header('User-Agent', random_header)
    req.add_header('GET', url)
    req.add_header('Host', 'tieba.baidu.com')
    req.add_header('Referer', 'http://tieba.baidu.com/p/4792769205')
    html = urlopen(req)
    return html

url = 'http://tieba.baidu.com/p/4792769205'

# 下面headers需要使用自己主机的User-Agent进行构造
my_headers = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36']

html = get_html(url, my_headers)

bsObj = BeautifulSoup(html, 'lxml')

imageList = bsObj.findAll('img', {'src': re.compile('http://imgsrc.baidu.com/forum/w%3D580/sign=.+\.jpg')})

for index, image in enumerate(imageList):
    imageUrl = image['src']
    imageLocation = '/home/wangdongdong/test/' + str(index + 1) + '.jpg'
    urlretrieve(imageUrl, imageLocation)
    print("图片 ", index + 1, "下载完成")

