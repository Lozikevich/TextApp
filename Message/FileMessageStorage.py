from Message.message import *
from abc import abstractmethod
from pathlib import Path
from typing import Iterable


class AbstractFileMessageStorage(object):
    @abstractmethod
    def get_all(self) -> Iterable[Message]:
        raise NotImplemented

    @abstractmethod
    def get_one(self, mg_time: datetime) -> Message | None:
        raise NotImplemented

    @abstractmethod
    def put_one(self, message: Message):
        raise NotImplemented

    @abstractmethod
    def delete_one(self, mg_time: datetime):
        raise NotImplemented

    @abstractmethod
    def message_maker(self, line: str) -> Message:
        raise NotImplemented

    @abstractmethod
    def _make_line(self, message: Message) -> str:
        raise NotImplemented


class FileMessageStorage(AbstractFileMessageStorage):
    def __init__(self, file: Path, delimiter=']['):
        self._path = file
        self._delimiter = delimiter

        if not self._path.exists:
            self._path.open('w')

    def get_all(self) -> Iterable[Message]:
        try:
            with self._path.open('r') as f:
                for line in f.readlines():
                    values = line.split('][')
                    yield Message(datetime.strptime(values[0], "%Y-%m-%d %H:%M:%S.%f"), values[1],
                                  values[2].removesuffix('\n'))

        except FileNotFoundError:
            pass

#   Преобразует строку из файла в объект Message
    def message_maker(self, line: str) -> Message:
        mg_time_str, login, message = line.split('][')
        mg_time = datetime.strptime(mg_time_str, "%Y-%m-%d %H:%M:%S.%f")
        return Message(mg_time, login, message)

#   Преобразует Message в строку
    def _make_line(self, message: Message) -> str:
        return self._delimiter.join([str(message.mg_time), message.login, message.message])

#   Добавляет строку в файл
    def put_one(self, message: Message):
        lines = [self._make_line(x) for x in self.get_all() if x.mg_time != message.mg_time] + [self._make_line(message)]
        self._path.write_text('\n'.join(lines))

#   Считывает строки из файла и перезаписывает в файл, если message.time не равен искомому
    def delete_one(self, mg_time: datetime):
        lines = [self._make_line(message) for message in self.get_all() if message.mg_time != mg_time]
        self._path.write_text('\n'.join(lines))

#   Находит message по mg_time
    def get_one(self, mg_time: str) -> Message | None:
        for message in self.get_all():
            if str(message.mg_time) == mg_time:
                return message
