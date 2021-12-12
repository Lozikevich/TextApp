import sqlite3
from datetime import datetime
from typing import Iterable, Tuple
from pathlib import Path
from Client.Message.MessageStorage import *


class DatabaseMessageStorage(AbstractMessageStorage):
    def __init__(self, path: Path):
        self.__connection = sqlite3.Connection(path)
        self.__cursor = self.__connection.cursor()
        # создаём таблицу "messages", если таковой ещё нет
        self.__cursor.execute(
            'CREATE TABLE IF NOT EXISTS messages (mg_time text PRIMARY KEY, t_num text, to_t_num text, txt text)'
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
            'INSERT INTO messages VALUES (:mg_time, :t_num, :to_t_num, :txt) '
            '  ON CONFLICT (mg_time) DO UPDATE SET mg_time=:mg_time, t_num=:t_num, to_t_num=:to_t_num, txt=:txt',
            (message.mg_time, message.t_num, message.to_t_num, message.txt))
        self.__connection.commit()

    def delete_one(self, mg_time: str):
        # обновляем указанную запись из таблицы
        self.__cursor.execute('DELETE FROM messages WHERE mg_time=:mg_time', {'mg_time': mg_time})
        self.__connection.commit()

    def max_time(self):
        time_list = []
        for message in self.get_all():
            time_list.append(datetime.strptime(message.mg_time, "%Y-%m-%d %H:%M:%S.%f"))
        return str(max(time_list))
