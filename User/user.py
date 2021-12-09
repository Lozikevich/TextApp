from enum import Enum
from datetime import date


class User:

    def __init__(self, telephone_number: str, login: str, password: str, email: str):
        self._telephone_number = telephone_number
        self._login = login
        self._password = password
        self._email = email

    @property
    def telephone_number(self) -> str:
        return self._telephone_number

    @property
    def login(self) -> str:
        return self._login

    @property
    def password(self) -> str:
        return self._password

    @property
    def email(self) -> str:
        return self._email

    @telephone_number.setter
    def telephone_number(self, telephone_number: str):
        self._telephone_number = telephone_number

    @login.setter
    def login(self, login: str):
        self._login = login

    @email.setter
    def email(self, email: str):
        self._email = email

    def __repr__(self):
        return f'User(telephone_number={self._telephone_number}, login={self._login}, email={self._email})'
