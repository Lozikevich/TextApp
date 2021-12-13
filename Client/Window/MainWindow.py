from PyQt6 import QtCore
import requests
from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QTextEdit, QPushButton, QTextBrowser, QLineEdit, QListWidget, QWidget, QLabel
from Client.Message.MessageManager import *
from Client.User.UserManager import *
from Client.Window.Config import *


class MainWindow(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('TextApp')
        self.__textEdit = QTextEdit(self)
        self.__textEdit.setToolTip('Enter your message')
        self.__textEdit.setGeometry(QRect(20, 420, 511, 71))
        self.enter_button = QPushButton('Send', self)
        self.enter_button.setToolTip('Push enter for send your message')
        self.enter_button.setGeometry(QRect(540, 420, 161, 71))
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setToolTip('Window of your messages')
        self.textBrowser.setGeometry(QRect(20, 30, 511, 371))
        self.__LineEdit1 = QLineEdit(self)
        self.__LineEdit1.setToolTip('Set your t_num')
        self.__LineEdit1.setGeometry(QRect(20, 510, 181, 31))
        self.__listWidget = QListWidget(self)
        self.__listWidget.setToolTip('List of users')
        self.__listWidget.setGeometry(QRect(540, 30, 161, 371))
        self.get_users_button = QPushButton('Get users list', self)
        self.get_users_button.setToolTip('Push enter for send your message')
        self.get_users_button.setGeometry(QRect(540, 510, 161, 71))
        # self.__model = None
        self.label = QLabel('Insert your telephone number (0, .., 5)', self)
        self.label.setGeometry(QRect(20, 490, 231, 16))
        self.label1 = QLabel('Insert your password (123)', self)
        self.label1.setGeometry(QRect(20, 540, 181, 16))
        self.autorization_button = QPushButton('Autorization', self)
        self.autorization_button.setToolTip('Push enter for autorization')
        self.autorization_button.setGeometry(QRect(20, 613, 181, 31))
        self.__LineEdit2 = QLineEdit(self)
        self.__LineEdit2.setToolTip('Set your password')
        self.__LineEdit2.setGeometry(QRect(20, 560, 181, 31))
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.__listWidget.itemDoubleClicked.connect(self.change_user)
        self.enter_button.clicked.connect(self.send_message)
        self.get_users_button.clicked.connect(self.get_users)
        self.autorization_button.clicked.connect(self.autorization)

    def autorization(self):
        __t_num = self.__LineEdit1.text()
        password = self.__LineEdit2.text()
        response = requests.get(f'http://{host}:{port}/user_registered', params={'t_num': str(__t_num),
                                                                                 'password': str(password)})
        if response.json()['answer'] == '1':
            self.label.setText('Вы авторизированы')
            global t_num_1
            t_num_1 = self.__LineEdit1.text()
            self.label1.setText('')
        if response.json()['answer'] == '0':
            return self.label.setText('Введен некорректный password или t_num')

    def change_user(self):
        tmp_message_storage = Path(__file__).parent.joinpath('MessageStorage.db')
        self.timer.stop()
        self.textBrowser.setText('')
        # t_num_1 = self.__LineEdit1.text()
        number = self.__listWidget.currentRow()
        response = requests.get(f'http://{host}:{port}/users')
        t_num_2 = str(response.json()[number]['t_num'])
        __main_message_storage = DatabaseMessageStorage(Path(tmp_message_storage))
        __manager = MessageManager(__main_message_storage)
        for message in __manager.get_all_messages():
            if (message.t_num == t_num_1 and message.to_t_num == t_num_2) or \
                        (message.t_num == t_num_2 and message.to_t_num == t_num_1):
                self.print_messages_from_db(message)
        return self.timer.start(10000)

    def get_messages(self):
        tmp_message_storage = Path(__file__).parent.joinpath('MessageStorage.db')
        tmp_user_storage = Path(__file__).parent.joinpath('UserStorage.db')
        __main_message_storage = DatabaseMessageStorage(Path(tmp_message_storage))
        __message_manager = MessageManager(__main_message_storage)
        __main_user_storage = DatabaseUserStorage(Path(tmp_user_storage))
        __user_manager = UserManager(__main_user_storage)
        m_time = datetime.strptime('2021-12-04 17:28:51.100000', "%Y-%m-%d %H:%M:%S.%f")
        for message in __message_manager.get_all_messages():
            if datetime.strptime(message.mg_time, "%Y-%m-%d %H:%M:%S.%f") > m_time:
                m_time = datetime.strptime(message.mg_time, "%Y-%m-%d %H:%M:%S.%f")
        max_time = m_time
        # t_num_1 = self.__LineEdit1.text()
        number = self.__listWidget.currentRow()
        i = -1
        for user in __user_manager.get_all_users:
            i = i + 1
            if i == number:
                t_num_2 = str(user.t_num)
        response = requests.get(f'http://{host}:{port}/messages',
                                params={'max_time': str(max_time), 't_num_1': str(t_num_1), 't_num_2': str(t_num_2)})
        for message in response.json():
            __message_manager.add_new_message(Message(message['mg_time'], message['t_num'], message['to_t_num'],
                                              message['txt']))
            self.print_messages_from_server(message)

    def get_users(self):
        response = requests.get(f'http://{host}:{port}/users')
        tmp_user_storage = Path(__file__).parent.joinpath('UserStorage.db')
        __main_user_storage = DatabaseUserStorage(Path(tmp_user_storage))
        __user_manager = UserManager(__main_user_storage)
        for user in response.json():
            self.__listWidget.addItem(str(user['login']))
            __user_manager.add_new_user(User(user['t_num'], user['login']))

    def print_messages_from_server(self, message):
        tmp_user_storage = Path(__file__).parent.joinpath('UserStorage.db')
        self.textBrowser.append(str(message['mg_time']))
        __main_user_storage = DatabaseUserStorage(Path(tmp_user_storage))
        __user_manager = UserManager(__main_user_storage)
        self.textBrowser.append(__user_manager.get_login(message['t_num']))
        self.textBrowser.append(message['txt'])

    def print_messages_from_db(self, message):
        tmp_user_storage = Path(__file__).parent.joinpath('UserStorage.db')
        self.textBrowser.append(message.mg_time)
        __main_user_storage = DatabaseUserStorage(Path(tmp_user_storage))
        __user_manager = UserManager(__main_user_storage)
        self.textBrowser.append(__user_manager.get_login(message.t_num))
        self.textBrowser.append(message.txt)

    def send_message(self):
        tmp_message_storage = Path(__file__).parent.joinpath('MessageStorage.db')
        __main_message_storage = DatabaseMessageStorage(Path(tmp_message_storage))
        __message_manager = MessageManager(__main_message_storage)
        tmp_user_storage = Path(__file__).parent.joinpath('UserStorage.db')
        __main_user_storage = DatabaseUserStorage(Path(tmp_user_storage))
        __user_manager = UserManager(__main_user_storage)
        mg_time = str(datetime.now())
        # t_num = self.__LineEdit1.text()
        t_num = t_num_1
        number = self.__listWidget.currentRow()
        i = -1
        for user in __user_manager.get_all_users:
            i = i + 1
            if i == number:
                to_t_num = user.t_num
        txt = self.__textEdit.toPlainText()
        new_message = {'mg_time': mg_time, 't_num': t_num, 'to_t_num': to_t_num, 'txt': txt}
        self.print_messages_from_server(new_message)
        __message_manager.add_new_message(Message(new_message['mg_time'], new_message['t_num'], new_message['to_t_num'],
                                                  new_message['txt']))
        requests.post(f'http://{host}:{port}/add_message', json=new_message)
        self.__textEdit.setText('')
