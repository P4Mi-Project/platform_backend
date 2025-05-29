from fastapi import APIRouter
from serializers import serializer
from services.CategoriesService import CategoriesService

community_router = APIRouter()


@community_router.get("/posts")
def get_posts()-> list[str]:
    pass