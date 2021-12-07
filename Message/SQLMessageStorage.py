import sqlite3
from typing import Iterable, Tuple
from pathlib import Path
from Message.message import *
from abc import abstractmethod


class AbstractDatabaseMessageStorage(object):
    @abstractmethod
    def get_all(self) -> Iterable[Message]:
        raise NotImplemented

    @abstractmethod
    def get_one(self, mg_time: str) -> Message | None:
        raise NotImplemented

    @abstractmethod
    def put_one(self, message: Message):
        raise NotImplemented

    @abstractmethod
    def delete_one(self, mg_time: str):
        raise NotImplemented


class DatabaseMessageStorage(AbstractDatabaseMessageStorage):
    def __init__(self, path: Path):
        self.__connection = sqlite3.Connection(path)
        self.__cursor = self.__connection.cursor()
        # создаём таблицу "messages", если таковой ещё нет
        self.__cursor.execute(
            'CREATE TABLE IF NOT EXISTS messages (mg_time text PRIMARY KEY, login text, message text)'
        )

    # Делает Message из строки db
    @staticmethod
    def __make_message(row: Tuple[str, str, str]) -> Message:
        return Message(datetime.strptime(row[0], "%Y-%m-%d %H:%M:%S.%f"), row[1], row[2])

    # Выгружает все строки из db и импотритует в User
    def get_all(self) -> Iterable[Message]:
        yield from (self.__make_message(row) for row in self.__cursor.execute('SELECT * FROM messages'))

    def get_one(self, mg_time) -> Message | None:
        # запрашиваем нужную запись по mg_time
        rows = self.__cursor.execute('SELECT * FROM users WHERE mg_time=:mg_time', {'mg_time': mg_time})
        # формируем user из первого (и единственного, вероятного) элемента rows, если таковой имеется
        try:
            return self.__make_message(next(rows))
        except StopIteration:
            return None

    def put_one(self, message: Message):
        # обновляем существующую запись в таблице или вставляем новую
        self.__cursor.execute(
            'INSERT INTO messages VALUES (:mg_time, :login, :message) '
            '  ON CONFLICT (mg_time) DO UPDATE SET mg_time=:mg_time, login=:login, message=:message',
            (message.mg_time, message.login, message.message))
        self.__connection.commit()

    def delete_one(self, mg_time: str):
        # обновляем указанную запись из таблицы
        self.__cursor.execute('DELETE FROM users WHERE mg_time=:mg_time', {'mg_time': mg_time})
        self.__connection.commit()


