from Message.MessageStorage import *


class MessageManager:
    def __init__(self, name: str, storage: FileMessageStorage):
        self.__name = name
        self.__storage = storage

    @property
    def get_all_messages(self):
        return self.__storage.get_all

    def get_one_message(self, time):
        return self.__storage.get_one(time)

    def add_new_message(self, message):
        self.__storage.put_one(message)

    def delete_message(self, time):
        self.__storage.delete_one(time)
