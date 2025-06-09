# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_win.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)
import icones_rc

class Ui_win_login(object):
    def setupUi(self, win_login):
        if not win_login.objectName():
            win_login.setObjectName(u"win_login")
        win_login.resize(481, 364)
        win_login.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.centralwidget = QWidget(win_login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QPushButton {\n"
"width: 135px;\n"
"height: 30px;\n"
"background-color: rgb(0, 170, 0);\n"
"font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: rgb(255, 170, 0);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frm_logo = QFrame(self.centralwidget)
        self.frm_logo.setObjectName(u"frm_logo")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frm_logo.sizePolicy().hasHeightForWidth())
        self.frm_logo.setSizePolicy(sizePolicy)
        self.frm_logo.setFrameShape(QFrame.StyledPanel)
        self.frm_logo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_logo)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_logo_description = QLabel(self.frm_logo)
        self.lbl_logo_description.setObjectName(u"lbl_logo_description")
        self.lbl_logo_description.setPixmap(QPixmap(u":/logotipo/imagens/logo/Logo_GuiaFertil-Pequeno.png"))
        self.lbl_logo_description.setScaledContents(True)

        self.verticalLayout_4.addWidget(self.lbl_logo_description)

        self.text_goal = QTextEdit(self.frm_logo)
        self.text_goal.setObjectName(u"text_goal")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setBold(True)
        self.text_goal.setFont(font)
        self.text_goal.setReadOnly(True)

        self.verticalLayout_4.addWidget(self.text_goal)


        self.horizontalLayout.addWidget(self.frm_logo)

        self.frm_login = QFrame(self.centralwidget)
        self.frm_login.setObjectName(u"frm_login")
        self.frm_login.setMinimumSize(QSize(0, 0))
        self.frm_login.setFrameShape(QFrame.StyledPanel)
        self.frm_login.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frm_login)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frm_user = QFrame(self.frm_login)
        self.frm_user.setObjectName(u"frm_user")
        self.frm_user.setFrameShape(QFrame.StyledPanel)
        self.frm_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frm_user)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_user = QLabel(self.frm_user)
        self.lbl_user.setObjectName(u"lbl_user")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_user.sizePolicy().hasHeightForWidth())
        self.lbl_user.setSizePolicy(sizePolicy1)
        self.lbl_user.setScaledContents(False)
        self.lbl_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lbl_user)

        self.edt_user = QLineEdit(self.frm_user)
        self.edt_user.setObjectName(u"edt_user")
        self.edt_user.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.edt_user)


        self.verticalLayout_3.addWidget(self.frm_user)

        self.frm_password = QFrame(self.frm_login)
        self.frm_password.setObjectName(u"frm_password")
        self.frm_password.setFrameShape(QFrame.StyledPanel)
        self.frm_password.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_password)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lbl_password = QLabel(self.frm_password)
        self.lbl_password.setObjectName(u"lbl_password")
        sizePolicy1.setHeightForWidth(self.lbl_password.sizePolicy().hasHeightForWidth())
        self.lbl_password.setSizePolicy(sizePolicy1)
        self.lbl_password.setScaledContents(False)
        self.lbl_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.lbl_password)

        self.edt_password = QLineEdit(self.frm_password)
        self.edt_password.setObjectName(u"edt_password")
        self.edt_password.setEchoMode(QLineEdit.Password)
        self.edt_password.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.edt_password)


        self.verticalLayout_3.addWidget(self.frm_password)

        self.btn_login = QPushButton(self.frm_login)
        self.btn_login.setObjectName(u"btn_login")

        self.verticalLayout_3.addWidget(self.btn_login)


        self.horizontalLayout.addWidget(self.frm_login)

        win_login.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.edt_user, self.edt_password)
        QWidget.setTabOrder(self.edt_password, self.btn_login)
        QWidget.setTabOrder(self.btn_login, self.text_goal)

        self.retranslateUi(win_login)

        QMetaObject.connectSlotsByName(win_login)
    # setupUi

    def retranslateUi(self, win_login):
        win_login.setWindowTitle(QCoreApplication.translate("win_login", u"Login", None))
        self.lbl_logo_description.setText("")
        self.text_goal.setHtml(QCoreApplication.translate("win_login", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Times New Roman'; font-size:8.25pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'MS Shell Dlg 2'; font-weight:400;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400; color:#000000;\"><br /></p>\n"
"<p al"
                        "ign=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt; font-weight:400; color:#000000;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent"
                        ":0px;\"><span style=\" font-family:'Calibri,sans-serif'; font-size:11pt; font-weight:400;\">An\u00e1lise Explorat\u00f3ria e Predi\u00e7\u00e3o do Limiar de Produtividade na Cultura da Soja com T\u00e9cnicas de Intelig\u00eancia Artificial Baseadas em Atributos Qu\u00edmicos do Solo, Clima e Aduba\u00e7\u00f5es</span></p></body></html>", None))
        self.lbl_user.setText(QCoreApplication.translate("win_login", u"<html><head/><body><p align=\"center\"><img src=\":/login/images/login/user.png\"/></p></body></html>", None))
        self.edt_user.setText("")
        self.edt_user.setPlaceholderText(QCoreApplication.translate("win_login", u"Informe o usu\u00e1rio", None))
        self.lbl_password.setText(QCoreApplication.translate("win_login", u"<html><head/><body><p align=\"center\"><img src=\":/login/images/login/password.png\"/></p></body></html>", None))
        self.edt_password.setPlaceholderText(QCoreApplication.translate("win_login", u"Informe a senha", None))
        self.btn_login.setText(QCoreApplication.translate("win_login", u"Login", None))
#if QT_CONFIG(shortcut)
        self.btn_login.setShortcut(QCoreApplication.translate("win_login", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

