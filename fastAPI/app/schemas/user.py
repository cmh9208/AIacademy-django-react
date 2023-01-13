from typing import List, Optional
from pydantic import BaseModel
from app.schemas.article import Article


class UserDTO(BaseModel):
    user_id : Optional[str]
    user_email : Optional[str]
    password : Optional[str]
    user_name : Optional[str]
    phone : Optional[str]
    birth : Optional[str]
    address : Optional[str]
    job : Optional[str]
    user_interests : Optional[str]
    token : Optional[str]
    create_at: Optional[str]
    updated_at: Optional[str]

    class Config:
        orm_mode = True

class UserDetail(UserDTO):
    articles: List[Article] = []