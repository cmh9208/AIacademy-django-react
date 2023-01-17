from abc import ABC
from typing import List
import pymysql
from sqlalchemy.orm import Session

from app.bases.article import ArticleBase
from app.schemas.article import ArticleDTO

pymysql.install_as_MySQLdb()


class ArticleCrud(ArticleBase, ABC):
    def write(self, request_article: ArticleDTO) -> str:
        pass

    def update_article(self, request_article: ArticleDTO) -> str:
        pass

    def delete_article(self, request_article: ArticleDTO) -> str:
        pass

    def find_all_articles(self, page: int) -> List[ArticleDTO]:
        pass

    def find_articles_by_userid(self, request_article: ArticleDTO) -> ArticleDTO:
        pass

    def find_articles_by_title(self, request_article: ArticleDTO) -> str:
        pass