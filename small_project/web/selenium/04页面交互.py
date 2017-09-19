from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

# 1.find_element_by_*
# 寻找网页元素的方法

# 例如下面有一个表单输入框
# <input type="text" name="passwd" id="passwd-id" />

element = driver.find_element_by_id("passwd-id")
element = driver.find_element_by_name("passwd")
element = driver.find_elements_by_tag_name("input")
element = driver.find_element_by_xpath("//input[@id='passwd-id']")


# 2.输入文本
# 获取了元素之后，下一步当然就是向文本输入内容了
element.send_keys("some text")

# 3.模拟按键
# 同样你还可以利用 Keys 这个类来模拟点击某个按键
element.send_keys(Keys.ARROW_DOWN)

# 4.清楚输入的文本
element.clear()
















