from fastapi import APIRouter
from serializers import serializer
from services.LanguageService import LanguageService
languages_router = APIRouter()

languages_service = LanguageService()

@languages_router.get("/languages")
def get_all_languages() -> list[serializer.Language]:
    return languages_service.get_all_languages()

@languages_router.get("/languages/{lang_id}")
def get_language_by_id(lang_id:str) -> serializer.Language:
    return languages_service.get_language_by_id(lang_id)