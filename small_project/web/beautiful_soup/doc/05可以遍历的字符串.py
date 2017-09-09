# 字符串常被包含在tag内.
# Beautiful Soup用 NavigableString 类来包装tag中的字符串
from bs4 import BeautifulSoup
from setuptools.compat import unicode

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>')
tag = soup.b

print(tag.string)  # Extremely bold

print(type(tag.string))  # <class 'bs4.element.NavigableString'>

# 一个 NavigableString 字符串与Python中的Unicode字符串相同
# 并且还支持包含在 遍历文档树 和 搜索文档树 中的一些特性.
# 通过 unicode() 方法可以直接将 NavigableString 对象转换成Unicode字符串
unicode_string = unicode(tag.string)

print(unicode_string)  # Extremely bold

print(type(unicode_string))  # <class 'str'>

# tag中包含的字符串不能编辑,但是可以被替换成其它的字符串,用 replace_with() 方法
tag.string.replace_with('No longer bold')
print(tag)  # <b class="boldest">No longer bold</b>

















