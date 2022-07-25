from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
from .storedata import StoreData
import json
import requests as req
from .auth import Auth


class Browser:
    """
        LinkedIn class consists of all the base functionalities of LinkedIn
    """
    def __init__(self,username,password):
        
        self.auth = Auth()
        self.username,self.password = (username, password)
        self.sd = StoreData()
        self.linkedin_urls = ["https://www.linkedin.com/login","https://www.linkedin.com/feed/"]
        self.cookie_path = "basefiles/user_creds/cookies.json"

    def login(self):
        """
            login() is used to login into the LinkedIn 
            1. Also,It gathers the cookies from the LinkedIn (if loggedin) 
                       
            @return DICT
        """
        user_dict,temp,ret_dict = (dict(),dict(),dict())
        
        try:
            
            display = Display(visible=0, size=(800, 600))
            display.start()
    
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
            print("Before dict")
            # user_dict[self.username] = json.dumps(res)
            self.sd.operate_file(self.cookie_path,'w',json.dumps(user_dict))
            
            if res == 400: 
                ret_dict['Error'] = "Error in token generation"
            else:
                ret_dict['status']="LoggedIn"
                ret_dict['authenticated']= "Yes"
                ret_dict['code']=200
            
        except Exception as e:
                ret_dict['status']="Not LoggedIn"
                ret_dict['authenticated']= "No"
                ret_dict['code']=400
            
            
        return ret_dict
        

    def test(self):
        buff = self.sd.operate_file(self.cookie_path,'r')
        dic = json.loads(buff)
        print(dic['suganthwork@gmail.com'])
        
        
    def check_data_existance(self):
        pass
    