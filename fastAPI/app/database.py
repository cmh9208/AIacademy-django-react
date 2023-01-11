from typing import Generator
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from app.env import HOSTNAME, PORT, USERNAME, PASSWORD, CHARSET, DATABASE, DB_URL
import pymysql

Base = declarative_base()
engine = create_engine(DB_URL, echo=True)
pymysql.install_as_MySQLdb()
conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)
SessionLocal = scoped_session(
    sessionmaker(
        bind=engine,
        autocommit=False,
        autoflush=False)
)
Base.query = SessionLocal.query_property()

async def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()