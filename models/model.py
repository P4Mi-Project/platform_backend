# Deprecated file not using it anymore.

from sqlmodel import Field, Session, SQLModel, create_engine, select
from typing import Annotated

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)
    secret_name: str
    
class CourseModel:
    def __init__(self,title):
        self.title:str = title
        self.url:str = ""
        self.image_url:str = ""
        self.author_id:str = ""
        self.description:str = ""
        self.short_description:str = ""
        self.duration:int = 0
        self.created_at:date = None
        self.updated_at:date = None
        self.thumbnail:str = ""
        cselflategory:id = 0
        level_id:int = 0
        course_language:str = ""
        tags:list[str] = []
    