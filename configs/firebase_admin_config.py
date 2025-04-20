from firebase_admin import credentials
import firebase_admin

cred = credentials.Certificate("google-service.json")

firebase_admin.initialize_app(credential=firebase_admin.credentials.from)