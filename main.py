from typing import Union

from fastapi import FastAPI
from controllers.AuthenticationController import auth_router
from controllers.QuestionerController import questionnaire_router
from controllers.CourseController import course_router
from middlewares.AuthorizationMiddleware import authorization_middleware
from configs.firebase_admin_config import db
import logging
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


coors_list = [
    "http://localhost:8001/",
    "https://l76kp2k5-8001.uks1.devtunnels.ms/"
]



@asynccontextmanager
def seed_data_base(app: FastAPI):
    # Need checks the existence of 3 collections 
    # * Category
    # * Language 
    # * 
    logging.info("Initiating the seeding process...")
    try:

        if db.collection("categories").get().to_dict() == None:
            db.collection("categories").document().add({
                "name" : "Learning Dutch"
            }, {
                "name": "Jobs Opportunities",
            },
            {
                "name": "Internships"
            },
            {
                "name": "Entrepreneurship"
            },
            {
                "name": "Legal Procedures"
            },
            {
                "name": "Cultural Adaptation"
            },
            {
                "name": "Psychological suppport"
            },
            {"name" : "Other"})
            
        
        if db.collection("languages").get().to_dict() == None:
            db.collection("languages").document().add(
                {
                 "name": "English",
                },
                {
                 "name": "Dutch",
                },
                {
                 "name": "Spanish",
                })
        
        logging.info("Seeding process is ended successfully...")
        # return True
    except:
        logging.info("Seeding process was unsuccessfull...")
        import traceback; traceback.print_exc();
        # return False

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=coors_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/", )
# app.add_middleware(authorization_middleware)

# adding controller routes
app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(course_router, prefix = "/api/v1")
app.include_router(questionnaire_router, prefix="/api/v1/questionnaire")