import sys

from sympy import Li
from basefiles import Browser, LinkedIn
from fastapi import FastAPI

sys.path.insert(0,'./lib/')

from typing import List, Optional
from basefiles import Browser,Auth
from pydantic import BaseModel

class LogIn(BaseModel):
    code: int
    status: str
    token: str
    authenticated: str
    
class Cred(BaseModel):
    username: str
    password: str
    
class Resp(BaseModel):
    code: int
    response: dict

class Profile(BaseModel):
    username: str
    public_id: str
    
class Error(BaseModel):
    code: int 
    error: str
    
app = FastAPI()
auth = Auth()

@app.get("/")
def main_func():
    return {"hello":"testing"}

@app.post("/login")
async def linkedin_creds(cred: Cred):
    
    response = {"status":"failure","loggedIn":"No"}
    br = Browser(username=cred.username, password=cred.password)
    res = br.login()
    
    print(f"res: {res}")
    if "code" not in res.keys():
        print("Res is none")
    
    else:    
        return LogIn(code=res['code'],status=res['status'],token=res['token'],authenticated=res['authenticated'])

@app.post("/profile")
def user_profile(profile: Profile):
    
    if auth.checktoken(profile.username) == False :
        return Error(code=400,error="Not Logged in")
    
    ln = LinkedIn(profile.username)
    res = ln.get_details(profile.public_id,detail="profile")
    
    if res[0] == 200:
        return Resp(code=res[0],response=res[1])
    else:
        return Error(code=res[0],error=res[1])
    
@app.post("/connections")
def user_profile(profile: Profile):
    
    if auth.checktoken(profile.username) == False :
        return Error(code=400,error="Not Logged in")
        
    ln = LinkedIn(profile.username)
    res = ln.get_details(profile.public_id,detail="conn")
    
    if res[0] == 200:
        return Resp(code=res[0],response=res[1])
    else:
        return Error(code=res[0],error=res[1])