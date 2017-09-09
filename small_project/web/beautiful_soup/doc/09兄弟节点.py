from bs4 import BeautifulSoup

sibling_soup = BeautifulSoup("<a><b>text1</b><c>text2</c></b></a>")
# print(sibling_soup.prettify())
# <html>
#  <body>
#   <a>
#    <b>
#     text1
#    </b>
#    <c>
#     text2
#    </c>
#   </a>
#  </body>
# </html>

# .next_sibling 和 .previous_sibling
# 在文档树中,使用 .next_sibling 和 .previous_sibling 属性来查询兄弟节点
print(sibling_soup.b.next_sibling)  # <c>text2</c>
print(sibling_soup.c.previous_sibling)  # <b>text1</b>

# <b>标签有 .next_sibling 属性,但是没有 .previous_sibling 属性,
# 因为<b>标签在同级节点中是第一个.
# 同理,<c>标签有 .previous_sibling 属性,却没有 .next_sibling 属性

print(sibling_soup.b.previous_sibling)  # None
print(sibling_soup.c.next_sibling)  # None

# 实际文档中的tag的 .next_sibling 和 .previous_sibling 属性通常是字符串或空白
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
# 如果以为第一个<a>标签的 .next_sibling 结果是第二个<a>标签,那就错了,
# 真实结果是第一个<a>标签和第二个<a>标签之间的顿号和换行符
index_soup = BeautifulSoup(open('index.html'))
link = index_soup.a
print(link)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

print(link.next_sibling)  # ,

# 第二个<a>标签是顿号的 .next_sibling 属性
print(link.next_sibling.next_sibling)  # <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>

# .next_siblings 和 .previous_siblings
# 通过 .next_siblings 和 .previous_siblings 属性可以对当前节点的兄弟节点迭代输出
print('------------------------')

for sibling in index_soup.a.next_siblings:
    print(repr(sibling))
# ',\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ' and\n'
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
# ';\nand they lived at the bottom of a well.'

print('------------------------')

for sibling in index_soup.find(id='link3').previous_siblings:
    print(repr(sibling))
# ' and\n'
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>
# ',\n'
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>
# 'Once upon a time there were three little sisters; and their names were\n'




