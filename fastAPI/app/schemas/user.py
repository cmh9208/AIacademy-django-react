from typing import List, Optional
from pydantic import BaseModel
from app.schemas.article import ArticleDTO


class UserDTO(BaseModel):
    userid : Optional[str]
    email : Optional[str]
    password : Optional[str]
    username : Optional[str]
    phone : Optional[str]
    birth : Optional[str]
    address : Optional[str]
    job : Optional[str]
    interests : Optional[str]
    token : Optional[str]
    created: Optional[str]
    modified: Optional[str]

    class Config:
        orm_mode = True

class UserDetail(UserDTO):
    articles: List[ArticleDTO] = []