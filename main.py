from User.UserStorageSQL import *
from User.UserManager import *


if __name__ == '__main__':

    main_user_storage = DatabaseUserStorage(Path('storage.db'))
    manager = UserManager(main_user_storage)

    # manager.add_new_user(User(0, 'Ivan_0', '123', 'Ivan_0@gmail.com'))
    # manager.add_new_user(User(1, 'Ivan_1', '123', 'Ivan_1@gmail.com'))
    # manager.add_new_user(User(2, 'Ivan_2', '123', 'Ivan_2@gmail.com'))
    # manager.add_new_user(User(3, 'Ivan_3', '123', 'Ivan_2@gmail.com'))
    # manager.add_new_user(User(4, 'Ivan_4', '123', 'Ivan_4@gmail.com'))
    # manager.add_new_user(User(5, 'Ivan_2', '123', 'Ivan_5@gmail.com'))
    print([user for user in manager.get_all_users])
    # print(main_user_storage.get_one(1))
    # manager.add_new_user(manager.user_creator())



    # print(manager.check_login_registration('Ivan_2'))
    # print(manager.get_all_users)
    # # manager.add_new_user(manager.user_creator())
    # # print(manager.get_all_users)
    # print(datetime.now())
    # data = str(datetime.now())
    # data_formatter = "%Y-%m-%d %H:%M:%S.%f"
    # print(datetime.strptime(str(datetime.now()), data_formatter))
    # # print(datetime.strptime(data, data_formatter))

    # print(manager.check_login_authorization('Ivan_3'))
    # manager.delete_user(6)
    # print(manager.get_all_users)
    # print(manager.user_id_creator())
    # print(manager.user_id_creator())
    # main_message_storage = FileMessageStorage(Path('MessageStorage.txt'))
    # manager = MessageManager('Public', main_message_storage)
    # manager.add_new_message(Message(datetime.now(), 'I_0', '0'))
    # print(manager.get_all_messages())
    # manager.add_new_message(Message(datetime.now(), 'I_1', '1'))
    # print(manager.get_all_messages())
    # manager.add_new_message(Message(datetime.now(), 'I_2', '2'))
    # print(manager.get_all_messages())
    # print(manager.get_one_message('2021-12-04 17:28:51.828210'))
    # print(datetime.strptime('2021-12-04 17:28:51.100000', "%Y-%m-%d %H:%M:%S.%f"))
