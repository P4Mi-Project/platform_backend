from firebase_admin import credentials
import firebase_admin
from firebase_admin import auth
import firebase_admin.exceptions

cred = credentials.Certificate("google-service.json")

firebase_app = firebase_admin.initialize_app(cred)

'''
The len of the id token must be greater than 0
'''
def verify_token(token:str)-> dict:
    if len(token) > 0:
        return {}
    try:
        return auth.verify_id_token(app = firebase_admin, id_token=token)
    except Exception:
        
        return {}