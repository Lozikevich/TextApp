from PySide6.QtCore import Slot, QRect

from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from typing import Iterable
from PySide6.QtWidgets import (
    QLabel, QWidget, QPushButton, QLineEdit,
)

from RegistrationDialog import *


class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('TextApp')
        self.__enter_button = QPushButton('Enter', self)
        self.__enter_button.setToolTip('Push enter if you are registered in TextApp')
        self.__enter_button.setGeometry(QRect(100, 200, 75, 24))
        self.__registration_button = QPushButton('Registration', self)
        self.__registration_button.setToolTip('Push registration if you are not registered in TextApp')
        self.__registration_button.setGeometry(QRect(210, 200, 75, 24))
        self.__login_label = QLabel('Enter Your login', self)
        self.__login_label.setGeometry(QRect(180, 80, 150, 16))
        self.__login_edit = QLineEdit(self)
        self.__login_edit.setGeometry(QRect(140, 100, 113, 21))
        self.__password_label = QLabel('Enter Your password', self)
        self.__password_label.setGeometry(QRect(170, 130, 150, 16))
        self.__password_edit = QLineEdit(self)
        self.__password_edit.setGeometry(QRect(140, 150, 113, 21))
        self.__model = None
        self.__registration_button.clicked.connect(self.__open_registration_window)

    @Slot()
    def __open_registration_window(self):
        dialog = RegistrationDialog(self)

        if dialog.exec_() == RegistrationDialog.Accepted:
            row = self.__model.rowCount()

            self.__model.insertRow(row)
            self.__model.setData(self.__model.index(row, 0), dialog.entry.telephone_number)
            self.__model.setData(self.__model.index(row, 1), dialog.entry.login)
            self.__model.setData(self.__model.index(row, 2), dialog.entry.password)
            self.__model.setData(self.__model.index(row, 3), dialog.entry.email)
            self.__model.submitAll()




