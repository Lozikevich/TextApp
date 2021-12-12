from datetime import datetime
# from Application.Message.MessageManager import *
import requests as requests

from Application.Message.SQLMessageStorage import *
import requests

from Client.Message.MessageManager import MessageManager
from Client.Message.SQLMessageStorage import *

# if __name__ == '__main__':
#     __main_user_storage = DatabaseMessageStorage(Path(
#         'C:/Users/ADMIN/PycharmProjects/TextApp/Client/Message/MessageStorage.db'))
#     __manager = MessageManager(__main_user_storage)
#     max_time = datetime.strptime('2021-12-04 17:28:51.100000', "%Y-%m-%d %H:%M:%S.%f")
#     for message in __manager.get_all_messages():
#         if datetime.strptime(message.mg_time, "%Y-%m-%d %H:%M:%S.%f") > max_time:
#             max_time = datetime.strptime(message.mg_time, "%Y-%m-%d %H:%M:%S.%f")
#     response = requests.get('http://127.0.0.1:5000/messages',
#                             params={'max_time': str(max_time), 't_num_1': '1', 't_num_2': '2'})
#     for message in response.json():
#         print(message)

if __name__ == '__main__':
    __main_user_storage = DatabaseMessageStorage(Path(
        'C:/Users/ADMIN/PycharmProjects/TextApp/Application/Message/MessageStorage.db'))
    __manager = MessageManager(__main_user_storage)
    __manager.add_new_message(Message(str(datetime.now()), '1', '3', 'txt'))
    print('13254')
    __manager.add_new_message(Message(str(datetime.now()), '3', '1', 'txt'))
    print('13254')
    __manager.add_new_message(Message(str(datetime.now()), '1', '3', 'txt'))
    print('13254')
    __manager.add_new_message(Message(str(datetime.now()), '3', '1', 'txt'))
    print('13254')
    __manager.add_new_message(Message(str(datetime.now()), '1', '3', 'txt'))
    print('13254')
    __manager.add_new_message(Message(str(datetime.now()), '3', '1', 'txt'))
    print('13254')
    __manager.add_new_message(Message(str(datetime.now()), '1', '3', 'txt'))
    print('13254')