from enum import Enum
list_of_users = {}


class Status:
    online = 1
    offline = 0


class User:
    def __init__(self, user_id: int, login: str, password: str, date_of_birth: str, country: str, email: str,
                 status: int):
        self.__user_id = user_id
        self.__login = login
        self.__password = password
        self.__date_of_birth = date_of_birth
        self.__country = country
        self.__email = email
        self.__status = status

    @property
    def user_id(self) -> int:
        return self.__user_id

    @property
    def login(self) -> str:
        return self.__login

    @property
    def password(self) -> str:
        return self.__password

    @property
    def date_of_birth(self) -> str:
        return self.__date_of_birth

    @property
    def country(self) -> str:
        return self.__country

    @property
    def email(self) -> str:
        return self.__email

    @property
    def status(self) -> int:
        return self.__status

    @login.setter
    def login(self, login: str):
        self.__login = login

    @password.setter
    def password(self, password: str):
        self.__password = password

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str):
        self.__date_of_birth = date_of_birth

    @country.setter
    def country(self, country: str):
        self.__country = country

    @email.setter
    def email(self, email: str):
        self.__email = email

    @status.setter
    def status(self, status: str):
        self.__status = status

    @staticmethod
    def list_of_users():
        return list_of_users.values()

    @staticmethod
    def add_new_user(login):
        list_of_users[login.user_id] = login

    @staticmethod
    def delete_user(login):
        del list_of_users[login]

    @staticmethod
    def get_user(login):
        return login

    def __repr__(self) -> str:
        return f'User(user_id={self.user_id}, login={self.login}, country={self.country}, email={self.email})'