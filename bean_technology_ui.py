# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'bean_technology_win.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDialog,
    QFrame, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)
import icones_rc

class Ui_bean_technology(object):
    def setupUi(self, bean_technology):
        if not bean_technology.objectName():
            bean_technology.setObjectName(u"bean_technology")
        bean_technology.resize(622, 177)
        bean_technology.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(bean_technology)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_technology_level = QLabel(bean_technology)
        self.lbl_technology_level.setObjectName(u"lbl_technology_level")

        self.gridLayout_2.addWidget(self.lbl_technology_level, 0, 0, 1, 2)

        self.cbx_technology_level = QComboBox(bean_technology)
        self.cbx_technology_level.addItem("")
        self.cbx_technology_level.addItem("")
        self.cbx_technology_level.addItem("")
        self.cbx_technology_level.addItem("")
        self.cbx_technology_level.setObjectName(u"cbx_technology_level")
        self.cbx_technology_level.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.cbx_technology_level, 1, 0, 1, 3)

        self.frm_limestone_plaster = QFrame(bean_technology)
        self.frm_limestone_plaster.setObjectName(u"frm_limestone_plaster")
        self.frm_limestone_plaster.setMaximumSize(QSize(300, 16777215))
        self.frm_limestone_plaster.setFrameShape(QFrame.StyledPanel)
        self.frm_limestone_plaster.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frm_limestone_plaster)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ckb_limestone_recommendation = QCheckBox(self.frm_limestone_plaster)
        self.ckb_limestone_recommendation.setObjectName(u"ckb_limestone_recommendation")
        font = QFont()
        font.setBold(True)
        self.ckb_limestone_recommendation.setFont(font)
        self.ckb_limestone_recommendation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.ckb_limestone_recommendation, 0, 0, 1, 1)

        self.lbl_V = QLabel(self.frm_limestone_plaster)
        self.lbl_V.setObjectName(u"lbl_V")
        self.lbl_V.setFont(font)

        self.gridLayout.addWidget(self.lbl_V, 1, 0, 1, 1)

        self.edt_V = QLineEdit(self.frm_limestone_plaster)
        self.edt_V.setObjectName(u"edt_V")

        self.gridLayout.addWidget(self.edt_V, 1, 1, 1, 1)

        self.ckb_plaster_recommendation = QCheckBox(self.frm_limestone_plaster)
        self.ckb_plaster_recommendation.setObjectName(u"ckb_plaster_recommendation")
        self.ckb_plaster_recommendation.setFont(font)
        self.ckb_plaster_recommendation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.ckb_plaster_recommendation, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frm_limestone_plaster, 2, 0, 1, 2)

        self.btn_confirm = QPushButton(bean_technology)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setMaximumSize(QSize(145, 16777215))
        self.btn_confirm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/buttons/images/button/Save-Update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_confirm.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_confirm, 3, 0, 1, 1)

        self.btn_cancel = QPushButton(bean_technology)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setMaximumSize(QSize(145, 16777215))
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/buttons/images/button/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cancel.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_cancel, 3, 1, 1, 1)

        QWidget.setTabOrder(self.cbx_technology_level, self.ckb_limestone_recommendation)
        QWidget.setTabOrder(self.ckb_limestone_recommendation, self.edt_V)
        QWidget.setTabOrder(self.edt_V, self.ckb_plaster_recommendation)
        QWidget.setTabOrder(self.ckb_plaster_recommendation, self.btn_confirm)
        QWidget.setTabOrder(self.btn_confirm, self.btn_cancel)

        self.retranslateUi(bean_technology)

        QMetaObject.connectSlotsByName(bean_technology)
    # setupUi

    def retranslateUi(self, bean_technology):
        bean_technology.setWindowTitle(QCoreApplication.translate("bean_technology", u"Cultura do feij\u00e3o", None))
        self.lbl_technology_level.setText(QCoreApplication.translate("bean_technology", u"<html><head/><body><p><span style=\" font-weight:600;\">Selecione o n\u00edvel de tecnologia empregado:</span></p></body></html>", None))
        self.cbx_technology_level.setItemText(0, QCoreApplication.translate("bean_technology", u"NT1 - Calagem, aduba\u00e7\u00e3o, sementes catadas, 220.000 a 240.000 plantas/ha, campinas at\u00e9 30 dias ap\u00f3s a emergencia.", None))
        self.cbx_technology_level.setItemText(1, QCoreApplication.translate("bean_technology", u"NT2 - Calagem, aduba\u00e7\u00e3o, sementes fiscalizadas, 220.000 a 240.000 plantas / ha. controle fitossanit\u00e1rio, TS.", None))
        self.cbx_technology_level.setItemText(2, QCoreApplication.translate("bean_technology", u"NT3 - NT 2, herbicidas, irriga\u00e7\u00e3o.", None))
        self.cbx_technology_level.setItemText(3, QCoreApplication.translate("bean_technology", u"NT4 - NT 3, apenas com maiores doses de adubos.", None))

        self.ckb_limestone_recommendation.setText(QCoreApplication.translate("bean_technology", u"Recomenda\u00e7\u00e3o de calagem.", None))
        self.lbl_V.setText(QCoreApplication.translate("bean_technology", u"Satura\u00e7\u00e3o por Bases Esperada (%):", None))
        self.edt_V.setText(QCoreApplication.translate("bean_technology", u"000,00", None))
        self.ckb_plaster_recommendation.setText(QCoreApplication.translate("bean_technology", u"Recomenda\u00e7\u00e3o de gesso.", None))
        self.btn_confirm.setText(QCoreApplication.translate("bean_technology", u"Confirmar (Return)", None))
#if QT_CONFIG(shortcut)
        self.btn_confirm.setShortcut(QCoreApplication.translate("bean_technology", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancel.setText(QCoreApplication.translate("bean_technology", u"Cancelar (Esc)", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel.setShortcut(QCoreApplication.translate("bean_technology", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

