from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://www.baidu.com")

# 获得当前窗口句柄
nowHandle = driver.current_window_handle

# 通过js的方式打开新的新闻窗口
driver.execute_script("window.open('http://news.baidu.com')")
time.sleep(5)

print(driver.current_window_handle)

# 获取当前打开所有窗口
allHandles = driver.window_handles

# 通过循环方式判断窗口是否为当前窗口
for handle in allHandles:
    if nowHandle != handle:
        driver.switch_to_window(nowHandle)
        time.sleep(5)

        driver.close()
        time.sleep(5)


driver.quit()
