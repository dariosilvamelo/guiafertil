# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'limestone_plaster_soy_win.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)
import icones_rc

class Ui_limestone_plaster_soy(object):
    def setupUi(self, limestone_plaster_soy):
        if not limestone_plaster_soy.objectName():
            limestone_plaster_soy.setObjectName(u"limestone_plaster_soy")
        limestone_plaster_soy.resize(293, 114)
        limestone_plaster_soy.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout = QGridLayout(limestone_plaster_soy)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ckb_limestone_recommendation = QCheckBox(limestone_plaster_soy)
        self.ckb_limestone_recommendation.setObjectName(u"ckb_limestone_recommendation")
        font = QFont()
        font.setBold(True)
        self.ckb_limestone_recommendation.setFont(font)
        self.ckb_limestone_recommendation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.ckb_limestone_recommendation, 0, 0, 1, 3)

        self.lbl_V = QLabel(limestone_plaster_soy)
        self.lbl_V.setObjectName(u"lbl_V")
        self.lbl_V.setFont(font)

        self.gridLayout.addWidget(self.lbl_V, 1, 0, 1, 2)

        self.edt_V = QLineEdit(limestone_plaster_soy)
        self.edt_V.setObjectName(u"edt_V")

        self.gridLayout.addWidget(self.edt_V, 1, 2, 1, 1)

        self.btn_confirm = QPushButton(limestone_plaster_soy)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/buttons/images/button/Save-Update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_confirm.setIcon(icon)

        self.gridLayout.addWidget(self.btn_confirm, 3, 0, 1, 1)

        self.btn_cancel = QPushButton(limestone_plaster_soy)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/buttons/images/button/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cancel.setIcon(icon1)
        self.btn_cancel.setAutoDefault(True)

        self.gridLayout.addWidget(self.btn_cancel, 3, 1, 1, 1)

        self.ckb_plaster_recommendation = QCheckBox(limestone_plaster_soy)
        self.ckb_plaster_recommendation.setObjectName(u"ckb_plaster_recommendation")
        self.ckb_plaster_recommendation.setFont(font)
        self.ckb_plaster_recommendation.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout.addWidget(self.ckb_plaster_recommendation, 2, 0, 1, 3)

        QWidget.setTabOrder(self.ckb_limestone_recommendation, self.edt_V)
        QWidget.setTabOrder(self.edt_V, self.ckb_plaster_recommendation)
        QWidget.setTabOrder(self.ckb_plaster_recommendation, self.btn_confirm)
        QWidget.setTabOrder(self.btn_confirm, self.btn_cancel)

        self.retranslateUi(limestone_plaster_soy)

        QMetaObject.connectSlotsByName(limestone_plaster_soy)
    # setupUi

    def retranslateUi(self, limestone_plaster_soy):
        limestone_plaster_soy.setWindowTitle(QCoreApplication.translate("limestone_plaster_soy", u"Recomenda\u00e7\u00e3o de calc\u00e1rio e gesso", None))
        self.ckb_limestone_recommendation.setText(QCoreApplication.translate("limestone_plaster_soy", u"Recomenda\u00e7\u00e3o de calagem.", None))
        self.lbl_V.setText(QCoreApplication.translate("limestone_plaster_soy", u"Satura\u00e7\u00e3o por Bases Esperada (%):", None))
        self.edt_V.setText(QCoreApplication.translate("limestone_plaster_soy", u"000,00", None))
        self.btn_confirm.setText(QCoreApplication.translate("limestone_plaster_soy", u"Confirmar (Return)", None))
#if QT_CONFIG(shortcut)
        self.btn_confirm.setShortcut(QCoreApplication.translate("limestone_plaster_soy", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancel.setText(QCoreApplication.translate("limestone_plaster_soy", u"Cancelar (Esc)", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel.setShortcut(QCoreApplication.translate("limestone_plaster_soy", u"Esc", None))
#endif // QT_CONFIG(shortcut)
        self.ckb_plaster_recommendation.setText(QCoreApplication.translate("limestone_plaster_soy", u"Recomenda\u00e7\u00e3o de gesso.", None))
    # retranslateUi

