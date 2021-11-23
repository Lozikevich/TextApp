from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Message:
    date_time: str
    author: str
    text: str


messages_in_chat = []


def get_all_messages() -> list[Message]:
    return messages_in_chat


def add_new_message(text: Message):
    messages_in_chat.append(text)


def delete_message(index: int):
    messages_in_chat.pop(index)


if __name__ == '__main__':
    print('hello')
