from enum import Enum
from dataclasses import dataclass
from datetime import date


class User:
    def __init__(self, user_id: int, login: str, password: str, date_of_birth: str, country: str, email: str):
        self._user_id = user_id
        self._login = login
        self._password = password
        self._date_of_birth = date_of_birth
        self._country = country
        self._email = email

    @property
    def user_id(self) -> int:
        return self._user_id

    @property
    def login(self) -> str:
        return self._login

    @property
    def email(self) -> str:
        return self._email

    def __repr__(self):
        return f'User(user_id={self._user_id}, login={self._login}, email={self._email})'
