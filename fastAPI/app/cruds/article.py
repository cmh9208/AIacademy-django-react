from abc import ABC
from typing import List
import pymysql
from sqlalchemy.orm import Session

from app.bases.article import ArticleBase
from app.models.article import Article
from app.schemas.article import ArticleDTO

pymysql.install_as_MySQLdb()


class ArticleCrud(ArticleBase, ABC):

    def __init__(self, db: Session):
        self.db: Session = db

    def add_article(self, request_article: ArticleDTO) -> str:
        article = Article(**request_article.dict())
        self.db.add(article)
        self.db.commit()
        return "success"

    def update_article(self, request_article: ArticleDTO) -> str:
        update_data = self.find_article_by_seq(request_article)
        self.db.update(update_data)
        self.db.commit()
        return "success"

    def delete_article(self, request_article: ArticleDTO) -> str:
        article = self.find_article_by_seq(Article.seq)
        self.db.delete(article)
        self.db.commit()
        return "success"

    def find_all_articles(self, page: int) -> List[Article]:
        return self.db.query(Article).all()

    def find_articles_by_userid(self, request_article: ArticleDTO) -> List[Article]:
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.userid == article.userid).all()

    def find_articles_by_title(self, request_article: ArticleDTO) -> List[Article]:
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.title == article.title).all()

    def find_article_by_seq(self, request_article: ArticleDTO) -> Article:
        article = Article(**request_article.dict())
        return self.db.query(Article).filter(Article.seq == article.seq).one_or_none()