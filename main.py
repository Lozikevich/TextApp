from datetime import datetime
from Message.MessageManager import *

from User.UserManager import *
from User.UserStorage import *
from User.user import *


if __name__ == '__main__':
    # main_storage = ReadWriteMessageStorage('~/data')
    # public_manager = MessageManager('public', main_storage)
    # public_manager.add_new_message(Message('25.11.2021 20:05', 'user_1', 'note_1'))
    # public_manager.add_new_message(Message('25.11.2021 20:06', 'user_2', 'note_2'))
    # public_manager.add_new_message(Message(str(datetime.now()), 'user_3', 'note_3'))
    #
    # private_manager = MessageManager('private', main_storage)
    # private_manager.add_new_message(Message('25.11.2021 20:05', 'user_1', 'note_1'))
    # private_manager.add_new_message(Message('25.11.2021 20:06', 'user_2', 'note_2'))
    # private_manager.add_new_message(Message(str(datetime.now()), 'user_3', 'note_3'))
    #
    # print(public_manager.get_all_messages)
    # print('-------')
    # public_manager.delete_message('25.11.2021 20:05')
    # print(public_manager.get_all_messages)
    # print('---------------')

    main_user_storage = ReadWriteUserStorage('~/data')
    manager = UserManager(main_user_storage)
    manager.add_new_user(User(0, 'Ivan_0', 'Ivan_0@gmail.com'))

    manager.add_new_user(User(1, 'Ivan_1', 'Ivan_1@gmail.com'))
    print(manager.get_all_users)
    manager.add_new_user(User(2, 'Ivan_2', 'Ivan_2@gmail.com'))
    print(manager.get_all_users)
    manager.add_new_user(User(3, 'Ivan_2', 'Ivan_3@gmail.com'))
    print(manager.get_all_users)
    manager.add_new_user(User(4, 'Ivan_4', 'Ivan_2@gmail.com'))
    print(manager.get_all_users)
    manager.add_new_user(User(5, 'Ivan_5', 'Ivan_5@gmail.com'))
    print(manager.get_all_users)
    # user_1 = manager.get_one(2)
    # print(user_1.email)
    # print(manager.get_login(2))

