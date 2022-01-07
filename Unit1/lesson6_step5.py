from selenium import webdriver
import time
import math

code_link = str(math.ceil(math.pow(math.pi, math.e)*10000))

url = "http://suninjuly.github.io/find_link_text"

try:
    driver = webdriver.Chrome()
    driver.get(url)
    
    link = driver.find_element_by_link_text(code_link)
    link.click()
    
    input1 = driver.find_element_by_name("first_name")
    input2 = driver.find_element_by_name("last_name")
    input3 = driver.find_element_by_class_name("city")
    input4 = driver.find_element_by_id("country")
    btn_submit = driver.find_element_by_class_name("btn")
    
    input1.send_keys("Ivan")
    input2.send_keys("Pretov")
    input3.send_keys("Smolensk")
    input4.send_keys("Russia")
    
    btn_submit.click()
    
finally:
    time.sleep(30)
    driver.quit()