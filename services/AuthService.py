from serializers import serializer
from configs.firebase_admin_config import db
import traceback

class AuthService:
    def anonymous_register(user_model: serializer.AnonymousUserModel) -> serializer.ServerResponse:
        try:
            db.collection("anonymous_users").add(user_model)
            return serializer.ServerResponse(status="200", message="Anonymous user is registered successfully.")
        except:
            traceback.print_exc()
            return serializer.ServerResponse(status = "500", message="Something went wrong while trying to register anonymous user.")