html_doc = """
<html><head><title>The Dormouse's story</title></head>

<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc)

head_tag = soup.head
title_tag = soup.title

print(head_tag)  # <head><title>The Dormouse's story</title></head>
print(title_tag)  # <title>The Dormouse's story</title>
print(title_tag.parent)  # <head><title>The Dormouse's story</title></head>

# 文档title的字符串也有父节点:<title>标签

print(title_tag.string.parent)  # <title>The Dormouse's story</title>

# 文档的顶层节点比如<html>的父节点是 BeautifulSoup 对象
html_tag = soup.html
print(type(html_tag.parent))  # <class 'bs4.BeautifulSoup'>

# BeautifulSoup 对象的 .parent 是None
print(soup.parent)  # None

# .parents
# 通过元素的 .parents 属性可以递归得到元素的所有父辈节点
print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

for parent in soup.a.parents:
    print(parent.name)
# p
# body
# html
# [document]



