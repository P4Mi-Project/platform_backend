from pydantic import BaseModel,EmailStr
from datetime import date

class UserModelPrimary(BaseModel):
    id:int
    name:str
    email:EmailStr
    
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



class Course(BaseModel):
    title:str = "Default title"
    # url:str = ""
    # image_url:str = ""
    # author_id:str = ""
    # description:str = ""
    # short_description:str = ""
    # duration:int = 0
    # # created_at:date = None
    # # updated_at:date = None
    # thumbnail:str = ""
    # category:id = 0
    # level_id:int = 0
    # course_language:str = ""
    # tags:list[str] = []
    
class Category(BaseModel):
    name:str = "Default cata"