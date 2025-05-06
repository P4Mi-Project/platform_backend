from fastapi import APIRouter
from serializers import serializer
from services.SubscribtionService import SubscriptionService
subscription_router = APIRouter()

subscription_service = SubscriptionService()

@subscription_router.post("/subscribe",response_model = serializer.ServerResponse)
def subscribe_newsletter(email:str):
    return subscription_service.subscribe(email)

@subscription_router.delete("/unsubscribe",response_model=serializer.ServerResponse)
def unsubscribe(email:str):
    return subscription_service.unsubscribe(email)

