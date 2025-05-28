from serializers import serializer
from configs.firebase_admin_config import db
from fastapi import Depends
from fastapi.exceptions import HTTPException

# Todo : need to test this service
class MentorshipService:
    def __init__(self):
        pass
    
    def get_mentor_list(self)-> list[serializer.Mentor]:
        try:
            mentor_result_list:list[serializer.Mentor] = db.collection("mentors").get()
            mentor_list = list()
            for mentor_item in mentor_result_list:
                mentor_list.append(mentor_item.to_dict())
                
            return mentor_list
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get mentor list. Please have a look at the log.")
        
    def get_mentor_by_id(self,mentor_id:str) -> serializer.Mentor:
        try:
            return db.collection("mentors").document(mentor_id).get().to_dict()
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get mentor by id. Please have a look at the log.")
    
    def update_mentor_by_id(self,mentor_id:str, new_mentor_data:serializer.Mentor)-> serializer.ServerResponse:
        try:
            res = db.collection("mentors").document(mentor_id).get()
            if res == None:
                raise HTTPException(status_code=404, detail=f"The mentor does not exist by that mentor id.")
            else:
                db.collection("mentors").document(mentor_id).set(new_mentor_data.model_dump(mode="json"), merge = True) # A bug is facing .that is ; if the mentor doc does not exists it's creating the doc becuase of merge = True attribute. Todo
                
                return serializer.ServerResponse(status="200",message= f"The mentor data by mentor id {mentor_id} has been updated successfully.")
                
        except:
            import traceback;traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to update mentor by id. Please have a look at the log.")
        
    def delete_mentor_by_id(self,mentor_id:str)-> serializer.ServerResponse:
        try:
            db.collection("mentors").document(mentor_id).delete()
            return serializer.ServerResponse(status="200", message="Mentor data has been deleted successfully.")
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to delete mentor by id. Please have a look at the log.")
        
        
    def add_mentor(self,mentor_data:serializer.Mentor)-> serializer.ServerResponse:
        try:
            db.collection("mentors").add(mentor_data.model_dump(mode="json"))
            
            return serializer.ServerResponse(status="200", message="The mentor data has been added to the database successfully.")
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to add mentor to database. Please have a look at the log.")
       
            
    '''
    Messages would be in two different ways ..
    One between anonymous user and mentor
    Second between regular user and mentor
    ======================================>
    structure for message data:
    {
        "sender_id": "sdfslkdfa",
        "receiver_id": "receiver_user_id",
        "body" : "asdfl;kjdfk",
        "media": [array of image url],
        "date": ""
}
    '''         
    def send_message_anonym(self, mentor_message:serializer.MentorMessageAnonym) -> serializer.ServerResponse:
        try:
            # there willbe a room created for the user and mentor conversation.
            db.collection("messages_mentors_anonym").document("")
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to send message to mentor.")
    
    '''
    This method for authenticated user.
    '''    
    def send_message_to_mentor(self,mentor_message:serializer.MentorMessageAuthUser):
        try:
            db.collection("messages_mentors_session").document(mentor_message.model_dump(mode="json")["sender_id"]+"_"+mentor_message.model_dump(mode="json")["receiver_id"]).add(mentor_message.model_dump(mode = "json"))
            return serializer.ServerResponse(status="200", message="The message has been successfully sent to the receiver.")
        except:
            import traceback; traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to send message to mentor.")