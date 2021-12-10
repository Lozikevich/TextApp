from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class User:
    t_num: str
    login: str
    password: str
    email: str

    @property
    def to_json(self) -> Dict[str, Any]:
        return {
            't_num': self.t_num,
            'login': self.login,
            'password': self.password,
            'email': self.email,

        }
