from typing import List

from pydantic import BaseModel


class User(BaseModel):
    user_email : str
    password : str
    user_name : str
    phone : str
    birth : str
    address : str
    job : str
    user_interests : str
    token : str

    class Config:
        orm_mode = True