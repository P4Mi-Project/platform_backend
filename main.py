from typing import Union

from fastapi import FastAPI
from controllers.AuthenticationController import auth_router
from controllers.QuestionerController import questionnaire_router
from controllers.CourseController import course_router
from controllers.CategoriesController import categories_router
from controllers.SubscriptionController import subscription_router
from controllers.ImageController import img_router
from controllers.MentorshipController import mentorship_router
from configs.firebase_admin_config import db
from controllers.LanguageController import languages_router
import logging
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from middlewares.AuthorizationMiddleware import AuthMiddleWare



coors_list = [
    "http://localhost:8080/",
    "https://l76kp2k5-8001.uks1.devtunnels.ms/"
]



@asynccontextmanager
async def lifespan(app: FastAPI):
    # Need checks the existence of 3 collections 
    # * Category
    # * Language 
    # * 
    logging.info("Initiating the seeding process...")
    try:
        print(db.collection("categories").get())
        if len(db.collection("categories").get()) == 0:
            db.collection("categories").add({
                "name" : "Learning Dutch"
            })
            {"name" : "Other"}
            db.collection("categories").add({
                "name": "Jobs Opportunities",
            })
            
            db.collection("categories").add(
            {
                "name": "Internships"
            })
            
            db.collection("categories").add({
                "name": "Entrepreneurship"
            })
            
            db.collection("categories").add(
            {
                "name": "Legal Procedures"
            })
            
            db.collection("categories").add(
            {
                "name": "Cultural Adaptation"
            })
            
            db.collection("categories").add(
            {
                "name": "Psychological support"
            })
            
            db.collection("categories").add(
            {"name" : "Other"}  
            )
        
        if len(db.collection("languages").get()) == 0:
            languages = ["English", "Dutch", "Spanish"]

            for lang in languages:
                db.collection("languages").add({"name": lang})

        logging.info("Seeding process is ended successfully...")
        yield
        # return True
    except:
        logging.info("Seeding process was unsuccessfull...")
        import traceback; traceback.print_exc();
        yield
        # return False

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    # allow_origins=["*"],
    allow_origins=coors_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    
    
    
)
app.add_middleware(AuthMiddleWare)

app.get("/", )
# app.add_middleware(authorization_middleware)

# adding controller routes
app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(course_router, prefix = "/api/v1")
app.include_router(categories_router, prefix="/api/v1")
app.include_router(questionnaire_router, prefix="/api/v1/questionnaire")
app.include_router(languages_router, prefix="/api/v1")
app.include_router(subscription_router,prefix="/api/v1")
app.include_router(img_router,prefix="/api/v1")
app.include_router(mentorship_router,prefix="/api/v1")