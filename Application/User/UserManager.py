from Application.User.SQLUserStorage import *
from Application.User.user import *


class UserManager:
    def __init__(self, storage: DatabaseUserStorage):
        self.__user_storage = storage

    @property
    def get_all_users(self) -> Iterable[User]:
        return self.__user_storage.get_all()

    def get_one(self, t_num: str) -> User:
        return self.__user_storage.get_one(t_num)

    # Достает параметры по t_num
    def get_login(self, t_num: str) -> str:
        return self.__user_storage.get_login(t_num)

    def get_email(self, t_num: str) -> str:
        return self.__user_storage.get_email(t_num)

    def get_password(self, t_num: str) -> str:
        return self.__user_storage.get_password(t_num)

    # Достает параметры по login
    def get_password_by_login(self, login: str):
        return self.__user_storage.get_password_by_login(login)

    # Проверка login на повторяемость при регистрации нового пользователя
    def check_login_registration(self, login: str) -> bool:
        _a = 0
        for users in self.get_all_users:
            if login == users.login:
                _a = 1
            else:
                continue
        if _a == 1:
            print('Пользователь с таким login уже зарегистрирован в системе')
            return True
        else:
            return False

        # Проверка t_num на регистрацию в базе данных

    def check_t_num_registration(self, t_num: str) -> bool:
        _a = 0
        for user in self.get_all_users:
            if t_num == user.t_num:
                _a = 1
            else:
                continue
            if _a == 1:
                return True
            else:
                return False

    # Проверка email на повторяемость при регистрации нового пользователя
    def check_email_registration(self, email: str) -> bool:
        for users in self.get_all_users:
            _a = 0
            if email == users.email:
                _a = 1
            else:
                continue
            if _a == 1:
                print('Пользователь с таким email уже зарегистрирован в системе')
                return True
            else:
                return False

    # Проверка login на совпадение при авторизации пользователя
    def check_login_authorization(self, login: str) -> bool:
        for users in self.get_all_users:
            _a = 0
            if login == users.login:
                _a = 1
            else:
                continue
            if _a == 1:
                return True
            else:
                print('Пользователь с таким login не зарегистрирован в системе')
                return False

    # Проверка password на совпадение при авторизации пользователя
    def check_password_authorization(self, login: str, password: str) -> bool:
        if password == self.get_password_by_login(login):
            return True
        else:
            return False

    # Проверка наличия пользователя по telephone_number
    def check_user_id(self, t_num) -> bool:
        for users in self.get_all_users:
            _a = 0
            if t_num == users.t_num:
                _a = 1
            else:
                continue
            if _a == 1:
                return True
            else:
                print('Пользователь с таким user_id не зарегистрирован в системе')
                return False

    # Удаление пользователя по t_num
    def delete_user(self, t_num):
        if not self.check_user_id(t_num):
            print('Пользователь с таким t_num не найден')
        else:
            return self.__user_storage.delete_one(t_num)

    # Добавление нового пользователя
    def add_new_user(self, user: User):
        return self.__user_storage.put_one(user)
