from Client.User.SQLUserStorage import *
from Client.User.user import *


class UserManager:
    def __init__(self, storage: DatabaseUserStorage):
        self.__user_storage = storage

    def get_one(self, t_num: str) -> User:
        return self.__user_storage.get_one(t_num)

    # Достает параметры по t_num
    def get_login(self, t_num: str) -> str:
        return self.__user_storage.get_login(t_num)

    # Добавление нового пользователя
    def add_new_user(self, user: User):
        return self.__user_storage.put_one(user)

    @property
    def get_all_users(self) -> Iterable[User]:
        return self.__user_storage.get_all()
