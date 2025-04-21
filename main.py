from typing import Union

from fastapi import FastAPI
from controllers.AuthenticationController import auth_router
from controllers.CourseController import course_router
from middlewares.AuthorizationMiddleware import authorization_middleware

app = FastAPI()
app.get("/", )
# app.add_middleware(authorization_middleware)

# adding controller routes
app.include_router(auth_router, prefix="/api/v1/auth")
app.include_router(course_router, prefix = "/api/v1/course")