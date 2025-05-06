from fastapi import APIRouter
from serializers import serializer
from services.QuestionerService import QuestionerService
from fastapi import Depends
from models.model import CourseModel

questionnaire_router = APIRouter()

questionnaire_service = QuestionerService()

@questionnaire_router.post("/submit")
def add_questioner(questioner: serializer.Questioner) -> serializer.ServerResponse:
    return questionnaire_service.add_questioner(questioner)


@questionnaire_router.get("/",response_model=list[serializer.Questioner])
def get_questioners()-> list[serializer.Questioner]:
    return questionnaire_service.get_questioners()

@questionnaire_router.get("/{question_id}", response_model=serializer.Questioner)
def get_questionnaire_by_id(question_id:str):
    return questionnaire_service.get_questionnaire_by_id(question_id)

@questionnaire_router.patch("/{qa_id}",response_model=serializer.Questioner)
def update_questioner_by_id(qa_id:str, new_qa_data:serializer.Questioner) -> serializer.ServerResponse:
    return questionnaire_service.update_questioner_by_id(qa_id,new_qa_data=new_qa_data)
