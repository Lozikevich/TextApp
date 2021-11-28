from enum import Enum
from datetime import date


class User:

    def __init__(self, user_id: int, login: str, password: str, email: str):
        self._user_id = user_id
        self._login = login
        self._password = password
        self._email = email

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def login(self) -> str:
        return self._login

    @property
    def password(self) -> str:
        return self._password

    @property
    def email(self) -> str:
        return self._email

    @user_id.setter
    def user_id(self, user_id: int):
        self._user_id = user_id

    @login.setter
    def login(self, login: str):
        self._login = login

    @email.setter
    def email(self, email: str):
        self._email = email

    def __repr__(self):
        return f'User(user_id={self._user_id}, login={self._login}, email={self._email})'
