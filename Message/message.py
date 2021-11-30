from dataclasses import dataclass
from datetime import datetime


# @dataclass()
# class Message:
#     time: str
#     login: str
#     message: str

class Message:

    def __init__(self, time: str, login: str, message: str):
        self._time = time
        self._login = login
        self._message = message

    @property
    def time(self) -> str:
        return self._time

    @property
    def login(self) -> str:
        return self._login

    @property
    def message(self) -> str:
        return self._message

    @time.setter
    def time(self, time: str):
        self._time = time

    @login.setter
    def login(self, login: str):
        self._login = login

    @message.setter
    def message(self, message: str):
        self._message = message

    def __repr__(self):
        return f'User(time={self._time}, login={self._login}, message={self._message})'
