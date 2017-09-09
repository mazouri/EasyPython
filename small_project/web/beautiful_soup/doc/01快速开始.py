from bs4 import BeautifulSoup  # 导入库

# 要解析的HTML文档
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc)

# print(soup.prettify())  # prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行


# 输出结果（按照标准的缩进格式输出）

# <html>
#  <head>
#   <title>
#    The Dormouse's story
#   </title>
#  </head>
#  <body>
#   <p class="title">
#    <b>
#     The Dormouse's story
#    </b>
#   </p>
#   <p class="story">
#    Once upon a time there were three little sisters; and their names were
#    <a class="sister" href="http://example.com/elsie" id="link1">
#     Elsie
#    </a>
#    ,
#    <a class="sister" href="http://example.com/lacie" id="link2">
#     Lacie
#    </a>
#    and
#    <a class="sister" href="http://example.com/tillie" id="link3">
#     Tillie
#    </a>
#    ;
# and they lived at the bottom of a well.
#   </p>
#   <p class="story">
#    ...
#   </p>
#  </body>
# </html>

# 浏览结构化数据
print(soup.title)  # <title>The Dormouse's story</title>

print(soup.title.name)  # title
print(soup.head.name)  # head

print(soup.title.text)  # The Dormouse's story

print(soup.title.parent.name)  # head

print(soup.p)  # <p class="title"><b>The Dormouse's story</b></p>

print(soup.p['class'])  # ['title']

print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(soup.find_all('a'))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.find(id='link3'))  # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# 找到所有a标签的链接
for link in soup.find_all('a'):
    href = link.get('href')
    print(href)

# http://example.com/elsie
# http://example.com/lacie
# http://example.com/tillie

# 获取所有文字内容

print(soup.get_text())
# print(soup.getText())

# The Dormouse's story
#
# The Dormouse's story
# Once upon a time there were three little sisters; and their names were
# Elsie,
# Lacie and
# Tillie;
# and they lived at the bottom of a well.
# ...




