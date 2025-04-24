from configs.firebase_admin_config import db
from serializers import serializer
import traceback

class QuestionerService:
    def add_questioner(self,questioner:serializer.Questioner):
        try:
            db.collection("questioners").add(questioner.model_dump(mode= "json"))
            return serializer.ServerResponse(status="200", message="The questioner has been added successfully")
        
        except:
            traceback.print_exc()
            
            return serializer.ServerResponse(status="500", message="Something went while trying to saving the questioner data to the server.")
        
        
    def get_questioners(self) -> list[serializer.Questioner] | None:
        try:
            return db.collection("questioner").get().to_dict()
        except:
            traceback.print_exc()
            
            return None
        
    def update_questioner_by_id(self,qa_id, new_qa_data:serializer.Questioner) -> serializer.Questioner:
        try:
            res= db.collection("questioners").document(qa_id).get().to_dict()
            
            if res != None:
                db.collection("questioners").document(qa_id),set(new_qa_data.model_dump(mode="json"), merge = True)
                
            return serializer.ServerResponse(status="200", message="The questioner has been updated successfully.")
        except:
            traceback.print_exc()
            return serializer.ServerResponse(status="500", message="Something went wrong while trying to update the questioner data. Please have a look at the log.")
    
    def delete_qa(self, qa_id:str) -> serializer.ServerResponse:
        try:
            db.collection("questioners").document(qa_id).delete()
            return serializer.ServerResponse(status="200", message="The questioner has been deleted successfully.")
        except:
            traceback.print_exc()
            
            return serializer.ServerResponse(status="500", message= "Something went wrong while trying to delete the questioner data. Plesae have a look at a the log.")
        
    def get_questionnaire_by_id(question_id:str) -> serializer.Questioner | None:
        try:
            return db.collection("questionnaire").document(question_id).get().to_dict()
        except:
            traceback.print_exc()
            return None