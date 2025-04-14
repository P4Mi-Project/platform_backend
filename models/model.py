from pydantic import BaseModel

class UserModelPrimary(BaseModel):
    id:int
    name:str
    email:str
    
class UserModelConfidential(UserModelPrimary):
    password:str
    
