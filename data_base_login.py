import os
import sqlite3

import pandas as pd

from tools import message


class DataBaseLogin:

    def __init__(self, name_data_base):
        self.data_base = name_data_base

    def open_data_base(self):
        self.connection_data_base = sqlite3.connect(self.data_base)

    def close_data_base(self):
        self.connection_data_base.close()

    def authenticate_user(self, name_user,password_user):
        self.open_data_base()
        try:
            cursor = self.connection_data_base.cursor()
            sql = """SELECT code_user, name_user, authentication_name_user FROM user 
                     WHERE authentication_name_user = ? 
                     and password_user = ?"""
            cursor.execute(sql, (name_user,password_user,))
            user = cursor.fetchall()
            return user
        except Exception as e:
            message('erro', str(e))
        finally:
            self.close_data_base()
