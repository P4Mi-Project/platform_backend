from fastapi import APIRouter
from serializers import serializer
from services.AuthService import AuthService
auth_router = APIRouter()

auth_service = AuthService()

@auth_router.get("/register")
async def register():
    return {"message": "User registration endpoint"}

@auth_router.post("/anonymous/register")
def anonymous_register(user_model:serializer.AnonymousUserModel):
    return auth_service.anonymous_register(user_model)
