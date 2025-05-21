from serializers import serializer
from configs.firebase_admin_config import db
from models.model import CourseModel
import traceback
from fastapi import Depends
from fastapi.exceptions import HTTPException

class MentorshipService:
    def __init__(self):
        pass
    
    def get_mentor_list()-> list[serializer.Mentor]:
        try:
            mentor_result_list:list[serializer.Mentor] = db.collection("mentors").get()
            mentor_list = list()
            for mentor_item in mentor_result_list:
                mentor_list.append(mentor_item.to_dict())
                
            return mentor_list
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get mentor list. Please have a look at the log.")
        
    def get_mentor_by_id(mentor_id:str) -> serializer.Mentor:
        try:
            return db.collection("mentors").document(mentor_id).get()
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get mentor by id. Please have a look at the log.")
            