import time
from selenium.webdriver.common.by import By

def test_find_basket_button(browser):
    
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    
    browser.get(link)
    time.sleep(6)
    try:
        basket_button = browser.find_element(By.CSS_SELECTOR, "#add_to_basket_form .btn")
        basket_button = True
    except:
        basket_button = False
    assert basket_button == True, "No button!"



