from fastapi import APIRouter
from serializers import serializer
from services.MentorshipService import MentorshipService


mentorship_router = APIRouter()

mentorship_service = MentorshipService()

@mentorship_router.get("mentors")
def get_mentor_list()-> list[serializer.Mentor]:
    return mentorship_service.get_mentor_list()