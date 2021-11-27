from distutils.command.install import value

from User.UserStorage import *


class UserManager:
    def __init__(self, storage: ReadWriteUserStorage):
        self.__user_storage = storage

    @property
    def get_all_users(self):
        return self.__user_storage.get_all()

    def get_one(self, user_id):
        return self.__user_storage.get_one(user_id)

    def get_login(self, user_id):
        return self.__user_storage.get_login(user_id)

    def get_email(self, user_id):
        return self.__user_storage.get_email(user_id)

    # def add_new_user(self, user):
    #     self.__user_storage.put_one(user)

    def delete_user(self, user_id):
        self.__user_storage.delete_one(user_id)

    def add_new_user(self, user: User):
        a = []
        b = []
        for i in range(len(self.get_all_users)):
            a.append(self.get_login(i))
            b.append(self.get_email(i))
        # print(a)
        # print(b)
        if user.login in a:
            print('Пользователь с таким login уже существует')
        elif user.email in b:
            print('Пользователь с таким email уже существует')
        else:
            return self.__user_storage.put_one(user)

