from typing import Iterable
from abc import abstractmethod
from Client.Message.message import *


class AbstractMessageStorage(object):
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


class BaseMessageStorage(object):
    def __init__(self, folder: str):
        self._messages = {}
        self.__folder = folder


class ReadOnlyMessageStorage(BaseMessageStorage):
    def get_all(self) -> Iterable[Message]:
        return self._messages.values()

    def get_one(self, mg_time: str) -> Message | None:
        return self._messages.get(mg_time, None)


class WriteOnlyMessageStorage(BaseMessageStorage):
    def put_one(self, message: Message):
        self._messages[message.mg_time] = message

    def delete_one(self, mg_time: str):
        del self._messages[mg_time]


class ReadWriteMessageStorage(ReadOnlyMessageStorage, WriteOnlyMessageStorage, AbstractMessageStorage):
    pass
