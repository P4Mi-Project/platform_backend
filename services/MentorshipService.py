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
            return db.collection("mentors").document(mentor_id).get().to_dict()
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get mentor by id. Please have a look at the log.")
    
    def update_mentor_by_id(mentor_id:str, new_mentor_data:serializer.Mentor)-> serializer.ServerResponse:
        try:
            res = db.collection("mentors").document(mentor_id).get()
            if res == None:
                raise HTTPException(status_code=404, detail=f"The mentor does not exist by that mentor id.")
            else:
                db.collection("mentors").document(mentor_id).set(new_mentor_data.model_dump(mode="json"), merge = True)
                
                return serializer.ServerResponse(status="200",message= f"The mentor data by mentor id {mentor_id} has been updated successfully.")
                
        except:
            import traceback;traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to update mentor by id. Please have a look at the log.")
        
    def delete_mentor_by_id(mentor_id:str)-> serializer.ServerResponse:
        try:
            db.collection("mentors").document(mentor_id).delete()
            return serializer.ServerResponse(status="200", message="Mentor data has been deleted successfully.")
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to delete mentor by id. Please have a look at the log.")