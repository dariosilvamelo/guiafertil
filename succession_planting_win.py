# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'succession_planting_win.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QFrame,
    QGridLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
import icones_rc

class Ui_succession_planting(object):
    def setupUi(self, succession_planting):
        if not succession_planting.objectName():
            succession_planting.setObjectName(u"succession_planting")
        succession_planting.resize(314, 157)
        succession_planting.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(succession_planting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.ckb_succession_planting = QCheckBox(succession_planting)
        self.ckb_succession_planting.setObjectName(u"ckb_succession_planting")
        font = QFont()
        font.setBold(True)
        self.ckb_succession_planting.setFont(font)
        self.ckb_succession_planting.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ckb_succession_planting.setChecked(False)

        self.gridLayout_2.addWidget(self.ckb_succession_planting, 0, 0, 1, 2)

        self.frm_limestone_plaster = QFrame(succession_planting)
        self.frm_limestone_plaster.setObjectName(u"frm_limestone_plaster")
        self.frm_limestone_plaster.setMaximumSize(QSize(300, 16777215))
        self.frm_limestone_plaster.setFrameShape(QFrame.StyledPanel)
        self.frm_limestone_plaster.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frm_limestone_plaster)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ckb_limestone_recommendation = QCheckBox(self.frm_limestone_plaster)
        self.ckb_limestone_recommendation.setObjectName(u"ckb_limestone_recommendation")
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


        self.gridLayout_2.addWidget(self.frm_limestone_plaster, 1, 0, 1, 2)

        self.btn_confirm = QPushButton(succession_planting)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/buttons/images/button/Save-Update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_confirm.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_confirm, 2, 0, 1, 1)

        self.btn_cancel = QPushButton(succession_planting)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/buttons/images/button/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cancel.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_cancel, 2, 1, 1, 1)

        QWidget.setTabOrder(self.ckb_succession_planting, self.ckb_limestone_recommendation)
        QWidget.setTabOrder(self.ckb_limestone_recommendation, self.edt_V)
        QWidget.setTabOrder(self.edt_V, self.ckb_plaster_recommendation)
        QWidget.setTabOrder(self.ckb_plaster_recommendation, self.btn_confirm)
        QWidget.setTabOrder(self.btn_confirm, self.btn_cancel)

        self.retranslateUi(succession_planting)

        QMetaObject.connectSlotsByName(succession_planting)
    # setupUi

    def retranslateUi(self, succession_planting):
        succession_planting.setWindowTitle(QCoreApplication.translate("succession_planting", u"Culturas do milho / sorgo", None))
        self.ckb_succession_planting.setText(QCoreApplication.translate("succession_planting", u"Plantio em sucess\u00e3o e, ou, em rota\u00e7\u00e3o com soja.", None))
        self.ckb_limestone_recommendation.setText(QCoreApplication.translate("succession_planting", u"Recomenda\u00e7\u00e3o de calagem.", None))
        self.lbl_V.setText(QCoreApplication.translate("succession_planting", u"Satura\u00e7\u00e3o por Bases Esperada (%):", None))
        self.edt_V.setText(QCoreApplication.translate("succession_planting", u"000,00", None))
        self.ckb_plaster_recommendation.setText(QCoreApplication.translate("succession_planting", u"Recomenda\u00e7\u00e3o de gesso.", None))
        self.btn_confirm.setText(QCoreApplication.translate("succession_planting", u"Confirmar (Return)", None))
#if QT_CONFIG(shortcut)
        self.btn_confirm.setShortcut(QCoreApplication.translate("succession_planting", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancel.setText(QCoreApplication.translate("succession_planting", u"Cancelar (Esc)", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel.setShortcut(QCoreApplication.translate("succession_planting", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

