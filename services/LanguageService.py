from serializers import serializer
from configs.firebase_admin_config import db

class LanguageService:
    def __init__(self):
        pass
    
    def get_all_languages(self) -> list[serializer.Language]:
        try:
            return [serializer.Language(name = item.to_dict()["name"]) for item in db.collection("languages").get()]
        except:
            import traceback; traceback.print_exc();
            return []
        
    def get_language_by_id(self,lang_id:str) -> serializer.Language | None:
        try:
            return db.collection("languages").document(lang_id).get().to_dict()
        except:
            import traceback; traceback.print_exc();
            return None