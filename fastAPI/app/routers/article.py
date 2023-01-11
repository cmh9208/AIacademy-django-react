from fastapi import APIRouter, Depends
import app.repositories.article as dao
from sqlalchemy.orm import Session
from app.schemas.article import Article
from app.database import get_db

router = APIRouter()


@router.post("/")
async def write(item: Article, db: Session = Depends(get_db)):
    article_dict = item.dict()
    print((f"SignUp Inform : {article_dict}"))
    dao.join(item=item,db=db)
    return {"data":"sucess"}

@router.put("/{id}")
async def update(id:str,item: Article, db: Session = Depends(get_db)):
    dao.update(id=id,item=item,db=db)
    return {"data":"sucess"}

@router.delete("/{id}")
async def delete(id:str,user: Article, db: Session = Depends(get_db)):
    dao.delte(id=id,item=user,db=db)
    return {"data":"sucess"}

## Q
@router.get("/{page}")
async def get_articles(page, db: Session = Depends(get_db)):
    ls = dao.find_articles(page,db)
    return {"data": ls}

@router.get("/email/{id}")
async def get_article(id : str,db: Session = Depends(get_db)):
    dao.find_article(id=id,db=db)
    return {"data": "sucess"}

@router.get("/job/{search}/{no}")
async def get_articles_by_title(search: str, page: int, db: Session = Depends(get_db)):
    dao.find_article_by_title(search,page,db)
    return {"data":"sucess"}