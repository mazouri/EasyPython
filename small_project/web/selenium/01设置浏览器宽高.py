# 发起请求,设置浏览器宽高

# 需要安装Selenium
# pip install selenium 或Pycharm插件安装

# 需要安装chrome驱动才能打开浏览器：
# 驱动下载地址：https://sites.google.com/a/chromium.org/chromedriver/downloads
# 放在 /usr/bin 目录下

# 代码中引入selenium版本为:3.4.3
# 通过Chrom浏览器访问发起请求
# Chrom版本:59 ,chromdriver:2.3

from selenium import webdriver

driver = webdriver.Chrome()

# 打开百度网页
driver.get('http://www.baidu.com')

# 设置浏览器全屏
# driver.maximize_window()

print("set browser width is 800 and height is 800")

driver.set_window_size(800, 800)

# exit the browser
driver.quit()
