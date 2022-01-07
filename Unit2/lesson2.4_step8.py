from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    btn_book = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    
    btn = browser.find_element_by_id("book")
    btn.click()
    
    input_value = browser.find_element_by_id("input_value").text
    answer = browser.find_element_by_id("answer")
    solve = browser.find_element_by_id("solve")
    
    result = calc(input_value)
    answer.send_keys(result)
    solve.click()
    
finally:
    time.sleep(10)
    browser.quit()