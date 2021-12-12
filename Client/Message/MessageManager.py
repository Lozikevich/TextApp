from Client.Message.MessageStorage import *
from Client.Message.SQLMessageStorage import *


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
        self.__storage.delete_one(mg_time)

    def max_time(self):
        return self.__storage.max_time
