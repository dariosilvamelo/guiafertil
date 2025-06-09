# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'predict_productivity_win.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QListWidget, QListWidgetItem,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import icones_rc

class Ui_predict_productivity(object):
    def setupUi(self, predict_productivity):
        if not predict_productivity.objectName():
            predict_productivity.setObjectName(u"predict_productivity")
        predict_productivity.resize(675, 319)
        predict_productivity.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(predict_productivity)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_list_network = QLabel(predict_productivity)
        self.lbl_list_network.setObjectName(u"lbl_list_network")

        self.verticalLayout.addWidget(self.lbl_list_network)

        self.frame_2 = QFrame(predict_productivity)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.list_network = QListWidget(self.frame_2)
        self.list_network.setObjectName(u"list_network")

        self.gridLayout.addWidget(self.list_network, 0, 0, 1, 1)

        self.list_linear_regression = QListWidget(self.frame_2)
        self.list_linear_regression.setObjectName(u"list_linear_regression")

        self.gridLayout.addWidget(self.list_linear_regression, 0, 1, 1, 1)

        self.list_svm = QListWidget(self.frame_2)
        self.list_svm.setObjectName(u"list_svm")

        self.gridLayout.addWidget(self.list_svm, 0, 2, 1, 1)

        self.list_random_forest = QListWidget(self.frame_2)
        self.list_random_forest.setObjectName(u"list_random_forest")

        self.gridLayout.addWidget(self.list_random_forest, 0, 3, 1, 1)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 2, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

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
        self.btn_predict_productivity.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/buttons/images/button/AI.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_predict_productivity.setIcon(icon)

        self.horizontalLayout.addWidget(self.btn_predict_productivity)

        self.btn_exit = QPushButton(self.frame)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setFont(font1)
        self.btn_exit.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/buttons/images/button/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_exit.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_exit)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(predict_productivity)

        QMetaObject.connectSlotsByName(predict_productivity)
    # setupUi

    def retranslateUi(self, predict_productivity):
        predict_productivity.setWindowTitle(QCoreApplication.translate("predict_productivity", u"Predi\u00e7\u00e3o da produtividade", None))
        self.lbl_list_network.setText(QCoreApplication.translate("predict_productivity", u"<html><head/><body><p><span style=\" font-weight:600;\">Lista de regressores salvos da rede neural:</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("predict_productivity", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Rede Neural</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("predict_productivity", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Regress\u00e3o Linear</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("predict_productivity", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">SVM</span></p></body></html>", None))
        self.label_4.setText(QCoreApplication.translate("predict_productivity", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Random Forest</span></p></body></html>", None))
        self.lbl_predict_productivity.setText(QCoreApplication.translate("predict_productivity", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt; color:#ffff00;\">0,00</span></p></body></html>", None))
        self.btn_predict_productivity.setText(QCoreApplication.translate("predict_productivity", u"Predi\u00e7\u00e3o (Return)", None))
#if QT_CONFIG(shortcut)
        self.btn_predict_productivity.setShortcut(QCoreApplication.translate("predict_productivity", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_exit.setText(QCoreApplication.translate("predict_productivity", u"Sair (Esc)", None))
#if QT_CONFIG(shortcut)
        self.btn_exit.setShortcut(QCoreApplication.translate("predict_productivity", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

