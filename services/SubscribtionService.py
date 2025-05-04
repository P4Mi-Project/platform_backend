from serializers import serializer
from configs.firebase_admin_config import db
import traceback
from fastapi.exceptions import HTTPException
from datetime import datetime

class SubscriptionService:
    def __init__(self):
        pass

    '''
    To unsubscribe just remove the record.
    '''
    def subscribe(self,email_addr) -> serializer.ServerResponse:
        try:
            db.collection("newsletter_subscribers").add({
                "email":email_addr,
                "subscribed_at": datetime.now()
            })
            return serializer.ServerResponse(status="200", message="Subscribed to the newsletter.")
        except:
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to subscribe to the newsletter.")
        
    
    def unsubscribe(self,email_addr):
        try:
            res = list(db.collection("newsletter_subscribers").where("email", "==", email_addr).stream())
            
            if len(res) == 0:
                raise HTTPException(status_code=404, detail = "The email address is not subscribed to the newsletter.")
            results = db.collection("newsletter_subscribers").where("email", "==", email_addr).stream()
            for doc in results:
                doc.reference.delete()
                
        except:
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="Something went wrong while trying to unsubscribe to the newsletter. Plesae have a look at the log.")