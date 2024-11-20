import os

import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QDialog

from predict_productivity_ui import Ui_predict_productivity
from tools import format_float, message


class Predict_Productivity(QDialog, Ui_predict_productivity):

    def __init__(self, predict_productivity):
        super(Predict_Productivity, self).__init__()
        self.setupUi(self)
        self.register = predict_productivity
        self.predictive_attributes = []
        icon = QIcon('./images/soon/guiafertil.png')
        self.setWindowIcon(icon)
        self.center_window()
        self.btn_predict_productivity.clicked.connect(lambda: self.predict_productivity())
        self.btn_exit.clicked.connect(lambda: self.exit())

    def predict_productivity(self):
        file = self.list_network.currentItem()
        if file is not None:
            selected_regressor = './network/saved_regressors/'+file.text()

            base = np.array(self.predictive_attributes)

            self.lbl_predict_productivity.setText('')

            prediction = self.register.neural_network.predict_productivity(base, selected_regressor)

            self.lbl_predict_productivity.setText(format_float(prediction[0][0]))
            font = QFont("Arial", 36) 
            font.setBold(True)
            self.lbl_predict_productivity.setFont(font)
            self.lbl_predict_productivity.setAlignment(Qt.AlignCenter)
            self.lbl_predict_productivity.setStyleSheet("color: yellow; background-color: rgb(0, 170, 0);")
        else:
            message('erro', 'Nenhum regressor selecionado.')  

    def exit(self): 
        self.close()

    def showEvent(self, event):
        super(Predict_Productivity, self).showEvent(event)
        self.load_files()
        self.lbl_predict_productivity.setText('0,00')
        font = QFont("Arial", 36)
        font.setBold(True)
        self.lbl_predict_productivity.setFont(font)
        self.lbl_predict_productivity.setAlignment(Qt.AlignCenter)
        self.lbl_predict_productivity.setStyleSheet("color: yellow; background-color: rgb(0, 170, 0);")

    def load_files(self):
        directory = './network/saved_regressors'
        if directory:
            self.list_network.clear()
            try:
                for filename in os.listdir(directory):
                    self.list_network.addItem(filename)
            except Exception as e:
                self.list_network.addItem(f"Erro: {str(e)}")

    def center_window(self):
        window_geometry = self.frameGeometry()
        screens = QApplication.screens()
        if screens:
            primary_screen = screens[0]
            screen_geometry = primary_screen.availableGeometry().center()
            window_geometry.moveCenter(screen_geometry)
            self.move(window_geometry.topLeft())
