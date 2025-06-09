# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'general_consultation_win.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QDialog, QFrame,
    QHBoxLayout, QHeaderView, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import icones_rc

class Ui_general_consultation(object):
    def setupUi(self, general_consultation):
        if not general_consultation.objectName():
            general_consultation.setObjectName(u"general_consultation")
        general_consultation.setWindowModality(Qt.ApplicationModal)
        general_consultation.resize(658, 360)
        general_consultation.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout = QVBoxLayout(general_consultation)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frm_edt_consult = QFrame(general_consultation)
        self.frm_edt_consult.setObjectName(u"frm_edt_consult")
        self.frm_edt_consult.setFrameShape(QFrame.StyledPanel)
        self.frm_edt_consult.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frm_edt_consult)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.edt_consult = QLineEdit(self.frm_edt_consult)
        self.edt_consult.setObjectName(u"edt_consult")

        self.verticalLayout_4.addWidget(self.edt_consult)


        self.verticalLayout.addWidget(self.frm_edt_consult)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frm_table = QFrame(general_consultation)
        self.frm_table.setObjectName(u"frm_table")
        self.frm_table.setFrameShape(QFrame.StyledPanel)
        self.frm_table.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frm_table)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.table_consult = QTableWidget(self.frm_table)
        if (self.table_consult.columnCount() < 2):
            self.table_consult.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_consult.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_consult.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.table_consult.setObjectName(u"table_consult")
        self.table_consult.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_consult.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_3.addWidget(self.table_consult)


        self.horizontalLayout.addWidget(self.frm_table)

        self.frm_menu = QFrame(general_consultation)
        self.frm_menu.setObjectName(u"frm_menu")
        self.frm_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frm_menu)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_confirm = QPushButton(self.frm_menu)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/buttons/images/button/Save-Update.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_confirm.setIcon(icon)

        self.verticalLayout_5.addWidget(self.btn_confirm)

        self.btn_exit = QPushButton(self.frm_menu)
        self.btn_exit.setObjectName(u"btn_exit")
        self.btn_exit.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/buttons/images/button/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_exit.setIcon(icon1)

        self.verticalLayout_5.addWidget(self.btn_exit)

        self.spacer_menu = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.spacer_menu)


        self.horizontalLayout.addWidget(self.frm_menu)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(general_consultation)

        QMetaObject.connectSlotsByName(general_consultation)
    # setupUi

    def retranslateUi(self, general_consultation):
        general_consultation.setWindowTitle(QCoreApplication.translate("general_consultation", u"Consulta", None))
        ___qtablewidgetitem = self.table_consult.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("general_consultation", u"C\u00f3digo", None));
        ___qtablewidgetitem1 = self.table_consult.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("general_consultation", u"Descri\u00e7\u00e3o", None));
        self.btn_confirm.setText(QCoreApplication.translate("general_consultation", u"Confirmar \n"
" (Return)", None))
#if QT_CONFIG(shortcut)
        self.btn_confirm.setShortcut(QCoreApplication.translate("general_consultation", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_exit.setText(QCoreApplication.translate("general_consultation", u"Sair \n"
" (Esc)", None))
#if QT_CONFIG(shortcut)
        self.btn_exit.setShortcut(QCoreApplication.translate("general_consultation", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

