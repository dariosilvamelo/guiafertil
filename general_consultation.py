import os
import sqlite3
import sys

import pandas as pd
from PySide6 import QtCore
from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog, QTableWidgetItem

from general_consultation_ui import Ui_general_consultation
from tools import message


class General_consultation(QDialog, Ui_general_consultation):

    def __init__(self,  name_data_base):
        super(General_consultation, self).__init__()
        self.setupUi(self)
        icon = QIcon('./images/soon/guiafertil.png')
        self.setWindowIcon(icon)
        self.center_window()
        self.data_base = name_data_base
        self.sql=''
        self.confirm_registration = False
        self.edt_consult.textChanged.connect(lambda: self.query())
        self.btn_confirm.clicked.connect(lambda: self.confirm())
        self.btn_exit.clicked.connect(lambda: self.exit())

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def confirm(self):
        self.table_consult.setFocus()
        self.confirm_registration = True
        self.close()
        
    def exit(self):
        self.confirm_registration = False
        self.close()

    def query(self):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            name = self.edt_consult.text() + '%'
            self.sql = """SELECT P.code_producer, P.name_producer
                          FROM PRODUCER P
                          WHERE P.name_producer LIKE ?
                          ORDER BY P.name_producer"""
            cursor.execute(self.sql, (name,))
            result = cursor.fetchall()
            self.table_assembly(result)
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def query_code(self, code):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            cursor.execute(self.sql, (code,))
            result = cursor.fetchall()
            return result
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()

    def table_assembly(self, result):
        if result is not None:
            self.table_consult.setAlternatingRowColors(True)
            self.table_consult.clearContents()

            self.table_consult.setRowCount(len(result))

            for row_index, row_text in enumerate(result):
                for column_index, data in enumerate(row_text):
                    item = QTableWidgetItem(str(data))
                    item.setTextAlignment(Qt.AlignCenter)
                    self.table_consult.setItem(row_index, column_index, item)

        self.table_consult.setColumnWidth(0, 50)
        self.table_consult.setColumnWidth(1, 200)

    def showEvent(self, event):
        super(General_consultation, self).showEvent(event)
        self.edt_consult.clear()
        self.edt_consult.setFocus()
        self.query()

    def center_window(self):
        window_geometry = self.frameGeometry()
        screens = QApplication.screens()
        if screens:
            primary_screen = screens[0]
            screen_geometry = primary_screen.availableGeometry().center()
            window_geometry.moveCenter(screen_geometry)
            self.move(window_geometry.topLeft())        