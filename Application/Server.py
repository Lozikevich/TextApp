from flask import Flask, abort, json, jsonify
from typing import Iterable
from requests import request
import math
from User.UserManager import *
from User.SQLUserStorage import *
from Message.MessageManager import *
from Message.SQLMessageStorage import *


if __name__ == '__main__':

    app = Flask(__name__)


    @app.route("/")
    def Hello():
        return 'Hello'


    # @app.route("/put_message", methods=['POST'])
    # def _put_message():
    #     data = request.json
    #     if isinstance(data, dict):
    #         return abort(400)
    #
    #     if 'login' not in data or not isinstance(data['login'], str) or len(data['login']) == 0:
    #         return abort(400)
    #
    #     if 'to_login' not in data or not isinstance(data['to_login'], str) or len(data['to_login']) == 0:
    #         return abort(400)
    #
    #     if 'txt' not in data or not isinstance(data['txt'], str) or len(data['txt']) == 0 \
    #             or len(data['txt']) > 1000:
    #         return abort(400)
    #
    #     main_message_storage = DatabaseMessageStorage(Path('Application/MessageStorage.db'))
    #     manager = MessageManager(main_message_storage)
    #     manager.add_new_message(Message(data['mg_time'], data['login'], data['to_login'], data['txt']))
    #
    #     return {'ok': True}
    #
    #
    # @app.route("/messages")
    # def _get_messages():
    #     messages = []
    #     main_message_storage = DatabaseMessageStorage(Path('Application/MessageStorage.db'))
    #     manager = MessageManager(main_message_storage)
    #     for msg in manager.get_all_messages():
    #         messages.append(msg)
    #     return {'messages'}


    @app.route("/put_user", methods=['POST'])
    def _put_user():
        data = request.json
        if isinstance(data, dict):
            return abort(400)

        if 'telephone_number' not in data or not data['telephone_number'].isdigit():
            return abort(400)

        if 'login' not in data or not isinstance(data['login'], str) or len(data['login']) == 0:
            return abort(400)

        if 'password' not in data or not isinstance(data['password'], str) or len(data['password']) == 0:
            return abort(400)

        if 'email' not in data or not isinstance(data['email'], str) or len(data['email']) == 0:
            return abort(400)

        main_user_storage = DatabaseUserStorage(Path('Application/UserStorage.db'))
        manager = UserManager(main_user_storage)
        manager.add_new_user(User(data['telephone_number'], data['login'], data['password'], data['email']))

        return {'ok': True}


    @app.route("/users")
    def _get_users():
        main_user_storage = DatabaseUserStorage(Path('Application/UserStorage.db'))
        manager = UserManager(main_user_storage)
        response = {}
        i = 0
        for user in manager.get_all_users:
            i = i + 1
            response = response + {str(i): user}
        return response

    app.run()
