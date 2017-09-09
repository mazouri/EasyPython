"""
Beautiful Soup定义了很多搜索方法,
这里着重介绍2个: find() 和 find_all() .其它方法的参数和用法类似
"""
import re

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

# 过滤器
# 过滤器可以被用在tag的name中,节点的属性中,字符串中或他们的混合中

# 1.字符串
# 在搜索方法中传入一个字符串参数,Beautiful Soup会查找与字符串完整匹配的内容,
# 下面的例子用于查找文档中所有的<b>标签
print(soup.find_all('b'))  # [<b>The Dormouse's story</b>]

# 2.正则表达式
# 如果传入正则表达式作为参数,Beautiful Soup会通过正则表达式的 match() 来匹配内容.
# 下面例子中找出所有 以b开头 的标签,这表示<body>和<b>标签都应该被找到

for tag in soup.find_all(re.compile('^b')):
    print(tag.name)
# body
# b

# 下面代码找出所有名字中 包含”t” 的标签
for tag in soup.find_all(re.compile('t')):
    print(tag.name)
# html
# title

# 3.列表
# 如果传入列表参数,BeautifulSoup会将与列表中"任一元素"匹配的内容返回.
# 下面代码找到文档中所有<a>标签和<b>标签

for tag in soup.find_all(['a', 'b']):
    print(tag.name)
# b
# a
# a
# a

# 4.True
# True 可以匹配任何值,
# 下面代码查找到所有的tag,但是不会返回字符串节点

for tag in soup.find_all(True):
    print(tag.name)


# html
# head
# title
# body
# p
# b
# p
# a
# a
# a
# p

# 5.方法
# 如果没有合适过滤器,那么还可以定义一个方法,方法只接受一个元素参数(元素参数,HTML文档中的一个tag节点,不能是文本节点)
# 如果这个方法返回 True 表示当前元素匹配并且被找到,如果不是则反回 False

# 下面方法校验了当前元素,如果包含 class 属性却不包含 id 属性,那么将返回 True
def has_class_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
# 将这个方法作为参数传入 find_all() 方法,将得到所有<p>标签
print('-------------------------')
tagList = soup.find_all(has_class_no_id)
for tag in tagList:
    print(tag.name)
# p
# p
# p

# 下面代码找到所有被文字包含的节点内容
from bs4 import NavigableString


def surrounded_by_string(tag):
    return isinstance(tag.next_element, NavigableString)\
           and isinstance(tag.previous_element, NavigableString)
print('-------------------------')

for tag in soup.find_all(surrounded_by_string):
    print(tag.name)
# p
# a
# a
# a
# p

# find_all( name , attrs , recursive , text , **kwargs )

# find_all() 方法搜索当前tag的"所有tag子节点",并判断是否符合过滤器的条件

print(soup.find_all('title'))  # [<title>The Dormouse's story</title>]
print(soup.find_all('p', 'title'))  # [<p class="title"><b>The Dormouse's story</b></p>]

