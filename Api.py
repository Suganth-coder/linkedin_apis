import sys
from fastapi import FastAPI
sys.path.insert(0,'./lib/')

app = FastAPI()

@app.get("/")
def base():
    return {"testing":"success"}