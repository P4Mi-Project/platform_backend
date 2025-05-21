from serializers import serializer
from configs.firebase_admin_config import db
from models.model import CourseModel
import traceback
from fastapi import Depends
from fastapi.exceptions import HTTPException

class CourseService:
    def add_course(self,course_data:serializer.Course) -> serializer.ServerResponse:
        try:
            db.collection("courses").add(
                # "title":course_data.title,
               course_data.model_dump(mode="json")
            )
        
            return serializer.ServerResponse(status = "200", message=f"The course with the title : {course_data.title} has been successfully saved!")
        except:
            traceback.print_exc()
            # return serializer.ServerResponse(status = "500", message=f"Something went wrong while trying to save the course info the database. Please have a look at the log.")
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to save the course info the database. Please have a look at the log.")
        
    def get_courses(self)-> list[serializer.Course] | None:
        try:
            collection_dict_list = list()
            for item in db.collection("courses").get():
                collection_dict_list.append(item.to_dict())
            return collection_dict_list
        except:
            traceback.print_exc()
            # return None
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get the course info from the database. Please have a look at the log.")
            
        
    '''
    Sample id : 5VOFdQgBrEe6xShCIlO1
    '''
    def get_course_by_id(self,course_id:str) -> serializer.Course | None:
        try:
            return db.collection("courses").document(course_id).get().to_dict()
        except:
            traceback.print_exc()
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to get the course by id from the database. Please have a look at the log.")
            
        
    def add_courses(self,course_list:list[serializer.Course]) -> serializer.ServerResponse:
        try:
            for item in course_list:
                db.collection("courses").add(item.model_dump(mode="json"))
            return serializer.ServerResponse(status="200", message="The course list is successfully been added to the server.")
        except:
            traceback.print_exc()
            # return serializer.ServerResponse(status="500", message="Something went wrong while trying to add the course list to the server.\nPlease have a look at the log.")
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to add courses info to the database. Please have a look at the log.")
            
        
        
    def update_course_by_id(self,course_id:str,new_course_data:serializer.Course) -> serializer.ServerResponse:
        try:
            res = db.collection("courses").document(course_id).get().to_dict()
            if res == None:
                # return serializer.ServerResponse(status="404", message="The course with that is does not exists in the database.")
                raise HTTPException(status_code=404, detail="The course with that is does not exists in the database.")
            else:
                db.collection("courses").document(course_id).set(new_course_data.model_dump(mode = "json"),merge = True)
                
                return serializer.ServerResponse(status="200", message="The course has been successfully updated to the data base.")
        except:
            traceback.print_exc()
            # return serializer.ServerResponse(status="500", message="Something went wrong while trying to update the course data to the server.")
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to update the course info by id. Please have a look at the log.")
        
        
        
    def delete_course(self,course_id:str) -> serializer.ServerResponse:
        try:
            db.collection("courses").document(course_id).delete()
            return serializer.ServerResponse(status="200", message="Course data has been deleted successfully.")
        except:
            traceback.print_exc()
            
            # return serializer.ServerResponse(status="500", message="Something went wrong while trying to delete the course from database")
            raise HTTPException(status_code=500, detail=f"Something went wrong while trying to delete the course info from the database. Please have a look at the log.")
            

    '''
    Todo : need to test this method before integrating to the frontend.
    This method fetches list of courses based on the category id.
    @param category_id:int -> The id of the category.
    '''
    def get_courses_by_category_id(category_id:str) -> list[serializer.Category]:
        try:
            db.collection("courses").where()
        except:
            traceback.print_exc()
            HTTPException(status_code=500, detail="Something went wrong while trying fetch course list based on category id. Please have a look at the log.")