from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
# (dto, vo, dao) dao 데이터에 접근하는 객체
import app.repositories.article as dao
from app.database import get_db
from app.schemas.article import Article

router = APIRouter()

@router.post("/")
async def write(item: Article, db: Session = Depends(get_db)):
    article_dict = item.dict()
    print(f"SignUp Inform : {article_dict}")
    dao.join(item, db)
    return {"data": "success"}

@router.post("/{id}")
async def login(id:str,item: Article, db: Session = Depends(get_db)):
    dao.login(id, item, db)
    return {"data": "success"}

@router.put("/{id}")
async def update(id:str, item: Article, db: Session = Depends(get_db)):
    dao.update(id,item,db)
    return {"data": "success"}

@router.delete("/{id}")
async def delete(id:str, item: Article, db: Session = Depends(get_db)):
    dao.delete(id,item,db)
    return {"data": "success"}

@router.get("/{page}")
async def get_articles(page: int, db: Session = Depends(get_db)):
    ls = dao.find_articlese(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_article(id: str, db: Session = Depends(get_db)):
    dao.find_article(id, db)
    return {"data": "success"}

@router.get("/job/{search}/{no}")
async def get_articlese_by_job(search:str, page: int, db: Session = Depends(get_db)):
    dao.find_articlese_by_job(search, page,db)
    return {"data": "success"}



