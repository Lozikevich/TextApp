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


    @app.route("/friends")
    def _get_friends_of_user():
        t_num = request.args.get('t_num')
        __main_user_storage = DatabaseUserStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/UserStorage.db'
        ))
        __manager = UserManager(__main_user_storage)
        if __manager.check_t_num_registration(t_num):
            return jsonify({'t_num': '1'})
        else:
            return jsonify({'t_num': '0'})


    @app.route("/add_user")
    def _add_user():
        data = request.json
        __main_user_storage = DatabaseUserStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Application/UserStorage.db'
        ))
        __manager = UserManager(__main_user_storage)
        __manager.add_new_user(User(data['t_num'], data['login'], data['password'], data['email']))


    app.run()
