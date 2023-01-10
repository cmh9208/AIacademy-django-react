from sqlalchemy_utils import UUIDType

from .mixins import TimestampMixin
from ..database import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Session, relationship
from pydantic import BaseModel, BaseConfig


class Article(Base, TimestampMixin):

    __tablename__ = "articlese"

    SEQ = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20), nullable=False)
    content = Column(String(20), nullable=False)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.user_id'), nullable=True)

    user = relationship('User', back_populates='article')

    class Config:
        # BaseConfig.arbitrary_types_allowed = True
        arbitrary_types_allowed = True