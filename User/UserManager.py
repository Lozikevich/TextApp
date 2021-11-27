from User.UserStorage import *


class UserManager:
    def __init__(self, storage: ReadWriteUserStorage):
        self.__user_storage = storage

    @property
    def get_all_users(self):
        return self.__user_storage.get_all()

    def add_new_user(self, user):
        self.__user_storage.put_one(user)

    def delete_message(self, user_id):
        self.__user_storage.delete_one(user_id)

    def get_one(self, user_id):
        return self.__user_storage.get_one(user_id)
