from datetime import datetime
from flask import Flask, jsonify, request, json, app
from Application.User.UserManager import *
from Application.User.SQLUserStorage import *
from Application.Message.MessageManager import *
from Application.Message.SQLMessageStorage import *
from Application.Config import *


app = Flask(__name__)


@app.route("/")
def Hello():
    return 'Hello'


@app.route("/users")
def _get_users():
    tmp_user_storage = Path(__file__).parent.joinpath('UserStorage.db')
    __main_user_storage = DatabaseUserStorage(Path(
        tmp_user_storage))
    __manager = UserManager(__main_user_storage)
    __response = [{'t_num': user.t_num, 'login': user.login} for user in __manager.get_all_users]
    return jsonify(__response)


@app.route("/user_registered")
def _user_registered():
    tmp_user_storage = Path(__file__).parent.joinpath('UserStorage.db')
    __main_user_storage = DatabaseUserStorage(Path(tmp_user_storage))
    __manager = UserManager(__main_user_storage)
    if request.args.get('password') == __manager.get_password(request.args.get('t_num')):
        return jsonify({'answer': '1'})
    else:
        return jsonify({'answer': '0'})


# @app.route("/delete_user")
# def _delete_user():
#     t_num = request.args.get('t_num')
#     __main_user_storage = DatabaseUserStorage(Path(
#         '../TextApp/Application/User/UserStorage.db'
#     ))
#     __manager = UserManager(__main_user_storage)
#     __manager.delete_user(t_num)


# @app.route("/add_user", methods=['POST'])
# def _add_user():
#     d = request.json
#     __main_user_storage = DatabaseUserStorage(Path(
#         '../TextApp/Application/User/UserStorage.db'
#     ))
#     __manager = UserManager(__main_user_storage)
#     __manager.add_new_user(User(d.get('t_num'), d.get('login'), d.get('password'), d.get('email')))
#     return {'Ok': True}


@app.route("/messages")
def _get_messages():
    max_time = request.args.get('max_time')
    t_num_1 = request.args.get('t_num_1')
    t_num_2 = request.args.get('t_num_2')
    tmp_message_storage = Path(__file__).parent.joinpath('MessageStorage.db')
    __main_message_storage = DatabaseMessageStorage(Path(
        tmp_message_storage))
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
    tmp_message_storage = Path(__file__).parent.joinpath('MessageStorage.db')
    __main_message_storage = DatabaseMessageStorage(Path(
        tmp_message_storage))
    __manager = MessageManager(__main_message_storage)
    __manager.add_new_message(Message(__data['mg_time'], __data['t_num'], __data['to_t_num'], __data['txt']))
    return {'Ok': True}


if __name__ == '__main__':
    # settings = {'host': "localhost", 'port': 8080}
    app.run(for_server['host'], for_server['port'], debug=True)
