from app.database import engine, conn
from app.models.article import Article
import pymysql
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
pymysql.install_as_MySQLdb()

def join(item: Article, db: Session):
    return None

def login(id: str, item: Article, db: Session):
    return None

def update(id, item, db):
    return None

def delete(id, item, db):
    return None


def find_articlese(page:int, db: Session):
    print(f" page number is {page}")
    return db.query(Article).all()

def find_articlese_legacy():
    cursor = conn.cursor()
    sql = "select * from articlese"
    cursor.execute(sql)
    return cursor.fetchall()

def find_article(id, db):
    return None

def find_articlese_by_job(search, page, db):
    return None