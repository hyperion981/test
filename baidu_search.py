#coding=utf-8

from selenium import webdriver

import time

driver = webdriver.Chrome(executable_path=r"D:\chromedriver.exe")
driver.get("http://www.baidu.com")

search_box = driver.find_element_by_id("kw")
search_box.send_keys("sssv")

search_click = driver.find_element_by_id("su")
search_click.click()
#driver.qiut()