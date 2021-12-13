from Application.User.UserManager import *
from Application.User.SQLUserStorage import *


if __name__ == '__main__':
    __main_user_storage = DatabaseUserStorage(Path(
        '~/TextApp/Application/User/UserStorage.db'))
    __manager = UserManager(__main_user_storage)
    __manager.add_new_user(User('0', 'user_0', '123', 'user_0@mail.ru'))
    __manager.add_new_user(User('1', 'user_1', '123', 'user_1@mail.ru'))
    __manager.add_new_user(User('2', 'user_2', '123', 'user_2@mail.ru'))
    __manager.add_new_user(User('3', 'user_3', '123', 'user_3@mail.ru'))
    __manager.add_new_user(User('4', 'user_4', '123', 'user_4@mail.ru'))
    __manager.add_new_user(User('5', 'user_5', '123', 'user_5@mail.ru'))
