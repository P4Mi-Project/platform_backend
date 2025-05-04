from fastapi import APIRouter
from serializers import serializer
from services.SubscribtionService import SubscriptionService
subscription_router = APIRouter()

subscription_service = SubscriptionService()

@subscription_router.post("/subscribe")
def subscribe_newsletter(email:str):
    return subscription_service.subscribe(email)

