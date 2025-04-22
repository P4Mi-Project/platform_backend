from pydantic import BaseModel,EmailStr
from datetime import date
import datetime

# class UserModelPrimary(BaseModel):
#     id:int
#     name:str
#     email:EmailStr
    
# class UserModelConfidential(UserModelPrimary):
#     password:str
    

class Category(BaseModel):
    name:str

'''
email
phone
text_message
'''
class MethodOfContact(BaseModel):
    name:str = "Email"

'''
Morning
Evening
Afternoon
'''
class TimeToContact(BaseModel):
    name:str = "Morning"
    
'''
1 == Begineer
2 == Intermediate
3 == Fluent
'''
class Language(BaseModel):
    name:str = "English"
    level:int = 1

class AnonymousUserModel(BaseModel):
    email:EmailStr
    name:str
    surname:str
    interested_category: list[Category] = []
    phone_number:str = ""
    has_work_skills:bool = False
    education_work_skills:str = ""
    preferred_method_of_contact:list[MethodOfContact] = []
    best_time_to_contact:list[TimeToContact] = []

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
    title:str
    url:str = ""
    image_url:str = ""
    author_id:str
    description:str = ""
    short_description:str = ""
    duration:int = 0
    created_at:date = datetime.datetime.now().strftime('%Y-%m-%d')
    updated_at:date = datetime.datetime.now().strftime('%Y-%m-%d')
    thumbnail:str = ""
    category:list[dict] = []
    level_id:int = 0
    course_language:str = ""
    lang_level_requirement:Language = None
    # tags:list[str] = []
    
class Category(BaseModel):
    name:str = "Default cata"
    



# {
#     name: "English",
#     level : ["basic", "inermediate"....]
# }