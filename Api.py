import sys

from sympy import Li
from basefiles import Browser, LinkedIn
from fastapi import FastAPI

sys.path.insert(0,'./lib/')

from typing import List, Optional
from basefiles import Browser,Auth
from basefiles.ApiClass import *



app = FastAPI()
auth = Auth()

@app.get("/")
def main_func():
    return Error

@app.post("/signup")
async def signup(sd: SignUpData):
    res = auth.signup(username=sd.username,password=sd.password,retype_pass=sd.retype_password)
    return SignUp(code=res[0],status=res[1])

@app.post("/login")
async def login(ld: LogInData):
    res = auth.login(username=ld.username,password=ld.password)
    return LogIn(code=res[0],status=res[1],token=res[2])
    
@app.post("/login/linkedin")
async def linkedin_creds(cred: Cred):
    
    check = auth.validate_token(token = cred.auth_token,username = cred.api_username)
    
    if check == 401:
            return Error(code=400,error="Not Logged in")
    if check == 400:
        return Error(code=400,error="Invalid Auth Token")
    elif check == 200:
    
        br = Browser(username=cred.linkedin_username, password=cred.linkedin_password)
        res = br.login()
        
        print(f"res: {res}")
        if "code" not in res.keys():
            print("Res is none")
        
        else:    
            return LogInLinkedIn(code=res['code'],status=res['status'],authenticated=res['authenticated'])

@app.post("/profile")
def user_profile(profile: Profile):
    
    check = auth.validate_token(token = profile.auth_token,username = profile.api_username)
    
    if check == 401:
        return Error(code=400,error="Not Logged in")
    if check == 400:
        return Error(code=400,error="Invalid Auth Token")
    elif check == 200:
 
        ln = LinkedIn(profile.linkedin_username)
        res = ln.get_details(profile.public_id,detail="profile")
        
        if res[0] == 200:
            return Resp(code=res[0],response=res[1])
        else:
            return Error(code=res[0],error=res[1])
    
@app.post("/connections")
def user_profile(profile: Profile):
    
    check = auth.validate_token(token = profile.auth_token,username = profile.api_username)
    
    if check == 401:
        return Error(code=400,error="Not Logged in")
    if check == 400:
        return Error(code=400,error="Invalid Auth Token")
    elif check == 200:
     
        ln = LinkedIn(profile.linkedin_username)
        res = ln.get_details(profile.public_id,detail="conn")
        
        if res[0] == 200:
            return Resp(code=res[0],response=res[1])
        else:
            return Error(code=res[0],error=res[1])
        
@app.post("/logout")
def logout(lg: LogoutData):
    res = auth.logout(lg.api_username)
    return Logout(code=res[0],status=res[1])