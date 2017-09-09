# 格式化输出
# prettify() 方法将Beautiful Soup的文档树格式化后以Unicode编码输出,每个XML/HTML标签都独占一行
from apt.package import unicode
from bs4 import BeautifulSoup

markup = '<a href="http://example.com/">I linked to <i>example.com</i></a>'
soup = BeautifulSoup(markup)
soup.prettify()


print(soup.prettify())
# <html>
#  <head>
#  </head>
#  <body>
#   <a href="http://example.com/">
#    I linked to
#    <i>
#     example.com
#    </i>
#   </a>
#  </body>
# </html>

# BeautifulSoup 对象和它的tag节点都可以调用 prettify() 方法

print(soup.a.prettify())
# <a href="http://example.com/">
#  I linked to
#  <i>
#   example.com
#  </i>
# </a>

# 压缩输出
# 如果只想得到结果字符串,不重视格式,那么可以对一个 BeautifulSoup 对象或 Tag 对象
# 使用Python的 unicode() 或 str() 方法
print(str(soup))
# <html><body><a href="http://example.com/">I linked to <i>example.com</i></a></body></html>
print(unicode(soup.a))
# <a href="http://example.com/">I linked to <i>example.com</i></a>

# str() 方法返回UTF-8编码的字符串,可以指定 编码 的设置.
#
# 还可以调用 encode() 方法获得字节码或调用 decode() 方法获得Unicode

# 输出格式
# Beautiful Soup输出是会将HTML中的特殊字符转换成Unicode,比如“&lquot;”
soup_str = BeautifulSoup("&ldquo;Dammit!&rdquo; he said.")
unicode(soup_str)
# u'<html><head></head><body>\u201cDammit!\u201d he said.</body></html>'
# 如果将文档转换成字符串,Unicode编码会被编码成UTF-8.这样就无法正确显示HTML特殊字符了
str(soup_str)
# '<html><head></head><body>\xe2\x80\x9cDammit!\xe2\x80\x9d he said.</body></html>'


# get_text()
# 如果只想得到tag中包含的文本内容
# 这个方法获取到tag中包含的所有文版内容包括子孙tag中的内容,
# 并将结果作为Unicode字符串返回
str(soup)
# markup = '<a href="http://example.com/">\nI linked to <i>example.com</i>\n</a>'
# soup = BeautifulSoup(markup)
#
# soup.get_text()
# u'\nI linked to example.com\n'
# soup.i.get_text()
# u'example.com'

# 可以通过参数指定tag的文本内容的分隔符
print(soup.get_text("|"))
# u'\nI linked to |example.com|\n'


# 还可以去除获得文本内容的前后空白
soup.get_text("|", strip=True)
# u'I linked to|example.com'

# 或者使用 .stripped_strings 生成器,获得文本列表后手动处理列表
print([text for text in soup.stripped_strings])
# ['I linked to', 'example.com']



