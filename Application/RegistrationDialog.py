from dataclasses import dataclass

from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QDialog, QLabel, QLineEdit, QDialogButtonBox


@dataclass
class Entry:
    telephone_number: int
    login: str
    password: str
    email: str


class RegistrationDialog(QDialog):
    def __init__(self, parent=None):
        super(RegistrationDialog, self).__init__(parent)

        self.entry = None

        self.setWindowTitle('Add new registration data')

        self._telephone_number_label = QLabel('telephone number', self)
        self._telephone_number_edit = QLineEdit(self)

        self._login_label = QLabel('login', self)
        self._login_edit = QLineEdit(self)

        self._password_label = QLabel('password', self)
        self._password_edit = QLineEdit(self)

        self._email_label = QLabel('email', self)
        self._email_edit = QLineEdit(self)

        self._button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel,
            parent=self
        )

        grid_layout = QGridLayout()
        grid_layout.addWidget(self._telephone_number_label, 0, 0)
        grid_layout.addWidget(self._telephone_number_edit, 0, 1)
        grid_layout.addWidget(self._login_label, 1, 0)
        grid_layout.addWidget(self._login_edit, 1, 1)
        grid_layout.addWidget(self._password_label, 2, 0)
        grid_layout.addWidget(self._password_edit, 2, 1)
        grid_layout.addWidget(self._email_label, 3, 0)
        grid_layout.addWidget(self._email_edit, 3, 1)

        layout = QVBoxLayout()
        layout.addLayout(grid_layout)
        layout.addWidget(self._button_box)

        self.setLayout(layout)

        self._button_box.accepted.connect(self.accept)
        self._button_box.rejected.connect(self.reject)

    def accept(self):
        self.entry = Entry(
            self._telephone_number_edit.text(),
            self._login_edit.text(),
            self._password_edit.text(),
            self._email_edit.text()
        )

        super().accept()
