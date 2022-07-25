import hashlib as hash
from .storedata import StoreData
import json

class Auth:
    
    def __init__(self):
        self.salt = "$@!(^*"
        self.sd = StoreData()
        self.username,self.password = (None,None)
        self.token_path = "basefiles/user_creds/token.json"
        
    def gentoken(self,username,password):
        
        try:
            self.username,self.password = (username,password)
            word = username+self.salt+password+self.salt
            token = hash.sha1((hash.md5(word.encode()).hexdigest()).encode()).hexdigest()
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
        
    def checktoken(self,username):
        
        buff = self.sd.operate_file(self.token_path,'r')
        dic = json.loads(buff)
        keys = dic.keys()
                    
        if username in keys: return True
        else: return False
        
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

        