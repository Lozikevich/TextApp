from User.user import *
from typing import Iterable
from abc import abstractmethod


class AbstractUserStorage(object):
    @abstractmethod
    def get_all(self) -> Iterable[User]:
        raise NotImplemented

    @abstractmethod
    def get_one(self, user_id: int) -> User | None:
        raise NotImplemented

    @abstractmethod
    def get_login(self, user_id):
        raise NotImplemented

    @abstractmethod
    def get_email(self, user_id):
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

    def get_one(self, user_id: int) -> User | None:
       return self._users.get(user_id, None)

    def get_login(self, user_id):
        return self.get_one(user_id).login

    def get_email(self, user_id):
        return self.get_one(user_id).email


class WriteOnlyUserStorage(BaseStorage):
    def put_one(self, user: User):
        self._users[user.user_id] = user

    def delete_one(self, user_id: int):
        del self._users[user_id]


class ReadWriteUserStorage(ReadOnlyUserStorage, WriteOnlyUserStorage, AbstractUserStorage):
    pass
