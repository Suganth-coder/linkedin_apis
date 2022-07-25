from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from .storedata import StoreData
import json
import requests as req


class Browser:
    """
        LinkedIn class consists of all the base functionalities of LinkedIn
    """
    def __init__(self,username,password):
        self.username,self.password = (username, password)
        self.sd = StoreData()
        self.linkedin_urls = ["https://www.linkedin.com/login","https://www.linkedin.com/feed/"]

    def login(self):
        """
            login() is used to login into the LinkedIn 
            1. Also,It gathers the cookies from the LinkedIn (if loggedin) 
                       
            @return STATUS_CODE
        """
        user_dict,temp = (dict(),dict())
        
        browser = web.Firefox()
        browser.get(self.linkedin_urls[0])
            
        email = browser.find_element(By.ID,"username")
        pass_word = browser.find_element(By.ID,"password")
            
        email.send_keys(self.username)
        pass_word.send_keys(self.password)
        browser.find_element_by_css_selector('[data-litms-control-urn="login-submit"]').click()
        
        res = browser.get_cookies()
        
        for cookie in res:
            temp[cookie['name']] = cookie['value']
        
        user_dict[self.username] = temp
        
        # user_dict[self.username] = json.dumps(res)
        self.sd.operate_file('test.txt','w',json.dumps(user_dict))
        

    def test(self):
        buff = self.sd.operate_file('test.txt','r')
        dic = json.loads(buff)
        print(dic['suganthwork@gmail.com'])
        
    def check_data_existance(self):
        pass
    