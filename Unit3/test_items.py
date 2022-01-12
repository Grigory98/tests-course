import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_web_site(browser):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-add-to-basket")))
    assert button, "Кнопка отсутствует"