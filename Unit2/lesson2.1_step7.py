from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    browser = webdriver.Chrome()
    browser.get(link)
    
    treasure = browser.find_element_by_id("treasure").get_attribute("valuex")
    answer = browser.find_element_by_id("answer")
    checkbox = browser.find_element_by_id("robotCheckbox")
    radio = browser.find_element_by_id("robotsRule")
    btn_submit = browser.find_element_by_css_selector(".btn")
    
    result = calc(treasure)
    answer.send_keys(result)
    checkbox.click()
    radio.click()
    btn_submit.click()
    
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()