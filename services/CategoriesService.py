from configs.firebase_admin_config import db
from serializers import serializer
from fastapi.exceptions import HTTPException

class CategoriesService:
    def __init__(self):
        pass
    
    def get_all_categories(self) -> list[serializer.Category]:
        try:
            return [serializer.Category(name = item.to_dict()["name"]) for item in db.collection("categories").get()]
        except:
            import traceback; traceback.print_exc();
            # return []
            raise HTTPException(status_code=500,detail="Something went wrong please have a look at the log.")
        
    def get_category_by_id(self, category_id) -> serializer.Category | None:
        try:
            return db.collection("categories").document(category_id).get().to_dict()
        
        except:
            import traceback; traceback.print_exc();
            # return None
            raise HTTPException(status_code=500,detail="Something went wrong please have a look at the log.")
