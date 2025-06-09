# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'npk_wheat_win.ui'
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

class Ui_npk_wheat(object):
    def setupUi(self, npk_wheat):
        if not npk_wheat.objectName():
            npk_wheat.setObjectName(u"npk_wheat")
        npk_wheat.resize(417, 275)
        npk_wheat.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.gridLayout_2 = QGridLayout(npk_wheat)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lbl_phosphate_fertilizer = QLabel(npk_wheat)
        self.lbl_phosphate_fertilizer.setObjectName(u"lbl_phosphate_fertilizer")

        self.gridLayout_2.addWidget(self.lbl_phosphate_fertilizer, 0, 0, 1, 2)

        self.cbx_phosphate_fertilizer = QComboBox(npk_wheat)
        self.cbx_phosphate_fertilizer.addItem("")
        self.cbx_phosphate_fertilizer.addItem("")
        self.cbx_phosphate_fertilizer.setObjectName(u"cbx_phosphate_fertilizer")
        self.cbx_phosphate_fertilizer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.cbx_phosphate_fertilizer, 1, 0, 1, 2)

        self.label = QLabel(npk_wheat)
        self.label.setObjectName(u"label")

        self.gridLayout_2.addWidget(self.label, 2, 0, 1, 2)

        self.ckb_previous_culture_corn = QCheckBox(npk_wheat)
        self.ckb_previous_culture_corn.setObjectName(u"ckb_previous_culture_corn")
        font = QFont()
        font.setBold(True)
        self.ckb_previous_culture_corn.setFont(font)
        self.ckb_previous_culture_corn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_2.addWidget(self.ckb_previous_culture_corn, 3, 0, 1, 2)

        self.lbl_cultivar_size = QLabel(npk_wheat)
        self.lbl_cultivar_size.setObjectName(u"lbl_cultivar_size")

        self.gridLayout_2.addWidget(self.lbl_cultivar_size, 4, 0, 1, 2)

        self.frm_limestone_plaster = QFrame(npk_wheat)
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


        self.gridLayout_2.addWidget(self.frm_limestone_plaster, 5, 0, 1, 2)

        self.cbx_cultivar_size = QComboBox(npk_wheat)
        self.cbx_cultivar_size.addItem("")
        self.cbx_cultivar_size.addItem("")
        self.cbx_cultivar_size.setObjectName(u"cbx_cultivar_size")
        self.cbx_cultivar_size.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.cbx_cultivar_size.setModelColumn(0)

        self.gridLayout_2.addWidget(self.cbx_cultivar_size, 6, 0, 1, 1)

        self.btn_confirm = QPushButton(npk_wheat)
        self.btn_confirm.setObjectName(u"btn_confirm")
        self.btn_confirm.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/buttons/images/button/Save-Update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_confirm.setIcon(icon)

        self.gridLayout_2.addWidget(self.btn_confirm, 7, 0, 1, 1)

        self.btn_cancel = QPushButton(npk_wheat)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/buttons/images/button/exit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cancel.setIcon(icon1)

        self.gridLayout_2.addWidget(self.btn_cancel, 7, 1, 1, 1)

        QWidget.setTabOrder(self.cbx_phosphate_fertilizer, self.ckb_previous_culture_corn)
        QWidget.setTabOrder(self.ckb_previous_culture_corn, self.ckb_limestone_recommendation)
        QWidget.setTabOrder(self.ckb_limestone_recommendation, self.edt_V)
        QWidget.setTabOrder(self.edt_V, self.ckb_plaster_recommendation)
        QWidget.setTabOrder(self.ckb_plaster_recommendation, self.cbx_cultivar_size)
        QWidget.setTabOrder(self.cbx_cultivar_size, self.btn_confirm)
        QWidget.setTabOrder(self.btn_confirm, self.btn_cancel)

        self.retranslateUi(npk_wheat)

        self.cbx_phosphate_fertilizer.setCurrentIndex(1)
        self.cbx_cultivar_size.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(npk_wheat)
    # setupUi

    def retranslateUi(self, npk_wheat):
        npk_wheat.setWindowTitle(QCoreApplication.translate("npk_wheat", u"Cultura do trigo", None))
        self.lbl_phosphate_fertilizer.setText(QCoreApplication.translate("npk_wheat", u"<html><head/><body><p><span style=\" font-weight:600;\">Aduba\u00e7\u00e3o Fosfatada:</span></p></body></html>", None))
        self.cbx_phosphate_fertilizer.setItemText(0, QCoreApplication.translate("npk_wheat", u"ADUBA\u00c7\u00c3O CORRETIVA TOTAL DE F\u00d3SFORO.", None))
        self.cbx_phosphate_fertilizer.setItemText(1, QCoreApplication.translate("npk_wheat", u"ADUBA\u00c7\u00c3O CORRETIVA GRADUAL DE F\u00d3SFORO.", None))

        self.label.setText(QCoreApplication.translate("npk_wheat", u"Obs.: Para teores de P dispon\u00edvel na classe m\u00e9dia e  boa utilizar somente aduba\u00e7\u00e3o\n"
" de manuten\u00e7\u00e3o (o sistema ajustar\u00e1 automaticamente). ", None))
        self.ckb_previous_culture_corn.setText(QCoreApplication.translate("npk_wheat", u"Trigo ser\u00e1 semeado ap\u00f3s a cultura do milho.", None))
        self.lbl_cultivar_size.setText(QCoreApplication.translate("npk_wheat", u"<html><head/><body><p><span style=\" font-weight:600;\">Porte de cultivares:</span></p></body></html>", None))
        self.ckb_limestone_recommendation.setText(QCoreApplication.translate("npk_wheat", u"Recomenda\u00e7\u00e3o de calagem.", None))
        self.lbl_V.setText(QCoreApplication.translate("npk_wheat", u"Satura\u00e7\u00e3o por Bases Esperada (%):", None))
        self.edt_V.setText(QCoreApplication.translate("npk_wheat", u"000,00", None))
        self.ckb_plaster_recommendation.setText(QCoreApplication.translate("npk_wheat", u"Recomenda\u00e7\u00e3o de gesso.", None))
        self.cbx_cultivar_size.setItemText(0, QCoreApplication.translate("npk_wheat", u"ALTO", None))
        self.cbx_cultivar_size.setItemText(1, QCoreApplication.translate("npk_wheat", u"BAIXO", None))

        self.btn_confirm.setText(QCoreApplication.translate("npk_wheat", u"Confirmar (Return)", None))
#if QT_CONFIG(shortcut)
        self.btn_confirm.setShortcut(QCoreApplication.translate("npk_wheat", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancel.setText(QCoreApplication.translate("npk_wheat", u"Cancelar (Esc)", None))
#if QT_CONFIG(shortcut)
        self.btn_cancel.setShortcut(QCoreApplication.translate("npk_wheat", u"Esc", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

