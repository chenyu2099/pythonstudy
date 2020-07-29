#coding=utf-8

import time#引入time
import keyword
#from pyvirtualdisplay import Display#虚拟屏幕
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #引入key 发送数据
from functools import reduce
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains 



#correct

driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

driver.get("http://www.test.com:8011/index.php")

time.sleep(4)
register = driver.find_element_by_xpath("//button[@type='button']").click()
time.sleep(4)
tongyi = driver.find_element_by_xpath("//button[contains(.,'同 意')]").click()
regname = str(input("请输入用户名"))
#name = driver.find_element_by_xpath("//input[@id='regname']").click()
#time.sleep(2)
#定位classs 并用 get_attribute('textContent')获取文本
#get_attribute('textContent')为获取元素文本 可以根据设置获取不同

#regname_info = driver.find_element_by_class_name("ignore").get_attribute('textContent')#用户名信息 用来判断是否用户名是否合法 具体用法需要网上
#print(regname_info)#打印确认
#regname_info = driver.find_element_by_id("regname_info").value_of_css_property("class")
#print(regname_info)

name = driver.find_element_by_xpath("//input[@id='regname']").send_keys(regname)
driver.find_element_by_xpath("//input[@id='regpwd']").click()
AB = driver.find_element_by_id('regname_info').get_attribute('class')
print(AB)

#driver.find_element_by_xpath("//input[@id='regpwd']").click()

# regpwd = str(input("请输入密码"))
# regpwdrepeat = regpwd
# pwd = driver.find_element_by_xpath("//input[@id='regpwd']").send_keys(regpwd)
# regpwdrepeat = driver.find_element_by_xpath("//input[@id='regpwdrepeat']").send_keys(regpwdrepeat)
# time.sleep(3)
# regemail= str(input("请输入邮箱"))
# remail = driver.find_element_by_xpath("//input[@id='regemail']").send_keys(regemail)
#driver.
#bg_config = driver.find_element_by_id("province_apartment")
#ActionChains(driver).move_to_element(bg_config).perform()
#time.sleep(3)
#se=driver.find_element_by_id("province_apartment")
#Select(se).select_by_value("130000")
#select(driver.find_element_by_id("province_apartment")).select_by_value("13000")
#se = driver.find_element_by_id("province_apartment")
#select(se).select_by_value("130000")
#Select(se).select_by_value("130000")
# sePa = driver.find_element_by_id("province_apartment")
# options_list = sePa.find_elements_by_tag_name('option')
# options = []
# for option in options_list :
#      options.append(option.text)
# list=[i[0]for i in options]
# print(list)
#
#



#Select(sePa).select_by_value("130000")
#seCa = driver.find_element_by_id("province_apartment")
#Select(seCa).select_by_value("131000")
#seCa = driver.find_element_by_id("province_apartment")
#Select(seCa).select_by_value("131003")

#time.sleep(3)
#driver.find_element_by_xpath("//button[contains(.,'提交注册')]").click()
#time.sleep(3)
#driver.find_element_by_xpath("//button[contains(.,'跳过')]").click()
#driver.quit()


# waitClickCompanyName = driver.find_elements_by_xpath('//div[@id="nsrzt"]//li')
#
# for i in waitClickCompanyName:
#
# 　　#找出标签中的文本内容
#
# 　　name = i.get_attribute('textContent')
#
# 　　#打印出获取到的文本
#
# 　　print(name)