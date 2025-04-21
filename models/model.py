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
    # url:str = ""
    # image_url:str = ""
    # author_id:str = ""
    # description:str = ""
    # short_description:str = ""
    # duration:int = 0
    # # created_at:date = None
    # # updated_at:date = None
    # thumbnail:str = ""
    # category:id = 0
    # level_id:int = 0
    # course_language:str = ""
    # tags:list[str] = []
    