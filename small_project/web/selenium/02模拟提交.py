from selenium import webdriver

from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get("http://www.python.org")

assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)  # 模拟点击回车
# print(driver.page_source)  # 获取网页渲染后的源代码

# 这样，我们就可以做到网页的动态爬取了









