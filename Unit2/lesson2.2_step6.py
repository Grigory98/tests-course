from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    checkbox = browser.find_element_by_id("robotCheckbox")
    radio = browser.find_element_by_id("robotsRule")
    btn_submit = browser.find_element_by_css_selector(".btn")
    
    result = calc(x)
    
    browser.execute_script("window.scrollBy(0, 100);")
    answer.send_keys(result)
    checkbox.click()
    radio.click()
    
    time.sleep(1)
    
    btn_submit.click()
    
finally:
    time.sleep(10)
    browser.quit()