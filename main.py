from datetime import datetime
from Message.MessageManager import *
from Message.MessageStorage import *
from User.UserManager import *
from User.UserStorage import *
from User.user import *
from pathlib import Path


if __name__ == '__main__':

    # main_user_storage = ReadWriteUserStorage('storage.txt')
    # manager = UserManager(main_user_storage)
    #
    # manager.add_new_user(User(0, 'Ivan_0', '123', 'Ivan_0@gmail.com'))
    #
    # manager.add_new_user(User(1, 'Ivan_1', '123', 'Ivan_1@gmail.com'))
    #
    # manager.add_new_user(User(2, 'Ivan_2', '123', 'Ivan_2@gmail.com'))
    #
    # manager.add_new_user(User(3, 'Ivan_3', '123', 'Ivan_2@gmail.com'))
    #
    # manager.add_new_user(User(4, 'Ivan_4', '123', 'Ivan_4@gmail.com'))
    #
    # manager.add_new_user(User(5, 'Ivan_2', '123', 'Ivan_5@gmail.com'))
    # # print(manager.check_login_registration('Ivan_2'))
    # print(manager.get_all_users)
    # # manager.add_new_user(manager.user_creator())
    # # print(manager.get_all_users)
    # print(datetime.now())
    data = str(datetime.now())
    data_formatter = "%Y-%m-%d %H:%M:%S.%f"
    print(datetime.strptime(str(datetime.now()), data_formatter))
    # print(datetime.strptime(data, data_formatter))

    # print(manager.check_login_authorization('Ivan_3'))
    # manager.delete_user(6)
    # print(manager.get_all_users)
    # print(manager.user_id_creator())
    # print(manager.user_id_creator())



    # main_message_storage = FileMessageStorage(Path('MessageStorage.txt'))
    # manager = MessageManager('Public', main_message_storage)
    #
    # manager.add_new_message(Message('20:05', 'I_0', '0'))
    #
    # manager.add_new_message(Message('20:06', 'I_1', '1'))
    #
    # manager.add_new_message(Message('20:07', 'I_2', '2'))
    #
    # print([message for message in manager.get_all_messages()])
    # print(manager.get_one_message('20:06'))

    # print('')
    # manager.add_new_message(Message(datetime.now(), 'Ivan_0', '123'))
    # print('')
    # manager.add_new_message(Message(datetime.now(), 'Ivan_1', '123'))
    # print('')
    # manager.add_new_message(Message(datetime.now(), 'Ivan_0', '123'))