print(soup.find_all("a"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

print(soup.find_all(id="link2"))
# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

print(soup.find(text=re.compile('sisters')))
# Once upon a time there were three little sisters; and their names were

#  find_all() 的参数

# find_all(name , attrs , recursive , text , **kwargs )

# name 参数
# name 参数可以查找所有名字为 name 的tag,字符串对象会被自动忽略掉

print(soup.find_all("title"))  # [<title>The Dormouse's story</title>]
# 搜索 name 参数的值可以使任一类型的 过滤器 ,字符窜,正则表达式,列表,方法或是 True

# keyword 参数

# 如果传入 href 参数,Beautiful Soup会搜索每个tag的”href”属性
print(soup.find_all(href=re.compile("elsie")))

# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]

# 搜索指定名字的属性时可以使用的参数值包括 字符串 , 正则表达式 , 列表, True

# 下面的例子在文档树中查找所有包含 id 属性的tag,无论 id 的值是什么
print(soup.find_all(id=True))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# 使用多个指定名字的参数可以同时过滤tag的多个属性
print(soup.find_all(href=re.compile("example.com"), id="link2"))

# [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# 有些tag属性在搜索不能使用,比如HTML5中的 data-* 属性
data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
# data_soup.find_all(data-foo="value")  # keyword can't be an expression

# 但是可以通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
print(data_soup.find_all(attrs={'data-foo': "value"}))
# [<div data-foo="value">foo!</div>]

# 按CSS搜索
# 按照CSS类名搜索tag的功能非常实用,但标识CSS类名的关键字 class 在Python中是保留字,
# 使用 class 做参数会导致语法错误.从Beautiful Soup的4.1.1版本开始,可以通过 class_
# 参数搜索有指定CSS类名的tag
print(soup.find_all("a", class_="sister"))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# class_ 参数同样接受不同类型的 过滤器 ,字符串,正则表达式,方法或 True
print(soup.find_all(class_=re.compile('itl')))
# [<p class="title"><b>The Dormouse's story</b></p>]


def has_six_characters(css_class):
    return css_class is not None and len(css_class) == 6


print(soup.find_all(class_=has_six_characters))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
# <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# tag的 class 属性是 多值属性 .按照CSS类名搜索tag时,可以分别搜索tag中的每个CSS类名
css_soup = BeautifulSoup('<p class="body strikeout"></p>')
css_soup.find_all("p", class_="strikeout")
# [<p class="body strikeout"></p>]

css_soup.find_all("p", class_="body")
# [<p class="body strikeout"></p>]

# 完全匹配 class 的值时,如果CSS类名的顺序与实际不符,将搜索不到结果
soup.find_all("a", attrs={"class": "sister"})
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>,
#  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>]

# text 参数
# 通过 text 参数可以搜搜文档中的字符串内容
soup.find_all("a", text="Elsie")
# [<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>]

# limit 参数
# find_all() 方法返回全部的搜索结构,如果文档树很大那么搜索会很慢.如果我们不需要全部结果,
# 可以使用 limit 参数限制返回结果的数量
# 当搜索到的结果数量达到 limit 的限制时,就停止搜索返回结果

# 文档树中有3个tag符合搜索条件,但结果只返回了2个,因为我们限制了返回数量
print(soup.find_all("a", limit=2))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>,
#  <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>]

# recursive 参数
# 调用tag的 find_all() 方法时,Beautiful Soup会检索当前tag的所有子孙节点,
# 如果只想搜索tag的直接子节点,可以使用参数 recursive=False
for tag in soup.find_all('html', recursive=False):
    print(tag.name)
# html
print(soup.find_all('title', recursive=False))
# []

# 像调用 find_all() 一样调用tag
# find_all() 几乎是Beautiful Soup中最常用的搜索方法,所以我们定义了它的简写方法.
#  BeautifulSoup 对象和 tag 对象可以被当作一个方法来使用,
# 这个方法的执行结果与调用这个对象的 find_all() 方法相同,
# 下面两行代码是等价的
print(soup.find_all("title"))  # [<title>The Dormouse's story</title>]
print(soup("title"))  # [<title>The Dormouse's story</title>]

# 这两行代码也是等价的
print(soup.find_all(text=True))
print(soup(text=True))

# ["The Dormouse's story", '\n', "The Dormouse's story",
#  '\n', 'Once upon a time there were three little sisters; and their names were\n',
#  'Elsie', ',\n', 'Lacie', ' and\n', 'Tillie', ';\nand they lived at the bottom of a well.',
#  '\n', '...', '\n']

# find()
# find( name , attrs , recursive , text , **kwargs )

# find_all() 方法将返回文档中符合条件的所有tag,尽管有时候我们只想得到一个结果.
# 比如文档中只有一个<body>标签,那么使用 find_all() 方法来查找<body>标签就不太合适,
#  使用 find_all 方法并设置 limit=1 参数不如直接使用 find() 方法.下面两行代码是等价的

print(soup.find_all('a', limit=1))
# [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>]
print(soup.find('a'))
# <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>

# 唯一的区别是 find_all() 方法的返回结果是值包含一个元素的列表,而 find() 方法直接返回结果
# find_all() 方法没有找到目标是返回空列表, find() 方法找不到目标时,返回 None
print(soup.find("123456"))  # None


# soup.head.title 是 tag的名字 方法的简写.这个简写的原理就是多次调用当前tag的 find() 方法
print(soup.head.title)  # <title>The Dormouse's story</title>
print(soup.find('head').find('title'))  # <title>The Dormouse's story</title>

# find_parents( name , attrs , recursive , text , **kwargs )
#
# find_parent( name , attrs , recursive , text , **kwargs )

# find_next_siblings( name , attrs , recursive , text , **kwargs )
#
# find_next_sibling( name , attrs , recursive , text , **kwargs )

# find_previous_siblings( name , attrs , recursive , text , **kwargs )
#
# find_previous_sibling( name , attrs , recursive , text , **kwargs )

# find_all_next( name , attrs , recursive , text , **kwargs )
#
# find_next( name , attrs , recursive , text , **kwargs )

# find_all_previous( name , attrs , recursive , text , **kwargs )
#
# find_previous( name , attrs , recursive , text , **kwargs )














