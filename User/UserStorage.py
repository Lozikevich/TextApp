from User.user import *
from typing import Iterable


class BaseStorage(object):
    def __init__(self, folder: str):
        self._users = {}
        self.__folder = folder


class ReadOnlyUserStorage(BaseStorage):
    def get_all(self) -> Iterable[User]:
        return self._users.values()

    def get_one(self, user_id: int) -> User | None:
        return self._users.get(user_id, None)


class WriteOnlyUserStorage(BaseStorage):
    def put_one(self, user: User):
        self._users[user.user_id] = user

    def delete_one(self, user_id: int):
        del self._users[user_id]


class ReadWriteUserStorage(ReadOnlyUserStorage, WriteOnlyUserStorage):
    pass
