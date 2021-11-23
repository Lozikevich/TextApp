from datetime import datetime
from typing import Dict


# from datetime import date, time

messages_in_chat = {}


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

    @time.setter
    def time(self, time: str):
        self.__time = time

    @author.setter
    def author(self, author: str):
        self.__author = author

    @message.setter
    def message(self, message: str):
        self.__message = message

    @staticmethod
    def get_all_messages():
        return messages_in_chat.values()

    @staticmethod
    def add_new_message(message):
        messages_in_chat[message.time] = message

    @staticmethod
    def delete_message(message):
        del messages_in_chat[message]

    @staticmethod
    def get_message(message):
        return message

    def __repr__(self) -> str:
        return f'Message(time={self.time}, author={self.author}, message={self.message})'


if __name__ == '__main__':
    Message.add_new_message(Message('20', 'user_1', 'note_1'))
    Message.add_new_message(Message('25', 'user_2', 'note_2'))
    Message.add_new_message(Message('30', 'user_3', 'note_3'))
    print(Message.get_all_messages())

    Message.delete_message('20')
    print(Message.get_all_messages())
