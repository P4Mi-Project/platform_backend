from fastapi import APIRouter
from serializers import serializer
from services.MentorshipService import MentorshipService

# Todo : need to test this endpoint
mentorship_router = APIRouter()

mentorship_service = MentorshipService()

@mentorship_router.get("/mentors")
def get_mentor_list()-> list[serializer.Mentor]:
    return mentorship_service.get_mentor_list()

@mentorship_router.get("/mentor/{mentor_id}")
def get_mentor_by_id(mentor_id:str):
    mentorship_service.get_mentor_by_id(mentor_id)
    
@mentorship_router.patch("/mentor/{mentor_id}",response_model = serializer.ServerResponse,)
def update_mentor_by_id(mentor_id:str,new_mentor_data:serializer.Mentor) -> serializer.ServerResponse:
    return mentorship_service.update_mentor_by_id(mentor_id, new_mentor_data)

@mentorship_router.delete("/mentor/{mentor_id}")
def delete_mentor_by_id(mentor_id):
    return mentorship_service.delete_mentor_by_id(mentor_id)

@mentorship_router.post("/mentor")
def add_mentor(mentor_data: serializer.Mentor) -> serializer.ServerResponse:
    mentorship_service.add_mentor(mentor_data)
    
@mentorship_router.post("/message")
def send_message(mentor_message:serializer.MentorMessageAnonym) -> serializer.ServerResponse:
    pass

@mentorship_router.post("/message/auth")
def send_message_to_mentor_auth(mentor_message: serializer.MentorMessageAuthUser) -> serializer.ServerResponse:
    mentorship_service.send_message_to_mentor(mentor_message=mentor_message)