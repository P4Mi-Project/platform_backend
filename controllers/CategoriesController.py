from fastapi import APIRouter
from serializers import serializer
from services.CategoriesService import CategoriesService
categories_router = APIRouter()

categories_service = CategoriesService()

@categories_router.get("/categories")
def get_all_categories() -> list[serializer.Category]:
    return categories_service.get_all_categories()


@categories_router.get("/category/{category_id}")
def get_category_by_id(category_id:str) -> serializer.Category:
    return categories_service.get_category_by_id(category_id=category_id)

@categories_router.get("/course/<category_id>")
def get_courses_by_category_id(category_id:str):
    pass