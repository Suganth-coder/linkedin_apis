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
                # print("writing")
                return 200
            else:
                try:
                    dic = json.loads(buff)
                    keys = dic.keys()
                    
                    if self.username in keys:
                        return 401
                    else:
                        dic[self.username] = token
                        # print("Changing")
                        return 200
                except Exception as e:
                    return 402
                
        except Exception as e:
            print(e)
            return 400
        