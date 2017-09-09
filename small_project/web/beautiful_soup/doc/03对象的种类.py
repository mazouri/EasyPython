"""
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构,
每个节点都是Python对象,所有对象可以归纳为4种:

 Tag , NavigableString , BeautifulSoup , Comment .
"""

from bs4 import BeautifulSoup

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')

# 1.Tag对象
# Tag 对象与XML或HTML原生文档中的tag相同
tag = soup.b
print(tag)  # <b class="boldest">Extremely bold</b>
print(type(tag))  # <class 'bs4.element.Tag'>

# tag中最重要的属性: name 和 attributes

# 1.1 name : 获取tag的名字
print(tag.name)  # b

# 如果改变了tag的name,那将影响所有通过当前Beautiful Soup对象生成的HTML文档
tag.name = 'hahaha'

print(tag)  # <hahaha class="boldest">Extremely bold</hahaha>

# 1.2 attributes ： 一个tag可能有很多个属性；
# <b class="boldest"> 有一个 “class” 的属性,值为 “boldest” . tag的属性的操作方法与字典相同
print(tag['class'])  # ['boldest']

# 也可以直接点取属性
print(tag.attrs)  # {'class': ['boldest']}

# tag的属性可以被添加、删除和修改
tag['class'] = 'verybold'  # 修改属性值
print(tag.attrs)  # {'class': 'verybold'}

tag['id'] = 1  # 添加属性
print(tag.attrs)  # {'class': 'verybold', 'id': 1}

del tag['id']  # 删除属性
print(tag.attrs)  # {'class': 'verybold'}

print(tag.get('class'))  # verybold


















