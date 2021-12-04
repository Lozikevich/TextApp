from distutils.command.install import value

from User.UserStorage import *


class UserManager:
    def __init__(self, storage: ReadWriteUserStorage):
        self.__user_storage = storage

    @property
    def get_all_users(self) -> Iterable[User]:
        return self.__user_storage.get_all()

    def get_one(self, user_id: int) -> User:
        return self.__user_storage.get_one(user_id)

    def get_user_id(self) -> int:
        return self.__user_storage.get_user_id

    # Достает параметры по user_id
    def get_login(self, user_id: int) -> str:
        return self.__user_storage.get_login(user_id)

    def get_email(self, user_id: int) -> str:
        return self.__user_storage.get_email(user_id)

    def get_password(self, user_id: int) -> str:
        return self.__user_storage.get_password(user_id)

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

    # Проверка наличия пользователя по user_id
    def check_user_id(self, user_id) -> bool:
        for users in self.get_all_users:
            _a = 0
            if user_id == users.user_id:
                _a = 1
            else:
                continue
            if _a == 1:
                return True
            else:
                print('Пользователь с таким user_id не зарегистрирован в системе')
                return False

    # Удаление пользователя по user_id
    def delete_user(self, user_id):
        if not self.check_user_id(user_id):
            print('Пользователь с таким user_id не найден')
        else:
            return self.__user_storage.delete_one(user_id)

    # Присвоение user_id
    def user_id_creator(self) -> int:
        a = 0
        for users in self.get_all_users:
            if users.user_id > a:
                a = users.user_id
        return a + 1

    # Задание пользовател в диалоговом окне
    def user_creator(self) -> User:
        print("Введите Ваш логин, пароль, электронную почту в строку через ' ;; ': ")
        a = input()
        user = []
        for i in a:
            values = a.split(' ;; ')
            user = User(int(self.user_id_creator()), values[0], values[1], values[2])
        return user

    # Добавление нового пользователя
    def add_new_user(self, user: User):
        if not (self.check_login_registration(user.login) or self.check_email_registration(user.email)):
            return self.__user_storage.put_one(user)
