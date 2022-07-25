import pickle
import os
class StoreData:
    """
        Store Python objects directly into the file
    """
    def operate_file(self,f_name,mode,content=None):
        """
            operate_file() used to operate the file with given mode
            1. if mode = read (r), return the buff
            2. else other do the respective operations
            
            @return None|handle
        """

        with open(f_name, mode) as handle:
            if mode == "r":
                buff = handle.read()
                return buff
            elif mode == "w" or mode == "a":
                if content == None: raise ValueError("Content value is not passed!")
                else:
                    handle.write(content)
            else:
                raise ValueError("Invalid mode is passed")
            
    def save_object(self,obj, filename):
        
        with open('basefiles/user_creds/'+filename, 'wb') as outp:
            pickle.dump(obj, outp, pickle.HIGHEST_PROTOCOL)

