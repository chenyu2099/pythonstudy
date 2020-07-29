from selenium import webdriver
import time
driver = webdriver.Firefox()
driver.get("https://www.yandy.com/Seductive-Crotchless-Teddy.php")
time.sleep(7)
driver.find_element_by_xpath("(//div[@class='product-price'])[1]").click()
