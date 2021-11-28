from Message.message import *
from typing import Iterable
from abc import abstractmethod


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


