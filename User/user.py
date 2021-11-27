from enum import Enum
from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    user_id: int
    login: str
    password: str
    date_of_birth: date
    country: str
    email: str


class Status(Enum):
    online = 1
    offline = 0
