from abc import abstractmethod, ABCMeta
from typing import List
from app.models.article import Article
from app.schemas.article import ArticleDTO


class ArticleBase(metaclass=ABCMeta):

    @abstractmethod
    def add_article(self, request_article: ArticleDTO): pass

    @abstractmethod
    def update_article(self, request_article: ArticleDTO): pass

    @abstractmethod
    def delete_article(self, request_article: ArticleDTO): pass

    @abstractmethod
    def find_all_articles(self, request_article: ArticleDTO) -> List[ArticleDTO]: pass

    @abstractmethod
    def find_articles_by_userid(self, request_article: ArticleDTO) -> List[ArticleDTO]: pass

    @abstractmethod
    def find_articles_by_title(self, request_article: ArticleDTO) -> List[ArticleDTO]: pass

    @abstractmethod
    def find_article_by_seq(self, request_article: ArticleDTO) -> ArticleDTO: pass