# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 19:31:17 2020

@author: USER
"""


from selenium import webdriver

url = "https://www.thsrc.com.tw/index.html"
ss = '新竹站'
es = '台北站'
dd = '2020/07/10'
dt = '09:00'

driver = webdriver.Chrome() # Use Chrome
driver.get(url)

driver.find_element_by_css_selector('#StartStation').send_keys(ss)

driver.find_element_by_css_selector('#EndStation').send_keys(es)

driver.find_element_by_css_selector('#DepartueSearchDate').click()
driver.find_element_by_css_selector('#DepartueSearchDate').clear()
driver.find_element_by_css_selector('#DepartueSearchDate').send_keys(dd)

driver.find_element_by_css_selector('#DepartueSearchTime').click()
driver.find_element_by_css_selector('#DepartueSearchTime').send_keys(dt)

driver.find_element_by_css_selector('#btnQuickSearchSubmit').click()


