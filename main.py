from datetime import datetime
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
    print('---------------')

    User.add_new_user(User(0, 'Jonny', '123', '01.01.1991', 'Russian', 'Jonny@mail.ru', 1))
    User.add_new_user(User(1, 'Jonny_1', '123', '01.01.1991', 'Russian', 'Jonny_1@mail.ru', 0))
    User.add_new_user(User(2, 'Jonny_2', '123', '01.01.1991', 'Russian', 'Jonny_2@mail.ru', 1))

    print(User.list_of_users())
    print('-------')
    User.delete_user(2)
    print(User.list_of_users())
