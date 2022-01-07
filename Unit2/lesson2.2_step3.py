from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

link = "http://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element_by_id("num1").text
    num2 = browser.find_element_by_id("num2").text
    btn_submit = browser.find_element_by_css_selector(".btn")
    
    sum = int(num1) + int(num2)
    
    print(sum)
    
    
    select = Select(browser.find_element_by_id("dropdown"))
    select.select_by_visible_text(str(sum))
    btn_submit.click()
    
finally:
    time.sleep(10)
    browser.quit()
    