import sqlite3
from typing import Iterable, Tuple
from pathlib import Path
from User.user import *
from abc import abstractmethod


class AbstractDatabaseUserStorage(object):
    @abstractmethod
    def get_all(self) -> Iterable[User]:
        raise NotImplemented

    @abstractmethod
    def get_one(self, user_id) -> User | None:
        raise NotImplemented

    @abstractmethod
    def put_one(self, user: User):
        raise NotImplemented

    @abstractmethod
    def delete_one(self, note_id: int):
        raise NotImplemented


class DatabaseUserStorage(AbstractDatabaseUserStorage):
    def __init__(self, path: Path):
        self.__connection = sqlite3.Connection(path)
        self.__cursor = self.__connection.cursor()
        # создаём таблицу "users", если таковой ещё нет
        self.__cursor.execute(
            'CREATE TABLE IF NOT EXISTS users (user_id int PRIMARY KEY, login text, password text, email text)'
        )

    # Делает User из строки db
    @staticmethod
    def __make_user(row: Tuple[int, str, str, str]) -> User:
        return User(row[0], row[1], row[2], row[3])

    # Выгружает все строки из db и импотритует в User
    def get_all(self) -> Iterable[User]:
        yield from (self.__make_user(row) for row in self.__cursor.execute('SELECT * FROM users'))

    def get_one(self, user_id) -> User | None:
        # запрашиваем нужную запись по user_id
        rows = self.__cursor.execute('SELECT * FROM users WHERE user_id=:user_id', {'user_id': user_id})
        # формируем user из первого (и единственного, вероятного) элемента rows, если таковой имеется
        try:
            return self.__make_user(next(rows))
        except StopIteration:
            return None

    # Выдает параметры по user_id
    def get_login(self, user_id):
        row = self.__cursor.execute('SELECT * FROM users WHERE user_id=:user_id', {'user_id': user_id})
        user = self.__make_user(next(row))
        return user.login

    def get_password(self, user_id):
        row = self.__cursor.execute('SELECT * FROM users WHERE user_id=:user_id', {'user_id': user_id})
        user = self.__make_user(next(row))
        return user.password

    def get_email(self, user_id):
        row = self.__cursor.execute('SELECT * FROM users WHERE user_id=:user_id', {'user_id': user_id})
        user = self.__make_user(next(row))
        return user.email

    # Вытаскивает параметры по login
    def get_password_by_login(self, login) -> str:
        row = self.__cursor.execute('SELECT * FROM users WHERE login=:login', {'login': login})
        user = self.__make_user(next(row))
        return user.password

    def get_user_id_by_login(self, login) -> int:
        row = self.__cursor.execute('SELECT * FROM users WHERE login=:login', {'login': login})
        user = self.__make_user(next(row))
        return user.user_id

    def put_one(self, user: User):
        # обновляем существующую запись в таблице или вставляем новую
        self.__cursor.execute(
            'INSERT INTO users VALUES (:user_id, :login, :password, :email) '
            '  ON CONFLICT (user_id) DO UPDATE SET user_id=:user_id, login=:login, password=:password, email=:email',
            (user.user_id, user.login, user.password, user.email))
        self.__connection.commit()

    def delete_one(self, user_id: int):
        # обновляем указанную запись из таблицы
        self.__cursor.execute('DELETE FROM users WHERE user_id=:user_id', {'user_id': user_id})
        self.__connection.commit()


