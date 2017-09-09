from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<p class="title"><b>The Dormouse's story</b></p>
"""
# HTML解析器把这段字符串转换成一连串的事件:
# “打开<html>标签”,”打开一个<head>标签”,
# ”打开一个<title>标签”,”添加一段字符串”,
# ”关闭<title>标签”,”打开<p>标签”,等等.
#
# Beautiful Soup提供了重现解析器初始化过程的方法.

# .next_element 和 .previous_element
# .next_element 属性指向解析过程中下一个被解析的对象(字符串或tag),
# 结果可能与 .next_sibling 相同,但通常是不一样的.

index_soup = BeautifulSoup(open('index.html'))

last_a_tag = index_soup.find("a", id='link3')
print(last_a_tag)  # <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

print(last_a_tag.next_sibling)
# ;
# and they lived at the bottom of a well.

# 但这个<a>标签的 .next_element 属性结果是在<a>标签被解析之后的解析内容,
# 不是<a>标签后的句子部分,应该是字符串”Tillie”
print(last_a_tag.next_element)  # Tillie

# 解析器先进入<a>标签,然后是字符串“Tillie”,然后关闭</a>标签,然后是分号和剩余部分
# 分号与<a>标签在同一层级,但是字符串“Tillie”会被先解析

# .previous_element 属性刚好与 .next_element 相反,它指向当前被解析的对象的前一个解析对象
print(last_a_tag.previous_element)  # and

print(last_a_tag.previous_element.next_element)
# <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>

# .next_elements 和 .previous_elements
# 通过 .next_elements 和 .previous_elements 的迭代器就可以向前或向后访问文档的解析内容,
# 就好像文档正在被解析一样

for ele in last_a_tag.next_elements:
    print(repr(ele))
# 'Tillie'
# ';\nand they lived at the bottom of a well.'
# '\n'
# <p class="story">...</p>
# '...'
