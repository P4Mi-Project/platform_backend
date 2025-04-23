from fastapi import APIRouter
from serializers import serializer
from services.QuestionerService import QuestionerService
from configs.firebase_admin_config import db
import base64

img_router = APIRouter()

qa_service = QuestionerService()

'''
You need to invoke the post::course route from CourseController to be able to use this route.
@param image:bytes the byte representation of image file.
@param course_id:str the id of the course record that is already exists in the firebase filestore.
'''
@img_router.post("/thumbnail")
def add_thumbnail(image: bytes,course_id)-> serializer.ServerResponse:
    try:
        image_b64 = base64.b64encode(image)
        res = db.collection("courses").document(course_id).get().to_dict()
        if res != None:
            db.collection("courses").document(course_id).set({
                "thumbnail": image_b64
            }, merge= True)
            
            return serializer.ServerResponse(status = "200", message="The thumbnail has been added to the server successfully.")
        return serializer.ServerResponse(status = "404", message="The course with that course id does not exists.")
    except:
        import traceback; traceback.print_exc();
        return serializer.ServerResponse(status="500", message="Something went wrong while trying to add thumbnail to the course. Please have a look at the log.")