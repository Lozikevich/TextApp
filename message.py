messages_in_chat = {}


class Message:
    def __init__(self, time: str, login: str, message: str):
        self.__time = time
        self.__login = login
        self.__message = message

    @property
    def time(self) -> str:
        return self.__time

    @property
    def login(self) -> str:
        return self.__login

    @property
    def message(self) -> str:
        return self.__message

    @time.setter
    def time(self, time: str):
        self.__time = time

    @login.setter
    def login(self, login: str):
        self.__login = login

    @message.setter
    def message(self, message: str):
        self.__message = message

    @staticmethod
    def get_all_messages():
        return messages_in_chat.values()

    @staticmethod
    def delete_message(message):
        del messages_in_chat[message]


    @staticmethod
    def add_new_message(message):
        messages_in_chat[message.time] = message

    @staticmethod
    def get_message(message):
        return message

    def __repr__(self) -> str:
        return f'Message(time={self.time}, login={self.login}, message={self.message})'


