from selenium import webdriver
from bs4 import BeautifulSoup
import os

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
browser = webdriver.Chrome(chromedriver)

#设置浏览器打开url
url = "http://www.baidu.com"
browser.get(url)
#在百度搜索框输入关键字"python"
browser.find_element_by_id("kw").send_keys("python")
#单机搜索按钮
browser.find_element_by_id("su").click()
html = browser.page_source

browser.quit()



