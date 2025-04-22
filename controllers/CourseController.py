from fastapi import APIRouter
from serializers import serializer
from services.CourseService import CourseService
from fastapi import Depends
from models.model import CourseModel

course_router = APIRouter()

course_service = CourseService()
@course_router.post("/add_course")
async def add_course(course_data:serializer.Course)-> serializer.ServerResponse:
    print(f"printing the value of the course : {course_data}")
    # course_model = CourseModel(title = course_data.title)
    return course_service.add_course(course_data=course_data)


@course_router.get("/courses")
async def get_courses():
    return course_service.get_courses()

@course_router.get("/course/{id}")
async def get_course_by_id(id:str):
    return course_service.get_course_by_id(id)

@course_router.post("/courses")
async def add_courses(course_list:list[serializer.Course]) -> serializer.ServerResponse:
    return course_service.add_courses(course_list)

@course_router.patch("/course/{course_id}")
def update_course(course_id:str, new_course_data: serializer.Course) -> serializer.ServerResponse:
    return course_service.update_course_by_id(course_id = course_id, new_course_data = new_course_data)