from typing import Iterable
from dataclasses import dataclass


@dataclass()
class Message:
    time: str
    login: str
    message: str


class MessageStorage:
    def __init__(self, folder: str):
        self.__messages = {}
        self.__folder = folder

    def get_all(self) -> Iterable[Message]:
        return self.__messages.values()

    def put_one(self, message: Message):
        self.__messages[message.time] = message

    def delete_one(self, time: str):
        del self.__messages[time]


class MessageManager:
    def __init__(self, name: str, storage: MessageStorage):
        self.__name = name
        self.__storage = storage

    @property
    def get_all_messages(self):
        return self.__storage.get_all()

    def add_new_message(self, message):
        self.__storage.put_one(message)

    def delete_message(self, time):
        self.__storage.delete_one(time)





