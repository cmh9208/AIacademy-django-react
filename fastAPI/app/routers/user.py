from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import app.repositories.user as dao
from app.database import get_db
from app.schemas.user import User

router = APIRouter()

@router.post("/")
async def join(item: User, db: Session = Depends(get_db)):
    user_dict = item.dict()
    print(f"SignUp Inform : {user_dict}")
    dao.join(item, db)
    return {"data": "success"}

@router.post("/{id}")
async def login(id:str,item: User, db: Session = Depends(get_db)):
    dao.login(id, item, db)
    return {"data": "success"}

@router.put("/{id}")
async def update(id:str, item: User, db: Session = Depends(get_db)):
    dao.update(id,item,db)
    return {"data": "success"}

@router.delete("/{id}")
async def delete(id:str, item: User, db: Session = Depends(get_db)):
    dao.delete(id,item,db)
    return {"data": "success"}

@router.get("/{page}")
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