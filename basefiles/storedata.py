import pickle
import os
class StoreData:
    """
        StoreData is used to user datas
    """
    def save_object(self,obj, filename):
        
        with open('basefiles/user_creds/'+filename, 'wb') as outp:
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

