import json
import requests
from .storedata import StoreData
class LinkedIn:
    def __init__(self,username):
        
        self.username = username
        self.sd = StoreData()
        self.cookies_path = "basefiles/user_creds/cookies.json"
        self.buff = self.sd.operate_file(f_name=self.cookies_path,mode="r")
        self.dic = json.loads(self.buff)
        
        self.headers = {}
        self.headers["user-agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36"  
        self.pre_url= "https://www.linkedin.com/voyager/api/"
    
    def get_details(self,profileID,detail=None):
        """
            get_details() used to get the user's profile details
            @return (code,details|errors)
        """
        
        if detail == "profile":
            sub_url = f"identity/profiles/{profileID}/profileView"
        elif detail == "conn":
            sub_url = f"identity/profiles/{profileID}/networkinfo"
            
        res = self.make_request(self.pre_url+sub_url)
        return res

    def make_request(self,url):

        try:
            with requests.session() as s:
        
                for key,value in self.dic[self.username].items():
                    s.cookies[key]=value
                
                s.headers = self.headers
                s.headers["csrf-token"] = s.cookies["JSESSIONID"].strip('"')
                print(s.headers["csrf-token"])
                response = s.get(url)
                response_dict = response.json()
                
                if "status" in response_dict.keys():
                    if "status" != 200:
                        return (400,"Error in retriving from LinkedIn")
                    
                print(response_dict)
                
            return (200,response_dict)
        
        except Exception as e:
            return (400,"Error in retriving from LinkedIn")




