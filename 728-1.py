#coding=utf-8
from time import sleep
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path = "C:\Program Files\Mozilla Firefox\geckodriver")

# first_url="http://www.test.com:8011/index.php"
# print("first")
# driver.get(first_url)
# seconed="http://www.test.com:8011/html/channel/tucool/"
# print("second")
# driver.get(seconed)

# sleep(5)
# print("back")
# driver.back()
# sleep(4)
# print("forward")
# driver.forward()
# sleep(4)
# print("refresh")
# driver.refresh()
driver.get("http://www.test.com:8011/index.php")
"""

time.sleep(4)
register = driver.find_element_by_xpath("//button[@type='button']").click()
time.sleep(4)
tongyi = driver.find_element_by_xpath("//button[contains(.,'同 意')]").click()
regname = str(input("请输入用户名"))
name = driver.find_element_by_xpath("//input[@id='regname']").send_keys(regname)
time.sleep(4)
print("clear")
driver.find_element_by_xpath("//input[@id='regname']").clear()
"""

time.sleep(4)
register = driver.find_element_by_xpath("//button[@type='button']").click()
time.sleep(4)
tongyi = driver.find_element_by_xpath("//button[contains(.,'同 意')]").click()
time.sleep(4)
#driver.find_element_by_css_selector("input[type=checkbox]").click()
#text=driver.find_element_by_css_selector("input[type=checkbox]")

#text=driver.find_element_by_class_name("rgpermit").is_displayed()
ab=driver.find_element_by_xpath("//dd[@class='mr10']//label[1]").get_attribute('textContent')#获取文本的规则？
#x=ab.encode('utf-8','ignore')
#x=ab.replace(u’\xa0’, u’ ')
x=ab.replace('\xa0' ,"")#出现问题的原因是:本身Unicode类型的字符中，包含了一些无法转换为GBK编码的一些字符。比如说u’\xa0’

#网上的解决方法有很多， 怎么舒服怎么来，选用最简单的方法就是去除u’\xa0’，

#text.replace(u’\xa0’, u’ ')
print(x)
#driver.quit()
driver.find_element_by_xpath("//a[@class='b s4']").click()