
from fastapi import FastAPI

from app.models.user import User

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

@app.get("/users/login")
async def login(user: User):
    print(f"리액트에서 넘긴 정보:{user.get_email()}, {user.get_password()}")

# python -m uvicorn app.main:app --reload
# 422는 스키마가 예상하는 일부 데이터가 누락되었음을 의미