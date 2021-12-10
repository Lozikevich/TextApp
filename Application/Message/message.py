# from dataclasses import dataclass
# from datetime import datetime
#
#
# class Message:
#
#     def __init__(self, mg_time: str, login: str, to_login: str, txt: str):
#         self._mg_time = mg_time
#         self._login = login
#         self._to_login = to_login
#         self._txt = txt
#
#     @property
#     def mg_time(self) -> str:
#         return self._mg_time
#
#     @property
#     def login(self) -> str:
#         return self._login
#
#     @property
#     def to_login(self) -> str:
#         return self._to_login
#
#     @property
#     def txt(self) -> str:
#         return self._txt
#
#     @mg_time.setter
#     def mg_time(self, mg_time: datetime):
#         self._mg_time = mg_time
#
#     @login.setter
#     def login(self, login: str):
#         self._login = login
#
#     @to_login.setter
#     def to_login(self, to_login: str):
#         self._to_login = to_login
#
#     @txt.setter
#     def txt(self, txt: str):
#         self._txt = txt
#
#     def __repr__(self):
#         return f'Message(time={self._mg_time}, login={self._login}, txt={self._txt})'

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class Message:
    mg_time: str
    login: str
    to_login: str
    txt: str

    @property
    def to_json(self) -> Dict[str, Any]:
        return {
            'mg_time': self.mg_time,
            'login': self.login,
            'to_login': self.to_login,
            'txt': self.txt,

        }