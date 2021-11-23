from dataclasses import dataclass
from datetime import datetime
from typing import Dict, Iterable


@dataclass
class Message:
    id: int
    author: str
    message: str


messages_in_chat: Dict[id, Message] = {}


def get_all_messages() -> Iterable:
    return messages_in_chat.values()


def add_new_message(message: Message):
    messages_in_chat[message.id] = message


def delete_message(id_message: int):
    del messages_in_chat[id_message]


if __name__ == '__main__':
    add_new_message(Message(1, 'user_1', 'note_1'))
    add_new_message(Message(2, 'user_2', 'note_2'))
    print(messages_in_chat)
    delete_message(1)
    print(messages_in_chat)