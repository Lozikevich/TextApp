from datetime import datetime
from flask import Flask, jsonify, request, json
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
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/User/UserStorage.db'))
        __manager = UserManager(__main_user_storage)
        __response = [user for user in __manager.get_all_users]
        return jsonify(__response)


    @app.route("/user_friends")
    def _user_friends():
        t_num = request.args.get('t_num')
        __main_user_storage = DatabaseUserStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/User/UserStorage.db'
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
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/User/UserStorage.db'
        ))
        __manager = UserManager(__main_user_storage)
        __manager.delete_user(t_num)


    @app.route("/add_user", methods=['POST'])
    def _add_user():
        d = request.json
        print(d.get('t_num'))
        __main_user_storage = DatabaseUserStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/User/UserStorage.db'
        ))
        __manager = UserManager(__main_user_storage)
        __manager.add_new_user(User(d.get('t_num'), d.get('login'), d.get('password'), d.get('email')))
        return {'Ok': True}


    @app.route("/messages")
    def _get_messages():
        max_time = request.args.get('max_time')
        t_num_1 = request.args.get('t_num_1')
        t_num_2 = request.args.get('t_num_2')
        __main_message_storage = DatabaseMessageStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/Message/MessageStorage.db'))
        __manager = MessageManager(__main_message_storage)
        messages = []
        for message in __manager.get_all_messages():
            if (datetime.strptime(message.mg_time, "%Y-%m-%d %H:%M:%S.%f") >
                    datetime.strptime(max_time, "%Y-%m-%d %H:%M:%S.%f")):
                if (message.t_num == t_num_1 and message.to_t_num == t_num_2) or \
                        (message.t_num == t_num_2 and message.to_t_num == t_num_1):
                    messages.append(message)
        return jsonify(messages)


    @app.route("/add_message", methods=['POST'])
    def _add_message():
        __data = request.json
        __main_message_storage = DatabaseMessageStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/Message/MessageStorage.db'
        ))
        __manager = MessageManager(__main_message_storage)
        __manager.add_new_message(Message(__data['mg_time'], __data['t_num'], __data['to_t_num'], __data['txt']))
        return {'Ok': True}


    app.run()
