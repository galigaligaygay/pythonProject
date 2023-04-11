from selenium import webdriver
import time

#实例化浏览器
driver = webdriver.Chrome()

#打开浏览器
driver.get(url="https://www.baidu.com")
#浏览器窗口最大化
driver.maximize_window()
driver.refresh()
#打开新网页
driver.get(url="http://news.baidu.com/")
#强制等待3s，方便观察
time.sleep(3)
#浏览器后退
driver.back()
#强制等待3s，方便观察
time.sleep(3)
#浏览器前进
driver.forward()
#强制等待3s，方便观察
time.sleep(3)

#浏览器退出
driver.quit()
