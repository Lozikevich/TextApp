from PyQt6 import QtCore
import requests
from PyQt6.QtCore import QRect
from PyQt6.QtWidgets import QTextEdit, QPushButton, QTextBrowser, QLineEdit, QListWidget, QWidget
from Client.Message.MessageManager import *


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
        self.__model = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.__listWidget.itemDoubleClicked.connect(self.change_user)
        self.enter_button.clicked.connect(self.send_message)
        self.get_users_button.clicked.connect(self.get_users)

    def change_user(self):
        self.timer.stop()
        self.textBrowser.setText('')
        t_num_1 = self.__LineEdit1.text()
        number = self.__listWidget.currentRow()
        response = requests.get('http://127.0.0.1:5000/users')
        t_num_2 = str(response.json()[number]['t_num'])
        __main_message_storage = DatabaseMessageStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Client/Message/MessageStorage.db'
        ))
        __manager = MessageManager(__main_message_storage)
        for message in __manager.get_all_messages():
            if (message.t_num == t_num_1 and message.to_t_num == t_num_2) or \
                        (message.t_num == t_num_2 and message.to_t_num == t_num_1):
                self.print_messages_from_db(message)
        return self.timer.start(3000)

    def get_messages(self):
        __main_message_storage = DatabaseMessageStorage(Path(
            'C:/Users/ADMIN/PycharmProjects/TextApp/Client/Message/MessageStorage.db'
        ))
        __manager = MessageManager(__main_message_storage)
        m_time = datetime.strptime('2021-12-04 17:28:51.100000', "%Y-%m-%d %H:%M:%S.%f")
        for message in __manager.get_all_messages():
            if datetime.strptime(message.mg_time, "%Y-%m-%d %H:%M:%S.%f") > m_time:
                m_time = datetime.strptime(message.mg_time, "%Y-%m-%d %H:%M:%S.%f")
        max_time = m_time
        t_num_1 = self.__LineEdit1.text()
        number = self.__listWidget.currentRow()
        response = requests.get('http://127.0.0.1:5000/users')
        t_num_2 = str(response.json()[number]['t_num'])
        response = requests.get('http://127.0.0.1:5000/messages',
                                params={'max_time': str(max_time), 't_num_1': str(t_num_1), 't_num_2': str(t_num_2)})
        for message in response.json():
            __manager.add_new_message(Message(message['mg_time'], message['t_num'], message['to_t_num'],
                                              message['txt']))
            self.print_messages_from_server(message)

    def get_users(self):
        response = requests.get('http://127.0.0.1:5000/users')
        for user in response.json():
            self.__listWidget.addItem(str(user['login']))

    def print_messages_from_server(self, message):
        self.textBrowser.append(str(message['mg_time']))
        self.textBrowser.append(message['t_num'])
        self.textBrowser.append(message['txt'])

    def print_messages_from_db(self, message):
        self.textBrowser.append(message.mg_time)
        self.textBrowser.append(message.t_num)
        self.textBrowser.append(message.txt)

    def send_message(self):
        mg_time = str(datetime.now())
        t_num = self.__LineEdit1.text()
        number = self.__listWidget.currentRow()
        response = requests.get('http://127.0.0.1:5000/users')
        to_t_num = str(response.json()[number]['t_num'])
        txt = self.__textEdit.toPlainText()
        new_message = {'mg_time': mg_time, 't_num': t_num, 'to_t_num': to_t_num, 'txt': txt}
        try:
            response = requests.post('http://127.0.0.1:5000/add_message', json=new_message)
        except:
            # TODO server недоступен

            return

        if response.status_code != 200:
            # TODO сообщить об ошибке

            self.__textEdit.setText('')
