from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import pickle
import json

def func(user,passw):
    
    # display = Display(visible=0, size=(800, 600))
    # display.start()
    
    browser = web.Firefox()
    browser.get("https://www.linkedin.com/login")
    
    # Found the user id
    email = browser.find_element(By.ID,"username")
    pass_word = browser.find_element(By.ID,"password")
    
    # Interact it
    email.send_keys(user)
    pass_word.send_keys(passw)
    browser.find_element_by_css_selector('[data-litms-control-urn="login-submit"]').click()
    
    # print(browser.manage().getCookies())
    res = json.dumps(browser.get_cookies())
    # browser.close()
    print(res)
    return res
