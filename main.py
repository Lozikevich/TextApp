from datetime import datetime
from typing import Dict
from message import *
from user import *



if __name__ == '__main__':
    Message.add_new_message(Message('25.11.2021 20:05', 'user_1', 'note_1'))
    Message.add_new_message(Message('25.11.2021 20:06', 'user_2', 'note_2'))
    Message.add_new_message(Message(str(datetime.now()), 'user_3', 'note_3'))
    print(Message.get_all_messages())
    print('-------')
    Message.delete_message('25.11.2021 20:05')
    print(Message.get_all_messages())
    print('-------')

