from pydantic import BaseModel

class SignUpData(BaseModel):
    username: str
    password: str
    retype_password: str
    
class LogInData(BaseModel):
    username: str
    password: str
    
class SignUp(BaseModel):
    code: int
    status: str
    
class LogIn(BaseModel):
    code: int
    status: str
    token: str
    
class LogInLinkedIn(BaseModel):
    code: int
    status: str
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
    auth_token: str
    
class Error(BaseModel):
    code: int 
    error: str
    