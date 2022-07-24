from linkedin_api import Linkedin
from storedata import StoreData
class LinkedIn:
    """
        LinkedIn class consists of all the base functionalities of LinkedIn
    """
    def __init__(self,username,password):
        self.username,self.password = (username, password)
        self.sd = StoreData()

    def get_connection(self):
        try:
            self.api = Linkedin(self.username,self.password)
            self.sd.save_object(self.api,'samp.txt')
            return 200
        
        except Exception as e:
            e = str(e)
            print(e)
            if e == "BAD_EMAIL":
                return 401            
            elif e == "BAD_PASSWORD":
                return 402

                    

        
    