from datetime import datetime
from typing import List
from uuid import UUID
from pydantic import BaseModel
from app.schemas.article import Article


class User(BaseModel):
    user_id : UUID
    user_email : str
    password : str
    user_name : str
    phone : str
    birth : str
    address : str
    job : str
    user_interests : str
    token : str
    create_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True

class UserDetail(User):
    articles: List[Article] = []