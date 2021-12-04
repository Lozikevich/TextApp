from Message.MessageStorage import *
from Message.FileMessageStorage import *


class MessageManager:
    def __init__(self, name: str, storage: FileMessageStorage):
        self.__name = name
        self.__storage = storage

    @property
    def get_all_messages(self):
        return self.__storage.get_all

    def get_one_message(self, mg_time: datetime):
        return self.__storage.get_one(mg_time)

    def add_new_message(self, message):
        self.__storage.put_one(message)

    def delete_message(self, mg_time: datetime):
        self.__storage.delete_one(mg_time)
