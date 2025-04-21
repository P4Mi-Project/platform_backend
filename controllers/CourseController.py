from fastapi import APIRouter
from serializers import serializer
from services.CourseService import CourseService
from fastapi import Depends
from models.model import CourseModel

course_router = APIRouter()

course_service = CourseService()
@course_router.post("/add_course")
async def add_course(course_data:serializer.Course =Depends(serializer.Course))-> serializer.ServerResponse:
    print(f"printing the value of the course : {course_data}")
    # course_model = CourseModel(title = course_data.title)
    return course_service.add_course(course_data=course_data)