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

# this class is being used to serve language data.
class LanguageResponseModel(Language):
    id:str = ""

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
    name:str = ""
    


class Questioner(BaseModel):
    full_name:str
    email_address:EmailStr
    phone_number:str
    method_of_contact:MethodOfContact
    best_time_to_contact:TimeToContact
    first_language:Language
    second_language:Language
    third_language:Language
    interested_topics:Category
    have_education_or_work_exp:bool
    additional_to_education_or_work_exp:str


class Mentor(BaseModel):
    full_name:str = ""
    description:str = ""
    spoken_language:list[Language] = []
    country:str = ""
    post_code:str = ""
    city:str = ""
    street_address:str = ""
    profile_image_url:str = ""
    
class MentorMessage(BaseModel):
    name:str = ""
    receiver_id:str # usually it has to be the id of mentor; later on we will fetch the email from the record and then send the notification via email
    surname:str = ""
    email:EmailStr = ""
    message:str = ""


# {
#     name: "English",
#     level : ["basic", "inermediate"....]
# }