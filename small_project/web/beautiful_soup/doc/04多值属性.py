# 最常见的多值的属性是 class (一个tag可以有多个CSS的class).
# 还有一些属性 rel , rev , accept-charset , headers , accesskey
# 在Beautiful Soup中多值属性的返回类型是list:

from bs4 import BeautifulSoup

css_soup = BeautifulSoup('<p class="body strikeout"></p>')

print(css_soup.p['class'])  # ['body', 'strikeout']

css_soup = BeautifulSoup('<p class="body"></p>')

print(css_soup.p['class'])  # ['body']

# 如果某个属性看起来好像有多个值,
# 但在任何版本的HTML定义中都没有被定义为多值属性,
# 那么Beautiful Soup会将这个属性作为字符串返回

id_soup = BeautifulSoup('<p id="my id"></p>')

print(id_soup.p['id'])  # my id

# 将tag转换成字符串时,多值属性会合并为一个值
rel_soup = BeautifulSoup('<p>Back to the <a rel="index">homepage</a></p>')
print(rel_soup.a['rel'])  # ['index']

rel_soup.a['rel'] = ['index', 'contents']
print(rel_soup.p)  # <p>Back to the <a rel="index contents">homepage</a></p>

# 如果转换的文档是XML格式,那么tag中不包含多值属性
xml_soup = BeautifulSoup('<p class="body strikeout"></p>', 'xml')
print(xml_soup.p['class'])  # body strikeout










