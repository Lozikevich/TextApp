from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class User:
    t_num: str
    login: str
    password: str
    email: str
