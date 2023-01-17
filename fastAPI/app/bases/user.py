from abc import abstractmethod, ABCMeta
from typing import List
from app.models.user import User
from app.schemas.user import UserDTO


class UserBase(metaclass=ABCMeta):

    @abstractmethod
    def add_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def login(self, request_user: UserDTO) -> User: pass

    @abstractmethod
    def update_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def delete_user(self, request_user: UserDTO) -> str: pass

    @abstractmethod
    def find_all_users(self, page: int) -> List[User]: pass

    @abstractmethod
    def find_user_by_id(self, request_user: UserDTO) -> UserDTO: pass

    @abstractmethod
    def find_userid_by_email(self, request_user: UserDTO) -> str: pass