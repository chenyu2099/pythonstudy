"""import sys
from os.path import dirname, abspath

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path+ "\\module")
print(project_path)
"""
#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 
import time
import keyword
driver= webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")
driver.get("https://passport.isoftstone.com/")
driver.find_element_by_xpath('//input[@id="emp_DomainName"]').send_keys("yuchens")
driver.find_element_by_xpath('//input[@id="emp_Password"]').send_keys("303101Cy7")
#driver.find_element_by_xpath('//buttn[@]').click()
#time.sleep(8)
driver.find_element_by_xpath('//input[@id="BtnLogin"]').click()
#driver.find_element_by_tag_name("")
time.sleep(3)
driver.find_element_by_link_text("http://timesheet.isoftstone.com/NewTS").click()
# regname=str(input("请输入用户名"))
# time.sleep(3)
# driver.find_element_by_xpath('//*[@id="regname"]').send_keys(regname)
# #name = driver.find_element_by_xpath("//input[@id='regname']").send_keys(regname)

