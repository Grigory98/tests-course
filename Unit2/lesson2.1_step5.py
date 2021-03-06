from selenium import webdriver
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    input_value = browser.find_element_by_id("input_value")
    answer = browser.find_element_by_id("answer")
    checkbox = browser.find_element_by_id("robotCheckbox")
    radio = browser.find_element_by_id("robotsRule")
    btn_submit = browser.find_element_by_css_selector(".btn")
    
    result = calc(input_value.text)
    answer.send_keys(result)
    checkbox.click()
    radio.click()
    btn_submit.click()
    
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()