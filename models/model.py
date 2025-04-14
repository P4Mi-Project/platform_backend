from pydantic import BaseModel

class UserModelPrimary(BaseModel):
    id:int
    name:str
    email:str
    
class UserModelConfidential(UserModelPrimary):
    password:str
    

class UserAddress(BaseModel):
    street:str
    city:str
    zip_code:str
    country:str
    
class ServerResponse(BaseModel):
    status:str    
    message:str
    extra:dict = {}
