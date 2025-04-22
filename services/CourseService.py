from serializers import serializer
from configs.firebase_admin_config import db
from models.model import CourseModel
import traceback
from fastapi import Depends

class CourseService:
    def add_course(self,course_data:serializer.Course) -> serializer.ServerResponse:
        try:
            db.collection("courses").add({
                "title":course_data.title,
               
            })
        
            return serializer.ServerResponse(status = "200", message=f"The course with the title : {course_data.title} has been successfully saved!")
        except:
            traceback.print_exc()
            return serializer.ServerResponse(status = "500", message=f"Something went wrong while trying to save the course info the database. Please have a look at the log.")
        
    async def get_courses(self)-> list[serializer.Course] | None:
        try:
            collection_dict_list = list()
            for item in db.collection("courses").get():
                collection_dict_list.append(item.to_dict())
            return collection_dict_list
        except:
            traceback.print_exc()
            return None