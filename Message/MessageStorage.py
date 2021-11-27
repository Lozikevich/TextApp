from Message.message import *
from typing import Iterable


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


class ReadWriteMessageStorage(ReadOnlyMessageStorage, WriteOnlyMessageStorage):
    pass


