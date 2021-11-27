from enum import Enum
from dataclasses import dataclass
from datetime import date


# class User:
#     def __init__(self, user_id: int, login: str, password: str, date_of_birth: str, country: str, email: str):
#         self._user_id = user_id
#         self._login = login
#         self._password = password
#         self._date_of_birth = date_of_birth
#         self._country = country
#         self._email = email
#
#     def __repr__(self):
#         return f'ReadWriteUserStorage(user_id={self.user_id}, login={self.login}, email={self.email})'
#
#     @property
#     def login(self) -> str:
#         return self._login
#
#     def get_login(self, user_id):
#         return self.login(user_id)


@dataclass
class User:
    user_id: int
    login: str
    password: str
    date_of_birth: str
    country: str
    email: str

