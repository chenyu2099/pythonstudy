from selenium import webdriver
import time



driver = webdriver.Firefox()
driver.find_element_by_xpath("(//div[@class='product-price'])[1]").click()