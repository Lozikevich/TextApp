from Message.message import *
from typing import Iterable
from abc import abstractmethod
from pathlib import Path


class AbstractMessageStorage(object):
    @abstractmethod
    def get_all(self) -> Iterable[Message]:
        raise NotImplemented

    @abstractmethod
    def get_one(self, time: str) -> Message | None:
        raise NotImplemented

    @abstractmethod
    def put_one(self, message: Message):
        raise NotImplemented

    @abstractmethod
    def delete_one(self, time: str):
        raise NotImplemented


class BaseMessageStorage(object):
    def __init__(self, folder: str):
        self._messages = {}
        self.__folder = folder


class ReadOnlyMessageStorage(BaseMessageStorage):
    def get_all(self) -> Iterable[Message]:
        return self._messages.values()

    def get_one(self, time: str) -> Message | None:
        return self._messages.get(time, None)


class WriteOnlyMessageStorage(BaseMessageStorage):
    def put_one(self, message: Message):
        self._messages[message.time] = message

    def delete_one(self, time: str):
        del self._messages[time]


class ReadWriteMessageStorage(ReadOnlyMessageStorage, WriteOnlyMessageStorage, AbstractMessageStorage):
    pass

# Определяем класс для файлового хранилища сообщений


class FileMessageStorage(AbstractMessageStorage):
    def __init__(self, file: Path):
        self._path = file

        if not self._path.exists:
            self._path.open('w')

    def get_all(self) -> Iterable[Message]:
        try:
            with self._path.open('r') as f:
                for line in f.readlines():
                    values = line.split('][')
                    yield Message(values[0], values[1], values[2].removesuffix('\n'))

        except FileNotFoundError:
            pass

    # def put_one(self, note: Note):
    #     # читаем заметки, фильтруем, перезаписываем с новыми данными
    #     lines = [self.__make_line(x) for x in self.get_all() if x.id != note.id] + [self.__make_line(note)]
    #     self.__path.write_text('\n'.join(lines))

    # def __make_line(self, note: Note) -> str:
    #     return self.__delimiter.join([str(note.id), note.author, note.message])
    #
    # def __make_note(self, line: str):
    #     note_id, author, message = line.split(self.__delimiter)
    #     return Note(int(note_id), author, message)

    def get_one(self, time: str) -> Message | None:
        for message in self.get_all():
            if message.time == time:
                return message

    def put_one(self, message: Message):
        lines = []
        with self._path.open('r') as f:
            lines.extend(f.readlines())
        lines.append(f'{message.time}][{message.login}][{message.message}\n')
        with self._path.open('w') as f:
            f.writelines(lines)

    # lines = [self.__make_line(x) for x in self.get_all() if x.id != note.id] + [self.__make_line(note)]
    # self.__path.write_text('\n'.join(lines))

    def delete_one(self, time: str):
        raise NotImplemented
