import sqlite3
from typing import Iterable, Tuple
from pathlib import Path
from abc import abstractmethod
from Client.User.user import *


class AbstractDatabaseUserStorage(object):
    @abstractmethod
    def get_all(self) -> Iterable[User]:
        raise NotImplemented

    @abstractmethod
    def get_one(self, t_num) -> User | None:
        raise NotImplemented

    @abstractmethod
    def put_one(self, user: User):
        raise NotImplemented

    @abstractmethod
    def delete_one(self, t_num: str):
        raise NotImplemented


class DatabaseUserStorage(AbstractDatabaseUserStorage):
    def __init__(self, path: Path):
        self.__connection = sqlite3.Connection(path)
        self.__cursor = self.__connection.cursor()
        # создаём таблицу "users", если таковой ещё нет
        self.__cursor.execute(
            'CREATE TABLE IF NOT EXISTS users (t_num text PRIMARY KEY, login text)')

    @staticmethod
    def __make_user(row: Tuple[str, str]) -> User:
        return User(row[0], row[1])

    # Выгружает все строки из db и импотритует в User
    def get_all(self) -> Iterable[User]:
        yield from (self.__make_user(row) for row in self.__cursor.execute('SELECT * FROM users'))

    def get_one(self, t_num) -> User | None:
        # запрашиваем нужную запись по t_num
        rows = self.__cursor.execute('SELECT * FROM users WHERE t_num=:t_num', {'t_num': t_num})
        # формируем user из первого (и единственного, вероятного) элемента rows, если таковой имеется
        try:
            return self.__make_user(next(rows))
        except StopIteration:
            return None

    # Выдает параметры по user_id
    def get_login(self, t_num) -> str:
        row = self.__cursor.execute('SELECT * FROM users WHERE t_num=:t_num', {'t_num': t_num})
        user = self.__make_user(next(row))
        return user.login

    def get_user_id_by_login(self, login) -> str:
        row = self.__cursor.execute('SELECT * FROM users WHERE login=:login', {'login': login})
        user = self.__make_user(next(row))
        return user.t_num

    def put_one(self, user: User):
        # обновляем существующую запись в таблице или вставляем новую
        self.__cursor.execute(
            'INSERT INTO users VALUES (:t_num, :login) '
            '  ON CONFLICT (t_num) DO UPDATE SET t_num=:t_num, login=:login',
            (user.t_num, user.login))
        self.__connection.commit()

    def delete_one(self, t_num: str):
        # обновляем указанную запись из таблицы
        self.__cursor.execute('DELETE FROM users WHERE t_num=:t_num', {'t_num': t_num})
        self.__connection.commit()

