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

# 1.tag的名字
# 操作文档树最简单的方法就是告诉它你想获取的tag的name
# 如果想获取 <head> 标签,只要用 soup.head
print(soup.head)  # <head><title>The Dormouse's story</title></head>

print(soup.title)  # <title>The Dormouse's story</title>

print(soup.body.b)  # <b>The Dormouse's story</b>

# 通过点取属性的方式只能获得当前名字的第一个tag
print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# 如果想要得到所有的<a>标签,或是通过名字得到比一个tag更多的内容的时候,
# 就需要用到 Searching the tree 中描述的方法,比如: find_all()
print(soup.find_all('a'))

# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

aList = soup.find_all('a')
for a in aList:
    print(a)

# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# .contents 和 .children
# .contents 属性可以将tag的子节点以列表的方式输出

head_tag = soup.head
print(head_tag)  # <head><title>The Dormouse's story</title></head>

print(head_tag.contents)  # [<title>The Dormouse's story</title>]

title_tag = head_tag.contents[0]
print(title_tag)  # <title>The Dormouse's story</title>

print(title_tag.contents)  # ["The Dormouse's story"]

# BeautifulSoup 对象本身一定会包含子节点,也就是说<html>标签也是 BeautifulSoup 对象的子节点
print(len(soup.contents))  # 1

print(soup.contents[0].name)  # html

# 字符串没有.contents属性，因为字符串没有子节点
text = title_tag.contents[0]
# print(text.contents)  # 'NavigableString' object has no attribute 'contents'

# 通过tag的 .children 生成器,可以对tag的子节点进行循环
for child in title_tag.children:
    print(child)

# The Dormouse's story

for child in soup.body.children:
    print(child)

# <p class="title"><b>The Dormouse's story</b></p>
#
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a> and
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
#
# <p class="story">...</p>

# .descendants
# .contents 和 .children 属性仅包含tag的直接子节点.例如,<head>标签只有一个直接子节点<title>


# .descendants 属性可以对所有tag的子孙节点进行递归循环
for child in head_tag.descendants:
    print(child)

# <title>The Dormouse's story</title>
# The Dormouse's story

# BeautifulSoup 有一个直接子节点(<html>节点),却有很多子孙节点
print(len(list(soup.children)))  # 1

print(len(list(soup.descendants)))  # 25

# .string
# 如果tag只有一个 NavigableString 类型子节点,那么这个tag可以使用 .string 得到子节点

print(title_tag.string)  # The Dormouse's story

# 如果一个tag仅有一个子节点,那么这个tag也可以使用 .string 方法,输出结果与当前唯一子节点的 .string 结果相同
print(head_tag.contents)  # [<title>The Dormouse's story</title>]

print(head_tag.string)  # The Dormouse's story

# 如果tag包含了多个子节点,tag就无法确定 .string 方法应该调用哪个子节点的内容, .string 的输出结果是 None
print(soup.html.string)  # None

# .strings 和 stripped_strings
# 如果tag中包含多个字符串, 可以使用 .strings 来循环获取
for string in soup.strings:
    print(repr(string))
# "The Dormouse's story"
# '\n'
# "The Dormouse's story"
# '\n'
# 'Once upon a time there were three little sisters; and their names were\n'
# 'Elsie'
# ',\n'
# 'Lacie'
# ' and\n'
# 'Tillie'
# ';\nand they lived at the bottom of a well.'
# '\n'
# '...'
# '\n'

# 输出的字符串中可能包含了很多空格或空行,使用 .stripped_strings 可以去除多余空白内容
for string in soup.stripped_strings:
    print(repr(string))
# "The Dormouse's story"
# "The Dormouse's story"
# 'Once upon a time there were three little sisters; and their names were'
# 'Elsie'
# ','
# 'Lacie'
# 'and'
# 'Tillie'
# ';\nand they lived at the bottom of a well.'
# '...'









