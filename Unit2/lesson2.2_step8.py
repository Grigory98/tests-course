from selenium import webdriver
import time
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    fname = browser.find_element_by_name("firstname")
    lname = browser.find_element_by_name("lastname")
    email = browser.find_element_by_name("email")
    file = browser.find_element_by_id("file")
    btn_submit = browser.find_element_by_css_selector(".btn")
    
    #current_dir = os.path.abspath(os.path.dirname(__file__))
    #file_path = os.path.join(current_dir, 'test.txt')
    file_path = os.getcwd() + "\\" + "test.txt"
    
    fname.send_keys("MrTest")
    lname.send_keys("Let'sCheck")
    email.send_keys("test@test.com")
    file.send_keys(file_path)
    
    btn_submit.click()
    
finally:
    time.sleep(10)
    browser.quit()