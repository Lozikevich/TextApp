from dataclasses import dataclass


@dataclass()
class Message:
    time: str
    login: str
    message: str

