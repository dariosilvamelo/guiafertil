import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
                               QMainWindow, QMessageBox, QPushButton,
                               QTextEdit)

from data_base_login import DataBaseLogin
from login_ui import Ui_win_login
from tools import message


class Login(QMainWindow,Ui_win_login):
    def __init__(self):
        super(Login,self).__init__()
        self.setupUi(self)
        icon = QIcon('./images/soon/guiafertil.png')
        self.setWindowIcon(icon)
        self.login_data = DataBaseLogin('./database/database.db')
        self.edt_user.setFocus()
