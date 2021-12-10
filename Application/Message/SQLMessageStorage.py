import sqlite3
from typing import Iterable, Tuple
from pathlib import Path
from Application.Message.message import *
from abc import abstractmethod
from Application.Message.MessageStorage import *


class DatabaseMessageStorage(AbstractMessageStorage):
    def __init__(self, path: Path):
        self.__connection = sqlite3.Connection(path)
        self.__cursor = self.__connection.cursor()
        # создаём таблицу "messages", если таковой ещё нет
        self.__cursor.execute(
            'CREATE TABLE IF NOT EXISTS messages (mg_time text PRIMARY KEY, login text, to_login text, txt text)'
        )

    # Делает Message из строки db
    @staticmethod
    def __make_message(row: Tuple[str, str, str, str]) -> Message:
        return Message(row[0], row[1], row[2], row[3])

    # Выгружает все строки из db и импотритует в Message
    def get_all(self) -> Iterable[Message]:
        yield from (self.__make_message(row) for row in self.__cursor.execute('SELECT * FROM messages'))

    def get_one(self, mg_time) -> Message | None:
        # запрашиваем нужную запись по mg_time
        rows = self.__cursor.execute('SELECT * FROM messages WHERE mg_time=:mg_time', {'mg_time': mg_time})
        # формируем message из первого (и единственного, вероятного) элемента rows, если таковой имеется
        try:
            return self.__make_message(next(rows))
        except StopIteration:
            return None

    def put_one(self, message: Message):
        # обновляем существующую запись в таблице или вставляем новую
        self.__cursor.execute(
            'INSERT INTO messages VALUES (:mg_time, :login, :to_login, :txt) '
            '  ON CONFLICT (mg_time) DO UPDATE SET mg_time=:mg_time, login=:login, to_login=:to_login, txt=:txt',
            (message.mg_time, message.login, message.to_login, message.txt))
        self.__connection.commit()

    def delete_one(self, mg_time: str):
        # обновляем указанную запись из таблицы
        self.__cursor.execute('DELETE FROM messages WHERE mg_time=:mg_time', {'mg_time': mg_time})
        self.__connection.commit()
