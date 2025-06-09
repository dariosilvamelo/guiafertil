import os
import re

import joblib
import numpy as np
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import QApplication, QDialog, QWidget

from predict_productivity_ui import Ui_predict_productivity
from tools import format_float, message


class Predict_Productivity(QDialog, Ui_predict_productivity):

    def __init__(self):
        super(Predict_Productivity, self).__init__()
        self.setupUi(self)
        self.predictive_attributes = []
        self.predictive_attributes_linear_regression = []

        icon = QIcon('./images/soon/guiafertil.png')
        self.setWindowIcon(icon)
        self.center_window()

        self.last_focused_widget = None
        self.list_network.focusInEvent = self.capture_focus(self.list_network)
        self.list_linear_regression.focusInEvent = self.capture_focus(self.list_linear_regression)
        self.list_random_forest.focusInEvent = self.capture_focus(self.list_random_forest)
        self.list_svm.focusInEvent = self.capture_focus(self.list_svm)

        self.btn_predict_productivity.clicked.connect(lambda: self.predict())

        self.btn_exit.clicked.connect(lambda: self.exit())

    def capture_focus(self, widget):
        def _focus_event(event):
            self.last_focused_widget = widget
            QWidget.focusInEvent(widget, event)
        return _focus_event

    def select_model(self):
        result1 = None
        result2 = None
        result3 = None

        if self.last_focused_widget == self.list_network:
            file = self.list_network.currentItem()
            if file is not None:
                result1 = './model/neural_network/regressors/'+file.text()
                result2 = './model/neural_network/schedulers/x_scaler_' + re.search(r'\d+', file.text()).group()+'.pkl'
                result3 = './model/neural_network/schedulers/y_scaler_' + re.search(r'\d+', file.text()).group()+'.pkl'

        elif self.last_focused_widget ==  self.list_linear_regression:
            file = self.list_linear_regression.currentItem()
            if file is not None:
                result1 = './model/linear_regression/regressors/'+file.text()
                result2 = './model/linear_regression/schedulers/x_scaler_' + re.search(r'\d+', file.text()).group()+'.pkl'
                result3 = './model/linear_regression/schedulers/y_scaler_' + re.search(r'\d+', file.text()).group()+'.pkl'

        elif self.last_focused_widget ==  self.list_random_forest:
            file = self.list_random_forest.currentItem()
            if file is not None:
                result1 = './model/random_forest/regressors/'+file.text()
                result2 = './model/random_forest/schedulers/x_scaler_' + re.search(r'\d+', file.text()).group()+'.pkl'
                result3 = './model/random_forest/schedulers/y_scaler_' + re.search(r'\d+', file.text()).group()+'.pkl'

        elif self.last_focused_widget == self.list_svm:
            file = self.list_svm.currentItem()
            if file is not None:
                result1 = './model/svm/regressors/'+file.text()
                result2 = './model/svm/schedulers/x_scaler_' + re.search(r'\d+', file.text()).group()+'.pkl'
                result3 = './model/svm/schedulers/y_scaler_' + re.search(r'\d+', file.text()).group()+'.pkl'

        return result1, result2, result3

    def predict(self):
        path_regressor, path_scheduler_x, path_scheduler_y = self.select_model()
        if path_regressor is not None and path_scheduler_x is not None and path_scheduler_y is not None:
            regressor = joblib.load(path_regressor)
            x_scaler = joblib.load(path_scheduler_x)
            y_scaler = joblib.load(path_scheduler_y)

            if 'linear_regression' in (path_regressor):
                x = x_scaler.transform(self.predictive_attributes_linear_regression )
            else:
                x = x_scaler.transform(self.predictive_attributes)

            prediction = regressor.predict(x).reshape(-1,1)
            prediction_inverse = y_scaler.inverse_transform(prediction)

            self.lbl_predict_productivity.setText(format_float(prediction_inverse[0][0]))
            font = QFont("Arial", 36)
            font.setBold(True)
            self.lbl_predict_productivity.setFont(font)
            self.lbl_predict_productivity.setAlignment(Qt.AlignCenter)
            self.lbl_predict_productivity.setStyleSheet("color: yellow; background-color: rgb(0, 170, 0);")
        else:
            message('erro', 'Regressor não selecionado.')

    def exit(self): 
        self.close()

    def showEvent(self, event):
        super(Predict_Productivity, self).showEvent(event)
        self.load_files('./model/neural_network/regressors', self.list_network)
        self.load_files('./model/linear_regression/regressors', self.list_linear_regression)
        self.load_files('./model/random_forest/regressors', self.list_random_forest)
        self.load_files('./model/svm/regressors', self.list_svm)
        self.lbl_predict_productivity.setText('0,00')
        font = QFont("Arial", 36)
        font.setBold(True)
        self.lbl_predict_productivity.setFont(font)
        self.lbl_predict_productivity.setAlignment(Qt.AlignCenter)
        self.lbl_predict_productivity.setStyleSheet("color: yellow; background-color: rgb(0, 170, 0);")

    def load_files(self, path, list):
        directory = path
        if directory:
            list.clear()
            try:
                for filename in os.listdir(directory):
                    list.addItem(filename)
            except Exception as e:
                list.addItem(f"Erro: {str(e)}")

    def center_window(self):
        window_geometry = self.frameGeometry()
        screens = QApplication.screens()
        if screens:
            primary_screen = screens[0]
            screen_geometry = primary_screen.availableGeometry().center()
            window_geometry.moveCenter(screen_geometry)
            self.move(window_geometry.topLeft())
