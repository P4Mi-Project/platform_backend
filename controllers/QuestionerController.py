from fastapi import APIRouter
from serializers import serializer
from services.QuestionerService import QuestionerService
from fastapi import Depends
from models.model import CourseModel

qa_router = APIRouter()

qa_service = QuestionerService()

@qa_router.post("/questioner")
def add_questioner(questioner: serializer.Questioner) -> serializer.ServerResponse:
    return qa_service.add_questioner(questioner)


@qa_router.get("/questioners")
def get_questioners()-> list[serializer.Questioner]:
    return qa_service.get_questioners()

@qa_router.patch("/questioner/{qa_id}")
def update_questioner_by_id(qa_id:str, new_qa_data:serializer.Questioner) -> serializer.ServerResponse:
    return qa_service.update_qa(qa_id)
