from User.UserStorage import *
from User.SQLUserStorage import *
# выбрать storage: ReadWriteUserStorage, DatabaseUserStorage


class UserManager:
    def __init__(self, storage: DatabaseUserStorage):
        self.__user_storage = storage

    @property
    def get_all_users(self) -> Iterable[User]:
        return self.__user_storage.get_all()

    def get_one(self, telephone_number: int) -> User:
        return self.__user_storage.get_one(telephone_number)

    # Достает параметры по user_id
    def get_login(self, telephone_number: int) -> str:
        return self.__user_storage.get_login(telephone_number)

    def get_email(self, telephone_number: int) -> str:
        return self.__user_storage.get_email(telephone_number)

    def get_password(self, telephone_number: int) -> str:
        return self.__user_storage.get_password(telephone_number)

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

    # Проверка наличия пользователя по telephone_number
    def check_user_id(self, telephone_number) -> bool:
        for users in self.get_all_users:
            _a = 0
            if telephone_number == users.telephone_number:
                _a = 1
            else:
                continue
            if _a == 1:
                return True
            else:
                print('Пользователь с таким user_id не зарегистрирован в системе')
                return False

    # Удаление пользователя по telephone_number
    def delete_user(self, telephone_number):
        if not self.check_user_id(telephone_number):
            print('Пользователь с таким user_id не найден')
        else:
            return self.__user_storage.delete_one(telephone_number)

    # # Присвоение user_id
    # def user_id_creator(self) -> int:
    #     a = 0
    #     for users in self.get_all_users:
    #         if users.user_id > a:
    #             a = users.user_id
    #     return a + 1

    # Задание пользовател в диалоговом окне
    def user_creator(self) -> User:
        print("Введите Ваш номер телефона, логин, пароль, электронную почту в строку через ' ;; ': ")
        a = input()
        user = []
        for i in a:
            values = a.split(' ;; ')
            user = User(int(values[0]), values[1], values[2], values[3])
        return user

    # Добавление нового пользователя
    def add_new_user(self, user: User):
        if not (self.check_login_registration(user.login) or self.check_email_registration(user.email)):
            return self.__user_storage.put_one(user)
