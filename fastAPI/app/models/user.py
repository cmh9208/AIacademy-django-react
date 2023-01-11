from uuid import uuid4
from .mixins import TimestampMixin
from ..database import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType

class User(Base, TimestampMixin): # Base

    __tablename__="users"

    user_id = Column(UUIDType(binary=False), primary_key=True, default=uuid4)
    user_email = Column(String(20), nullable=False)
    password = Column(String(20), nullable=False)
    user_name = Column(String(20), nullable=False)
    phone = Column(String(20))
    birth = Column(String(20))
    address = Column(String(20))
    job = Column(String(20))
    user_interests = Column(String(20))
    token = Column(String(20))

    articles = relationship('Article', back_populates='user')

    class Config:
        arbitrary_types_allowed = True