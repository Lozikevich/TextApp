from datetime import datetime
from Message.MessageManager import *

from User.UserManager import *
from User.UserStorage import *
from User.user import *


if __name__ == '__main__':

    main_user_storage = ReadWriteUserStorage('~/data')
    manager = UserManager(main_user_storage)
    manager.add_new_user(User(0, 'Ivan_0', '123', 'Ivan_0@gmail.com'))

    manager.add_new_user(User(1, 'Ivan_1', '123', 'Ivan_1@gmail.com'))
    manager.add_new_user(User(2, 'Ivan_2', '123', 'Ivan_2@gmail.com'))
    print(manager.get_all_users)
    manager.add_new_user(User(3, 'Ivan_2', '123', 'Ivan_3@gmail.com'))
    print(manager.get_all_users)
    manager.add_new_user(User(4, 'Ivan_4', '123', 'Ivan_2@gmail.com'))
    manager.add_new_user(User(5, 'Ivan_5', '123', 'Ivan_5@gmail.com'))
    print(manager.get_all_users)
    manager.delete_user(6)
    print(manager.get_all_users)

    main_message_storage = ReadWriteMessageStorage('~/data')
    manager = MessageManager('~/data', main_message_storage)
    manager.add_new_message(Message('17:00', 'Ivan_0', '123'))
    manager.add_new_message(Message('17:01', 'Ivan_1', '123'))
    manager.add_new_message(Message(str(datetime.now()), 'Ivan_0', '123'))
    print(manager.get_all_messages)
