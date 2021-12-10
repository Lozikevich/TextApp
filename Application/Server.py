from flask import Flask, jsonify, request
from Application.User.UserManager import *
from Application.User.SQLUserStorage import *
from Application.Message.MessageManager import *
from Application.Message.SQLMessageStorage import *

if __name__ == '__main__':

    app = Flask(__name__)

    @app.route("/")
    def Hello():
        return 'Hello'

    @app.route("/users")
    def _get_users():
        __main_user_storage = DatabaseUserStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/UserStorage.db'))
        __manager = UserManager(__main_user_storage)
        __response = [user for user in __manager.get_all_users]
        return jsonify(__response)

    @app.route("/user_friends")
    def _user_friends():
        t_num = request.args.get('t_num')
        __main_user_storage = DatabaseUserStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/UserStorage.db'
        ))
        __manager = UserManager(__main_user_storage)
        if __manager.check_t_num_registration(t_num):
            return jsonify({'t_num': '1'})
        else:
            return jsonify({'t_num': '0'})

    @app.route("/delete_user")
    def _delete_user():
        t_num = request.args.get('t_num')
        __main_user_storage = DatabaseUserStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/UserStorage.db'
        ))
        __manager = UserManager(__main_user_storage)
        __manager.delete_user(t_num)

    @app.route("/add_user")
    def _add_user():
        data = request.json
        __main_user_storage = DatabaseUserStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/UserStorage.db'
        ))
        __manager = UserManager(__main_user_storage)
        __manager.add_new_user(User(data['t_num'], data['login'], data['password'], data['email']))

    @app.route("/messages")
    def _get_messages():
        login_1 = request.args.get('login_1')
        login_2 = request.args.get('login_2')
        __main_message_storage = DatabaseMessageStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/MessageStorage.db'))
        __manager = MessageManager(__main_message_storage)
        messages = []
        for message in __manager.get_all_messages:
            if (message.login == login_1 and message.to_login == login_2) or (message.login == login_2 and message.to_login == login_1):
                messages.append(message)
        return jsonify(messages)

    @app.route("/add_message")
    def _add_message():
        data = request.json
        __main_message_storage = DatabaseMessageStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/MessageStorage.db'
        ))
        __manager = MessageManager(__main_message_storage)
        __manager.add_new_message(Message(data['mg_time'], data['login'], data['to_login'], data['txt']))

    app.run()
