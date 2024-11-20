# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'predict_productivity_win.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QListWidget, QListWidgetItem, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)
import icones_rc

class Ui_predict_productivity(object):
    def setupUi(self, predict_productivity):
        if not predict_productivity.objectName():
            predict_productivity.setObjectName(u"predict_productivity")
        predict_productivity.resize(358, 279)
        predict_productivity.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(predict_productivity)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_list_network = QLabel(predict_productivity)
        self.lbl_list_network.setObjectName(u"lbl_list_network")

        self.verticalLayout.addWidget(self.lbl_list_network)

        self.list_network = QListWidget(predict_productivity)
        self.list_network.setObjectName(u"list_network")

        self.verticalLayout.addWidget(self.list_network)

        self.lbl_predict_productivity = QLabel(predict_productivity)
        self.lbl_predict_productivity.setObjectName(u"lbl_predict_productivity")
        self.lbl_predict_productivity.setMinimumSize(QSize(340, 57))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.lbl_predict_productivity.setFont(font)
        self.lbl_predict_productivity.setStyleSheet(u"background-color: rgb(0, 170, 0);")

        self.verticalLayout.addWidget(self.lbl_predict_productivity)

        self.frame = QFrame(predict_productivity)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_predict_productivity = QPushButton(self.frame)
        self.btn_predict_productivity.setObjectName(u"btn_predict_productivity")
        font1 = QFont()
        font1.setBold(True)
        self.btn_predict_productivity.setFont(font1)
        icon = QIcon()
        icon.addFile(u":/buttons/images/button/AI.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_predict_productivity.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_predict_productivity)

        self.btn_exit = QPushButton(self.frame)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/buttons/images/button/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(predict_productivity)

        QMetaObject.connectSlotsByName(predict_productivity)
    # setupUi

    def retranslateUi(self, predict_productivity):
        predict_productivity.setWindowTitle(QCoreApplication.translate("predict_productivity", u"Predi\u00e7\u00e3o da produtividade", None))
        self.lbl_list_network.setText(QCoreApplication.translate("predict_productivity", u"<html><head/><body><p><span style=\" font-weight:600;\">Lista de regressores salvos:</span></p></body></html>", None))
        self.lbl_predict_productivity.setText(QCoreApplication.translate("predict_productivity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ffff00;\">0,00</span></p></body></html>", None))
        self.btn_predict_productivity.setText(QCoreApplication.translate("predict_productivity", u"Executar presi\u00e7\u00e3o da produtividade", None))
        self.btn_exit.setText(QCoreApplication.translate("predict_productivity", u"Sair", None))
    # retranslateUi

