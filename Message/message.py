from dataclasses import dataclass
from datetime import datetime


class Message:

    def __init__(self, mg_time: datetime, login: str, message: str):
        self._mg_time = mg_time
        self._login = login
        self._message = message

    @property
    def mg_time(self) -> datetime:
        return self._mg_time

    @property
    def login(self) -> str:
        return self._login

    @property
    def message(self) -> str:
        return self._message

    @mg_time.setter
    def mg_time(self, mg_time: datetime):
        self._mg_time = mg_time

    @login.setter
    def login(self, login: str):
        self._login = login

    @message.setter
    def message(self, message: str):
        self._message = message

    def __repr__(self):
        return f'User(time={self._time}, login={self._login}, message={self._message})'
