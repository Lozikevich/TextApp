from Message.message import *
from typing import Iterable
from abc import abstractmethod


class AbstractMessageStorage(object):
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


class BaseMessageStorage(object):
    def __init__(self, folder: str):
        self._messages = {}
        self.__folder = folder


class ReadOnlyMessageStorage(BaseMessageStorage):
    def get_all(self) -> Iterable[Message]:
        return self._messages.values()

    def get_one(self, mg_time: str) -> Message | None:
        # mg_time = datetime.strptime(mg_time, "%Y-%m-%d %H:%M:%S.%f")
        return self._messages.get(mg_time, None)


class WriteOnlyMessageStorage(BaseMessageStorage):
    def put_one(self, message: Message):
        self._messages[message.mg_time] = message

    def delete_one(self, mg_time: datetime):
        del self._messages[mg_time]


class ReadWriteMessageStorage(ReadOnlyMessageStorage, WriteOnlyMessageStorage, AbstractMessageStorage):
    pass
