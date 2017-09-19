# 访问百度,模拟自动输入搜索

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

import time

driver = webdriver.Chrome()

driver.get("http://www.baidu.com")

# 输入框输入内容
driver.find_element_by_id('kw').send_keys("python")

time.sleep(3)

# 删除操作 模拟键盘的Backspace
# driver.find_element_by_id('kw').send_keys(Keys.BACK_SPACE)
# time.sleep(3)

# 输入空格 + '教程'
driver.find_element_by_id('kw').send_keys(Keys.SPACE)
driver.find_element_by_id('kw').send_keys(u"教程")
time.sleep(3)

# 模拟ctrl+a 操作 全选输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
time.sleep(3)

# 模拟Ctrl+X 操作 剪切输入框内容
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')
time.sleep(3)

# 模拟Ctrl+V 操作  将剪切内容填入输入框
driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
time.sleep(3)

# 模拟回车操作 ,开始搜索
driver.find_element_by_id('su').send_keys(Keys.ENTER)
time.sleep(3)

driver.quit()

