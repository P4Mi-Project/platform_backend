from serializers import serializer
from configs.firebase_admin_config import db
from fastapi.exceptions import HTTPException

class LanguageService:
    def __init__(self):
        pass
    
    def get_all_languages(self) -> list[serializer.Language]:
        try:
            return [serializer.Language(name = item.to_dict()["name"]) for item in db.collection("languages").get()]
        except:
            import traceback; traceback.print_exc();
            # return []
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get all the language info from the database. Please have a look at the log.")
            
        
    def get_language_by_id(self,lang_id:str) -> serializer.Language | None:
        try:
            return db.collection("languages").document(lang_id).get().to_dict()
        except:
            import traceback; traceback.print_exc();
            # return None
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get the language info from the database. Please have a look at the log.")
            