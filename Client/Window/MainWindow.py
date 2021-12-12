from PyQt6 import QtCore
from PySide6.QtCore import QRect
from PySide6.QtWidgets import (
    QWidget, QPushButton, QTextEdit, QTextBrowser, QListWidget, QLineEdit, )
import requests
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
        self.__LineEdit2 = QLineEdit(self)
        self.__LineEdit2.setToolTip('Set t_num of your friend')
        self.__LineEdit2.setGeometry(QRect(250, 510, 181, 31))
        self.__listWidget = QListWidget(self)
        self.__listWidget.setToolTip('List of users')
        self.__listWidget.setGeometry(QRect(540, 30, 161, 371))
        self.__model = None
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(3000)

        self.enter_button.clicked.connect(self.send_message)
        # self.__listWidget.currentItemChanged.connect(self.item_clicked)

    def get_messages(self):
        __main_message_storage = DatabaseMessageStorage(Path(
            '/Client/Message/MessageStorage.db'
        ))
        __manager = MessageManager(__main_message_storage)
        max_time = __manager.max_time()
        t_num_1 = self.__LineEdit1.text()
        t_num_2 = self.__LineEdit2.text()
        try:
            response = requests.get('http://127.0.0.1:5000/messages',
                                    params={'max_time': max_time, 't_num_1': t_num_1, 't_num_2': t_num_2})
        except:
            return

        for message in response:
            print(message)
            # self.print_messages(message)

    # def get_users(self):
    #     return requests.get('http://127.0.0.1:5000/users')

    # def print_messages(self, message):
    #     self.textBrowser.append(message['mg_time'])
    #     self.textBrowser.append(message['t_num'])
    #     self.textBrowser.append(message['txt'])

    def send_message(self):
        mg_time = str(datetime.now())
        t_num = self.__LineEdit1.text()
        to_t_num = self.__LineEdit2.text()
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
