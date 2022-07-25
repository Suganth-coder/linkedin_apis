import hashlib as hash
from .storedata import StoreData
import json

class Auth:
    
    def __init__(self):
        self.salt = "$@!(^*"
        self.sd = StoreData()
        self.username,self.password = (None,None)
        self.token_path = "basefiles/user_creds/token.json"
        self.signup_path = "basefiles/user_creds/signup.json"
        
        
    def hashdata(self,data):
        return hash.sha1((hash.md5(data.encode()).hexdigest()).encode()).hexdigest()
    
    def gentoken(self,username,password):
        
        try:
            self.username,self.password = (username,password)
            word = username+self.salt+password+self.salt
            token = self.hashdata(word)
            self.savetoken(token)
            return 200
        
        except Exception as e:
            return 400

    def savetoken(self,token):
        
        token_dict = {self.username:token}
        try:
            buff = self.sd.operate_file(self.token_path,'r')
            if (len(buff) == 0):
                self.sd.operate_file(self.token_path,'w',json.dumps(token_dict))
                return 200
            else:
                try:
                    if self.checktoken(token):
                        return 401
                    else:
                        dic = json.loads(buff)
                        dic[self.username] = token
                        self.sd.operate_file(self.token_path,'w',json.dumps(dic))
                        return 200
                except Exception as e:
                    return 402
                
        except Exception as e:
            # print(e)
            return 400
      
    def checkaccess(self,username,path):
        
        buff = self.sd.operate_file(path,'r')
        dic = json.loads(buff)
        keys = dic.keys()
                    
        if username in keys: return True
        else: return False 
         
    def checktoken(self,username):
        return self.checkaccess(username,self.token_path)
        
        
    def gettoken(self,username):
        
        if self.checktoken(username):
            buff = self.sd.operate_file(self.token_path,'r')
            dic = json.loads(buff)
            
            return dic[username]
        else:
            return 400
        
    def validate_token(self,token,username):
        if self.checktoken(username):
            v_token = self.gettoken(username)
            if v_token == token:
                return 200
            else: return 400
        else:
            return 401

    def check_signup(self,username):
        return self.checkaccess(username,self.signup_path)
    
    def signup(self,username,password,retype_pass):
        
        if self.check_signup(username) == True: 
            return (400,"Already Signed Up")
        else:
            if password == retype_pass:
                buff = self.sd.operate_file(self.signup_path,'r')
                dic = json.loads(buff)
                dic[username] = self.hashdata(password)
                self.sd.operate_file(self.signup_path,'w',json.dumps(dic))
                return (200,"Successfully Signed up")
            else: return (400,"Passwords Doesn't Match")
    
    def login(self,username,password):
        
        buff = self.sd.operate_file(self.signup_path,'r')
        dic = json.loads(buff)
                
        if self.check_signup(username) == True: 
            if self.hashdata(password) == dic[username]:
                self.gentoken(username,password)
                return (200,"Logged In",self.gettoken(username))
            else:
                return (400,"Invalid Password","Not Generated")
        else:
            return (400,"Not Signed Up","Not Generated")
        
    def logout(self,username):
        
        buff = self.sd.operate_file(self.signup_path,'r')
        dic = json.loads(buff)
        
        if self.checktoken(username):
            del dic[username]
            self.sd.operate_file(self.token_path,'w',json.dumps(dic))
            return (200,"Logged out")
        else:
            return (400,"Not LoggedIn or Invalid username")
                    
        