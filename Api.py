import sys
from fastapi import FastAPI

sys.path.insert(0,'./lib/')

from basefiles import LinkedIn
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
    ln = LinkedIn(username=cred.username, password=cred.password)
    res = ln.get_connection()
    
    if (res == 200):
        response["status"] = "success"
        response["loggedIn"]="yes"
    elif res == 401:
        response["Error"] = "Invalid Credentials"
    elif res == 402:
        response["Error"] = "Invalid Password"
    else:
        response["Error"] = "Internal Server Error"
    
    return response
