from typing import Iterable
from abc import abstractmethod
from Application.User.user import *


class AbstractUserStorage(object):
    @abstractmethod
    def get_all(self) -> Iterable[User]:
        raise NotImplemented

    @abstractmethod
    def get_one(self, user_id: int) -> User | None:
        raise NotImplemented

    @abstractmethod
    def get_login(self, user_id) -> str:
        raise NotImplemented

    @abstractmethod
    def get_email(self, user_id) -> str:
        raise NotImplemented

    @abstractmethod
    def put_one(self, user: User):
        raise NotImplemented

    @abstractmethod
    def delete_one(self, user_id: int):
        raise NotImplemented


class BaseStorage(object):
    def __init__(self, folder: str):
        self._users = {}
        self.__folder = folder


class ReadOnlyUserStorage(BaseStorage):
    def get_all(self) -> Iterable[User]:
        return self._users.values()

    @property
    def get_user_id(self) -> int:
        return self._users.user_id

    def get_one(self, user_id: int) -> User | None:
        return self._users.get(user_id, None)

# Вытаскивает параметры по user_id
    def get_login(self, user_id) -> str:
        return self.get_one(user_id).login

    def get_email(self, user_id) -> str:
        return self.get_one(user_id).email

    def get_password(self, user_id) -> str:
        return self.get_one(user_id).password

# Вытаскивает параметры по login
    def get_password_by_login(self, login) -> str:
        return self.get_one(login).password

    def get_user_id_by_login(self, login) -> int:
        return self.get_one(login).user_id


class WriteOnlyUserStorage(BaseStorage):
    def put_one(self, user: User):
        self._users[user.user_id] = user

    def delete_one(self, user_id: int):
        del self._users[user_id]


class ReadWriteUserStorage(ReadOnlyUserStorage, WriteOnlyUserStorage, AbstractUserStorage):
    pass
