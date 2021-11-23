from datetime import datetime
from typing import Dict, Iterable


class Message:
    def __init__(self, time: str, author: str, message: str):
        self.__time = time
        self.__author = author
        self.__message = message

    @property
    def time(self) -> str:
        return self.__time

    @property
    def author(self) -> str:
        return self.__author

    @property
    def message(self) -> str:
        return self.__message

    @message.setter
    def time(self, time: str):
        self.__time = time

    def author(self, author: str):
        self.__author = author

    def message(self, message: str):
        self.__message = message





    @staticmethod
    def get_all_messages():
        return messages_in_chat.values()

    @staticmethod
    def add_new_message():
        messages_in_chat[message.time] = message

    def delete_message(self):
        del messages_in_chat[self.time]

    def get_message(self) -> str:
        return self.message


messages_in_chat: Dict[id, Message] = {}

if __name__ == '__main__':
    # Message(1, 'user_1', 'note_1')
    # Message(2, 'user_2', 'note_2')
    # print(messages_in_chat)
    # delete_message.Message(1)
    # print(messages_in_chat)

    body = Message('20:30', 'user_1', 'note_1')
    print(body.message)
    print(get_all_messages())
