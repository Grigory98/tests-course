from selenium import webdriver
import time

link = "http://suninjuly.github.io/find_xpath_form"


try:
    driver = webdriver.Chrome()
    driver.get(link)
    
    input1 = driver.find_element_by_name("first_name")
    input2 = driver.find_element_by_name("last_name")
    input3 = driver.find_element_by_class_name("city")
    input4 = driver.find_element_by_id("country")
    button = driver.find_element_by_xpath("//button[text()='Submit']")
    
    input1.send_keys("Ivan")
    input2.send_keys("Pretov")
    input3.send_keys("Smolensk")
    input4.send_keys("Russia")
    
    
    button.click()
    
finally:
    time.sleep(30)
    driver.quit()