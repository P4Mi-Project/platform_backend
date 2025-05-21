from fastapi import APIRouter
from serializers import serializer
from services.MentorshipService import MentorshipService


mentorship_router = APIRouter()

mentorship_service = MentorshipService()

@mentorship_router.get("/mentors")
def get_mentor_list()-> list[serializer.Mentor]:
    return mentorship_service.get_mentor_list()

@mentorship_router.get("/mentor/{mentor_id}")
def get_mentor_by_id(mentor_id:str):
    mentorship_service.get_mentor_by_id(mentor_id)
    
@mentorship_router.patch("/mentor/{mentor_id}")
def update_mentor_by_id(mentor_id:str,new_mentor_data:serializer.Mentor) -> serializer.ServerResponse:
    return mentorship_service.update_mentor_by_id(mentor_id, new_mentor_data)

@mentorship_router.delete("/mentor/{mentor_id}")
def delete_mentor_by_id(mentor_id):
    pass