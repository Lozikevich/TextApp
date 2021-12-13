import sqlite3
from abc import abstractmethod
from typing import Iterable, Tuple
from Client.User.user import *
from pathlib import Path


class AbstractDatabaseUserStorage(object):
    @abstractmethod
    def get_all(self) -> Iterable[User]:
        raise NotImplemented


class DatabaseUserStorage(AbstractDatabaseUserStorage):
    def __init__(self, path: Path):
        self.__connection = sqlite3.Connection(path)
        self.__cursor = self.__connection.cursor()
        # создаём таблицу "users", если таковой ещё нет
        self.__cursor.execute(
            'CREATE TABLE IF NOT EXISTS users (t_num text PRIMARY KEY, login text)'
        )

    @staticmethod
    def __make_user(row: Tuple[str, str]) -> User:
        return User(row[0], row[1])

    def get_all(self) -> Iterable[User]:
        yield from (self.__make_user(row) for row in self.__cursor.execute('SELECT * FROM users'))

    def get_login(self, t_num):
        row = self.__cursor.execute('SELECT * FROM users WHERE t_num=:t_num',
                                    {'t_num': t_num})
        user = self.__make_user(next(row))
        return user.login

    def put_one(self, user: User):
        # обновляем существующую запись в таблице или вставляем новую
        self.__cursor.execute(
            'INSERT INTO users VALUES (:t_num, :login) '
            '  ON CONFLICT (t_num) DO UPDATE SET t_num=:t_num, login=:login',
            (user.t_num, user.login))
        self.__connection.commit()
