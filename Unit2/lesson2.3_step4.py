from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    btn = browser.find_element_by_css_selector(".btn-primary")
    btn.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    input_value = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    btn_submit = browser.find_element_by_css_selector("button[type='Submit']")
    
    result = calc(input_value)
    answer.send_keys(result)
    btn_submit.click()
    
finally:
    time.sleep(10)
    browser.quit()