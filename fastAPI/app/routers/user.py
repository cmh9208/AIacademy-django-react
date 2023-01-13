from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.repositories.user as dao
from app.admin.utils import current_time
from app.database import get_db
from app.schemas.user import UserDTO

router = APIRouter()

@router.post("/join")
async def join(user: UserDTO, db: Session = Depends(get_db)):
    print(f" 회원가입에 진입한 시간: {current_time()} ")
    print(f"SignUp Inform : {user}")
    result = dao.join(user, db)
    if result =="":
        result = "failure"
    return {"data": result}

@router.post("/login")
async def login(user: UserDTO, db: Session = Depends(get_db)):
    return_user = dao.login(user, db)
    print(f"로그인 정보 : {return_user.user_email}")
    return {"data": return_user}

@router.put("/modify/{id}")
async def update(id:str, item: UserDTO, db: Session = Depends(get_db)):
    dao.update(id,item,db)
    return {"data": "success"}

@router.delete("/delete/{id}", tags=['age'])
async def delete(id:str, item: UserDTO, db: Session = Depends(get_db)):
    dao.delete(id,item,db)
    return {"data": "success"}

@router.get("/page/{page}")
async def get_users(page: int, db: Session = Depends(get_db)):
    ls = dao.find_users(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_user(id: str, db: Session = Depends(get_db)):
    dao.find_user(id, db)
    return {"data": "success"}

@router.get("/job/{search}/{page}")
async def get_users_by_job(search:str, page: int, db: Session = Depends(get_db)):
    dao.find_users_by_job(search, page,db)
    return {"data": "success"}