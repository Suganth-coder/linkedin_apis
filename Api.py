import sys
from basefiles.browser import Browser
import sel
from fastapi import FastAPI

sys.path.insert(0,'./lib/')

from basefiles import Browser
from pydantic import BaseModel

class Cred(BaseModel):
    username: str
    password: str

app = FastAPI()

@app.get("/")
def main_func():
    return {"hello":"testing"}

@app.post("/credentials/")
async def linkedin_creds(cred: Cred):
    
    response = {"status":"failure","loggedIn":"No"}
    br = Browser(username=cred.username, password=cred.password)
    res = br.login()
    

@app.post("/local")
def local(cred: Cred):
    return sel.func(cred.username, cred.password)