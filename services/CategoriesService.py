from configs.firebase_admin_config import db
from serializers import serializer

class CategoriesService:
    def __init__(self):
        pass
    
    def get_all_categories(self) -> list[serializer.Category]:
        try:
            return [serializer.Category(name = item.to_dict()["name"]) for item in db.collection("categories").get()]
        except:
            import traceback; traceback.print_exc();
            return []
        
    def get_category_by_id(self, category_id) -> serializer.Category | None:
        try:
            return db.collection("categories").document(category_id).get().to_dict()
        
        except:
            import traceback; traceback.print_exc();
            return None