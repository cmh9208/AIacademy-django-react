from typing import List, Optional
from pydantic import BaseModel
from app.schemas.article import ArticleDTO

class UserVO(BaseModel):
    class Config:
        orm_mode = True

class UserDTO(UserVO):
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

    def __str__(self):
        return f'이름: {self.username}, \n ' \
               f'이메일: {self.email} \n ' \
               f'비번: {self.password} \n' \
               f'생년월일: {self.birth} \n' \
               f'주소: {self.address} \n'

class UserList(UserVO):
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


class UserDetail(UserDTO):
    articles: List[ArticleDTO] = []

class UserUpdate(BaseModel):
    userid: Optional[str]
    phone: Optional[str]
    job: Optional[str]
    interests: Optional[str]
    modified: Optional[str]
    token: Optional[str]

    class Config:
        orm_mode = True