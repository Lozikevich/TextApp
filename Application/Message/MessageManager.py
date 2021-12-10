from Application.Message.MessageStorage import *
from Application.Message.FileMessageStorage import *
from Application.Message.MessageStorage import *
from Application.Message.SQLMessageStorage import *


class MessageManager:
    def __init__(self, storage):
        self.__storage = storage

    @property
    def get_all_messages(self):
        return self.__storage.get_all

    def get_one_message(self, mg_time: str):
        return self.__storage.get_one(mg_time)

    def add_new_message(self, message):
        self.__storage.put_one(message)

    def delete_message(self, mg_time: str):
        # mg_time = datetime.strptime(mg_time, "%Y-%m-%d %H:%M:%S.%f")
        self.__storage.delete_one(mg_time)
