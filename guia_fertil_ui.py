# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guia_fertil.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QComboBox, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QToolBox, QVBoxLayout, QWidget)
import icones_rc

class Ui_win_guia_fertil(object):
    def setupUi(self, win_guia_fertil):
        if not win_guia_fertil.objectName():
            win_guia_fertil.setObjectName(u"win_guia_fertil")
        win_guia_fertil.resize(1329, 646)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(win_guia_fertil.sizePolicy().hasHeightForWidth())
        win_guia_fertil.setSizePolicy(sizePolicy)
        win_guia_fertil.setStyleSheet(u"")
        self.centralwidget = QWidget(win_guia_fertil)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_21 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.frm_window = QFrame(self.centralwidget)
        self.frm_window.setObjectName(u"frm_window")
        self.frm_window.setMaximumSize(QSize(1310, 650))
        self.frm_window.setFrameShape(QFrame.StyledPanel)
        self.frm_window.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frm_window)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frm_left = QFrame(self.frm_window)
        self.frm_left.setObjectName(u"frm_left")
        sizePolicy.setHeightForWidth(self.frm_left.sizePolicy().hasHeightForWidth())
        self.frm_left.setSizePolicy(sizePolicy)
        self.frm_left.setMinimumSize(QSize(0, 0))
        self.frm_left.setMaximumSize(QSize(0, 16777215))
        self.frm_left.setFrameShape(QFrame.Box)
        self.frm_left.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frm_left)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frm_Logo = QFrame(self.frm_left)
        self.frm_Logo.setObjectName(u"frm_Logo")
        sizePolicy.setHeightForWidth(self.frm_Logo.sizePolicy().hasHeightForWidth())
        self.frm_Logo.setSizePolicy(sizePolicy)
        self.frm_Logo.setMaximumSize(QSize(16777215, 16777215))
        self.frm_Logo.setFrameShape(QFrame.StyledPanel)
        self.frm_Logo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frm_Logo)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.lbl_logo_menu = QLabel(self.frm_Logo)
        self.lbl_logo_menu.setObjectName(u"lbl_logo_menu")

        self.horizontalLayout_16.addWidget(self.lbl_logo_menu)


        self.verticalLayout_3.addWidget(self.frm_Logo)

        self.frm_menu = QFrame(self.frm_left)
        self.frm_menu.setObjectName(u"frm_menu")
        self.frm_menu.setMinimumSize(QSize(0, 0))
        self.frm_menu.setFrameShape(QFrame.StyledPanel)
        self.frm_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frm_menu)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.too_box_menu = QToolBox(self.frm_menu)
        self.too_box_menu.setObjectName(u"too_box_menu")
        sizePolicy.setHeightForWidth(self.too_box_menu.sizePolicy().hasHeightForWidth())
        self.too_box_menu.setSizePolicy(sizePolicy)
        self.too_box_menu.setMinimumSize(QSize(220, 0))
        self.too_box_menu.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pag_menu_main = QWidget()
        self.pag_menu_main.setObjectName(u"pag_menu_main")
        self.pag_menu_main.setGeometry(QRect(0, 0, 220, 461))
        self.pag_menu_main.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.verticalLayout_7 = QVBoxLayout(self.pag_menu_main)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.btn_menu_home = QPushButton(self.pag_menu_main)
        self.btn_menu_home.setObjectName(u"btn_menu_home")
        self.btn_menu_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_home.setFocusPolicy(Qt.NoFocus)
        icon = QIcon()
        icon.addFile(u":/buttons/images/button/Home.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_home.setIcon(icon)

        self.verticalLayout_7.addWidget(self.btn_menu_home)

        self.btn_menu_user = QPushButton(self.pag_menu_main)
        self.btn_menu_user.setObjectName(u"btn_menu_user")
        icon1 = QIcon()
        icon1.addFile(u":/buttons/images/button/user.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_user.setIcon(icon1)

        self.verticalLayout_7.addWidget(self.btn_menu_user)

        self.btn_menu_producer = QPushButton(self.pag_menu_main)
        self.btn_menu_producer.setObjectName(u"btn_menu_producer")
        self.btn_menu_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_producer.setFocusPolicy(Qt.NoFocus)
        icon2 = QIcon()
        icon2.addFile(u":/buttons/images/button/Producer.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_producer.setIcon(icon2)

        self.verticalLayout_7.addWidget(self.btn_menu_producer)

        self.btn_menu_analysis = QPushButton(self.pag_menu_main)
        self.btn_menu_analysis.setObjectName(u"btn_menu_analysis")
        self.btn_menu_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_analysis.setFocusPolicy(Qt.NoFocus)
        icon3 = QIcon()
        icon3.addFile(u":/buttons/images/button/Solo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_analysis.setIcon(icon3)

        self.verticalLayout_7.addWidget(self.btn_menu_analysis)

        self.btn_menu_neural_network = QPushButton(self.pag_menu_main)
        self.btn_menu_neural_network.setObjectName(u"btn_menu_neural_network")
        self.btn_menu_neural_network.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_neural_network.setFocusPolicy(Qt.NoFocus)
        icon4 = QIcon()
        icon4.addFile(u":/buttons/images/button/AI.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_neural_network.setIcon(icon4)

        self.verticalLayout_7.addWidget(self.btn_menu_neural_network)

        self.btn_menu_about = QPushButton(self.pag_menu_main)
        self.btn_menu_about.setObjectName(u"btn_menu_about")
        self.btn_menu_about.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_menu_about.setFocusPolicy(Qt.NoFocus)
        icon5 = QIcon()
        icon5.addFile(u":/buttons/images/button/Abolt.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_menu_about.setIcon(icon5)

        self.verticalLayout_7.addWidget(self.btn_menu_about)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)

        icon6 = QIcon()
        icon6.addFile(u":/buttons/images/button/Menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.too_box_menu.addItem(self.pag_menu_main, icon6, u"Menu")
        self.pag_menu_information = QWidget()
        self.pag_menu_information.setObjectName(u"pag_menu_information")
        self.pag_menu_information.setGeometry(QRect(0, 0, 220, 461))
        self.pag_menu_information.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.verticalLayout_6 = QVBoxLayout(self.pag_menu_information)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_6.addItem(self.verticalSpacer_4)

        self.label = QLabel(self.pag_menu_information)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u":/buttons/imagens/button/Producer.png"))

        self.verticalLayout_6.addWidget(self.label, 0, Qt.AlignHCenter)

        self.lbl_title_user = QLabel(self.pag_menu_information)
        self.lbl_title_user.setObjectName(u"lbl_title_user")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.lbl_title_user.setFont(font)

        self.verticalLayout_6.addWidget(self.lbl_title_user)

        self.lbl_user = QLabel(self.pag_menu_information)
        self.lbl_user.setObjectName(u"lbl_user")
        self.lbl_user.setMaximumSize(QSize(16777215, 100))
        self.lbl_user.setFont(font)

        self.verticalLayout_6.addWidget(self.lbl_user)

        icon7 = QIcon()
        icon7.addFile(u":/buttons/images/button/Information.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.too_box_menu.addItem(self.pag_menu_information, icon7, u"Informa\u00e7\u00f5es")

        self.horizontalLayout_5.addWidget(self.too_box_menu)


        self.verticalLayout_3.addWidget(self.frm_menu)


        self.horizontalLayout_2.addWidget(self.frm_left)

        self.frm_right = QFrame(self.frm_window)
        self.frm_right.setObjectName(u"frm_right")
        sizePolicy.setHeightForWidth(self.frm_right.sizePolicy().hasHeightForWidth())
        self.frm_right.setSizePolicy(sizePolicy)
        self.frm_right.setMaximumSize(QSize(16777215, 16777215))
        self.frm_right.setStyleSheet(u"")
        self.frm_right.setFrameShape(QFrame.StyledPanel)
        self.frm_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frm_right)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frm_header = QFrame(self.frm_right)
        self.frm_header.setObjectName(u"frm_header")
        self.frm_header.setMaximumSize(QSize(16777215, 50))
        self.frm_header.setFrameShape(QFrame.Box)
        self.frm_header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frm_header)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.btn_home = QPushButton(self.frm_header)
        self.btn_home.setObjectName(u"btn_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(10)
        sizePolicy1.setHeightForWidth(self.btn_home.sizePolicy().hasHeightForWidth())
        self.btn_home.setSizePolicy(sizePolicy1)
        self.btn_home.setMinimumSize(QSize(0, 0))
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setFocusPolicy(Qt.NoFocus)
        self.btn_home.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/buttons/images/button/Start.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home.setIcon(icon8)
        self.btn_home.setIconSize(QSize(40, 40))

        self.horizontalLayout_10.addWidget(self.btn_home, 0, Qt.AlignLeft)

        self.lbl_title = QLabel(self.frm_header)
        self.lbl_title.setObjectName(u"lbl_title")

        self.horizontalLayout_10.addWidget(self.lbl_title, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.frm_header)

        self.frm_main = QFrame(self.frm_right)
        self.frm_main.setObjectName(u"frm_main")
        self.frm_main.setMaximumSize(QSize(16777215, 16777215))
        self.frm_main.setStyleSheet(u"")
        self.frm_main.setFrameShape(QFrame.Box)
        self.frm_main.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frm_main)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.stk_pag = QStackedWidget(self.frm_main)
        self.stk_pag.setObjectName(u"stk_pag")
        font1 = QFont()
        font1.setBold(False)
        self.stk_pag.setFont(font1)
        self.stk_pag.setStyleSheet(u"")
        self.pag_analysis = QWidget()
        self.pag_analysis.setObjectName(u"pag_analysis")
        self.verticalLayout_19 = QVBoxLayout(self.pag_analysis)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.tab_register_analysis = QTabWidget(self.pag_analysis)
        self.tab_register_analysis.setObjectName(u"tab_register_analysis")
        sizePolicy.setHeightForWidth(self.tab_register_analysis.sizePolicy().hasHeightForWidth())
        self.tab_register_analysis.setSizePolicy(sizePolicy)
        self.tab_register_analysis.setFocusPolicy(Qt.NoFocus)
        self.tab_register_analysis.setStyleSheet(u"")
        self.tab_register_analysis01 = QWidget()
        self.tab_register_analysis01.setObjectName(u"tab_register_analysis01")
        self.verticalLayout_11 = QVBoxLayout(self.tab_register_analysis01)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frm_register_analysis = QFrame(self.tab_register_analysis01)
        self.frm_register_analysis.setObjectName(u"frm_register_analysis")
        sizePolicy.setHeightForWidth(self.frm_register_analysis.sizePolicy().hasHeightForWidth())
        self.frm_register_analysis.setSizePolicy(sizePolicy)
        self.frm_register_analysis.setStyleSheet(u"")
        self.frm_register_analysis.setFrameShape(QFrame.Box)
        self.frm_register_analysis.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frm_register_analysis)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.edt_code_producer = QLineEdit(self.frm_register_analysis)
        self.edt_code_producer.setObjectName(u"edt_code_producer")
        sizePolicy.setHeightForWidth(self.edt_code_producer.sizePolicy().hasHeightForWidth())
        self.edt_code_producer.setSizePolicy(sizePolicy)
        self.edt_code_producer.setMinimumSize(QSize(0, 0))
        self.edt_code_producer.setMaximumSize(QSize(16777215, 16777215))
        self.edt_code_producer.setAlignment(Qt.AlignCenter)
        self.edt_code_producer.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_code_producer, 1, 1, 1, 1)

        self.lbl_kg_ha_ = QLabel(self.frm_register_analysis)
        self.lbl_kg_ha_.setObjectName(u"lbl_kg_ha_")

        self.gridLayout_2.addWidget(self.lbl_kg_ha_, 18, 1, 1, 1)

        self.edt_longitude_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_longitude_analysis.setObjectName(u"edt_longitude_analysis")
        sizePolicy.setHeightForWidth(self.edt_longitude_analysis.sizePolicy().hasHeightForWidth())
        self.edt_longitude_analysis.setSizePolicy(sizePolicy)
        self.edt_longitude_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_longitude_analysis.setAlignment(Qt.AlignCenter)
        self.edt_longitude_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_longitude_analysis, 3, 4, 1, 2)

        self.edt_prnt_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_prnt_analysis.setObjectName(u"edt_prnt_analysis")
        sizePolicy.setHeightForWidth(self.edt_prnt_analysis.sizePolicy().hasHeightForWidth())
        self.edt_prnt_analysis.setSizePolicy(sizePolicy)
        self.edt_prnt_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_prnt_analysis.setAlignment(Qt.AlignCenter)
        self.edt_prnt_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_prnt_analysis, 16, 11, 1, 1)

        self.lbl_prnt_analysis = QLabel(self.frm_register_analysis)
        self.lbl_prnt_analysis.setObjectName(u"lbl_prnt_analysis")

        self.gridLayout_2.addWidget(self.lbl_prnt_analysis, 15, 11, 1, 1)

        self.edt_micro_b_analysis_kg = QLineEdit(self.frm_register_analysis)
        self.edt_micro_b_analysis_kg.setObjectName(u"edt_micro_b_analysis_kg")
        sizePolicy.setHeightForWidth(self.edt_micro_b_analysis_kg.sizePolicy().hasHeightForWidth())
        self.edt_micro_b_analysis_kg.setSizePolicy(sizePolicy)
        self.edt_micro_b_analysis_kg.setMinimumSize(QSize(55, 0))
        self.edt_micro_b_analysis_kg.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_b_analysis_kg.setAlignment(Qt.AlignCenter)
        self.edt_micro_b_analysis_kg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_micro_b_analysis_kg, 18, 3, 1, 1)

        self.edt_micro_mo_analysis_kg = QLineEdit(self.frm_register_analysis)
        self.edt_micro_mo_analysis_kg.setObjectName(u"edt_micro_mo_analysis_kg")
        sizePolicy.setHeightForWidth(self.edt_micro_mo_analysis_kg.sizePolicy().hasHeightForWidth())
        self.edt_micro_mo_analysis_kg.setSizePolicy(sizePolicy)
        self.edt_micro_mo_analysis_kg.setMinimumSize(QSize(55, 0))
        self.edt_micro_mo_analysis_kg.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_mo_analysis_kg.setAlignment(Qt.AlignCenter)
        self.edt_micro_mo_analysis_kg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_micro_mo_analysis_kg, 18, 6, 1, 1)

        self.lbl_limestone_analysis = QLabel(self.frm_register_analysis)
        self.lbl_limestone_analysis.setObjectName(u"lbl_limestone_analysis")
        self.lbl_limestone_analysis.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.lbl_limestone_analysis, 15, 10, 1, 1)

        self.edt_micro_zn_analysis_kg = QLineEdit(self.frm_register_analysis)
        self.edt_micro_zn_analysis_kg.setObjectName(u"edt_micro_zn_analysis_kg")
        sizePolicy.setHeightForWidth(self.edt_micro_zn_analysis_kg.sizePolicy().hasHeightForWidth())
        self.edt_micro_zn_analysis_kg.setSizePolicy(sizePolicy)
        self.edt_micro_zn_analysis_kg.setMinimumSize(QSize(55, 0))
        self.edt_micro_zn_analysis_kg.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_zn_analysis_kg.setAlignment(Qt.AlignCenter)
        self.edt_micro_zn_analysis_kg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_micro_zn_analysis_kg, 18, 2, 1, 1)

        self.edt_limestone_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_limestone_analysis.setObjectName(u"edt_limestone_analysis")
        sizePolicy.setHeightForWidth(self.edt_limestone_analysis.sizePolicy().hasHeightForWidth())
        self.edt_limestone_analysis.setSizePolicy(sizePolicy)
        self.edt_limestone_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_limestone_analysis.setAlignment(Qt.AlignCenter)
        self.edt_limestone_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_limestone_analysis, 16, 10, 1, 1)

        self.edt_tca_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_tca_analysis.setObjectName(u"edt_tca_analysis")
        sizePolicy.setHeightForWidth(self.edt_tca_analysis.sizePolicy().hasHeightForWidth())
        self.edt_tca_analysis.setSizePolicy(sizePolicy)
        self.edt_tca_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_tca_analysis.setAlignment(Qt.AlignCenter)
        self.edt_tca_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_tca_analysis, 16, 13, 1, 1)

        self.edt_plaster_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_plaster_analysis.setObjectName(u"edt_plaster_analysis")
        sizePolicy.setHeightForWidth(self.edt_plaster_analysis.sizePolicy().hasHeightForWidth())
        self.edt_plaster_analysis.setSizePolicy(sizePolicy)
        self.edt_plaster_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_plaster_analysis.setAlignment(Qt.AlignCenter)
        self.edt_plaster_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_plaster_analysis, 16, 12, 1, 1)

        self.lbl_minimum_temperature_analysis = QLabel(self.frm_register_analysis)
        self.lbl_minimum_temperature_analysis.setObjectName(u"lbl_minimum_temperature_analysis")

        self.gridLayout_2.addWidget(self.lbl_minimum_temperature_analysis, 2, 10, 1, 1)

        self.lbl_rain_reproductive_analysis = QLabel(self.frm_register_analysis)
        self.lbl_rain_reproductive_analysis.setObjectName(u"lbl_rain_reproductive_analysis")

        self.gridLayout_2.addWidget(self.lbl_rain_reproductive_analysis, 2, 13, 1, 1)

        self.edt_latitude_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_latitude_analysis.setObjectName(u"edt_latitude_analysis")
        sizePolicy.setHeightForWidth(self.edt_latitude_analysis.sizePolicy().hasHeightForWidth())
        self.edt_latitude_analysis.setSizePolicy(sizePolicy)
        self.edt_latitude_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_latitude_analysis.setAlignment(Qt.AlignCenter)
        self.edt_latitude_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_latitude_analysis, 3, 2, 1, 2)

        self.lbl_rain_vegetative_analysis = QLabel(self.frm_register_analysis)
        self.lbl_rain_vegetative_analysis.setObjectName(u"lbl_rain_vegetative_analysis")

        self.gridLayout_2.addWidget(self.lbl_rain_vegetative_analysis, 2, 12, 1, 1)

        self.lbl_maximum_temperature_analysis = QLabel(self.frm_register_analysis)
        self.lbl_maximum_temperature_analysis.setObjectName(u"lbl_maximum_temperature_analysis")

        self.gridLayout_2.addWidget(self.lbl_maximum_temperature_analysis, 2, 11, 1, 1)

        self.lbl_culture_analysis = QLabel(self.frm_register_analysis)
        self.lbl_culture_analysis.setObjectName(u"lbl_culture_analysis")

        self.gridLayout_2.addWidget(self.lbl_culture_analysis, 0, 12, 1, 1)

        self.edt_altitude_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_altitude_analysis.setObjectName(u"edt_altitude_analysis")
        sizePolicy.setHeightForWidth(self.edt_altitude_analysis.sizePolicy().hasHeightForWidth())
        self.edt_altitude_analysis.setSizePolicy(sizePolicy)
        self.edt_altitude_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_altitude_analysis.setAlignment(Qt.AlignCenter)
        self.edt_altitude_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_altitude_analysis, 3, 0, 1, 2)

        self.lbl_code_analysis = QLabel(self.frm_register_analysis)
        self.lbl_code_analysis.setObjectName(u"lbl_code_analysis")
        self.lbl_code_analysis.setMaximumSize(QSize(16777215, 18))

        self.gridLayout_2.addWidget(self.lbl_code_analysis, 1, 0, 1, 1)

        self.edt_agricultural_period_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_agricultural_period_analysis.setObjectName(u"edt_agricultural_period_analysis")
        sizePolicy.setHeightForWidth(self.edt_agricultural_period_analysis.sizePolicy().hasHeightForWidth())
        self.edt_agricultural_period_analysis.setSizePolicy(sizePolicy)
        self.edt_agricultural_period_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_agricultural_period_analysis.setAlignment(Qt.AlignCenter)
        self.edt_agricultural_period_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_agricultural_period_analysis, 1, 10, 1, 2)

        self.edt_maximum_temperature_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_maximum_temperature_analysis.setObjectName(u"edt_maximum_temperature_analysis")
        sizePolicy.setHeightForWidth(self.edt_maximum_temperature_analysis.sizePolicy().hasHeightForWidth())
        self.edt_maximum_temperature_analysis.setSizePolicy(sizePolicy)
        self.edt_maximum_temperature_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_maximum_temperature_analysis.setAlignment(Qt.AlignCenter)
        self.edt_maximum_temperature_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_maximum_temperature_analysis, 3, 11, 1, 1)

        self.lbl_P_rem_analysis = QLabel(self.frm_register_analysis)
        self.lbl_P_rem_analysis.setObjectName(u"lbl_P_rem_analysis")

        self.gridLayout_2.addWidget(self.lbl_P_rem_analysis, 8, 1, 1, 1)

        self.lbl_K_mg_analysis = QLabel(self.frm_register_analysis)
        self.lbl_K_mg_analysis.setObjectName(u"lbl_K_mg_analysis")

        self.gridLayout_2.addWidget(self.lbl_K_mg_analysis, 8, 3, 1, 1)

        self.edt_rain_vegetative_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_rain_vegetative_analysis.setObjectName(u"edt_rain_vegetative_analysis")
        sizePolicy.setHeightForWidth(self.edt_rain_vegetative_analysis.sizePolicy().hasHeightForWidth())
        self.edt_rain_vegetative_analysis.setSizePolicy(sizePolicy)
        self.edt_rain_vegetative_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_rain_vegetative_analysis.setAlignment(Qt.AlignCenter)
        self.edt_rain_vegetative_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_rain_vegetative_analysis, 3, 12, 1, 1)

        self.edt_minimum_temperature_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_minimum_temperature_analysis.setObjectName(u"edt_minimum_temperature_analysis")
        sizePolicy.setHeightForWidth(self.edt_minimum_temperature_analysis.sizePolicy().hasHeightForWidth())
        self.edt_minimum_temperature_analysis.setSizePolicy(sizePolicy)
        self.edt_minimum_temperature_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_minimum_temperature_analysis.setAlignment(Qt.AlignCenter)
        self.edt_minimum_temperature_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_minimum_temperature_analysis, 3, 10, 1, 1)

        self.edt_rain_reproductive_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_rain_reproductive_analysis.setObjectName(u"edt_rain_reproductive_analysis")
        sizePolicy.setHeightForWidth(self.edt_rain_reproductive_analysis.sizePolicy().hasHeightForWidth())
        self.edt_rain_reproductive_analysis.setSizePolicy(sizePolicy)
        self.edt_rain_reproductive_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_rain_reproductive_analysis.setAlignment(Qt.AlignCenter)
        self.edt_rain_reproductive_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_rain_reproductive_analysis, 3, 13, 1, 1)

        self.lbl_mg_dm3 = QLabel(self.frm_register_analysis)
        self.lbl_mg_dm3.setObjectName(u"lbl_mg_dm3")
        self.lbl_mg_dm3.setFrameShape(QFrame.StyledPanel)
        self.lbl_mg_dm3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_mg_dm3, 10, 0, 1, 10)

        self.lbl_percent_3 = QLabel(self.frm_register_analysis)
        self.lbl_percent_3.setObjectName(u"lbl_percent_3")
        self.lbl_percent_3.setFrameShape(QFrame.StyledPanel)
        self.lbl_percent_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_percent_3, 4, 12, 1, 2)

        self.lbl_percent_4 = QLabel(self.frm_register_analysis)
        self.lbl_percent_4.setObjectName(u"lbl_percent_4")
        self.lbl_percent_4.setFrameShape(QFrame.StyledPanel)
        self.lbl_percent_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_percent_4, 4, 10, 1, 2)

        self.cbx_culture_analysis = QComboBox(self.frm_register_analysis)
        self.cbx_culture_analysis.addItem("")
        self.cbx_culture_analysis.addItem("")
        self.cbx_culture_analysis.addItem("")
        self.cbx_culture_analysis.addItem("")
        self.cbx_culture_analysis.addItem("")
        self.cbx_culture_analysis.setObjectName(u"cbx_culture_analysis")
        self.cbx_culture_analysis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.cbx_culture_analysis.sizePolicy().hasHeightForWidth())
        self.cbx_culture_analysis.setSizePolicy(sizePolicy)
        self.cbx_culture_analysis.setMinimumSize(QSize(55, 0))

        self.gridLayout_2.addWidget(self.cbx_culture_analysis, 1, 12, 1, 1)

        self.lbl_area_analysis = QLabel(self.frm_register_analysis)
        self.lbl_area_analysis.setObjectName(u"lbl_area_analysis")

        self.gridLayout_2.addWidget(self.lbl_area_analysis, 0, 13, 1, 1)

        self.lbl_code_producer_analysis = QLabel(self.frm_register_analysis)
        self.lbl_code_producer_analysis.setObjectName(u"lbl_code_producer_analysis")

        self.gridLayout_2.addWidget(self.lbl_code_producer_analysis, 0, 1, 1, 1)

        self.edt_area_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_area_analysis.setObjectName(u"edt_area_analysis")
        sizePolicy.setHeightForWidth(self.edt_area_analysis.sizePolicy().hasHeightForWidth())
        self.edt_area_analysis.setSizePolicy(sizePolicy)
        self.edt_area_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_area_analysis.setAlignment(Qt.AlignCenter)
        self.edt_area_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_area_analysis, 1, 13, 1, 1)

        self.edt_initial_depth_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_initial_depth_analysis.setObjectName(u"edt_initial_depth_analysis")
        sizePolicy.setHeightForWidth(self.edt_initial_depth_analysis.sizePolicy().hasHeightForWidth())
        self.edt_initial_depth_analysis.setSizePolicy(sizePolicy)
        self.edt_initial_depth_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_initial_depth_analysis.setAlignment(Qt.AlignCenter)
        self.edt_initial_depth_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_initial_depth_analysis, 6, 0, 1, 1)

        self.edt_final_depth_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_final_depth_analysis.setObjectName(u"edt_final_depth_analysis")
        sizePolicy.setHeightForWidth(self.edt_final_depth_analysis.sizePolicy().hasHeightForWidth())
        self.edt_final_depth_analysis.setSizePolicy(sizePolicy)
        self.edt_final_depth_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_final_depth_analysis.setAlignment(Qt.AlignCenter)
        self.edt_final_depth_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_final_depth_analysis, 6, 1, 1, 1)

        self.label_2 = QLabel(self.frm_register_analysis)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)

        self.edt_Ca_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_Ca_analysis.setObjectName(u"edt_Ca_analysis")
        sizePolicy.setHeightForWidth(self.edt_Ca_analysis.sizePolicy().hasHeightForWidth())
        self.edt_Ca_analysis.setSizePolicy(sizePolicy)
        self.edt_Ca_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_Ca_analysis.setAlignment(Qt.AlignCenter)
        self.edt_Ca_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_Ca_analysis, 6, 5, 1, 1)

        self.edt_ph_H2O_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_ph_H2O_analysis.setObjectName(u"edt_ph_H2O_analysis")
        sizePolicy.setHeightForWidth(self.edt_ph_H2O_analysis.sizePolicy().hasHeightForWidth())
        self.edt_ph_H2O_analysis.setSizePolicy(sizePolicy)
        self.edt_ph_H2O_analysis.setAlignment(Qt.AlignCenter)
        self.edt_ph_H2O_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_ph_H2O_analysis, 6, 2, 1, 1)

        self.edt_K_cmolc_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_K_cmolc_analysis.setObjectName(u"edt_K_cmolc_analysis")
        sizePolicy.setHeightForWidth(self.edt_K_cmolc_analysis.sizePolicy().hasHeightForWidth())
        self.edt_K_cmolc_analysis.setSizePolicy(sizePolicy)
        self.edt_K_cmolc_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_K_cmolc_analysis.setAlignment(Qt.AlignCenter)
        self.edt_K_cmolc_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_K_cmolc_analysis, 6, 4, 1, 1)

        self.edt_ph_CaCl2_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_ph_CaCl2_analysis.setObjectName(u"edt_ph_CaCl2_analysis")
        sizePolicy.setHeightForWidth(self.edt_ph_CaCl2_analysis.sizePolicy().hasHeightForWidth())
        self.edt_ph_CaCl2_analysis.setSizePolicy(sizePolicy)
        self.edt_ph_CaCl2_analysis.setAlignment(Qt.AlignCenter)
        self.edt_ph_CaCl2_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_ph_CaCl2_analysis, 6, 3, 1, 1)

        self.lbl_final_depth_analysis = QLabel(self.frm_register_analysis)
        self.lbl_final_depth_analysis.setObjectName(u"lbl_final_depth_analysis")

        self.gridLayout_2.addWidget(self.lbl_final_depth_analysis, 5, 1, 1, 1)

        self.lbl_ph_CaCl2_analysis = QLabel(self.frm_register_analysis)
        self.lbl_ph_CaCl2_analysis.setObjectName(u"lbl_ph_CaCl2_analysis")

        self.gridLayout_2.addWidget(self.lbl_ph_CaCl2_analysis, 5, 3, 1, 1)

        self.lbl_ph_H2O_analysis = QLabel(self.frm_register_analysis)
        self.lbl_ph_H2O_analysis.setObjectName(u"lbl_ph_H2O_analysis")

        self.gridLayout_2.addWidget(self.lbl_ph_H2O_analysis, 5, 2, 1, 1)

        self.lbl_Ca_analysis = QLabel(self.frm_register_analysis)
        self.lbl_Ca_analysis.setObjectName(u"lbl_Ca_analysis")

        self.gridLayout_2.addWidget(self.lbl_Ca_analysis, 5, 5, 1, 1)

        self.lbl_K_cmolc_analysis = QLabel(self.frm_register_analysis)
        self.lbl_K_cmolc_analysis.setObjectName(u"lbl_K_cmolc_analysis")

        self.gridLayout_2.addWidget(self.lbl_K_cmolc_analysis, 5, 4, 1, 1)

        self.lbl_Al_analysis = QLabel(self.frm_register_analysis)
        self.lbl_Al_analysis.setObjectName(u"lbl_Al_analysis")

        self.gridLayout_2.addWidget(self.lbl_Al_analysis, 5, 7, 1, 1)

        self.lbl_Mg_analysis = QLabel(self.frm_register_analysis)
        self.lbl_Mg_analysis.setObjectName(u"lbl_Mg_analysis")

        self.gridLayout_2.addWidget(self.lbl_Mg_analysis, 5, 6, 1, 1)

        self.lbl_SB_analysis = QLabel(self.frm_register_analysis)
        self.lbl_SB_analysis.setObjectName(u"lbl_SB_analysis")

        self.gridLayout_2.addWidget(self.lbl_SB_analysis, 5, 9, 1, 1)

        self.lbl_T_analysis = QLabel(self.frm_register_analysis)
        self.lbl_T_analysis.setObjectName(u"lbl_T_analysis")

        self.gridLayout_2.addWidget(self.lbl_T_analysis, 5, 11, 1, 1)

        self.lbl_H_Al_analysis = QLabel(self.frm_register_analysis)
        self.lbl_H_Al_analysis.setObjectName(u"lbl_H_Al_analysis")

        self.gridLayout_2.addWidget(self.lbl_H_Al_analysis, 5, 8, 1, 1)

        self.lbl_t_effective_CTC_analysis_2 = QLabel(self.frm_register_analysis)
        self.lbl_t_effective_CTC_analysis_2.setObjectName(u"lbl_t_effective_CTC_analysis_2")

        self.gridLayout_2.addWidget(self.lbl_t_effective_CTC_analysis_2, 5, 10, 1, 1)

        self.lbl_m_analysis = QLabel(self.frm_register_analysis)
        self.lbl_m_analysis.setObjectName(u"lbl_m_analysis")

        self.gridLayout_2.addWidget(self.lbl_m_analysis, 5, 13, 1, 1)

        self.lbl_V_analysis = QLabel(self.frm_register_analysis)
        self.lbl_V_analysis.setObjectName(u"lbl_V_analysis")

        self.gridLayout_2.addWidget(self.lbl_V_analysis, 5, 12, 1, 1)

        self.lbl_Zn_analysis = QLabel(self.frm_register_analysis)
        self.lbl_Zn_analysis.setObjectName(u"lbl_Zn_analysis")

        self.gridLayout_2.addWidget(self.lbl_Zn_analysis, 8, 9, 1, 1)

        self.edt_Cu_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_Cu_analysis.setObjectName(u"edt_Cu_analysis")
        sizePolicy.setHeightForWidth(self.edt_Cu_analysis.sizePolicy().hasHeightForWidth())
        self.edt_Cu_analysis.setSizePolicy(sizePolicy)
        self.edt_Cu_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_Cu_analysis.setAlignment(Qt.AlignCenter)
        self.edt_Cu_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_Cu_analysis, 9, 6, 1, 1)

        self.lbl_Fe_analysis = QLabel(self.frm_register_analysis)
        self.lbl_Fe_analysis.setObjectName(u"lbl_Fe_analysis")

        self.gridLayout_2.addWidget(self.lbl_Fe_analysis, 8, 7, 1, 1)

        self.lbl_S_SO4_analysis = QLabel(self.frm_register_analysis)
        self.lbl_S_SO4_analysis.setObjectName(u"lbl_S_SO4_analysis")

        self.gridLayout_2.addWidget(self.lbl_S_SO4_analysis, 8, 4, 1, 1)

        self.edt_V_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_V_analysis.setObjectName(u"edt_V_analysis")
        sizePolicy.setHeightForWidth(self.edt_V_analysis.sizePolicy().hasHeightForWidth())
        self.edt_V_analysis.setSizePolicy(sizePolicy)
        self.edt_V_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_V_analysis.setAlignment(Qt.AlignCenter)
        self.edt_V_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_V_analysis, 6, 12, 1, 1)

        self.lbl_MO_analysis = QLabel(self.frm_register_analysis)
        self.lbl_MO_analysis.setObjectName(u"lbl_MO_analysis")

        self.gridLayout_2.addWidget(self.lbl_MO_analysis, 8, 10, 1, 1)

        self.lbl_name_producer_analysis = QLabel(self.frm_register_analysis)
        self.lbl_name_producer_analysis.setObjectName(u"lbl_name_producer_analysis")

        self.gridLayout_2.addWidget(self.lbl_name_producer_analysis, 0, 2, 1, 4)

        self.lbl_altitude_analysis = QLabel(self.frm_register_analysis)
        self.lbl_altitude_analysis.setObjectName(u"lbl_altitude_analysis")

        self.gridLayout_2.addWidget(self.lbl_altitude_analysis, 2, 0, 1, 2)

        self.lbl_P2O5_analysis = QLabel(self.frm_register_analysis)
        self.lbl_P2O5_analysis.setObjectName(u"lbl_P2O5_analysis")

        self.gridLayout_2.addWidget(self.lbl_P2O5_analysis, 11, 4, 1, 2)

        self.cbx_planting_system_analysis = QComboBox(self.frm_register_analysis)
        self.cbx_planting_system_analysis.addItem("")
        self.cbx_planting_system_analysis.addItem("")
        self.cbx_planting_system_analysis.addItem("")
        self.cbx_planting_system_analysis.addItem("")
        self.cbx_planting_system_analysis.setObjectName(u"cbx_planting_system_analysis")
        self.cbx_planting_system_analysis.setEnabled(False)
        sizePolicy.setHeightForWidth(self.cbx_planting_system_analysis.sizePolicy().hasHeightForWidth())
        self.cbx_planting_system_analysis.setSizePolicy(sizePolicy)
        self.cbx_planting_system_analysis.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.cbx_planting_system_analysis, 3, 6, 1, 3)

        self.lbl_sector_analysis = QLabel(self.frm_register_analysis)
        self.lbl_sector_analysis.setObjectName(u"lbl_sector_analysis")

        self.gridLayout_2.addWidget(self.lbl_sector_analysis, 0, 6, 1, 4)

        self.edt_average_productivity_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_average_productivity_analysis.setObjectName(u"edt_average_productivity_analysis")
        sizePolicy.setHeightForWidth(self.edt_average_productivity_analysis.sizePolicy().hasHeightForWidth())
        self.edt_average_productivity_analysis.setSizePolicy(sizePolicy)
        self.edt_average_productivity_analysis.setMinimumSize(QSize(0, 0))
        self.edt_average_productivity_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_average_productivity_analysis.setAlignment(Qt.AlignCenter)
        self.edt_average_productivity_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_average_productivity_analysis, 3, 9, 1, 1)

        self.lbl_dag_kg = QLabel(self.frm_register_analysis)
        self.lbl_dag_kg.setObjectName(u"lbl_dag_kg")
        self.lbl_dag_kg.setFrameShape(QFrame.StyledPanel)
        self.lbl_dag_kg.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_dag_kg, 10, 10, 1, 2)

        self.lbl_g_kg = QLabel(self.frm_register_analysis)
        self.lbl_g_kg.setObjectName(u"lbl_g_kg")
        self.lbl_g_kg.setFrameShape(QFrame.StyledPanel)
        self.lbl_g_kg.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_g_kg, 10, 12, 1, 2)

        self.lbl_initial_depth_analysis = QLabel(self.frm_register_analysis)
        self.lbl_initial_depth_analysis.setObjectName(u"lbl_initial_depth_analysis")

        self.gridLayout_2.addWidget(self.lbl_initial_depth_analysis, 5, 0, 1, 1)

        self.lbl_percent = QLabel(self.frm_register_analysis)
        self.lbl_percent.setObjectName(u"lbl_percent")
        self.lbl_percent.setFrameShape(QFrame.StyledPanel)
        self.lbl_percent.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_percent, 7, 12, 1, 2)

        self.lbl_cm = QLabel(self.frm_register_analysis)
        self.lbl_cm.setObjectName(u"lbl_cm")
        self.lbl_cm.setFrameShape(QFrame.StyledPanel)
        self.lbl_cm.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_cm, 7, 0, 1, 2)

        self.lbl_cmolc_dm3 = QLabel(self.frm_register_analysis)
        self.lbl_cmolc_dm3.setObjectName(u"lbl_cmolc_dm3")
        self.lbl_cmolc_dm3.setMaximumSize(QSize(16777215, 16777215))
        self.lbl_cmolc_dm3.setFrameShape(QFrame.StyledPanel)
        self.lbl_cmolc_dm3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_cmolc_dm3, 7, 4, 1, 8)

        self.edt_P_rem_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_P_rem_analysis.setObjectName(u"edt_P_rem_analysis")
        sizePolicy.setHeightForWidth(self.edt_P_rem_analysis.sizePolicy().hasHeightForWidth())
        self.edt_P_rem_analysis.setSizePolicy(sizePolicy)
        self.edt_P_rem_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_P_rem_analysis.setAlignment(Qt.AlignCenter)
        self.edt_P_rem_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_P_rem_analysis, 9, 1, 1, 1)

        self.edt_Na_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_Na_analysis.setObjectName(u"edt_Na_analysis")
        sizePolicy.setHeightForWidth(self.edt_Na_analysis.sizePolicy().hasHeightForWidth())
        self.edt_Na_analysis.setSizePolicy(sizePolicy)
        self.edt_Na_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_Na_analysis.setAlignment(Qt.AlignCenter)
        self.edt_Na_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_Na_analysis, 9, 2, 1, 1)

        self.edt_S_SO4_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_S_SO4_analysis.setObjectName(u"edt_S_SO4_analysis")
        sizePolicy.setHeightForWidth(self.edt_S_SO4_analysis.sizePolicy().hasHeightForWidth())
        self.edt_S_SO4_analysis.setSizePolicy(sizePolicy)
        self.edt_S_SO4_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_S_SO4_analysis.setAlignment(Qt.AlignCenter)
        self.edt_S_SO4_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_S_SO4_analysis, 9, 4, 1, 1)

        self.lbl_Cu_analysis = QLabel(self.frm_register_analysis)
        self.lbl_Cu_analysis.setObjectName(u"lbl_Cu_analysis")

        self.gridLayout_2.addWidget(self.lbl_Cu_analysis, 8, 6, 1, 1)

        self.lbl_ph_1_25 = QLabel(self.frm_register_analysis)
        self.lbl_ph_1_25.setObjectName(u"lbl_ph_1_25")
        self.lbl_ph_1_25.setFrameShape(QFrame.StyledPanel)
        self.lbl_ph_1_25.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_ph_1_25, 7, 2, 1, 2)

        self.lbl_P_meh_analysis = QLabel(self.frm_register_analysis)
        self.lbl_P_meh_analysis.setObjectName(u"lbl_P_meh_analysis")

        self.gridLayout_2.addWidget(self.lbl_P_meh_analysis, 8, 0, 1, 1)

        self.lbl_Na_analysis = QLabel(self.frm_register_analysis)
        self.lbl_Na_analysis.setObjectName(u"lbl_Na_analysis")

        self.gridLayout_2.addWidget(self.lbl_Na_analysis, 8, 2, 1, 1)

        self.edt_T_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_T_analysis.setObjectName(u"edt_T_analysis")
        sizePolicy.setHeightForWidth(self.edt_T_analysis.sizePolicy().hasHeightForWidth())
        self.edt_T_analysis.setSizePolicy(sizePolicy)
        self.edt_T_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_T_analysis.setAlignment(Qt.AlignCenter)
        self.edt_T_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_T_analysis, 6, 11, 1, 1)

        self.edt_m_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_m_analysis.setObjectName(u"edt_m_analysis")
        self.edt_m_analysis.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edt_m_analysis.sizePolicy().hasHeightForWidth())
        self.edt_m_analysis.setSizePolicy(sizePolicy)
        self.edt_m_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_m_analysis.setAlignment(Qt.AlignCenter)
        self.edt_m_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_m_analysis, 6, 13, 1, 1)

        self.edt_H_Al_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_H_Al_analysis.setObjectName(u"edt_H_Al_analysis")
        sizePolicy.setHeightForWidth(self.edt_H_Al_analysis.sizePolicy().hasHeightForWidth())
        self.edt_H_Al_analysis.setSizePolicy(sizePolicy)
        self.edt_H_Al_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_H_Al_analysis.setAlignment(Qt.AlignCenter)
        self.edt_H_Al_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_H_Al_analysis, 6, 8, 1, 1)

        self.lbl_Mn_analysis = QLabel(self.frm_register_analysis)
        self.lbl_Mn_analysis.setObjectName(u"lbl_Mn_analysis")

        self.gridLayout_2.addWidget(self.lbl_Mn_analysis, 8, 8, 1, 1)

        self.edt_SB_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_SB_analysis.setObjectName(u"edt_SB_analysis")
        sizePolicy.setHeightForWidth(self.edt_SB_analysis.sizePolicy().hasHeightForWidth())
        self.edt_SB_analysis.setSizePolicy(sizePolicy)
        self.edt_SB_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_SB_analysis.setAlignment(Qt.AlignCenter)
        self.edt_SB_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_SB_analysis, 6, 9, 1, 1)

        self.edt_Al_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_Al_analysis.setObjectName(u"edt_Al_analysis")
        sizePolicy.setHeightForWidth(self.edt_Al_analysis.sizePolicy().hasHeightForWidth())
        self.edt_Al_analysis.setSizePolicy(sizePolicy)
        self.edt_Al_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_Al_analysis.setAlignment(Qt.AlignCenter)
        self.edt_Al_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_Al_analysis, 6, 7, 1, 1)

        self.lbl_CO_analysis = QLabel(self.frm_register_analysis)
        self.lbl_CO_analysis.setObjectName(u"lbl_CO_analysis")

        self.gridLayout_2.addWidget(self.lbl_CO_analysis, 8, 11, 1, 1)

        self.edt_Mg_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_Mg_analysis.setObjectName(u"edt_Mg_analysis")
        sizePolicy.setHeightForWidth(self.edt_Mg_analysis.sizePolicy().hasHeightForWidth())
        self.edt_Mg_analysis.setSizePolicy(sizePolicy)
        self.edt_Mg_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_Mg_analysis.setAlignment(Qt.AlignCenter)
        self.edt_Mg_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_Mg_analysis, 6, 6, 1, 1)

        self.edt_K_mg_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_K_mg_analysis.setObjectName(u"edt_K_mg_analysis")
        sizePolicy.setHeightForWidth(self.edt_K_mg_analysis.sizePolicy().hasHeightForWidth())
        self.edt_K_mg_analysis.setSizePolicy(sizePolicy)
        self.edt_K_mg_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_K_mg_analysis.setAlignment(Qt.AlignCenter)
        self.edt_K_mg_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_K_mg_analysis, 9, 3, 1, 1)

        self.lbl_N_analysis = QLabel(self.frm_register_analysis)
        self.lbl_N_analysis.setObjectName(u"lbl_N_analysis")

        self.gridLayout_2.addWidget(self.lbl_N_analysis, 11, 2, 1, 2)

        self.lbl_N_analysis_KG = QLabel(self.frm_register_analysis)
        self.lbl_N_analysis_KG.setObjectName(u"lbl_N_analysis_KG")

        self.gridLayout_2.addWidget(self.lbl_N_analysis_KG, 11, 8, 1, 2)

        self.edt_B_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_B_analysis.setObjectName(u"edt_B_analysis")
        sizePolicy.setHeightForWidth(self.edt_B_analysis.sizePolicy().hasHeightForWidth())
        self.edt_B_analysis.setSizePolicy(sizePolicy)
        self.edt_B_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_B_analysis.setAlignment(Qt.AlignCenter)
        self.edt_B_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_B_analysis, 9, 5, 1, 1)

        self.lbl_B_analysis = QLabel(self.frm_register_analysis)
        self.lbl_B_analysis.setObjectName(u"lbl_B_analysis")

        self.gridLayout_2.addWidget(self.lbl_B_analysis, 8, 5, 1, 1)

        self.edt_P_meh_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_P_meh_analysis.setObjectName(u"edt_P_meh_analysis")
        sizePolicy.setHeightForWidth(self.edt_P_meh_analysis.sizePolicy().hasHeightForWidth())
        self.edt_P_meh_analysis.setSizePolicy(sizePolicy)
        self.edt_P_meh_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_P_meh_analysis.setAlignment(Qt.AlignCenter)
        self.edt_P_meh_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_P_meh_analysis, 9, 0, 1, 1)

        self.edt_sector_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_sector_analysis.setObjectName(u"edt_sector_analysis")
        sizePolicy.setHeightForWidth(self.edt_sector_analysis.sizePolicy().hasHeightForWidth())
        self.edt_sector_analysis.setSizePolicy(sizePolicy)

        self.gridLayout_2.addWidget(self.edt_sector_analysis, 1, 6, 1, 4)

        self.edt_name_producer_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_name_producer_analysis.setObjectName(u"edt_name_producer_analysis")
        self.edt_name_producer_analysis.setEnabled(True)
        sizePolicy.setHeightForWidth(self.edt_name_producer_analysis.sizePolicy().hasHeightForWidth())
        self.edt_name_producer_analysis.setSizePolicy(sizePolicy)
        self.edt_name_producer_analysis.setMinimumSize(QSize(145, 0))
        self.edt_name_producer_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_name_producer_analysis.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.edt_name_producer_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_name_producer_analysis, 1, 2, 1, 4)

        self.edt_MO_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_MO_analysis.setObjectName(u"edt_MO_analysis")
        sizePolicy.setHeightForWidth(self.edt_MO_analysis.sizePolicy().hasHeightForWidth())
        self.edt_MO_analysis.setSizePolicy(sizePolicy)
        self.edt_MO_analysis.setMinimumSize(QSize(0, 0))
        self.edt_MO_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_MO_analysis.setSizeIncrement(QSize(0, 0))
        self.edt_MO_analysis.setAlignment(Qt.AlignCenter)
        self.edt_MO_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_MO_analysis, 9, 10, 1, 1)

        self.edt_pre_sowing_P2O5_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_pre_sowing_P2O5_analysis.setObjectName(u"edt_pre_sowing_P2O5_analysis")
        sizePolicy.setHeightForWidth(self.edt_pre_sowing_P2O5_analysis.sizePolicy().hasHeightForWidth())
        self.edt_pre_sowing_P2O5_analysis.setSizePolicy(sizePolicy)
        self.edt_pre_sowing_P2O5_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_pre_sowing_P2O5_analysis.setAlignment(Qt.AlignCenter)
        self.edt_pre_sowing_P2O5_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_pre_sowing_P2O5_analysis, 12, 4, 1, 2)

        self.edt_t_effective_CTC_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_t_effective_CTC_analysis.setObjectName(u"edt_t_effective_CTC_analysis")
        sizePolicy.setHeightForWidth(self.edt_t_effective_CTC_analysis.sizePolicy().hasHeightForWidth())
        self.edt_t_effective_CTC_analysis.setSizePolicy(sizePolicy)
        self.edt_t_effective_CTC_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_t_effective_CTC_analysis.setAlignment(Qt.AlignCenter)
        self.edt_t_effective_CTC_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_t_effective_CTC_analysis, 6, 10, 1, 1)

        self.edt_planting_fertilizer_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_planting_fertilizer_analysis.setObjectName(u"edt_planting_fertilizer_analysis")
        sizePolicy.setHeightForWidth(self.edt_planting_fertilizer_analysis.sizePolicy().hasHeightForWidth())
        self.edt_planting_fertilizer_analysis.setSizePolicy(sizePolicy)
        self.edt_planting_fertilizer_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_planting_fertilizer_analysis.setAlignment(Qt.AlignCenter)
        self.edt_planting_fertilizer_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_planting_fertilizer_analysis, 13, 1, 1, 1)

        self.lbl_planting_analysis = QLabel(self.frm_register_analysis)
        self.lbl_planting_analysis.setObjectName(u"lbl_planting_analysis")

        self.gridLayout_2.addWidget(self.lbl_planting_analysis, 13, 0, 1, 1)

        self.edt_planting_fertilizer_N_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_planting_fertilizer_N_analysis.setObjectName(u"edt_planting_fertilizer_N_analysis")
        sizePolicy.setHeightForWidth(self.edt_planting_fertilizer_N_analysis.sizePolicy().hasHeightForWidth())
        self.edt_planting_fertilizer_N_analysis.setSizePolicy(sizePolicy)
        self.edt_planting_fertilizer_N_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_planting_fertilizer_N_analysis.setAlignment(Qt.AlignCenter)
        self.edt_planting_fertilizer_N_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_planting_fertilizer_N_analysis, 13, 2, 1, 2)

        self.edt_Fe_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_Fe_analysis.setObjectName(u"edt_Fe_analysis")
        sizePolicy.setHeightForWidth(self.edt_Fe_analysis.sizePolicy().hasHeightForWidth())
        self.edt_Fe_analysis.setSizePolicy(sizePolicy)
        self.edt_Fe_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_Fe_analysis.setAlignment(Qt.AlignCenter)
        self.edt_Fe_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_Fe_analysis, 9, 7, 1, 1)

        self.edt_planting_fertilizer_N_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_planting_fertilizer_N_analysis_KG.setObjectName(u"edt_planting_fertilizer_N_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_planting_fertilizer_N_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_planting_fertilizer_N_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_planting_fertilizer_N_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_planting_fertilizer_N_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_planting_fertilizer_N_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_planting_fertilizer_N_analysis_KG, 13, 8, 1, 2)

        self.edt_planting_fertilizer_K2O_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_planting_fertilizer_K2O_analysis.setObjectName(u"edt_planting_fertilizer_K2O_analysis")
        sizePolicy.setHeightForWidth(self.edt_planting_fertilizer_K2O_analysis.sizePolicy().hasHeightForWidth())
        self.edt_planting_fertilizer_K2O_analysis.setSizePolicy(sizePolicy)
        self.edt_planting_fertilizer_K2O_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_planting_fertilizer_K2O_analysis.setAlignment(Qt.AlignCenter)
        self.edt_planting_fertilizer_K2O_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_planting_fertilizer_K2O_analysis, 13, 6, 1, 2)

        self.edt_pre_sowing_N_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_pre_sowing_N_analysis_KG.setObjectName(u"edt_pre_sowing_N_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_pre_sowing_N_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_pre_sowing_N_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_pre_sowing_N_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_pre_sowing_N_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_pre_sowing_N_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_pre_sowing_N_analysis_KG, 12, 8, 1, 2)

        self.edt_Mn_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_Mn_analysis.setObjectName(u"edt_Mn_analysis")
        sizePolicy.setHeightForWidth(self.edt_Mn_analysis.sizePolicy().hasHeightForWidth())
        self.edt_Mn_analysis.setSizePolicy(sizePolicy)
        self.edt_Mn_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_Mn_analysis.setAlignment(Qt.AlignCenter)
        self.edt_Mn_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_Mn_analysis, 9, 8, 1, 1)

        self.edt_Zn_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_Zn_analysis.setObjectName(u"edt_Zn_analysis")
        sizePolicy.setHeightForWidth(self.edt_Zn_analysis.sizePolicy().hasHeightForWidth())
        self.edt_Zn_analysis.setSizePolicy(sizePolicy)
        self.edt_Zn_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_Zn_analysis.setAlignment(Qt.AlignCenter)
        self.edt_Zn_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_Zn_analysis, 9, 9, 1, 1)

        self.edt_planting_fertilizer_P2O5_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_planting_fertilizer_P2O5_analysis.setObjectName(u"edt_planting_fertilizer_P2O5_analysis")
        sizePolicy.setHeightForWidth(self.edt_planting_fertilizer_P2O5_analysis.sizePolicy().hasHeightForWidth())
        self.edt_planting_fertilizer_P2O5_analysis.setSizePolicy(sizePolicy)
        self.edt_planting_fertilizer_P2O5_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_planting_fertilizer_P2O5_analysis.setAlignment(Qt.AlignCenter)
        self.edt_planting_fertilizer_P2O5_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_planting_fertilizer_P2O5_analysis, 13, 4, 1, 2)

        self.edt_clay_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_clay_analysis.setObjectName(u"edt_clay_analysis")
        sizePolicy.setHeightForWidth(self.edt_clay_analysis.sizePolicy().hasHeightForWidth())
        self.edt_clay_analysis.setSizePolicy(sizePolicy)
        self.edt_clay_analysis.setMinimumSize(QSize(0, 0))
        self.edt_clay_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_clay_analysis.setAlignment(Qt.AlignCenter)
        self.edt_clay_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_clay_analysis, 9, 12, 1, 2)

        self.lbl_NPK_analysis = QLabel(self.frm_register_analysis)
        self.lbl_NPK_analysis.setObjectName(u"lbl_NPK_analysis")

        self.gridLayout_2.addWidget(self.lbl_NPK_analysis, 11, 1, 1, 1)

        self.edt_planting_fertilizer_P2O5_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_planting_fertilizer_P2O5_analysis_KG.setObjectName(u"edt_planting_fertilizer_P2O5_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_planting_fertilizer_P2O5_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_planting_fertilizer_P2O5_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_planting_fertilizer_P2O5_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_planting_fertilizer_P2O5_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_planting_fertilizer_P2O5_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_planting_fertilizer_P2O5_analysis_KG, 13, 10, 1, 2)

        self.edt_pre_sowing_N_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_pre_sowing_N_analysis.setObjectName(u"edt_pre_sowing_N_analysis")
        sizePolicy.setHeightForWidth(self.edt_pre_sowing_N_analysis.sizePolicy().hasHeightForWidth())
        self.edt_pre_sowing_N_analysis.setSizePolicy(sizePolicy)
        self.edt_pre_sowing_N_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_pre_sowing_N_analysis.setAlignment(Qt.AlignCenter)
        self.edt_pre_sowing_N_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_pre_sowing_N_analysis, 12, 2, 1, 2)

        self.edt_pre_sowing_P2O5_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_pre_sowing_P2O5_analysis_KG.setObjectName(u"edt_pre_sowing_P2O5_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_pre_sowing_P2O5_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_pre_sowing_P2O5_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_pre_sowing_P2O5_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_pre_sowing_P2O5_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_pre_sowing_P2O5_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_pre_sowing_P2O5_analysis_KG, 12, 10, 1, 2)

        self.edt_pre_sowing_fertilizer_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_pre_sowing_fertilizer_analysis.setObjectName(u"edt_pre_sowing_fertilizer_analysis")
        sizePolicy.setHeightForWidth(self.edt_pre_sowing_fertilizer_analysis.sizePolicy().hasHeightForWidth())
        self.edt_pre_sowing_fertilizer_analysis.setSizePolicy(sizePolicy)
        self.edt_pre_sowing_fertilizer_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_pre_sowing_fertilizer_analysis.setAlignment(Qt.AlignCenter)
        self.edt_pre_sowing_fertilizer_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_pre_sowing_fertilizer_analysis, 12, 1, 1, 1)

        self.edt_pre_sowing_K2O_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_pre_sowing_K2O_analysis.setObjectName(u"edt_pre_sowing_K2O_analysis")
        sizePolicy.setHeightForWidth(self.edt_pre_sowing_K2O_analysis.sizePolicy().hasHeightForWidth())
        self.edt_pre_sowing_K2O_analysis.setSizePolicy(sizePolicy)
        self.edt_pre_sowing_K2O_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_pre_sowing_K2O_analysis.setAlignment(Qt.AlignCenter)
        self.edt_pre_sowing_K2O_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_pre_sowing_K2O_analysis, 12, 6, 1, 2)

        self.edt_pre_sowing_K2O_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_pre_sowing_K2O_analysis_KG.setObjectName(u"edt_pre_sowing_K2O_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_pre_sowing_K2O_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_pre_sowing_K2O_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_pre_sowing_K2O_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_pre_sowing_K2O_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_pre_sowing_K2O_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_pre_sowing_K2O_analysis_KG, 12, 12, 1, 2)

        self.edt_planting_fertilizer_K2O_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_planting_fertilizer_K2O_analysis_KG.setObjectName(u"edt_planting_fertilizer_K2O_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_planting_fertilizer_K2O_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_planting_fertilizer_K2O_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_planting_fertilizer_K2O_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_planting_fertilizer_K2O_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_planting_fertilizer_K2O_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_planting_fertilizer_K2O_analysis_KG, 13, 12, 1, 2)

        self.edt_CO_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_CO_analysis.setObjectName(u"edt_CO_analysis")
        sizePolicy.setHeightForWidth(self.edt_CO_analysis.sizePolicy().hasHeightForWidth())
        self.edt_CO_analysis.setSizePolicy(sizePolicy)
        self.edt_CO_analysis.setMinimumSize(QSize(0, 0))
        self.edt_CO_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_CO_analysis.setAlignment(Qt.AlignCenter)
        self.edt_CO_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_CO_analysis, 9, 11, 1, 1)

        self.lbl_micro_co_analysis = QLabel(self.frm_register_analysis)
        self.lbl_micro_co_analysis.setObjectName(u"lbl_micro_co_analysis")
        self.lbl_micro_co_analysis.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.lbl_micro_co_analysis, 15, 7, 1, 1)

        self.lbl_pre_sowing_analysis = QLabel(self.frm_register_analysis)
        self.lbl_pre_sowing_analysis.setObjectName(u"lbl_pre_sowing_analysis")

        self.gridLayout_2.addWidget(self.lbl_pre_sowing_analysis, 12, 0, 1, 1)

        self.lbl_P2O5_analysis_KG = QLabel(self.frm_register_analysis)
        self.lbl_P2O5_analysis_KG.setObjectName(u"lbl_P2O5_analysis_KG")

        self.gridLayout_2.addWidget(self.lbl_P2O5_analysis_KG, 11, 10, 1, 2)

        self.edt_top_dressing_P2O5_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_top_dressing_P2O5_analysis.setObjectName(u"edt_top_dressing_P2O5_analysis")
        sizePolicy.setHeightForWidth(self.edt_top_dressing_P2O5_analysis.sizePolicy().hasHeightForWidth())
        self.edt_top_dressing_P2O5_analysis.setSizePolicy(sizePolicy)
        self.edt_top_dressing_P2O5_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_top_dressing_P2O5_analysis.setAlignment(Qt.AlignCenter)
        self.edt_top_dressing_P2O5_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_top_dressing_P2O5_analysis, 14, 4, 1, 2)

        self.lbl_micro_zn_analysis = QLabel(self.frm_register_analysis)
        self.lbl_micro_zn_analysis.setObjectName(u"lbl_micro_zn_analysis")

        self.gridLayout_2.addWidget(self.lbl_micro_zn_analysis, 15, 2, 1, 1)

        self.edt_top_dressing_P2O5_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_top_dressing_P2O5_analysis_KG.setObjectName(u"edt_top_dressing_P2O5_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_top_dressing_P2O5_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_top_dressing_P2O5_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_top_dressing_P2O5_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_top_dressing_P2O5_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_top_dressing_P2O5_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_top_dressing_P2O5_analysis_KG, 14, 10, 1, 2)

        self.edt_micro_b_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_b_analysis.setObjectName(u"edt_micro_b_analysis")
        sizePolicy.setHeightForWidth(self.edt_micro_b_analysis.sizePolicy().hasHeightForWidth())
        self.edt_micro_b_analysis.setSizePolicy(sizePolicy)
        self.edt_micro_b_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_b_analysis.setAlignment(Qt.AlignCenter)
        self.edt_micro_b_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_micro_b_analysis, 16, 3, 1, 1)

        self.lbl_micro_mo_analysis = QLabel(self.frm_register_analysis)
        self.lbl_micro_mo_analysis.setObjectName(u"lbl_micro_mo_analysis")

        self.gridLayout_2.addWidget(self.lbl_micro_mo_analysis, 15, 6, 1, 1)

        self.edt_top_dressing_N_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_top_dressing_N_analysis.setObjectName(u"edt_top_dressing_N_analysis")
        sizePolicy.setHeightForWidth(self.edt_top_dressing_N_analysis.sizePolicy().hasHeightForWidth())
        self.edt_top_dressing_N_analysis.setSizePolicy(sizePolicy)
        self.edt_top_dressing_N_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_top_dressing_N_analysis.setAlignment(Qt.AlignCenter)
        self.edt_top_dressing_N_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_top_dressing_N_analysis, 14, 2, 1, 2)

        self.edt_micro_cu_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_cu_analysis.setObjectName(u"edt_micro_cu_analysis")
        sizePolicy.setHeightForWidth(self.edt_micro_cu_analysis.sizePolicy().hasHeightForWidth())
        self.edt_micro_cu_analysis.setSizePolicy(sizePolicy)
        self.edt_micro_cu_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_cu_analysis.setAlignment(Qt.AlignCenter)
        self.edt_micro_cu_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_micro_cu_analysis, 16, 4, 1, 1)

        self.edt_micro_mn_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_mn_analysis.setObjectName(u"edt_micro_mn_analysis")
        sizePolicy.setHeightForWidth(self.edt_micro_mn_analysis.sizePolicy().hasHeightForWidth())
        self.edt_micro_mn_analysis.setSizePolicy(sizePolicy)
        self.edt_micro_mn_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_mn_analysis.setAlignment(Qt.AlignCenter)
        self.edt_micro_mn_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_micro_mn_analysis, 16, 5, 1, 1)

        self.edt_top_dressing_K2O_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_top_dressing_K2O_analysis.setObjectName(u"edt_top_dressing_K2O_analysis")
        sizePolicy.setHeightForWidth(self.edt_top_dressing_K2O_analysis.sizePolicy().hasHeightForWidth())
        self.edt_top_dressing_K2O_analysis.setSizePolicy(sizePolicy)
        self.edt_top_dressing_K2O_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_top_dressing_K2O_analysis.setAlignment(Qt.AlignCenter)
        self.edt_top_dressing_K2O_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_top_dressing_K2O_analysis, 14, 6, 1, 2)

        self.edt_micro_zn_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_zn_analysis.setObjectName(u"edt_micro_zn_analysis")
        sizePolicy.setHeightForWidth(self.edt_micro_zn_analysis.sizePolicy().hasHeightForWidth())
        self.edt_micro_zn_analysis.setSizePolicy(sizePolicy)
        self.edt_micro_zn_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_zn_analysis.setAlignment(Qt.AlignCenter)
        self.edt_micro_zn_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_micro_zn_analysis, 16, 2, 1, 1)

        self.edt_micro_co_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_co_analysis.setObjectName(u"edt_micro_co_analysis")
        sizePolicy.setHeightForWidth(self.edt_micro_co_analysis.sizePolicy().hasHeightForWidth())
        self.edt_micro_co_analysis.setSizePolicy(sizePolicy)
        self.edt_micro_co_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_co_analysis.setAlignment(Qt.AlignCenter)
        self.edt_micro_co_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_micro_co_analysis, 16, 7, 1, 1)

        self.edt_top_dressing_N_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_top_dressing_N_analysis_KG.setObjectName(u"edt_top_dressing_N_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_top_dressing_N_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_top_dressing_N_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_top_dressing_N_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_top_dressing_N_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_top_dressing_N_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_top_dressing_N_analysis_KG, 14, 8, 1, 2)

        self.lbl_micro_b_analysis = QLabel(self.frm_register_analysis)
        self.lbl_micro_b_analysis.setObjectName(u"lbl_micro_b_analysis")
        self.lbl_micro_b_analysis.setMinimumSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.lbl_micro_b_analysis, 15, 3, 1, 1)

        self.edt_top_dressing_K2O_analysis_KG = QLineEdit(self.frm_register_analysis)
        self.edt_top_dressing_K2O_analysis_KG.setObjectName(u"edt_top_dressing_K2O_analysis_KG")
        sizePolicy.setHeightForWidth(self.edt_top_dressing_K2O_analysis_KG.sizePolicy().hasHeightForWidth())
        self.edt_top_dressing_K2O_analysis_KG.setSizePolicy(sizePolicy)
        self.edt_top_dressing_K2O_analysis_KG.setMaximumSize(QSize(16777215, 16777215))
        self.edt_top_dressing_K2O_analysis_KG.setAlignment(Qt.AlignCenter)
        self.edt_top_dressing_K2O_analysis_KG.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_top_dressing_K2O_analysis_KG, 14, 12, 1, 2)

        self.edt_top_dressing_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_top_dressing_analysis.setObjectName(u"edt_top_dressing_analysis")
        sizePolicy.setHeightForWidth(self.edt_top_dressing_analysis.sizePolicy().hasHeightForWidth())
        self.edt_top_dressing_analysis.setSizePolicy(sizePolicy)
        self.edt_top_dressing_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_top_dressing_analysis.setAlignment(Qt.AlignCenter)
        self.edt_top_dressing_analysis.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_top_dressing_analysis, 14, 1, 1, 1)

        self.lbl_micro_cu_analysis = QLabel(self.frm_register_analysis)
        self.lbl_micro_cu_analysis.setObjectName(u"lbl_micro_cu_analysis")

        self.gridLayout_2.addWidget(self.lbl_micro_cu_analysis, 15, 4, 1, 1)

        self.lbl_top_dressing_analysis = QLabel(self.frm_register_analysis)
        self.lbl_top_dressing_analysis.setObjectName(u"lbl_top_dressing_analysis")
        self.lbl_top_dressing_analysis.setMinimumSize(QSize(51, 0))

        self.gridLayout_2.addWidget(self.lbl_top_dressing_analysis, 14, 0, 1, 1)

        self.lbl_micro_mn_analysis = QLabel(self.frm_register_analysis)
        self.lbl_micro_mn_analysis.setObjectName(u"lbl_micro_mn_analysis")

        self.gridLayout_2.addWidget(self.lbl_micro_mn_analysis, 15, 5, 1, 1)

        self.lbl_latitude_analysis = QLabel(self.frm_register_analysis)
        self.lbl_latitude_analysis.setObjectName(u"lbl_latitude_analysis")

        self.gridLayout_2.addWidget(self.lbl_latitude_analysis, 2, 2, 1, 2)

        self.lbl_longitude = QLabel(self.frm_register_analysis)
        self.lbl_longitude.setObjectName(u"lbl_longitude")

        self.gridLayout_2.addWidget(self.lbl_longitude, 2, 4, 1, 2)

        self.lbl_agricultural_period_analysis = QLabel(self.frm_register_analysis)
        self.lbl_agricultural_period_analysis.setObjectName(u"lbl_agricultural_period_analysis")

        self.gridLayout_2.addWidget(self.lbl_agricultural_period_analysis, 0, 10, 1, 2)

        self.lbl_clay_analysis = QLabel(self.frm_register_analysis)
        self.lbl_clay_analysis.setObjectName(u"lbl_clay_analysis")

        self.gridLayout_2.addWidget(self.lbl_clay_analysis, 8, 12, 1, 2)

        self.lbl_K2O_analysis = QLabel(self.frm_register_analysis)
        self.lbl_K2O_analysis.setObjectName(u"lbl_K2O_analysis")

        self.gridLayout_2.addWidget(self.lbl_K2O_analysis, 11, 6, 1, 2)

        self.lbl_average_productivity_analysis = QLabel(self.frm_register_analysis)
        self.lbl_average_productivity_analysis.setObjectName(u"lbl_average_productivity_analysis")
        self.lbl_average_productivity_analysis.setMinimumSize(QSize(0, 0))
        self.lbl_average_productivity_analysis.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_2.addWidget(self.lbl_average_productivity_analysis, 2, 9, 1, 1)

        self.lbl_planting_system_analysis = QLabel(self.frm_register_analysis)
        self.lbl_planting_system_analysis.setObjectName(u"lbl_planting_system_analysis")

        self.gridLayout_2.addWidget(self.lbl_planting_system_analysis, 2, 6, 1, 3)

        self.label_7 = QLabel(self.frm_register_analysis)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFrameShape(QFrame.StyledPanel)
        self.label_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.label_7, 4, 9, 1, 1)

        self.edt_micro_mn_analysis_kg = QLineEdit(self.frm_register_analysis)
        self.edt_micro_mn_analysis_kg.setObjectName(u"edt_micro_mn_analysis_kg")
        sizePolicy.setHeightForWidth(self.edt_micro_mn_analysis_kg.sizePolicy().hasHeightForWidth())
        self.edt_micro_mn_analysis_kg.setSizePolicy(sizePolicy)
        self.edt_micro_mn_analysis_kg.setMinimumSize(QSize(55, 0))
        self.edt_micro_mn_analysis_kg.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_mn_analysis_kg.setAlignment(Qt.AlignCenter)
        self.edt_micro_mn_analysis_kg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_micro_mn_analysis_kg, 18, 5, 1, 1)

        self.lbl_plaster_analysis = QLabel(self.frm_register_analysis)
        self.lbl_plaster_analysis.setObjectName(u"lbl_plaster_analysis")

        self.gridLayout_2.addWidget(self.lbl_plaster_analysis, 15, 12, 1, 1)

        self.edt_micro_cu_analysis_kg = QLineEdit(self.frm_register_analysis)
        self.edt_micro_cu_analysis_kg.setObjectName(u"edt_micro_cu_analysis_kg")
        sizePolicy.setHeightForWidth(self.edt_micro_cu_analysis_kg.sizePolicy().hasHeightForWidth())
        self.edt_micro_cu_analysis_kg.setSizePolicy(sizePolicy)
        self.edt_micro_cu_analysis_kg.setMinimumSize(QSize(55, 0))
        self.edt_micro_cu_analysis_kg.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_cu_analysis_kg.setAlignment(Qt.AlignCenter)
        self.edt_micro_cu_analysis_kg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_micro_cu_analysis_kg, 18, 4, 1, 1)

        self.edt_micro_co_analysis_kg = QLineEdit(self.frm_register_analysis)
        self.edt_micro_co_analysis_kg.setObjectName(u"edt_micro_co_analysis_kg")
        sizePolicy.setHeightForWidth(self.edt_micro_co_analysis_kg.sizePolicy().hasHeightForWidth())
        self.edt_micro_co_analysis_kg.setSizePolicy(sizePolicy)
        self.edt_micro_co_analysis_kg.setMinimumSize(QSize(55, 0))
        self.edt_micro_co_analysis_kg.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_co_analysis_kg.setAlignment(Qt.AlignCenter)
        self.edt_micro_co_analysis_kg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_micro_co_analysis_kg, 18, 7, 1, 1)

        self.edt_micro_mo_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_mo_analysis.setObjectName(u"edt_micro_mo_analysis")
        sizePolicy.setHeightForWidth(self.edt_micro_mo_analysis.sizePolicy().hasHeightForWidth())
        self.edt_micro_mo_analysis.setSizePolicy(sizePolicy)
        self.edt_micro_mo_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_mo_analysis.setAlignment(Qt.AlignCenter)
        self.edt_micro_mo_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_micro_mo_analysis, 16, 6, 1, 1)

        self.lbl_tca_analysis = QLabel(self.frm_register_analysis)
        self.lbl_tca_analysis.setObjectName(u"lbl_tca_analysis")

        self.gridLayout_2.addWidget(self.lbl_tca_analysis, 15, 13, 1, 1)

        self.edt_micro_ca_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_ca_analysis.setObjectName(u"edt_micro_ca_analysis")
        self.edt_micro_ca_analysis.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.edt_micro_ca_analysis, 16, 8, 1, 1)

        self.lbl_K2O_analysis_KG = QLabel(self.frm_register_analysis)
        self.lbl_K2O_analysis_KG.setObjectName(u"lbl_K2O_analysis_KG")

        self.gridLayout_2.addWidget(self.lbl_K2O_analysis_KG, 11, 12, 1, 2)

        self.edt_micro_s_analysis_kg = QLineEdit(self.frm_register_analysis)
        self.edt_micro_s_analysis_kg.setObjectName(u"edt_micro_s_analysis_kg")
        self.edt_micro_s_analysis_kg.setAlignment(Qt.AlignCenter)
        self.edt_micro_s_analysis_kg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_micro_s_analysis_kg, 18, 9, 1, 1)

        self.edt_micro_s_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_s_analysis.setObjectName(u"edt_micro_s_analysis")
        self.edt_micro_s_analysis.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.edt_micro_s_analysis, 16, 9, 1, 1)

        self.edt_micro_ca_analysis_kg = QLineEdit(self.frm_register_analysis)
        self.edt_micro_ca_analysis_kg.setObjectName(u"edt_micro_ca_analysis_kg")
        self.edt_micro_ca_analysis_kg.setAlignment(Qt.AlignCenter)
        self.edt_micro_ca_analysis_kg.setReadOnly(True)

        self.gridLayout_2.addWidget(self.edt_micro_ca_analysis_kg, 18, 8, 1, 1)

        self.lbl_micros = QLabel(self.frm_register_analysis)
        self.lbl_micros.setObjectName(u"lbl_micros")

        self.gridLayout_2.addWidget(self.lbl_micros, 16, 0, 1, 1)

        self.edt_micro_analysis = QLineEdit(self.frm_register_analysis)
        self.edt_micro_analysis.setObjectName(u"edt_micro_analysis")
        sizePolicy.setHeightForWidth(self.edt_micro_analysis.sizePolicy().hasHeightForWidth())
        self.edt_micro_analysis.setSizePolicy(sizePolicy)
        self.edt_micro_analysis.setMaximumSize(QSize(16777215, 16777215))
        self.edt_micro_analysis.setAlignment(Qt.AlignCenter)
        self.edt_micro_analysis.setReadOnly(False)

        self.gridLayout_2.addWidget(self.edt_micro_analysis, 16, 1, 1, 1)

        self.lbl_title_user_analysis = QLabel(self.frm_register_analysis)
        self.lbl_title_user_analysis.setObjectName(u"lbl_title_user_analysis")

        self.gridLayout_2.addWidget(self.lbl_title_user_analysis, 19, 0, 1, 1)

        self.lbl_kg_ha_2 = QLabel(self.frm_register_analysis)
        self.lbl_kg_ha_2.setObjectName(u"lbl_kg_ha_2")
        self.lbl_kg_ha_2.setFrameShape(QFrame.StyledPanel)
        self.lbl_kg_ha_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_kg_ha_2, 18, 12, 1, 1)

        self.lbl_kg_ha = QLabel(self.frm_register_analysis)
        self.lbl_kg_ha.setObjectName(u"lbl_kg_ha")
        self.lbl_kg_ha.setFrameShape(QFrame.StyledPanel)
        self.lbl_kg_ha.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_kg_ha, 18, 10, 1, 1)

        self.lbl_percente = QLabel(self.frm_register_analysis)
        self.lbl_percente.setObjectName(u"lbl_percente")
        self.lbl_percente.setFrameShape(QFrame.StyledPanel)
        self.lbl_percente.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_percente, 18, 11, 1, 1)

        self.lbl_percente_2 = QLabel(self.frm_register_analysis)
        self.lbl_percente_2.setObjectName(u"lbl_percente_2")
        self.lbl_percente_2.setFrameShape(QFrame.StyledPanel)
        self.lbl_percente_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.lbl_percente_2, 18, 13, 1, 1)

        self.lbl_name_user_analysis = QLabel(self.frm_register_analysis)
        self.lbl_name_user_analysis.setObjectName(u"lbl_name_user_analysis")
        self.lbl_name_user_analysis.setMaximumSize(QSize(16777215, 19))

        self.gridLayout_2.addWidget(self.lbl_name_user_analysis, 19, 1, 1, 5)

        self.lbl_micro_s_analysis = QLabel(self.frm_register_analysis)
        self.lbl_micro_s_analysis.setObjectName(u"lbl_micro_s_analysis")

        self.gridLayout_2.addWidget(self.lbl_micro_s_analysis, 15, 9, 1, 1)

        self.lbl_micro_ca_analysis = QLabel(self.frm_register_analysis)
        self.lbl_micro_ca_analysis.setObjectName(u"lbl_micro_ca_analysis")

        self.gridLayout_2.addWidget(self.lbl_micro_ca_analysis, 15, 8, 1, 1)

        self.lbl_code_producer_analysis.raise_()
        self.lbl_agricultural_period_analysis.raise_()
        self.lbl_culture_analysis.raise_()
        self.lbl_area_analysis.raise_()
        self.lbl_altitude_analysis.raise_()
        self.lbl_latitude_analysis.raise_()
        self.lbl_longitude.raise_()
        self.lbl_code_analysis.raise_()
        self.lbl_planting_system_analysis.raise_()
        self.lbl_minimum_temperature_analysis.raise_()
        self.lbl_maximum_temperature_analysis.raise_()
        self.lbl_rain_vegetative_analysis.raise_()
        self.lbl_rain_reproductive_analysis.raise_()
        self.lbl_initial_depth_analysis.raise_()
        self.lbl_final_depth_analysis.raise_()
        self.lbl_ph_H2O_analysis.raise_()
        self.lbl_ph_CaCl2_analysis.raise_()
        self.lbl_MO_analysis.raise_()
        self.lbl_CO_analysis.raise_()
        self.lbl_cm.raise_()
        self.lbl_ph_1_25.raise_()
        self.lbl_g_kg.raise_()
        self.lbl_dag_kg.raise_()
        self.lbl_K_cmolc_analysis.raise_()
        self.lbl_Ca_analysis.raise_()
        self.lbl_Mg_analysis.raise_()
        self.lbl_Al_analysis.raise_()
        self.lbl_H_Al_analysis.raise_()
        self.lbl_SB_analysis.raise_()
        self.lbl_t_effective_CTC_analysis_2.raise_()
        self.lbl_T_analysis.raise_()
        self.lbl_V_analysis.raise_()
        self.lbl_m_analysis.raise_()
        self.lbl_cmolc_dm3.raise_()
        self.lbl_percent.raise_()
        self.lbl_P_meh_analysis.raise_()
        self.lbl_P_rem_analysis.raise_()
        self.lbl_Na_analysis.raise_()
        self.lbl_K_mg_analysis.raise_()
        self.lbl_S_SO4_analysis.raise_()
        self.lbl_B_analysis.raise_()
        self.lbl_Cu_analysis.raise_()
        self.lbl_Fe_analysis.raise_()
        self.lbl_Mn_analysis.raise_()
        self.lbl_Zn_analysis.raise_()
        self.lbl_mg_dm3.raise_()
        self.lbl_NPK_analysis.raise_()
        self.lbl_N_analysis.raise_()
        self.lbl_P2O5_analysis.raise_()
        self.lbl_K2O_analysis.raise_()
        self.lbl_N_analysis_KG.raise_()
        self.lbl_P2O5_analysis_KG.raise_()
        self.lbl_K2O_analysis_KG.raise_()
        self.lbl_pre_sowing_analysis.raise_()
        self.lbl_planting_analysis.raise_()
        self.lbl_top_dressing_analysis.raise_()
        self.lbl_average_productivity_analysis.raise_()
        self.lbl_clay_analysis.raise_()
        self.label_2.raise_()
        self.lbl_name_producer_analysis.raise_()
        self.edt_final_depth_analysis.raise_()
        self.edt_SB_analysis.raise_()
        self.edt_Zn_analysis.raise_()
        self.edt_K_cmolc_analysis.raise_()
        self.edt_Ca_analysis.raise_()
        self.edt_ph_CaCl2_analysis.raise_()
        self.edt_average_productivity_analysis.raise_()
        self.edt_rain_vegetative_analysis.raise_()
        self.edt_pre_sowing_K2O_analysis_KG.raise_()
        self.edt_agricultural_period_analysis.raise_()
        self.edt_planting_fertilizer_P2O5_analysis_KG.raise_()
        self.edt_rain_reproductive_analysis.raise_()
        self.cbx_culture_analysis.raise_()
        self.edt_Cu_analysis.raise_()
        self.edt_P_meh_analysis.raise_()
        self.edt_code_producer.raise_()
        self.edt_CO_analysis.raise_()
        self.edt_initial_depth_analysis.raise_()
        self.edt_Al_analysis.raise_()
        self.edt_top_dressing_K2O_analysis.raise_()
        self.edt_Mg_analysis.raise_()
        self.edt_T_analysis.raise_()
        self.edt_top_dressing_P2O5_analysis.raise_()
        self.edt_planting_fertilizer_K2O_analysis_KG.raise_()
        self.edt_name_producer_analysis.raise_()
        self.edt_latitude_analysis.raise_()
        self.cbx_planting_system_analysis.raise_()
        self.edt_area_analysis.raise_()
        self.edt_B_analysis.raise_()
        self.edt_pre_sowing_K2O_analysis.raise_()
        self.edt_top_dressing_N_analysis_KG.raise_()
        self.edt_minimum_temperature_analysis.raise_()
        self.edt_t_effective_CTC_analysis.raise_()
        self.edt_K_mg_analysis.raise_()
        self.edt_V_analysis.raise_()
        self.edt_H_Al_analysis.raise_()
        self.edt_planting_fertilizer_K2O_analysis.raise_()
        self.edt_top_dressing_analysis.raise_()
        self.edt_pre_sowing_N_analysis_KG.raise_()
        self.edt_planting_fertilizer_P2O5_analysis.raise_()
        self.edt_altitude_analysis.raise_()
        self.edt_maximum_temperature_analysis.raise_()
        self.edt_Na_analysis.raise_()
        self.edt_top_dressing_K2O_analysis_KG.raise_()
        self.edt_Fe_analysis.raise_()
        self.edt_longitude_analysis.raise_()
        self.edt_planting_fertilizer_N_analysis.raise_()
        self.edt_MO_analysis.raise_()
        self.edt_m_analysis.raise_()
        self.edt_pre_sowing_N_analysis.raise_()
        self.edt_pre_sowing_P2O5_analysis.raise_()
        self.edt_planting_fertilizer_N_analysis_KG.raise_()
        self.edt_Mn_analysis.raise_()
        self.edt_clay_analysis.raise_()
        self.edt_ph_H2O_analysis.raise_()
        self.edt_planting_fertilizer_analysis.raise_()
        self.edt_top_dressing_P2O5_analysis_KG.raise_()
        self.edt_S_SO4_analysis.raise_()
        self.edt_P_rem_analysis.raise_()
        self.edt_pre_sowing_P2O5_analysis_KG.raise_()
        self.edt_pre_sowing_fertilizer_analysis.raise_()
        self.edt_top_dressing_N_analysis.raise_()
        self.edt_micro_zn_analysis.raise_()
        self.edt_micro_b_analysis.raise_()
        self.lbl_micro_zn_analysis.raise_()
        self.lbl_micro_b_analysis.raise_()
        self.lbl_micro_mn_analysis.raise_()
        self.edt_micro_mn_analysis.raise_()
        self.lbl_micro_cu_analysis.raise_()
        self.edt_micro_cu_analysis.raise_()
        self.lbl_micro_co_analysis.raise_()
        self.edt_micro_co_analysis.raise_()
        self.lbl_micro_mo_analysis.raise_()
        self.edt_micro_mo_analysis.raise_()
        self.lbl_percent_3.raise_()
        self.lbl_percent_4.raise_()
        self.edt_sector_analysis.raise_()
        self.lbl_sector_analysis.raise_()
        self.label_7.raise_()
        self.edt_micro_mo_analysis_kg.raise_()
        self.edt_micro_co_analysis_kg.raise_()
        self.edt_tca_analysis.raise_()
        self.edt_plaster_analysis.raise_()
        self.lbl_plaster_analysis.raise_()
        self.lbl_tca_analysis.raise_()
        self.edt_micro_mn_analysis_kg.raise_()
        self.edt_micro_cu_analysis_kg.raise_()
        self.edt_micro_b_analysis_kg.raise_()
        self.lbl_prnt_analysis.raise_()
        self.edt_prnt_analysis.raise_()
        self.edt_limestone_analysis.raise_()
        self.lbl_limestone_analysis.raise_()
        self.edt_micro_zn_analysis_kg.raise_()
        self.edt_micro_ca_analysis.raise_()
        self.edt_micro_s_analysis.raise_()
        self.edt_micro_ca_analysis_kg.raise_()
        self.edt_micro_s_analysis_kg.raise_()
        self.edt_micro_analysis.raise_()
        self.lbl_micros.raise_()
        self.lbl_kg_ha_.raise_()
        self.lbl_title_user_analysis.raise_()
        self.lbl_name_user_analysis.raise_()
        self.lbl_kg_ha.raise_()
        self.lbl_kg_ha_2.raise_()
        self.lbl_percente.raise_()
        self.lbl_percente_2.raise_()
        self.lbl_micro_s_analysis.raise_()
        self.lbl_micro_ca_analysis.raise_()

        self.horizontalLayout_3.addWidget(self.frm_register_analysis)

        self.frm_menu_analysis_register = QFrame(self.tab_register_analysis01)
        self.frm_menu_analysis_register.setObjectName(u"frm_menu_analysis_register")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.frm_menu_analysis_register.sizePolicy().hasHeightForWidth())
        self.frm_menu_analysis_register.setSizePolicy(sizePolicy2)
        self.frm_menu_analysis_register.setMaximumSize(QSize(16777215, 16777215))
        self.frm_menu_analysis_register.setFrameShape(QFrame.Box)
        self.frm_menu_analysis_register.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frm_menu_analysis_register)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_insert_analysis = QPushButton(self.frm_menu_analysis_register)
        self.btn_insert_analysis.setObjectName(u"btn_insert_analysis")
        self.btn_insert_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_insert_analysis.setFocusPolicy(Qt.NoFocus)
        icon9 = QIcon()
        icon9.addFile(u":/buttons/images/button/Insert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_insert_analysis.setIcon(icon9)

        self.verticalLayout_16.addWidget(self.btn_insert_analysis)

        self.btn_update_analysis = QPushButton(self.frm_menu_analysis_register)
        self.btn_update_analysis.setObjectName(u"btn_update_analysis")
        self.btn_update_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update_analysis.setFocusPolicy(Qt.NoFocus)
        icon10 = QIcon()
        icon10.addFile(u":/buttons/images/button/Update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_update_analysis.setIcon(icon10)

        self.verticalLayout_16.addWidget(self.btn_update_analysis)

        self.btn_consult_analysis = QPushButton(self.frm_menu_analysis_register)
        self.btn_consult_analysis.setObjectName(u"btn_consult_analysis")
        self.btn_consult_analysis.setEnabled(False)
        self.btn_consult_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/buttons/images/button/search.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_consult_analysis.setIcon(icon11)

        self.verticalLayout_16.addWidget(self.btn_consult_analysis)

        self.btn_cancelar_analysis = QPushButton(self.frm_menu_analysis_register)
        self.btn_cancelar_analysis.setObjectName(u"btn_cancelar_analysis")
        self.btn_cancelar_analysis.setEnabled(False)
        self.btn_cancelar_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancelar_analysis.setFocusPolicy(Qt.NoFocus)
        icon12 = QIcon()
        icon12.addFile(u":/buttons/images/button/Delete.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_cancelar_analysis.setIcon(icon12)

        self.verticalLayout_16.addWidget(self.btn_cancelar_analysis)

        self.btn_save_change_analysis = QPushButton(self.frm_menu_analysis_register)
        self.btn_save_change_analysis.setObjectName(u"btn_save_change_analysis")
        self.btn_save_change_analysis.setEnabled(False)
        self.btn_save_change_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_change_analysis.setFocusPolicy(Qt.NoFocus)
        icon13 = QIcon()
        icon13.addFile(u":/buttons/images/button/Save-Update.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_change_analysis.setIcon(icon13)

        self.verticalLayout_16.addWidget(self.btn_save_change_analysis)

        self.btn_save_analysis = QPushButton(self.frm_menu_analysis_register)
        self.btn_save_analysis.setObjectName(u"btn_save_analysis")
        self.btn_save_analysis.setEnabled(False)
        self.btn_save_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_analysis.setFocusPolicy(Qt.NoFocus)
        icon14 = QIcon()
        icon14.addFile(u":/buttons/images/button/Save-Insert.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save_analysis.setIcon(icon14)

        self.verticalLayout_16.addWidget(self.btn_save_analysis)

        self.btn_Interpretation_analysis = QPushButton(self.frm_menu_analysis_register)
        self.btn_Interpretation_analysis.setObjectName(u"btn_Interpretation_analysis")
        self.btn_Interpretation_analysis.setEnabled(True)
        self.btn_Interpretation_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_Interpretation_analysis.setIcon(icon3)

        self.verticalLayout_16.addWidget(self.btn_Interpretation_analysis)

        self.btn_productivity_prediction = QPushButton(self.frm_menu_analysis_register)
        self.btn_productivity_prediction.setObjectName(u"btn_productivity_prediction")
        self.btn_productivity_prediction.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_productivity_prediction.setIcon(icon4)

        self.verticalLayout_16.addWidget(self.btn_productivity_prediction)

        self.verticalSpacer_analysis = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_analysis)


        self.horizontalLayout_3.addWidget(self.frm_menu_analysis_register)


        self.verticalLayout_11.addLayout(self.horizontalLayout_3)

        self.tab_register_analysis.addTab(self.tab_register_analysis01, "")
        self.tab_register_analysis02 = QWidget()
        self.tab_register_analysis02.setObjectName(u"tab_register_analysis02")
        self.verticalLayout_5 = QVBoxLayout(self.tab_register_analysis02)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.lbl_title_register_analysis = QLabel(self.tab_register_analysis02)
        self.lbl_title_register_analysis.setObjectName(u"lbl_title_register_analysis")

        self.verticalLayout_5.addWidget(self.lbl_title_register_analysis)

        self.frame = QFrame(self.tab_register_analysis02)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lbl_agricultural_period_analysis_3 = QLabel(self.frame)
        self.lbl_agricultural_period_analysis_3.setObjectName(u"lbl_agricultural_period_analysis_3")

        self.gridLayout_3.addWidget(self.lbl_agricultural_period_analysis_3, 0, 2, 1, 1)

        self.lbl_culture_analysis_2 = QLabel(self.frame)
        self.lbl_culture_analysis_2.setObjectName(u"lbl_culture_analysis_2")

        self.gridLayout_3.addWidget(self.lbl_culture_analysis_2, 0, 4, 1, 1)

        self.lbl_agricultural_period_analysis_2 = QLabel(self.frame)
        self.lbl_agricultural_period_analysis_2.setObjectName(u"lbl_agricultural_period_analysis_2")

        self.gridLayout_3.addWidget(self.lbl_agricultural_period_analysis_2, 0, 3, 1, 1)

        self.lbl_planting_system_analysis_2 = QLabel(self.frame)
        self.lbl_planting_system_analysis_2.setObjectName(u"lbl_planting_system_analysis_2")

        self.gridLayout_3.addWidget(self.lbl_planting_system_analysis_2, 0, 5, 1, 1)

        self.cbx_query_agricultural_period_analysis = QComboBox(self.frame)
        self.cbx_query_agricultural_period_analysis.addItem("")
        self.cbx_query_agricultural_period_analysis.addItem("")
        self.cbx_query_agricultural_period_analysis.setObjectName(u"cbx_query_agricultural_period_analysis")
        self.cbx_query_agricultural_period_analysis.setMinimumSize(QSize(95, 0))

        self.gridLayout_3.addWidget(self.cbx_query_agricultural_period_analysis, 1, 3, 1, 1)

        self.edt_query_agricultural_period_analysis = QLineEdit(self.frame)
        self.edt_query_agricultural_period_analysis.setObjectName(u"edt_query_agricultural_period_analysis")
        self.edt_query_agricultural_period_analysis.setMaximumSize(QSize(80, 16777215))
        self.edt_query_agricultural_period_analysis.setAlignment(Qt.AlignCenter)
        self.edt_query_agricultural_period_analysis.setReadOnly(False)

        self.gridLayout_3.addWidget(self.edt_query_agricultural_period_analysis, 1, 2, 1, 1)

        self.edt_query_analysis = QLineEdit(self.frame)
        self.edt_query_analysis.setObjectName(u"edt_query_analysis")

        self.gridLayout_3.addWidget(self.edt_query_analysis, 1, 0, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.cbx_query_planting_system_analysis = QComboBox(self.frame)
        self.cbx_query_planting_system_analysis.addItem("")
        self.cbx_query_planting_system_analysis.addItem("")
        self.cbx_query_planting_system_analysis.addItem("")
        self.cbx_query_planting_system_analysis.addItem("")
        self.cbx_query_planting_system_analysis.addItem("")
        self.cbx_query_planting_system_analysis.setObjectName(u"cbx_query_planting_system_analysis")
        self.cbx_query_planting_system_analysis.setMinimumSize(QSize(170, 0))

        self.gridLayout_3.addWidget(self.cbx_query_planting_system_analysis, 1, 5, 1, 1)

        self.cbx_query_culture_analysis = QComboBox(self.frame)
        self.cbx_query_culture_analysis.addItem("")
        self.cbx_query_culture_analysis.addItem("")
        self.cbx_query_culture_analysis.addItem("")
        self.cbx_query_culture_analysis.addItem("")
        self.cbx_query_culture_analysis.addItem("")
        self.cbx_query_culture_analysis.addItem("")
        self.cbx_query_culture_analysis.setObjectName(u"cbx_query_culture_analysis")
        self.cbx_query_culture_analysis.setMinimumSize(QSize(70, 0))

        self.gridLayout_3.addWidget(self.cbx_query_culture_analysis, 1, 4, 1, 1)

        self.cbx_query_ordering_analysis = QComboBox(self.frame)
        self.cbx_query_ordering_analysis.addItem("")
        self.cbx_query_ordering_analysis.addItem("")
        self.cbx_query_ordering_analysis.addItem("")
        self.cbx_query_ordering_analysis.addItem("")
        self.cbx_query_ordering_analysis.setObjectName(u"cbx_query_ordering_analysis")
        self.cbx_query_ordering_analysis.setMinimumSize(QSize(116, 0))

        self.gridLayout_3.addWidget(self.cbx_query_ordering_analysis, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_3.addWidget(self.label_4, 0, 1, 1, 1)


        self.verticalLayout_5.addWidget(self.frame)

        self.horizontalLayout_analysis = QHBoxLayout()
        self.horizontalLayout_analysis.setObjectName(u"horizontalLayout_analysis")
        self.table_grid_analysis = QTableWidget(self.tab_register_analysis02)
        if (self.table_grid_analysis.columnCount() < 86):
            self.table_grid_analysis.setColumnCount(86)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(13, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(14, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(15, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(16, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(17, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(18, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(19, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(20, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(21, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(22, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(23, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(24, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(25, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(26, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(27, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(28, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(29, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(30, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(31, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(32, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(33, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(34, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(35, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(36, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(37, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(38, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(39, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(40, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(41, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(42, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(43, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        __qtablewidgetitem44.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(44, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(45, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        __qtablewidgetitem46.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(46, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(47, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(48, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(49, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        __qtablewidgetitem50.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(50, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        __qtablewidgetitem51.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(51, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        __qtablewidgetitem52.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(52, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(53, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(54, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(55, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        __qtablewidgetitem56.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(56, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(57, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        __qtablewidgetitem58.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(58, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        __qtablewidgetitem59.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(59, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        __qtablewidgetitem60.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(60, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(61, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(62, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        __qtablewidgetitem63.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(63, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        __qtablewidgetitem64.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(64, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(65, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        __qtablewidgetitem66.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(66, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        __qtablewidgetitem67.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(67, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(68, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(69, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        __qtablewidgetitem70.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(70, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        __qtablewidgetitem71.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(71, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        __qtablewidgetitem72.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(72, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(73, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        __qtablewidgetitem74.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(74, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(75, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(76, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(77, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        __qtablewidgetitem78.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(78, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        __qtablewidgetitem79.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(79, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        __qtablewidgetitem80.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(80, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(81, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(82, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(83, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        __qtablewidgetitem84.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(84, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setTextAlignment(Qt.AlignCenter);
        self.table_grid_analysis.setHorizontalHeaderItem(85, __qtablewidgetitem85)
        self.table_grid_analysis.setObjectName(u"table_grid_analysis")
        self.table_grid_analysis.setMinimumSize(QSize(0, 0))
        self.table_grid_analysis.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_grid_analysis.setAlternatingRowColors(True)
        self.table_grid_analysis.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_analysis.addWidget(self.table_grid_analysis)

        self.frm_menu_analysis_navegation = QFrame(self.tab_register_analysis02)
        self.frm_menu_analysis_navegation.setObjectName(u"frm_menu_analysis_navegation")
        self.frm_menu_analysis_navegation.setFrameShape(QFrame.Box)
        self.frm_menu_analysis_navegation.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frm_menu_analysis_navegation)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.btn_search_analysis = QPushButton(self.frm_menu_analysis_navegation)
        self.btn_search_analysis.setObjectName(u"btn_search_analysis")
        self.btn_search_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_search_analysis.setFocusPolicy(Qt.NoFocus)
        self.btn_search_analysis.setIcon(icon11)

        self.verticalLayout_18.addWidget(self.btn_search_analysis)

        self.btn_excel_analysis = QPushButton(self.frm_menu_analysis_navegation)
        self.btn_excel_analysis.setObjectName(u"btn_excel_analysis")
        self.btn_excel_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excel_analysis.setFocusPolicy(Qt.NoFocus)
        icon15 = QIcon()
        icon15.addFile(u":/buttons/images/button/Excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_excel_analysis.setIcon(icon15)

        self.verticalLayout_18.addWidget(self.btn_excel_analysis)

        self.btn_pdf_report_analysis = QPushButton(self.frm_menu_analysis_navegation)
        self.btn_pdf_report_analysis.setObjectName(u"btn_pdf_report_analysis")
        self.btn_pdf_report_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pdf_report_analysis.setFocusPolicy(Qt.NoFocus)
        icon16 = QIcon()
        icon16.addFile(u":/buttons/images/button/Print.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_pdf_report_analysis.setIcon(icon16)

        self.verticalLayout_18.addWidget(self.btn_pdf_report_analysis)

        self.btn_delete_analysis = QPushButton(self.frm_menu_analysis_navegation)
        self.btn_delete_analysis.setObjectName(u"btn_delete_analysis")
        self.btn_delete_analysis.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_analysis.setFocusPolicy(Qt.NoFocus)
        self.btn_delete_analysis.setIcon(icon12)

        self.verticalLayout_18.addWidget(self.btn_delete_analysis)

        self.verticalSpacer_analisis = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_analisis)


        self.horizontalLayout_analysis.addWidget(self.frm_menu_analysis_navegation)


        self.verticalLayout_5.addLayout(self.horizontalLayout_analysis)

        self.tab_register_analysis.addTab(self.tab_register_analysis02, "")

        self.verticalLayout_19.addWidget(self.tab_register_analysis)

        self.stk_pag.addWidget(self.pag_analysis)
        self.pag_home = QWidget()
        self.pag_home.setObjectName(u"pag_home")
        self.verticalLayout_9 = QVBoxLayout(self.pag_home)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_logo_home = QLabel(self.pag_home)
        self.lbl_logo_home.setObjectName(u"lbl_logo_home")
        self.lbl_logo_home.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_9.addWidget(self.lbl_logo_home)

        self.stk_pag.addWidget(self.pag_home)
        self.pag_network = QWidget()
        self.pag_network.setObjectName(u"pag_network")
        self.verticalLayout_26 = QVBoxLayout(self.pag_network)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.frame_3 = QFrame(self.pag_network)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_3)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.frame_2 = QFrame(self.frame_3)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.lbl_epochs = QLabel(self.frame_2)
        self.lbl_epochs.setObjectName(u"lbl_epochs")
        self.lbl_epochs.setMaximumSize(QSize(190, 16777215))

        self.gridLayout_4.addWidget(self.lbl_epochs, 0, 0, 1, 1)

        self.edt_epochs = QLineEdit(self.frame_2)
        self.edt_epochs.setObjectName(u"edt_epochs")
        self.edt_epochs.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.edt_epochs, 0, 1, 1, 1)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(300, 16777215))

        self.gridLayout_4.addWidget(self.label_5, 0, 2, 1, 1)

        self.edt_batch_size = QLineEdit(self.frame_2)
        self.edt_batch_size.setObjectName(u"edt_batch_size")
        self.edt_batch_size.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.edt_batch_size, 0, 3, 1, 1)

        self.list_network = QListWidget(self.frame_2)
        self.list_network.setObjectName(u"list_network")
        self.list_network.setMinimumSize(QSize(0, 0))
        self.list_network.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.list_network, 0, 4, 3, 3)

        self.list_linear_regression = QListWidget(self.frame_2)
        self.list_linear_regression.setObjectName(u"list_linear_regression")
        self.list_linear_regression.setMinimumSize(QSize(0, 0))
        self.list_linear_regression.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.list_linear_regression, 0, 7, 3, 3)

        self.list_svm = QListWidget(self.frame_2)
        self.list_svm.setObjectName(u"list_svm")
        self.list_svm.setMinimumSize(QSize(0, 0))
        self.list_svm.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.list_svm, 0, 10, 3, 4)

        self.list_random_forest = QListWidget(self.frame_2)
        self.list_random_forest.setObjectName(u"list_random_forest")
        self.list_random_forest.setMinimumSize(QSize(0, 0))
        self.list_random_forest.viewport().setProperty(u"cursor", QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.list_random_forest, 0, 14, 3, 3)

        self.label_6 = QLabel(self.frame_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(190, 16777215))

        self.gridLayout_4.addWidget(self.label_6, 1, 0, 1, 1)

        self.edt_training = QLineEdit(self.frame_2)
        self.edt_training.setObjectName(u"edt_training")
        self.edt_training.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.edt_training, 1, 1, 1, 1)

        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(260, 16777215))

        self.gridLayout_4.addWidget(self.label_8, 1, 2, 1, 1)

        self.edt_cv = QLineEdit(self.frame_2)
        self.edt_cv.setObjectName(u"edt_cv")
        self.edt_cv.setMaximumSize(QSize(30, 16777215))

        self.gridLayout_4.addWidget(self.edt_cv, 1, 3, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(190, 16777215))

        self.gridLayout_4.addWidget(self.label_12, 2, 0, 1, 1)

        self.edt_learning_rate = QLineEdit(self.frame_2)
        self.edt_learning_rate.setObjectName(u"edt_learning_rate")
        self.edt_learning_rate.setMaximumSize(QSize(50, 16777215))

        self.gridLayout_4.addWidget(self.edt_learning_rate, 2, 1, 1, 1)

        self.lbl_list_network = QLabel(self.frame_2)
        self.lbl_list_network.setObjectName(u"lbl_list_network")

        self.gridLayout_4.addWidget(self.lbl_list_network, 2, 2, 1, 2)

        self.btn_neural_network = QPushButton(self.frame_2)
        self.btn_neural_network.setObjectName(u"btn_neural_network")
        self.btn_neural_network.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_neural_network.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_neural_network, 3, 4, 1, 3)

        self.btn_linear_regression = QPushButton(self.frame_2)
        self.btn_linear_regression.setObjectName(u"btn_linear_regression")
        self.btn_linear_regression.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_linear_regression.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_linear_regression, 3, 7, 1, 3)

        self.btn_SVR = QPushButton(self.frame_2)
        self.btn_SVR.setObjectName(u"btn_SVR")
        self.btn_SVR.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_SVR.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_SVR, 3, 10, 1, 4)

        self.btn_random_forest = QPushButton(self.frame_2)
        self.btn_random_forest.setObjectName(u"btn_random_forest")
        self.btn_random_forest.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_random_forest.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_random_forest, 3, 14, 1, 3)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 16777215))

        self.gridLayout_4.addWidget(self.label_13, 4, 0, 1, 4)

        self.frame_15 = QFrame(self.frame_2)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.NoFrame)
        self.frame_15.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_15, 4, 4, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(0, 0))
        self.label_14.setMaximumSize(QSize(54, 16777215))

        self.gridLayout_4.addWidget(self.label_14, 4, 5, 1, 1)

        self.edt_seed_neural_network = QLineEdit(self.frame_2)
        self.edt_seed_neural_network.setObjectName(u"edt_seed_neural_network")
        self.edt_seed_neural_network.setMaximumSize(QSize(25, 16777215))

        self.gridLayout_4.addWidget(self.edt_seed_neural_network, 4, 6, 1, 1)

        self.frame_14 = QFrame(self.frame_2)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.NoFrame)
        self.frame_14.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_14, 4, 7, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(54, 16777215))

        self.gridLayout_4.addWidget(self.label_15, 4, 8, 1, 1)

        self.edt_seed_linear_regression = QLineEdit(self.frame_2)
        self.edt_seed_linear_regression.setObjectName(u"edt_seed_linear_regression")
        self.edt_seed_linear_regression.setMaximumSize(QSize(25, 16777215))

        self.gridLayout_4.addWidget(self.edt_seed_linear_regression, 4, 9, 1, 1)

        self.frame_13 = QFrame(self.frame_2)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.NoFrame)
        self.frame_13.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_13, 4, 10, 1, 2)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(54, 16777215))

        self.gridLayout_4.addWidget(self.label_16, 4, 12, 1, 1)

        self.edt_seed_SVR = QLineEdit(self.frame_2)
        self.edt_seed_SVR.setObjectName(u"edt_seed_SVR")
        self.edt_seed_SVR.setMaximumSize(QSize(25, 16777215))

        self.gridLayout_4.addWidget(self.edt_seed_SVR, 4, 13, 1, 1)

        self.frame_11 = QFrame(self.frame_2)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.NoFrame)
        self.frame_11.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_11, 4, 14, 1, 1)

        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(54, 16777215))

        self.gridLayout_4.addWidget(self.label_17, 4, 15, 1, 1)

        self.edt_seed_random_forest = QLineEdit(self.frame_2)
        self.edt_seed_random_forest.setObjectName(u"edt_seed_random_forest")
        self.edt_seed_random_forest.setMaximumSize(QSize(25, 16777215))

        self.gridLayout_4.addWidget(self.edt_seed_random_forest, 4, 16, 1, 1)

        self.btn_cross_validation_neural_network = QPushButton(self.frame_2)
        self.btn_cross_validation_neural_network.setObjectName(u"btn_cross_validation_neural_network")
        self.btn_cross_validation_neural_network.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cross_validation_neural_network.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_cross_validation_neural_network, 5, 0, 1, 2)

        self.btn_cross_validation_linear_regression = QPushButton(self.frame_2)
        self.btn_cross_validation_linear_regression.setObjectName(u"btn_cross_validation_linear_regression")
        self.btn_cross_validation_linear_regression.setMinimumSize(QSize(129, 0))
        self.btn_cross_validation_linear_regression.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cross_validation_linear_regression.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_cross_validation_linear_regression, 5, 2, 1, 2)

        self.frame_9 = QFrame(self.frame_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_9, 5, 4, 1, 3)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_8, 5, 7, 1, 3)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout_4.addWidget(self.label_10, 5, 10, 1, 1)

        self.cbx_kernel = QComboBox(self.frame_2)
        self.cbx_kernel.addItem("")
        self.cbx_kernel.addItem("")
        self.cbx_kernel.addItem("")
        self.cbx_kernel.addItem("")
        self.cbx_kernel.setObjectName(u"cbx_kernel")
        self.cbx_kernel.setMaximumSize(QSize(60, 16777215))
        self.cbx_kernel.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.gridLayout_4.addWidget(self.cbx_kernel, 5, 11, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(54, 16777215))

        self.gridLayout_4.addWidget(self.label_11, 5, 12, 1, 1)

        self.edt_degree = QLineEdit(self.frame_2)
        self.edt_degree.setObjectName(u"edt_degree")
        self.edt_degree.setMaximumSize(QSize(25, 16777215))

        self.gridLayout_4.addWidget(self.edt_degree, 5, 13, 1, 1)

        self.frame_10 = QFrame(self.frame_2)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.NoFrame)
        self.frame_10.setFrameShadow(QFrame.Raised)

        self.gridLayout_4.addWidget(self.frame_10, 5, 14, 1, 1)

        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 5, 15, 1, 1)

        self.edt_n_tree = QLineEdit(self.frame_2)
        self.edt_n_tree.setObjectName(u"edt_n_tree")
        self.edt_n_tree.setMinimumSize(QSize(30, 0))
        self.edt_n_tree.setMaximumSize(QSize(25, 16777215))

        self.gridLayout_4.addWidget(self.edt_n_tree, 5, 16, 1, 1)

        self.btn_cross_validation_SVR = QPushButton(self.frame_2)
        self.btn_cross_validation_SVR.setObjectName(u"btn_cross_validation_SVR")
        self.btn_cross_validation_SVR.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cross_validation_SVR.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_cross_validation_SVR, 6, 0, 1, 2)

        self.btn_cross_validation_random_forest = QPushButton(self.frame_2)
        self.btn_cross_validation_random_forest.setObjectName(u"btn_cross_validation_random_forest")
        self.btn_cross_validation_random_forest.setMinimumSize(QSize(129, 0))
        self.btn_cross_validation_random_forest.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cross_validation_random_forest.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_cross_validation_random_forest, 6, 2, 1, 2)

        self.btr_delete_regressor = QPushButton(self.frame_2)
        self.btr_delete_regressor.setObjectName(u"btr_delete_regressor")
        self.btr_delete_regressor.setMaximumSize(QSize(16777215, 16777215))
        self.btr_delete_regressor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btr_delete_regressor.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btr_delete_regressor, 6, 4, 1, 13)

        self.btn_correlation_between_attributes = QPushButton(self.frame_2)
        self.btn_correlation_between_attributes.setObjectName(u"btn_correlation_between_attributes")
        self.btn_correlation_between_attributes.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_correlation_between_attributes.setIcon(icon4)

        self.gridLayout_4.addWidget(self.btn_correlation_between_attributes, 3, 0, 1, 4)


        self.verticalLayout_25.addWidget(self.frame_2)

        self.edt_process = QTextEdit(self.frame_3)
        self.edt_process.setObjectName(u"edt_process")
        font2 = QFont()
        font2.setFamilies([u"Courier New"])
        font2.setBold(True)
        self.edt_process.setFont(font2)
        self.edt_process.setStyleSheet(u"background-color: rgb(255, 255, 127);")

        self.verticalLayout_25.addWidget(self.edt_process)

        self.frame_12 = QFrame(self.frame_3)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.btn_save_regressor = QPushButton(self.frame_12)
        self.btn_save_regressor.setObjectName(u"btn_save_regressor")
        self.btn_save_regressor.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_regressor.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.btn_save_regressor)

        self.btn_save_regressor_RL = QPushButton(self.frame_12)
        self.btn_save_regressor_RL.setObjectName(u"btn_save_regressor_RL")
        self.btn_save_regressor_RL.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_regressor_RL.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.btn_save_regressor_RL)

        self.btn_save_regressor_SVM = QPushButton(self.frame_12)
        self.btn_save_regressor_SVM.setObjectName(u"btn_save_regressor_SVM")
        self.btn_save_regressor_SVM.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_regressor_SVM.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.btn_save_regressor_SVM)

        self.btn_save_regressor_RF = QPushButton(self.frame_12)
        self.btn_save_regressor_RF.setObjectName(u"btn_save_regressor_RF")
        self.btn_save_regressor_RF.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_regressor_RF.setIcon(icon14)

        self.horizontalLayout_4.addWidget(self.btn_save_regressor_RF)


        self.verticalLayout_25.addWidget(self.frame_12)


        self.verticalLayout_26.addWidget(self.frame_3)

        self.stk_pag.addWidget(self.pag_network)
        self.pag_producer = QWidget()
        self.pag_producer.setObjectName(u"pag_producer")
        self.verticalLayout_8 = QVBoxLayout(self.pag_producer)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.tab_register_producer = QTabWidget(self.pag_producer)
        self.tab_register_producer.setObjectName(u"tab_register_producer")
        self.tab_register_producer.setFocusPolicy(Qt.NoFocus)
        self.tab_register_producer.setStyleSheet(u"")
        self.tab_register_producer01 = QWidget()
        self.tab_register_producer01.setObjectName(u"tab_register_producer01")
        self.verticalLayout_20 = QVBoxLayout(self.tab_register_producer01)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.lbl_title_register_producer01 = QLabel(self.tab_register_producer01)
        self.lbl_title_register_producer01.setObjectName(u"lbl_title_register_producer01")

        self.verticalLayout_20.addWidget(self.lbl_title_register_producer01)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frm_register_producer01 = QFrame(self.tab_register_producer01)
        self.frm_register_producer01.setObjectName(u"frm_register_producer01")
        self.frm_register_producer01.setStyleSheet(u"")
        self.frm_register_producer01.setFrameShape(QFrame.Box)
        self.frm_register_producer01.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frm_register_producer01)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lbl_cep_producer = QLabel(self.frm_register_producer01)
        self.lbl_cep_producer.setObjectName(u"lbl_cep_producer")

        self.gridLayout.addWidget(self.lbl_cep_producer, 5, 2, 1, 1)

        self.lbl_neighborhood_producer = QLabel(self.frm_register_producer01)
        self.lbl_neighborhood_producer.setObjectName(u"lbl_neighborhood_producer")

        self.gridLayout.addWidget(self.lbl_neighborhood_producer, 3, 3, 1, 1)

        self.edt_phone_producer = QLineEdit(self.frm_register_producer01)
        self.edt_phone_producer.setObjectName(u"edt_phone_producer")
        self.edt_phone_producer.setStyleSheet(u"")
        self.edt_phone_producer.setReadOnly(True)
        self.edt_phone_producer.setPlaceholderText(u"")

        self.gridLayout.addWidget(self.edt_phone_producer, 6, 3, 1, 1)

        self.lbl_title_user_producer = QLabel(self.frm_register_producer01)
        self.lbl_title_user_producer.setObjectName(u"lbl_title_user_producer")

        self.gridLayout.addWidget(self.lbl_title_user_producer, 9, 0, 1, 1)

        self.cbx_state_producer = QComboBox(self.frm_register_producer01)
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.addItem("")
        self.cbx_state_producer.setObjectName(u"cbx_state_producer")
        self.cbx_state_producer.setEnabled(False)
        self.cbx_state_producer.setMaximumSize(QSize(50, 16777215))
        self.cbx_state_producer.setStyleSheet(u"")
        self.cbx_state_producer.setMaxVisibleItems(11)

        self.gridLayout.addWidget(self.cbx_state_producer, 6, 1, 1, 1)

        self.lbl_name_producer = QLabel(self.frm_register_producer01)
        self.lbl_name_producer.setObjectName(u"lbl_name_producer")

        self.gridLayout.addWidget(self.lbl_name_producer, 1, 0, 1, 1)

        self.lbl_address_producer = QLabel(self.frm_register_producer01)
        self.lbl_address_producer.setObjectName(u"lbl_address_producer")

        self.gridLayout.addWidget(self.lbl_address_producer, 3, 0, 1, 1)

        self.edt_cpf_cnpj_producer = QLineEdit(self.frm_register_producer01)
        self.edt_cpf_cnpj_producer.setObjectName(u"edt_cpf_cnpj_producer")
        self.edt_cpf_cnpj_producer.setStyleSheet(u"")
        self.edt_cpf_cnpj_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_cpf_cnpj_producer, 2, 3, 1, 1)

        self.edt_name_producer = QLineEdit(self.frm_register_producer01)
        self.edt_name_producer.setObjectName(u"edt_name_producer")
        self.edt_name_producer.setStyleSheet(u"")
        self.edt_name_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_name_producer, 2, 0, 1, 3)

        self.lbl_code_producer = QLabel(self.frm_register_producer01)
        self.lbl_code_producer.setObjectName(u"lbl_code_producer")
        self.lbl_code_producer.setMinimumSize(QSize(80, 40))
        self.lbl_code_producer.setMaximumSize(QSize(80, 40))

        self.gridLayout.addWidget(self.lbl_code_producer, 0, 0, 1, 1)

        self.edt_neighborhood_producer = QLineEdit(self.frm_register_producer01)
        self.edt_neighborhood_producer.setObjectName(u"edt_neighborhood_producer")
        self.edt_neighborhood_producer.setStyleSheet(u"")
        self.edt_neighborhood_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_neighborhood_producer, 4, 3, 1, 1)

        self.lbl_cpf_cnpj_producer = QLabel(self.frm_register_producer01)
        self.lbl_cpf_cnpj_producer.setObjectName(u"lbl_cpf_cnpj_producer")

        self.gridLayout.addWidget(self.lbl_cpf_cnpj_producer, 1, 3, 1, 1)

        self.edt_number_producer = QLineEdit(self.frm_register_producer01)
        self.edt_number_producer.setObjectName(u"edt_number_producer")
        self.edt_number_producer.setMaximumSize(QSize(50, 16777215))
        self.edt_number_producer.setSizeIncrement(QSize(0, 0))
        self.edt_number_producer.setStyleSheet(u"")
        self.edt_number_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_number_producer, 4, 1, 1, 1)

        self.lbl_state_producer = QLabel(self.frm_register_producer01)
        self.lbl_state_producer.setObjectName(u"lbl_state_producer")

        self.gridLayout.addWidget(self.lbl_state_producer, 5, 1, 1, 1)

        self.lbl_phone_producer = QLabel(self.frm_register_producer01)
        self.lbl_phone_producer.setObjectName(u"lbl_phone_producer")

        self.gridLayout.addWidget(self.lbl_phone_producer, 5, 3, 1, 1)

        self.edt_address_producer = QLineEdit(self.frm_register_producer01)
        self.edt_address_producer.setObjectName(u"edt_address_producer")
        self.edt_address_producer.setStyleSheet(u"")
        self.edt_address_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_address_producer, 4, 0, 1, 1)

        self.lbl_number_producer = QLabel(self.frm_register_producer01)
        self.lbl_number_producer.setObjectName(u"lbl_number_producer")

        self.gridLayout.addWidget(self.lbl_number_producer, 3, 1, 1, 1)

        self.edt_cep_producer = QLineEdit(self.frm_register_producer01)
        self.edt_cep_producer.setObjectName(u"edt_cep_producer")
        self.edt_cep_producer.setStyleSheet(u"")
        self.edt_cep_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_cep_producer, 6, 2, 1, 1)

        self.edt_city_producer = QLineEdit(self.frm_register_producer01)
        self.edt_city_producer.setObjectName(u"edt_city_producer")
        self.edt_city_producer.setStyleSheet(u"")
        self.edt_city_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_city_producer, 6, 0, 1, 1)

        self.lbl_complement_producer = QLabel(self.frm_register_producer01)
        self.lbl_complement_producer.setObjectName(u"lbl_complement_producer")

        self.gridLayout.addWidget(self.lbl_complement_producer, 3, 2, 1, 1)

        self.lbl_email_producer = QLabel(self.frm_register_producer01)
        self.lbl_email_producer.setObjectName(u"lbl_email_producer")

        self.gridLayout.addWidget(self.lbl_email_producer, 7, 0, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_5, 11, 0, 1, 1)

        self.edt_complement_producer = QLineEdit(self.frm_register_producer01)
        self.edt_complement_producer.setObjectName(u"edt_complement_producer")
        self.edt_complement_producer.setStyleSheet(u"")
        self.edt_complement_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_complement_producer, 4, 2, 1, 1)

        self.edt_email_producer = QLineEdit(self.frm_register_producer01)
        self.edt_email_producer.setObjectName(u"edt_email_producer")
        self.edt_email_producer.setStyleSheet(u"")
        self.edt_email_producer.setReadOnly(True)

        self.gridLayout.addWidget(self.edt_email_producer, 8, 0, 1, 4)

        self.lbl_city_producer = QLabel(self.frm_register_producer01)
        self.lbl_city_producer.setObjectName(u"lbl_city_producer")

        self.gridLayout.addWidget(self.lbl_city_producer, 5, 0, 1, 1)

        self.lbl_name_user_producer = QLabel(self.frm_register_producer01)
        self.lbl_name_user_producer.setObjectName(u"lbl_name_user_producer")

        self.gridLayout.addWidget(self.lbl_name_user_producer, 10, 0, 1, 4)


        self.horizontalLayout.addWidget(self.frm_register_producer01)

        self.frm_menu_produce_register = QFrame(self.tab_register_producer01)
        self.frm_menu_produce_register.setObjectName(u"frm_menu_produce_register")
        self.frm_menu_produce_register.setMaximumSize(QSize(16777215, 16777215))
        self.frm_menu_produce_register.setFrameShape(QFrame.Box)
        self.frm_menu_produce_register.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frm_menu_produce_register)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_insert_producer = QPushButton(self.frm_menu_produce_register)
        self.btn_insert_producer.setObjectName(u"btn_insert_producer")
        self.btn_insert_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_insert_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_insert_producer.setIcon(icon9)

        self.verticalLayout_12.addWidget(self.btn_insert_producer)

        self.btn_update_producer = QPushButton(self.frm_menu_produce_register)
        self.btn_update_producer.setObjectName(u"btn_update_producer")
        self.btn_update_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_update_producer.setIcon(icon10)

        self.verticalLayout_12.addWidget(self.btn_update_producer)

        self.btn_cancelar_producer = QPushButton(self.frm_menu_produce_register)
        self.btn_cancelar_producer.setObjectName(u"btn_cancelar_producer")
        self.btn_cancelar_producer.setEnabled(False)
        self.btn_cancelar_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancelar_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_cancelar_producer.setIcon(icon12)

        self.verticalLayout_12.addWidget(self.btn_cancelar_producer)

        self.btn_save_change_producer = QPushButton(self.frm_menu_produce_register)
        self.btn_save_change_producer.setObjectName(u"btn_save_change_producer")
        self.btn_save_change_producer.setEnabled(False)
        self.btn_save_change_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_change_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_save_change_producer.setIcon(icon13)

        self.verticalLayout_12.addWidget(self.btn_save_change_producer)

        self.btn_save_producer = QPushButton(self.frm_menu_produce_register)
        self.btn_save_producer.setObjectName(u"btn_save_producer")
        self.btn_save_producer.setEnabled(False)
        self.btn_save_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_save_producer.setIcon(icon14)

        self.verticalLayout_12.addWidget(self.btn_save_producer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.frm_menu_produce_register)


        self.verticalLayout_20.addLayout(self.horizontalLayout)

        self.tab_register_producer.addTab(self.tab_register_producer01, "")
        self.tab_register_producer02 = QWidget()
        self.tab_register_producer02.setObjectName(u"tab_register_producer02")
        self.verticalLayout_13 = QVBoxLayout(self.tab_register_producer02)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lbl_title_register_producer02 = QLabel(self.tab_register_producer02)
        self.lbl_title_register_producer02.setObjectName(u"lbl_title_register_producer02")

        self.verticalLayout_13.addWidget(self.lbl_title_register_producer02)

        self.edt_query_producer = QLineEdit(self.tab_register_producer02)
        self.edt_query_producer.setObjectName(u"edt_query_producer")

        self.verticalLayout_13.addWidget(self.edt_query_producer)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.table_grid_producer = QTableWidget(self.tab_register_producer02)
        if (self.table_grid_producer.columnCount() < 14):
            self.table_grid_producer.setColumnCount(14)
        __qtablewidgetitem86 = QTableWidgetItem()
        __qtablewidgetitem86.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        __qtablewidgetitem87.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        __qtablewidgetitem88.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(2, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(3, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(4, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        __qtablewidgetitem91.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(5, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        __qtablewidgetitem92.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(6, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(7, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        __qtablewidgetitem94.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(8, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        __qtablewidgetitem95.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(9, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(10, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(11, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        __qtablewidgetitem98.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(12, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        __qtablewidgetitem99.setTextAlignment(Qt.AlignCenter);
        self.table_grid_producer.setHorizontalHeaderItem(13, __qtablewidgetitem99)
        self.table_grid_producer.setObjectName(u"table_grid_producer")
        self.table_grid_producer.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_grid_producer.setAlternatingRowColors(True)
        self.table_grid_producer.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_6.addWidget(self.table_grid_producer)

        self.frm_menu_producer_navegation = QFrame(self.tab_register_producer02)
        self.frm_menu_producer_navegation.setObjectName(u"frm_menu_producer_navegation")
        self.frm_menu_producer_navegation.setFrameShape(QFrame.Box)
        self.frm_menu_producer_navegation.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frm_menu_producer_navegation)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.btn_search_producer = QPushButton(self.frm_menu_producer_navegation)
        self.btn_search_producer.setObjectName(u"btn_search_producer")
        self.btn_search_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_search_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_search_producer.setIcon(icon11)

        self.verticalLayout_14.addWidget(self.btn_search_producer)

        self.btn_excel_producer = QPushButton(self.frm_menu_producer_navegation)
        self.btn_excel_producer.setObjectName(u"btn_excel_producer")
        self.btn_excel_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excel_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_excel_producer.setIcon(icon15)

        self.verticalLayout_14.addWidget(self.btn_excel_producer)

        self.btn_pdf_report_producer = QPushButton(self.frm_menu_producer_navegation)
        self.btn_pdf_report_producer.setObjectName(u"btn_pdf_report_producer")
        self.btn_pdf_report_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pdf_report_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_pdf_report_producer.setIcon(icon16)

        self.verticalLayout_14.addWidget(self.btn_pdf_report_producer)

        self.btn_delete_producer = QPushButton(self.frm_menu_producer_navegation)
        self.btn_delete_producer.setObjectName(u"btn_delete_producer")
        self.btn_delete_producer.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_producer.setFocusPolicy(Qt.NoFocus)
        self.btn_delete_producer.setIcon(icon12)

        self.verticalLayout_14.addWidget(self.btn_delete_producer)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_3)


        self.horizontalLayout_6.addWidget(self.frm_menu_producer_navegation)


        self.verticalLayout_13.addLayout(self.horizontalLayout_6)

        self.tab_register_producer.addTab(self.tab_register_producer02, "")

        self.verticalLayout_8.addWidget(self.tab_register_producer)

        self.stk_pag.addWidget(self.pag_producer)
        self.pag_about = QWidget()
        self.pag_about.setObjectName(u"pag_about")
        self.verticalLayout_15 = QVBoxLayout(self.pag_about)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lbl_about = QLabel(self.pag_about)
        self.lbl_about.setObjectName(u"lbl_about")

        self.verticalLayout_15.addWidget(self.lbl_about)

        self.txt_about = QTextEdit(self.pag_about)
        self.txt_about.setObjectName(u"txt_about")

        self.verticalLayout_15.addWidget(self.txt_about)

        self.lbl_contact = QLabel(self.pag_about)
        self.lbl_contact.setObjectName(u"lbl_contact")

        self.verticalLayout_15.addWidget(self.lbl_contact)

        self.frm_contact = QFrame(self.pag_about)
        self.frm_contact.setObjectName(u"frm_contact")
        self.frm_contact.setFrameShape(QFrame.StyledPanel)
        self.frm_contact.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frm_contact)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lbl_email = QLabel(self.frm_contact)
        self.lbl_email.setObjectName(u"lbl_email")

        self.verticalLayout_10.addWidget(self.lbl_email)

        self.lbl_linkedin = QLabel(self.frm_contact)
        self.lbl_linkedin.setObjectName(u"lbl_linkedin")

        self.verticalLayout_10.addWidget(self.lbl_linkedin)

        self.lbl_phone = QLabel(self.frm_contact)
        self.lbl_phone.setObjectName(u"lbl_phone")

        self.verticalLayout_10.addWidget(self.lbl_phone)


        self.verticalLayout_15.addWidget(self.frm_contact, 0, Qt.AlignHCenter)

        self.stk_pag.addWidget(self.pag_about)
        self.pag_user = QWidget()
        self.pag_user.setObjectName(u"pag_user")
        self.verticalLayout = QVBoxLayout(self.pag_user)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tab_user = QTabWidget(self.pag_user)
        self.tab_user.setObjectName(u"tab_user")
        self.tab_user.setFocusPolicy(Qt.NoFocus)
        self.tab_user.setStyleSheet(u"")
        self.tab_register_user = QWidget()
        self.tab_register_user.setObjectName(u"tab_register_user")
        self.verticalLayout_4 = QVBoxLayout(self.tab_register_user)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_title_register_user = QLabel(self.tab_register_user)
        self.lbl_title_register_user.setObjectName(u"lbl_title_register_user")

        self.verticalLayout_4.addWidget(self.lbl_title_register_user)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frm_register_user = QFrame(self.tab_register_user)
        self.frm_register_user.setObjectName(u"frm_register_user")
        self.frm_register_user.setStyleSheet(u"")
        self.frm_register_user.setFrameShape(QFrame.Box)
        self.frm_register_user.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frm_register_user)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.lbl_code_user = QLabel(self.frm_register_user)
        self.lbl_code_user.setObjectName(u"lbl_code_user")
        self.lbl_code_user.setMinimumSize(QSize(80, 40))
        self.lbl_code_user.setMaximumSize(QSize(80, 40))

        self.gridLayout_7.addWidget(self.lbl_code_user, 0, 0, 1, 1)

        self.lbl_name_user = QLabel(self.frm_register_user)
        self.lbl_name_user.setObjectName(u"lbl_name_user")

        self.gridLayout_7.addWidget(self.lbl_name_user, 1, 0, 1, 1)

        self.lbl_cpf_user = QLabel(self.frm_register_user)
        self.lbl_cpf_user.setObjectName(u"lbl_cpf_user")

        self.gridLayout_7.addWidget(self.lbl_cpf_user, 1, 5, 1, 1)

        self.edt_name_user = QLineEdit(self.frm_register_user)
        self.edt_name_user.setObjectName(u"edt_name_user")
        self.edt_name_user.setStyleSheet(u"")
        self.edt_name_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_name_user, 2, 0, 1, 5)

        self.edt_cpf_user = QLineEdit(self.frm_register_user)
        self.edt_cpf_user.setObjectName(u"edt_cpf_user")
        self.edt_cpf_user.setStyleSheet(u"")
        self.edt_cpf_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_cpf_user, 2, 5, 1, 1)

        self.lbl_address_user = QLabel(self.frm_register_user)
        self.lbl_address_user.setObjectName(u"lbl_address_user")

        self.gridLayout_7.addWidget(self.lbl_address_user, 3, 0, 1, 1)

        self.lbl_number_user = QLabel(self.frm_register_user)
        self.lbl_number_user.setObjectName(u"lbl_number_user")

        self.gridLayout_7.addWidget(self.lbl_number_user, 3, 1, 1, 1)

        self.lbl_complement_user = QLabel(self.frm_register_user)
        self.lbl_complement_user.setObjectName(u"lbl_complement_user")

        self.gridLayout_7.addWidget(self.lbl_complement_user, 3, 2, 1, 3)

        self.lbl_neighborhood_user = QLabel(self.frm_register_user)
        self.lbl_neighborhood_user.setObjectName(u"lbl_neighborhood_user")

        self.gridLayout_7.addWidget(self.lbl_neighborhood_user, 3, 5, 1, 1)

        self.edt_address_user = QLineEdit(self.frm_register_user)
        self.edt_address_user.setObjectName(u"edt_address_user")
        self.edt_address_user.setStyleSheet(u"")
        self.edt_address_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_address_user, 4, 0, 1, 1)

        self.edt_number_user = QLineEdit(self.frm_register_user)
        self.edt_number_user.setObjectName(u"edt_number_user")
        self.edt_number_user.setMaximumSize(QSize(50, 16777215))
        self.edt_number_user.setSizeIncrement(QSize(0, 0))
        self.edt_number_user.setStyleSheet(u"")
        self.edt_number_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_number_user, 4, 1, 1, 1)

        self.edt_complement_user = QLineEdit(self.frm_register_user)
        self.edt_complement_user.setObjectName(u"edt_complement_user")
        self.edt_complement_user.setStyleSheet(u"")
        self.edt_complement_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_complement_user, 4, 2, 1, 3)

        self.edt_neighborhood_user = QLineEdit(self.frm_register_user)
        self.edt_neighborhood_user.setObjectName(u"edt_neighborhood_user")
        self.edt_neighborhood_user.setStyleSheet(u"")
        self.edt_neighborhood_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_neighborhood_user, 4, 5, 1, 1)

        self.lbl_city_user = QLabel(self.frm_register_user)
        self.lbl_city_user.setObjectName(u"lbl_city_user")

        self.gridLayout_7.addWidget(self.lbl_city_user, 5, 0, 1, 1)

        self.lbl_state_uer = QLabel(self.frm_register_user)
        self.lbl_state_uer.setObjectName(u"lbl_state_uer")

        self.gridLayout_7.addWidget(self.lbl_state_uer, 5, 1, 1, 1)

        self.lbl_cep_user = QLabel(self.frm_register_user)
        self.lbl_cep_user.setObjectName(u"lbl_cep_user")

        self.gridLayout_7.addWidget(self.lbl_cep_user, 5, 2, 1, 1)

        self.lbl_phone_user = QLabel(self.frm_register_user)
        self.lbl_phone_user.setObjectName(u"lbl_phone_user")

        self.gridLayout_7.addWidget(self.lbl_phone_user, 5, 5, 1, 1)

        self.edt_city_user = QLineEdit(self.frm_register_user)
        self.edt_city_user.setObjectName(u"edt_city_user")
        self.edt_city_user.setStyleSheet(u"")
        self.edt_city_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_city_user, 6, 0, 1, 1)

        self.cbx_state_user = QComboBox(self.frm_register_user)
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.addItem("")
        self.cbx_state_user.setObjectName(u"cbx_state_user")
        self.cbx_state_user.setEnabled(False)
        self.cbx_state_user.setMaximumSize(QSize(50, 16777215))
        self.cbx_state_user.setStyleSheet(u"")
        self.cbx_state_user.setMaxVisibleItems(11)

        self.gridLayout_7.addWidget(self.cbx_state_user, 6, 1, 1, 1)

        self.edt_cep_user = QLineEdit(self.frm_register_user)
        self.edt_cep_user.setObjectName(u"edt_cep_user")
        self.edt_cep_user.setStyleSheet(u"")
        self.edt_cep_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_cep_user, 6, 2, 1, 3)

        self.edt_phone_user = QLineEdit(self.frm_register_user)
        self.edt_phone_user.setObjectName(u"edt_phone_user")
        self.edt_phone_user.setStyleSheet(u"")
        self.edt_phone_user.setReadOnly(True)
        self.edt_phone_user.setPlaceholderText(u"")

        self.gridLayout_7.addWidget(self.edt_phone_user, 6, 5, 1, 1)

        self.lbl_email_user = QLabel(self.frm_register_user)
        self.lbl_email_user.setObjectName(u"lbl_email_user")

        self.gridLayout_7.addWidget(self.lbl_email_user, 7, 0, 1, 1)

        self.edt_email_user = QLineEdit(self.frm_register_user)
        self.edt_email_user.setObjectName(u"edt_email_user")
        self.edt_email_user.setStyleSheet(u"")
        self.edt_email_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_email_user, 8, 0, 1, 6)

        self.lbl_email_user_2 = QLabel(self.frm_register_user)
        self.lbl_email_user_2.setObjectName(u"lbl_email_user_2")

        self.gridLayout_7.addWidget(self.lbl_email_user_2, 9, 0, 1, 1)

        self.verticalSpacer_register_user = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_register_user, 11, 3, 1, 1)

        self.edt_authentication_name_user = QLineEdit(self.frm_register_user)
        self.edt_authentication_name_user.setObjectName(u"edt_authentication_name_user")
        self.edt_authentication_name_user.setStyleSheet(u"")
        self.edt_authentication_name_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_authentication_name_user, 10, 0, 1, 1)

        self.edt_password_user = QLineEdit(self.frm_register_user)
        self.edt_password_user.setObjectName(u"edt_password_user")
        self.edt_password_user.setStyleSheet(u"")
        self.edt_password_user.setEchoMode(QLineEdit.Password)
        self.edt_password_user.setReadOnly(True)

        self.gridLayout_7.addWidget(self.edt_password_user, 10, 1, 1, 4)

        self.lbl_email_user_3 = QLabel(self.frm_register_user)
        self.lbl_email_user_3.setObjectName(u"lbl_email_user_3")

        self.gridLayout_7.addWidget(self.lbl_email_user_3, 9, 1, 1, 4)


        self.horizontalLayout_8.addWidget(self.frm_register_user)

        self.frm_menu_register_user = QFrame(self.tab_register_user)
        self.frm_menu_register_user.setObjectName(u"frm_menu_register_user")
        self.frm_menu_register_user.setMaximumSize(QSize(16777215, 16777215))
        self.frm_menu_register_user.setFrameShape(QFrame.Box)
        self.frm_menu_register_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frm_menu_register_user)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.btn_insert_user = QPushButton(self.frm_menu_register_user)
        self.btn_insert_user.setObjectName(u"btn_insert_user")
        self.btn_insert_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_insert_user.setFocusPolicy(Qt.NoFocus)
        self.btn_insert_user.setIcon(icon9)

        self.verticalLayout_22.addWidget(self.btn_insert_user)

        self.btn_update_user = QPushButton(self.frm_menu_register_user)
        self.btn_update_user.setObjectName(u"btn_update_user")
        self.btn_update_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update_user.setFocusPolicy(Qt.NoFocus)
        self.btn_update_user.setIcon(icon10)

        self.verticalLayout_22.addWidget(self.btn_update_user)

        self.btn_cancelar_user = QPushButton(self.frm_menu_register_user)
        self.btn_cancelar_user.setObjectName(u"btn_cancelar_user")
        self.btn_cancelar_user.setEnabled(False)
        self.btn_cancelar_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_cancelar_user.setFocusPolicy(Qt.NoFocus)
        self.btn_cancelar_user.setIcon(icon12)

        self.verticalLayout_22.addWidget(self.btn_cancelar_user)

        self.btn_save_change_user = QPushButton(self.frm_menu_register_user)
        self.btn_save_change_user.setObjectName(u"btn_save_change_user")
        self.btn_save_change_user.setEnabled(False)
        self.btn_save_change_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_change_user.setFocusPolicy(Qt.NoFocus)
        self.btn_save_change_user.setIcon(icon13)

        self.verticalLayout_22.addWidget(self.btn_save_change_user)

        self.btn_save_user = QPushButton(self.frm_menu_register_user)
        self.btn_save_user.setObjectName(u"btn_save_user")
        self.btn_save_user.setEnabled(False)
        self.btn_save_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save_user.setFocusPolicy(Qt.NoFocus)
        self.btn_save_user.setIcon(icon14)

        self.verticalLayout_22.addWidget(self.btn_save_user)

        self.verticalSpacer_register_user_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_22.addItem(self.verticalSpacer_register_user_2)

        self.btn_update_user.raise_()
        self.btn_cancelar_user.raise_()
        self.btn_save_change_user.raise_()
        self.btn_save_user.raise_()
        self.btn_insert_user.raise_()

        self.horizontalLayout_8.addWidget(self.frm_menu_register_user)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.tab_user.addTab(self.tab_register_user, "")
        self.tab_consult_user = QWidget()
        self.tab_consult_user.setObjectName(u"tab_consult_user")
        self.verticalLayout_23 = QVBoxLayout(self.tab_consult_user)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.lbl_title_consult_user = QLabel(self.tab_consult_user)
        self.lbl_title_consult_user.setObjectName(u"lbl_title_consult_user")

        self.verticalLayout_23.addWidget(self.lbl_title_consult_user)

        self.edt_query_user = QLineEdit(self.tab_consult_user)
        self.edt_query_user.setObjectName(u"edt_query_user")

        self.verticalLayout_23.addWidget(self.edt_query_user)

        self.horizontalLayout_consult_user = QHBoxLayout()
        self.horizontalLayout_consult_user.setObjectName(u"horizontalLayout_consult_user")
        self.table_grid_user = QTableWidget(self.tab_consult_user)
        if (self.table_grid_user.columnCount() < 14):
            self.table_grid_user.setColumnCount(14)
        __qtablewidgetitem100 = QTableWidgetItem()
        __qtablewidgetitem100.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(0, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(1, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        __qtablewidgetitem102.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(2, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(3, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(4, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(5, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        __qtablewidgetitem106.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(6, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        __qtablewidgetitem107.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(7, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        __qtablewidgetitem108.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(8, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(9, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(10, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(11, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        __qtablewidgetitem112.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(12, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setTextAlignment(Qt.AlignCenter);
        self.table_grid_user.setHorizontalHeaderItem(13, __qtablewidgetitem113)
        self.table_grid_user.setObjectName(u"table_grid_user")
        self.table_grid_user.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_grid_user.setAlternatingRowColors(True)
        self.table_grid_user.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.horizontalLayout_consult_user.addWidget(self.table_grid_user)

        self.frm_menu_consult_user = QFrame(self.tab_consult_user)
        self.frm_menu_consult_user.setObjectName(u"frm_menu_consult_user")
        self.frm_menu_consult_user.setFrameShape(QFrame.Box)
        self.frm_menu_consult_user.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frm_menu_consult_user)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.btn_search_user = QPushButton(self.frm_menu_consult_user)
        self.btn_search_user.setObjectName(u"btn_search_user")
        self.btn_search_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_search_user.setFocusPolicy(Qt.NoFocus)
        self.btn_search_user.setIcon(icon11)

        self.verticalLayout_24.addWidget(self.btn_search_user)

        self.btn_excel_user = QPushButton(self.frm_menu_consult_user)
        self.btn_excel_user.setObjectName(u"btn_excel_user")
        self.btn_excel_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_excel_user.setFocusPolicy(Qt.NoFocus)
        self.btn_excel_user.setIcon(icon15)

        self.verticalLayout_24.addWidget(self.btn_excel_user)

        self.btn_pdf_report_user = QPushButton(self.frm_menu_consult_user)
        self.btn_pdf_report_user.setObjectName(u"btn_pdf_report_user")
        self.btn_pdf_report_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_pdf_report_user.setFocusPolicy(Qt.NoFocus)
        self.btn_pdf_report_user.setIcon(icon16)

        self.verticalLayout_24.addWidget(self.btn_pdf_report_user)

        self.btn_delete_user = QPushButton(self.frm_menu_consult_user)
        self.btn_delete_user.setObjectName(u"btn_delete_user")
        self.btn_delete_user.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_delete_user.setFocusPolicy(Qt.NoFocus)
        self.btn_delete_user.setIcon(icon12)

        self.verticalLayout_24.addWidget(self.btn_delete_user)

        self.verticalSpacer_consult_user = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_24.addItem(self.verticalSpacer_consult_user)


        self.horizontalLayout_consult_user.addWidget(self.frm_menu_consult_user)


        self.verticalLayout_23.addLayout(self.horizontalLayout_consult_user)

        self.tab_user.addTab(self.tab_consult_user, "")

        self.verticalLayout.addWidget(self.tab_user)

        self.stk_pag.addWidget(self.pag_user)

        self.verticalLayout_17.addWidget(self.stk_pag)


        self.verticalLayout_2.addWidget(self.frm_main)


        self.horizontalLayout_2.addWidget(self.frm_right)


        self.verticalLayout_21.addWidget(self.frm_window)

        win_guia_fertil.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.edt_code_producer, self.edt_name_producer_analysis)
        QWidget.setTabOrder(self.edt_name_producer_analysis, self.edt_sector_analysis)
        QWidget.setTabOrder(self.edt_sector_analysis, self.edt_agricultural_period_analysis)
        QWidget.setTabOrder(self.edt_agricultural_period_analysis, self.cbx_culture_analysis)
        QWidget.setTabOrder(self.cbx_culture_analysis, self.edt_area_analysis)
        QWidget.setTabOrder(self.edt_area_analysis, self.edt_altitude_analysis)
        QWidget.setTabOrder(self.edt_altitude_analysis, self.edt_latitude_analysis)
        QWidget.setTabOrder(self.edt_latitude_analysis, self.edt_longitude_analysis)
        QWidget.setTabOrder(self.edt_longitude_analysis, self.cbx_planting_system_analysis)
        QWidget.setTabOrder(self.cbx_planting_system_analysis, self.edt_average_productivity_analysis)
        QWidget.setTabOrder(self.edt_average_productivity_analysis, self.edt_minimum_temperature_analysis)
        QWidget.setTabOrder(self.edt_minimum_temperature_analysis, self.edt_maximum_temperature_analysis)
        QWidget.setTabOrder(self.edt_maximum_temperature_analysis, self.edt_rain_vegetative_analysis)
        QWidget.setTabOrder(self.edt_rain_vegetative_analysis, self.edt_rain_reproductive_analysis)
        QWidget.setTabOrder(self.edt_rain_reproductive_analysis, self.edt_initial_depth_analysis)
        QWidget.setTabOrder(self.edt_initial_depth_analysis, self.edt_final_depth_analysis)
        QWidget.setTabOrder(self.edt_final_depth_analysis, self.edt_ph_H2O_analysis)
        QWidget.setTabOrder(self.edt_ph_H2O_analysis, self.edt_ph_CaCl2_analysis)
        QWidget.setTabOrder(self.edt_ph_CaCl2_analysis, self.edt_K_cmolc_analysis)
        QWidget.setTabOrder(self.edt_K_cmolc_analysis, self.edt_Ca_analysis)
        QWidget.setTabOrder(self.edt_Ca_analysis, self.edt_Mg_analysis)
        QWidget.setTabOrder(self.edt_Mg_analysis, self.edt_Al_analysis)
        QWidget.setTabOrder(self.edt_Al_analysis, self.edt_H_Al_analysis)
        QWidget.setTabOrder(self.edt_H_Al_analysis, self.edt_SB_analysis)
        QWidget.setTabOrder(self.edt_SB_analysis, self.edt_t_effective_CTC_analysis)
        QWidget.setTabOrder(self.edt_t_effective_CTC_analysis, self.edt_T_analysis)
        QWidget.setTabOrder(self.edt_T_analysis, self.edt_V_analysis)
        QWidget.setTabOrder(self.edt_V_analysis, self.edt_m_analysis)
        QWidget.setTabOrder(self.edt_m_analysis, self.edt_P_meh_analysis)
        QWidget.setTabOrder(self.edt_P_meh_analysis, self.edt_P_rem_analysis)
        QWidget.setTabOrder(self.edt_P_rem_analysis, self.edt_Na_analysis)
        QWidget.setTabOrder(self.edt_Na_analysis, self.edt_K_mg_analysis)
        QWidget.setTabOrder(self.edt_K_mg_analysis, self.edt_S_SO4_analysis)
        QWidget.setTabOrder(self.edt_S_SO4_analysis, self.edt_B_analysis)
        QWidget.setTabOrder(self.edt_B_analysis, self.edt_Cu_analysis)
        QWidget.setTabOrder(self.edt_Cu_analysis, self.edt_Fe_analysis)
        QWidget.setTabOrder(self.edt_Fe_analysis, self.edt_Mn_analysis)
        QWidget.setTabOrder(self.edt_Mn_analysis, self.edt_Zn_analysis)
        QWidget.setTabOrder(self.edt_Zn_analysis, self.edt_MO_analysis)
        QWidget.setTabOrder(self.edt_MO_analysis, self.edt_CO_analysis)
        QWidget.setTabOrder(self.edt_CO_analysis, self.edt_clay_analysis)
        QWidget.setTabOrder(self.edt_clay_analysis, self.edt_pre_sowing_fertilizer_analysis)
        QWidget.setTabOrder(self.edt_pre_sowing_fertilizer_analysis, self.edt_pre_sowing_N_analysis)
        QWidget.setTabOrder(self.edt_pre_sowing_N_analysis, self.edt_pre_sowing_P2O5_analysis)
        QWidget.setTabOrder(self.edt_pre_sowing_P2O5_analysis, self.edt_pre_sowing_K2O_analysis)
        QWidget.setTabOrder(self.edt_pre_sowing_K2O_analysis, self.edt_pre_sowing_N_analysis_KG)
        QWidget.setTabOrder(self.edt_pre_sowing_N_analysis_KG, self.edt_pre_sowing_P2O5_analysis_KG)
        QWidget.setTabOrder(self.edt_pre_sowing_P2O5_analysis_KG, self.edt_pre_sowing_K2O_analysis_KG)
        QWidget.setTabOrder(self.edt_pre_sowing_K2O_analysis_KG, self.edt_planting_fertilizer_analysis)
        QWidget.setTabOrder(self.edt_planting_fertilizer_analysis, self.edt_planting_fertilizer_N_analysis)
        QWidget.setTabOrder(self.edt_planting_fertilizer_N_analysis, self.edt_planting_fertilizer_P2O5_analysis)
        QWidget.setTabOrder(self.edt_planting_fertilizer_P2O5_analysis, self.edt_planting_fertilizer_K2O_analysis)
        QWidget.setTabOrder(self.edt_planting_fertilizer_K2O_analysis, self.edt_planting_fertilizer_N_analysis_KG)
        QWidget.setTabOrder(self.edt_planting_fertilizer_N_analysis_KG, self.edt_planting_fertilizer_P2O5_analysis_KG)
        QWidget.setTabOrder(self.edt_planting_fertilizer_P2O5_analysis_KG, self.edt_planting_fertilizer_K2O_analysis_KG)
        QWidget.setTabOrder(self.edt_planting_fertilizer_K2O_analysis_KG, self.edt_top_dressing_analysis)
        QWidget.setTabOrder(self.edt_top_dressing_analysis, self.edt_top_dressing_N_analysis)
        QWidget.setTabOrder(self.edt_top_dressing_N_analysis, self.edt_top_dressing_P2O5_analysis)
        QWidget.setTabOrder(self.edt_top_dressing_P2O5_analysis, self.edt_top_dressing_K2O_analysis)
        QWidget.setTabOrder(self.edt_top_dressing_K2O_analysis, self.edt_top_dressing_N_analysis_KG)
        QWidget.setTabOrder(self.edt_top_dressing_N_analysis_KG, self.edt_top_dressing_P2O5_analysis_KG)
        QWidget.setTabOrder(self.edt_top_dressing_P2O5_analysis_KG, self.edt_top_dressing_K2O_analysis_KG)
        QWidget.setTabOrder(self.edt_top_dressing_K2O_analysis_KG, self.edt_micro_analysis)
        QWidget.setTabOrder(self.edt_micro_analysis, self.edt_micro_zn_analysis)
        QWidget.setTabOrder(self.edt_micro_zn_analysis, self.edt_micro_b_analysis)
        QWidget.setTabOrder(self.edt_micro_b_analysis, self.edt_micro_cu_analysis)
        QWidget.setTabOrder(self.edt_micro_cu_analysis, self.edt_micro_mn_analysis)
        QWidget.setTabOrder(self.edt_micro_mn_analysis, self.edt_micro_mo_analysis)
        QWidget.setTabOrder(self.edt_micro_mo_analysis, self.edt_micro_co_analysis)
        QWidget.setTabOrder(self.edt_micro_co_analysis, self.edt_micro_ca_analysis)
        QWidget.setTabOrder(self.edt_micro_ca_analysis, self.edt_micro_s_analysis)
        QWidget.setTabOrder(self.edt_micro_s_analysis, self.edt_limestone_analysis)
        QWidget.setTabOrder(self.edt_limestone_analysis, self.edt_prnt_analysis)
        QWidget.setTabOrder(self.edt_prnt_analysis, self.edt_plaster_analysis)
        QWidget.setTabOrder(self.edt_plaster_analysis, self.edt_tca_analysis)
        QWidget.setTabOrder(self.edt_tca_analysis, self.edt_micro_zn_analysis_kg)
        QWidget.setTabOrder(self.edt_micro_zn_analysis_kg, self.edt_micro_b_analysis_kg)
        QWidget.setTabOrder(self.edt_micro_b_analysis_kg, self.edt_micro_cu_analysis_kg)
        QWidget.setTabOrder(self.edt_micro_cu_analysis_kg, self.edt_micro_mn_analysis_kg)
        QWidget.setTabOrder(self.edt_micro_mn_analysis_kg, self.edt_micro_mo_analysis_kg)
        QWidget.setTabOrder(self.edt_micro_mo_analysis_kg, self.edt_micro_co_analysis_kg)
        QWidget.setTabOrder(self.edt_micro_co_analysis_kg, self.edt_micro_ca_analysis_kg)
        QWidget.setTabOrder(self.edt_micro_ca_analysis_kg, self.edt_micro_s_analysis_kg)
        QWidget.setTabOrder(self.edt_micro_s_analysis_kg, self.btn_consult_analysis)
        QWidget.setTabOrder(self.btn_consult_analysis, self.btn_Interpretation_analysis)
        QWidget.setTabOrder(self.btn_Interpretation_analysis, self.edt_query_analysis)
        QWidget.setTabOrder(self.edt_query_analysis, self.cbx_query_ordering_analysis)
        QWidget.setTabOrder(self.cbx_query_ordering_analysis, self.edt_query_agricultural_period_analysis)
        QWidget.setTabOrder(self.edt_query_agricultural_period_analysis, self.cbx_query_agricultural_period_analysis)
        QWidget.setTabOrder(self.cbx_query_agricultural_period_analysis, self.cbx_query_culture_analysis)
        QWidget.setTabOrder(self.cbx_query_culture_analysis, self.cbx_query_planting_system_analysis)
        QWidget.setTabOrder(self.cbx_query_planting_system_analysis, self.table_grid_analysis)
        QWidget.setTabOrder(self.table_grid_analysis, self.edt_name_producer)
        QWidget.setTabOrder(self.edt_name_producer, self.edt_cpf_cnpj_producer)
        QWidget.setTabOrder(self.edt_cpf_cnpj_producer, self.edt_address_producer)
        QWidget.setTabOrder(self.edt_address_producer, self.edt_number_producer)
        QWidget.setTabOrder(self.edt_number_producer, self.edt_complement_producer)
        QWidget.setTabOrder(self.edt_complement_producer, self.edt_neighborhood_producer)
        QWidget.setTabOrder(self.edt_neighborhood_producer, self.edt_city_producer)
        QWidget.setTabOrder(self.edt_city_producer, self.cbx_state_producer)
        QWidget.setTabOrder(self.cbx_state_producer, self.edt_cep_producer)
        QWidget.setTabOrder(self.edt_cep_producer, self.edt_phone_producer)
        QWidget.setTabOrder(self.edt_phone_producer, self.edt_email_producer)
        QWidget.setTabOrder(self.edt_email_producer, self.edt_query_producer)
        QWidget.setTabOrder(self.edt_query_producer, self.table_grid_producer)
        QWidget.setTabOrder(self.table_grid_producer, self.edt_query_user)
        QWidget.setTabOrder(self.edt_query_user, self.table_grid_user)
        QWidget.setTabOrder(self.table_grid_user, self.btn_menu_user)
        QWidget.setTabOrder(self.btn_menu_user, self.edt_name_user)
        QWidget.setTabOrder(self.edt_name_user, self.edt_cpf_user)
        QWidget.setTabOrder(self.edt_cpf_user, self.edt_address_user)
        QWidget.setTabOrder(self.edt_address_user, self.edt_number_user)
        QWidget.setTabOrder(self.edt_number_user, self.edt_complement_user)
        QWidget.setTabOrder(self.edt_complement_user, self.edt_neighborhood_user)
        QWidget.setTabOrder(self.edt_neighborhood_user, self.edt_city_user)
        QWidget.setTabOrder(self.edt_city_user, self.cbx_state_user)
        QWidget.setTabOrder(self.cbx_state_user, self.edt_cep_user)
        QWidget.setTabOrder(self.edt_cep_user, self.edt_phone_user)
        QWidget.setTabOrder(self.edt_phone_user, self.edt_email_user)
        QWidget.setTabOrder(self.edt_email_user, self.edt_authentication_name_user)
        QWidget.setTabOrder(self.edt_authentication_name_user, self.edt_password_user)
        QWidget.setTabOrder(self.edt_password_user, self.txt_about)
        QWidget.setTabOrder(self.txt_about, self.edt_epochs)
        QWidget.setTabOrder(self.edt_epochs, self.edt_batch_size)
        QWidget.setTabOrder(self.edt_batch_size, self.edt_training)
        QWidget.setTabOrder(self.edt_training, self.edt_cv)
        QWidget.setTabOrder(self.edt_cv, self.edt_learning_rate)
        QWidget.setTabOrder(self.edt_learning_rate, self.edt_seed_neural_network)
        QWidget.setTabOrder(self.edt_seed_neural_network, self.edt_seed_linear_regression)
        QWidget.setTabOrder(self.edt_seed_linear_regression, self.edt_seed_SVR)
        QWidget.setTabOrder(self.edt_seed_SVR, self.edt_seed_random_forest)
        QWidget.setTabOrder(self.edt_seed_random_forest, self.cbx_kernel)
        QWidget.setTabOrder(self.cbx_kernel, self.edt_degree)
        QWidget.setTabOrder(self.edt_degree, self.edt_n_tree)
        QWidget.setTabOrder(self.edt_n_tree, self.list_network)
        QWidget.setTabOrder(self.list_network, self.list_linear_regression)
        QWidget.setTabOrder(self.list_linear_regression, self.list_svm)
        QWidget.setTabOrder(self.list_svm, self.list_random_forest)
        QWidget.setTabOrder(self.list_random_forest, self.edt_process)
        QWidget.setTabOrder(self.edt_process, self.btn_productivity_prediction)
        QWidget.setTabOrder(self.btn_productivity_prediction, self.btn_neural_network)
        QWidget.setTabOrder(self.btn_neural_network, self.btn_linear_regression)
        QWidget.setTabOrder(self.btn_linear_regression, self.btn_SVR)
        QWidget.setTabOrder(self.btn_SVR, self.btn_random_forest)
        QWidget.setTabOrder(self.btn_random_forest, self.btr_delete_regressor)
        QWidget.setTabOrder(self.btr_delete_regressor, self.btn_save_regressor)
        QWidget.setTabOrder(self.btn_save_regressor, self.btn_save_regressor_RL)
        QWidget.setTabOrder(self.btn_save_regressor_RL, self.btn_save_regressor_SVM)
        QWidget.setTabOrder(self.btn_save_regressor_SVM, self.btn_save_regressor_RF)
        QWidget.setTabOrder(self.btn_save_regressor_RF, self.btn_correlation_between_attributes)
        QWidget.setTabOrder(self.btn_correlation_between_attributes, self.btn_cross_validation_neural_network)
        QWidget.setTabOrder(self.btn_cross_validation_neural_network, self.btn_cross_validation_linear_regression)
        QWidget.setTabOrder(self.btn_cross_validation_linear_regression, self.btn_cross_validation_SVR)
        QWidget.setTabOrder(self.btn_cross_validation_SVR, self.btn_cross_validation_random_forest)

        self.retranslateUi(win_guia_fertil)

        self.too_box_menu.setCurrentIndex(1)
        self.stk_pag.setCurrentIndex(1)
        self.tab_register_analysis.setCurrentIndex(1)
        self.cbx_culture_analysis.setCurrentIndex(2)
        self.cbx_planting_system_analysis.setCurrentIndex(0)
        self.cbx_query_agricultural_period_analysis.setCurrentIndex(1)
        self.cbx_query_planting_system_analysis.setCurrentIndex(4)
        self.cbx_query_culture_analysis.setCurrentIndex(5)
        self.cbx_query_ordering_analysis.setCurrentIndex(1)
        self.cbx_kernel.setCurrentIndex(2)
        self.tab_register_producer.setCurrentIndex(1)
        self.cbx_state_producer.setCurrentIndex(12)
        self.tab_user.setCurrentIndex(1)
        self.cbx_state_user.setCurrentIndex(12)


        QMetaObject.connectSlotsByName(win_guia_fertil)
    # setupUi

    def retranslateUi(self, win_guia_fertil):
        win_guia_fertil.setWindowTitle(QCoreApplication.translate("win_guia_fertil", u"GUIAFERTIL", None))
        self.lbl_logo_menu.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">GUIA</span><span style=\" font-size:12pt; font-weight:600; color:#00aa00;\">FERTIL</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_menu_home.setToolTip(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_menu_home.setText(QCoreApplication.translate("win_guia_fertil", u"In\u00edcio", None))
        self.btn_menu_user.setText(QCoreApplication.translate("win_guia_fertil", u"Usu\u00e1rio", None))
        self.btn_menu_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Produtor Rural", None))
        self.btn_menu_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Solo, Clima e Produtividade", None))
        self.btn_menu_neural_network.setText(QCoreApplication.translate("win_guia_fertil", u"Predi\u00e7\u00e3o de Produtividade", None))
        self.btn_menu_about.setText(QCoreApplication.translate("win_guia_fertil", u"Sobre", None))
        self.too_box_menu.setItemText(self.too_box_menu.indexOf(self.pag_menu_main), QCoreApplication.translate("win_guia_fertil", u"Menu", None))
        self.label.setText("")
        self.lbl_title_user.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><img src=\":/buttons/images/button/user.png\"/></p><p>Usu\u00e1rio:</p></body></html>", None))
        self.lbl_user.setText(QCoreApplication.translate("win_guia_fertil", u"admin", None))
        self.too_box_menu.setItemText(self.too_box_menu.indexOf(self.pag_menu_information), QCoreApplication.translate("win_guia_fertil", u"Informa\u00e7\u00f5es", None))
        self.btn_home.setText("")
        self.lbl_title.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-size:16pt;\">Sistema de An\u00e1lise Explorat\u00f3ria</span></p></body></html>", None))
        self.edt_code_producer.setText("")
        self.lbl_kg_ha_.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa5500;\">kg/ha -&gt;</span></p></body></html>", None))
        self.edt_longitude_analysis.setText("")
        self.edt_prnt_analysis.setInputMask("")
        self.edt_prnt_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_prnt_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#686868;\">PRNT</span></p></body></html>", None))
        self.edt_micro_b_analysis_kg.setInputMask("")
        self.edt_micro_b_analysis_kg.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_mo_analysis_kg.setInputMask("")
        self.edt_micro_mo_analysis_kg.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_limestone_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#686868;\">Calc\u00e1rio</span></p></body></html>", None))
        self.edt_micro_zn_analysis_kg.setInputMask("")
        self.edt_micro_zn_analysis_kg.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_limestone_analysis.setInputMask("")
        self.edt_limestone_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_tca_analysis.setInputMask("")
        self.edt_tca_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_plaster_analysis.setInputMask("")
        self.edt_plaster_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_minimum_temperature_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">M\u00ednima</span></p></body></html>", None))
        self.lbl_rain_reproductive_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aaff;\">Reprod.</span></p></body></html>", None))
        self.edt_latitude_analysis.setText("")
        self.lbl_rain_vegetative_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aaff;\">Veget.</span></p></body></html>", None))
        self.lbl_maximum_temperature_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\"> M\u00e1xima</span></p></body></html>", None))
        self.lbl_culture_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Cultura</span></p></body></html>", None))
        self.edt_altitude_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_code_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
        self.edt_agricultural_period_analysis.setInputMask(QCoreApplication.translate("win_guia_fertil", u"9999/9999;_", None))
        self.edt_agricultural_period_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"2024/2025", None))
        self.edt_maximum_temperature_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_P_rem_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">P rem.</span></p></body></html>", None))
        self.lbl_K_mg_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">K</span></p></body></html>", None))
        self.edt_rain_vegetative_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_minimum_temperature_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_rain_reproductive_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_mg_dm3.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">mg dm</span><span style=\" font-weight:600; color:#0000ff; vertical-align:super;\">-3</span></p></body></html>", None))
        self.lbl_percent_3.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aaff;\">Chuva - mm</span></p></body></html>", None))
        self.lbl_percent_4.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff0000;\">Temperatura - C\u00b0</span></p></body></html>", None))
        self.cbx_culture_analysis.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"Feij\u00e3o", None))
        self.cbx_culture_analysis.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"Milho", None))
        self.cbx_culture_analysis.setItemText(2, QCoreApplication.translate("win_guia_fertil", u"Soja", None))
        self.cbx_culture_analysis.setItemText(3, QCoreApplication.translate("win_guia_fertil", u"Sorgo", None))
        self.cbx_culture_analysis.setItemText(4, QCoreApplication.translate("win_guia_fertil", u"Trigo", None))

        self.lbl_area_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">\u00c1rea-ha</span></p></body></html>", None))
        self.lbl_code_producer_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Produtor</span></p></body></html>", None))
        self.edt_area_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_initial_depth_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_final_depth_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.label_2.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-weight:600;\">An\u00e1lise</span></p></body></html>", None))
        self.edt_Ca_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_ph_H2O_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_K_cmolc_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_ph_CaCl2_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_final_depth_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa0000;\">P. Final</span></p></body></html>", None))
        self.lbl_ph_CaCl2_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00007f;\">pH CaCl2</span></p></body></html>", None))
        self.lbl_ph_H2O_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00007f;\">pH H2O</span></p></body></html>", None))
        self.lbl_Ca_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">Ca</span><span style=\" font-weight:600; color:#ff5500; vertical-align:super;\">2+</span></p></body></html>", None))
        self.lbl_K_cmolc_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">K</span><span style=\" font-weight:600; color:#ff5500; vertical-align:super;\">+</span></p></body></html>", None))
        self.lbl_Al_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">Al</span><span style=\" font-weight:600; color:#ff5500; vertical-align:super;\">3+</span></p></body></html>", None))
        self.lbl_Mg_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">Mg</span><span style=\" font-weight:600; color:#ff5500; vertical-align:super;\">2+</span></p></body></html>", None))
        self.lbl_SB_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">SB</span></p></body></html>", None))
        self.lbl_T_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">T</span></p></body></html>", None))
        self.lbl_H_Al_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">H + Al</span></p></body></html>", None))
        self.lbl_t_effective_CTC_analysis_2.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">t</span></p></body></html>", None))
        self.lbl_m_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff007f;\">m</span></p></body></html>", None))
        self.lbl_V_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff007f;\">V</span></p></body></html>", None))
        self.lbl_Zn_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">Zn</span></p></body></html>", None))
        self.edt_Cu_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_Fe_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">Fe</span></p></body></html>", None))
        self.lbl_S_SO4_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">S-SO</span><span style=\" font-weight:600; color:#0000ff; vertical-align:sub;\">4</span><span style=\" font-weight:600; color:#0000ff; vertical-align:super;\">2-</span></p></body></html>", None))
        self.edt_V_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_MO_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#55aa7f;\">MO</span></p></body></html>", None))
        self.lbl_name_producer_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Nome</span></p></body></html>", None))
        self.lbl_altitude_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Altitude-m</span></p></body></html>", None))
        self.lbl_P2O5_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">P2O5 - %</span></p></body></html>", None))
        self.cbx_planting_system_analysis.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"CONVENCIONAL - IRRIGADO", None))
        self.cbx_planting_system_analysis.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"CONVENCIONAL - SEQUEIRO", None))
        self.cbx_planting_system_analysis.setItemText(2, QCoreApplication.translate("win_guia_fertil", u"PLANTIO DIRETO - IRRIGADO", None))
        self.cbx_planting_system_analysis.setItemText(3, QCoreApplication.translate("win_guia_fertil", u"PLANTIO DIRETO - SEQUEIRO", None))

        self.lbl_sector_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\"> Talh\u00e3o</span></p></body></html>", None))
        self.edt_average_productivity_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_dag_kg.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#55aa7f;\">g/dm</span><span style=\" font-weight:600; color:#55aa7f; vertical-align:super;\">3</span></p></body></html>", None))
        self.lbl_g_kg.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#550000;\">g kg</span><span style=\" font-weight:600; color:#550000; vertical-align:super;\">-1</span></p></body></html>", None))
        self.lbl_initial_depth_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa0000;\">P. Inicial</span></p></body></html>", None))
        self.lbl_percent.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff007f;\">%</span></p></body></html>", None))
        self.lbl_cm.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa0000;\">cm</span></p></body></html>", None))
        self.lbl_cmolc_dm3.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#ff5500;\">cmolc dm</span><span style=\" font-weight:600; color:#ff5500; vertical-align:super;\">-3</span></p></body></html>", None))
        self.edt_P_rem_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_Na_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_S_SO4_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_Cu_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">Cu</span></p></body></html>", None))
        self.lbl_ph_1_25.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00007f;\">1 : 2,5</span></p></body></html>", None))
        self.lbl_P_meh_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">P</span></p></body></html>", None))
        self.lbl_Na_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">Na</span></p></body></html>", None))
        self.edt_T_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_m_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_H_Al_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_Mn_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">Mn</span></p></body></html>", None))
        self.edt_SB_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_Al_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_CO_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#55aa7f;\">CO</span></p></body></html>", None))
        self.edt_Mg_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_K_mg_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_N_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">N - %</span></p></body></html>", None))
        self.lbl_N_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa5500;\">N - kg/ha</span></p></body></html>", None))
        self.edt_B_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_B_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#0000ff;\">B</span></p></body></html>", None))
        self.edt_P_meh_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_name_producer_analysis.setText("")
        self.edt_MO_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_pre_sowing_P2O5_analysis.setInputMask("")
        self.edt_pre_sowing_P2O5_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_t_effective_CTC_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_planting_fertilizer_analysis.setInputMask("")
        self.edt_planting_fertilizer_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_planting_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Plantio</span></p></body></html>", None))
        self.edt_planting_fertilizer_N_analysis.setInputMask("")
        self.edt_planting_fertilizer_N_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_Fe_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_planting_fertilizer_N_analysis_KG.setInputMask("")
        self.edt_planting_fertilizer_N_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_planting_fertilizer_K2O_analysis.setInputMask("")
        self.edt_planting_fertilizer_K2O_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_pre_sowing_N_analysis_KG.setInputMask("")
        self.edt_pre_sowing_N_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_Mn_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_Zn_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_planting_fertilizer_P2O5_analysis.setInputMask("")
        self.edt_planting_fertilizer_P2O5_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_clay_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_NPK_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">kg/ha</span></p></body></html>", None))
        self.edt_planting_fertilizer_P2O5_analysis_KG.setInputMask("")
        self.edt_planting_fertilizer_P2O5_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_pre_sowing_N_analysis.setInputMask("")
        self.edt_pre_sowing_N_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_pre_sowing_P2O5_analysis_KG.setInputMask("")
        self.edt_pre_sowing_P2O5_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_pre_sowing_fertilizer_analysis.setInputMask("")
        self.edt_pre_sowing_fertilizer_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_pre_sowing_K2O_analysis.setInputMask("")
        self.edt_pre_sowing_K2O_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_pre_sowing_K2O_analysis_KG.setInputMask("")
        self.edt_pre_sowing_K2O_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_planting_fertilizer_K2O_analysis_KG.setInputMask("")
        self.edt_planting_fertilizer_K2O_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_CO_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_micro_co_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Co-%</span></p></body></html>", None))
        self.lbl_pre_sowing_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Pr\u00e9-Sem.</span></p></body></html>", None))
        self.lbl_P2O5_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa5500;\">P2O5 - kg/ha</span></p></body></html>", None))
        self.edt_top_dressing_P2O5_analysis.setInputMask("")
        self.edt_top_dressing_P2O5_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_micro_zn_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Zn-%</span></p></body></html>", None))
        self.edt_top_dressing_P2O5_analysis_KG.setInputMask("")
        self.edt_top_dressing_P2O5_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_b_analysis.setInputMask("")
        self.edt_micro_b_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_micro_mo_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Mo-%</span></p></body></html>", None))
        self.edt_top_dressing_N_analysis.setInputMask("")
        self.edt_top_dressing_N_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_cu_analysis.setInputMask("")
        self.edt_micro_cu_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_mn_analysis.setInputMask("")
        self.edt_micro_mn_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_top_dressing_K2O_analysis.setInputMask("")
        self.edt_top_dressing_K2O_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_zn_analysis.setInputMask("")
        self.edt_micro_zn_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_co_analysis.setInputMask("")
        self.edt_micro_co_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_top_dressing_N_analysis_KG.setInputMask("")
        self.edt_top_dressing_N_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_micro_b_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">B-%</span></p></body></html>", None))
        self.edt_top_dressing_K2O_analysis_KG.setInputMask("")
        self.edt_top_dressing_K2O_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_top_dressing_analysis.setInputMask("")
        self.edt_top_dressing_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_micro_cu_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Cu-%</span></p></body></html>", None))
        self.lbl_top_dressing_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Cobetura</span></p></body></html>", None))
        self.lbl_micro_mn_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Mn-%</span></p></body></html>", None))
        self.lbl_latitude_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Latitude</span></p></body></html>", None))
        self.lbl_longitude.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Longitude</span></p></body></html>", None))
        self.lbl_agricultural_period_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Safra</span></p></body></html>", None))
        self.lbl_clay_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#550000;\">Argila</span></p></body></html>", None))
        self.lbl_K2O_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">K2O - %</span></p></body></html>", None))
        self.lbl_average_productivity_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">M\u00e9dia</span></p></body></html>", None))
        self.lbl_planting_system_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Sist. de Plantio</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">60 kg</span></p></body></html>", None))
        self.edt_micro_mn_analysis_kg.setInputMask("")
        self.edt_micro_mn_analysis_kg.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_plaster_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#686868;\">Gesso</span></p></body></html>", None))
        self.edt_micro_cu_analysis_kg.setInputMask("")
        self.edt_micro_cu_analysis_kg.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_co_analysis_kg.setInputMask("")
        self.edt_micro_co_analysis_kg.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_mo_analysis.setInputMask("")
        self.edt_micro_mo_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_tca_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#686868;\">T</span><span style=\" font-weight:600; color:#686868; vertical-align:sub;\">Ca</span></p></body></html>", None))
        self.edt_micro_ca_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_K2O_analysis_KG.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#aa5500;\">K2O - kg/ha</span></p></body></html>", None))
        self.edt_micro_s_analysis_kg.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_s_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.edt_micro_ca_analysis_kg.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_micros.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Micros</span></p></body></html>", None))
        self.edt_micro_analysis.setInputMask("")
        self.edt_micro_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"0,00", None))
        self.lbl_title_user_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Usu\u00e1rio:</span></p></body></html>", None))
        self.lbl_kg_ha_2.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#686868;\">kg/ha</span></p></body></html>", None))
        self.lbl_kg_ha.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#686868;\">kg/ha</span></p></body></html>", None))
        self.lbl_percente.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#686868;\">%</span></p></body></html>", None))
        self.lbl_percente_2.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#686868;\">%</span></p></body></html>", None))
        self.lbl_name_user_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lbl_micro_s_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">S - %</span></p></body></html>", None))
        self.lbl_micro_ca_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#00aa00;\">Ca - %</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_insert_analysis.setToolTip(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p>Pressione o bot\u00e3o ou tecla \u201cInsert\u201d para abrir a janela de cadastra do Produtor.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_insert_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Inserir\n"
"(Ins)", None))
#if QT_CONFIG(shortcut)
        self.btn_insert_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Ins", None))
#endif // QT_CONFIG(shortcut)
        self.btn_update_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Alterar \n"
"(Shift+Ins)", None))
#if QT_CONFIG(shortcut)
        self.btn_update_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Ins", None))
#endif // QT_CONFIG(shortcut)
        self.btn_consult_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Consultar \n"
"(F2)", None))
#if QT_CONFIG(shortcut)
        self.btn_consult_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancelar_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Cancelar\n"
"(Ctrl+Space)", None))
#if QT_CONFIG(shortcut)
        self.btn_cancelar_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Ctrl+Space", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_change_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar Altera\u00e7\u00f5es \n"
"(Shift+Enter)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_change_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar\n"
" (Enter)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_Interpretation_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Interpretar pela\n"
"5\u00aa Aproxima\u00e7\u00e3o\n"
"(F12)", None))
#if QT_CONFIG(shortcut)
        self.btn_Interpretation_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.btn_productivity_prediction.setText(QCoreApplication.translate("win_guia_fertil", u"An\u00e1lise Explorat\u00f3ria\n"
"(Ctrl+Space)", None))
#if QT_CONFIG(shortcut)
        self.btn_productivity_prediction.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Ctrl+Space", None))
#endif // QT_CONFIG(shortcut)
        self.tab_register_analysis.setTabText(self.tab_register_analysis.indexOf(self.tab_register_analysis01), QCoreApplication.translate("win_guia_fertil", u"Cadastro", None))
        self.lbl_title_register_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Atributos de Solo, Clima e Produtividade</span></p></body></html>", None))
        self.lbl_agricultural_period_analysis_3.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Per\u00edodo</span></p></body></html>", None))
        self.lbl_culture_analysis_2.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Cultura</span></p></body></html>", None))
        self.lbl_agricultural_period_analysis_2.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Safra</span></p></body></html>", None))
        self.lbl_planting_system_analysis_2.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Sist. de Plantio</span></p></body></html>", None))
        self.cbx_query_agricultural_period_analysis.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"ESPECIFICAR", None))
        self.cbx_query_agricultural_period_analysis.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"TODAS", None))

        self.edt_query_agricultural_period_analysis.setInputMask(QCoreApplication.translate("win_guia_fertil", u"9999/9999;_", None))
        self.edt_query_agricultural_period_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"/", None))
        self.label_3.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-weight:600;\">Produtor</span></p></body></html>", None))
        self.cbx_query_planting_system_analysis.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"CONVENCIONAL - IRRIGADO", None))
        self.cbx_query_planting_system_analysis.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"CONVENCIONAL - SEQUEIRO", None))
        self.cbx_query_planting_system_analysis.setItemText(2, QCoreApplication.translate("win_guia_fertil", u"PLANTIO DIRETO - IRRIGADO", None))
        self.cbx_query_planting_system_analysis.setItemText(3, QCoreApplication.translate("win_guia_fertil", u"PLANTIO DIRETO - SEQUEIRO", None))
        self.cbx_query_planting_system_analysis.setItemText(4, QCoreApplication.translate("win_guia_fertil", u"TODOS", None))

        self.cbx_query_culture_analysis.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"Feij\u00e3o", None))
        self.cbx_query_culture_analysis.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"Milho", None))
        self.cbx_query_culture_analysis.setItemText(2, QCoreApplication.translate("win_guia_fertil", u"Soja", None))
        self.cbx_query_culture_analysis.setItemText(3, QCoreApplication.translate("win_guia_fertil", u"Sorgo", None))
        self.cbx_query_culture_analysis.setItemText(4, QCoreApplication.translate("win_guia_fertil", u"Trigo", None))
        self.cbx_query_culture_analysis.setItemText(5, QCoreApplication.translate("win_guia_fertil", u"TODAS", None))

        self.cbx_query_ordering_analysis.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"CULTURA", None))
        self.cbx_query_ordering_analysis.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"NOME", None))
        self.cbx_query_ordering_analysis.setItemText(2, QCoreApplication.translate("win_guia_fertil", u"SAFRA", None))
        self.cbx_query_ordering_analysis.setItemText(3, QCoreApplication.translate("win_guia_fertil", u"SIST. DE PLANTIO", None))

        self.label_4.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-weight:600;\">Ordena\u00e7\u00e3o</span></p></body></html>", None))
        ___qtablewidgetitem = self.table_grid_analysis.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("win_guia_fertil", u"C\u00f3d. da An\u00e1lise", None));
        ___qtablewidgetitem1 = self.table_grid_analysis.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("win_guia_fertil", u"C\u00f3digo", None));
        ___qtablewidgetitem2 = self.table_grid_analysis.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("win_guia_fertil", u"Nome", None));
        ___qtablewidgetitem3 = self.table_grid_analysis.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("win_guia_fertil", u" Talh\u00e3o", None));
        ___qtablewidgetitem4 = self.table_grid_analysis.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("win_guia_fertil", u"Safra", None));
        ___qtablewidgetitem5 = self.table_grid_analysis.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("win_guia_fertil", u"Cultura", None));
        ___qtablewidgetitem6 = self.table_grid_analysis.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("win_guia_fertil", u"\u00c1rea-ha", None));
        ___qtablewidgetitem7 = self.table_grid_analysis.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("win_guia_fertil", u"Altidude-m", None));
        ___qtablewidgetitem8 = self.table_grid_analysis.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("win_guia_fertil", u"Latitude", None));
        ___qtablewidgetitem9 = self.table_grid_analysis.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("win_guia_fertil", u"Longitude", None));
        ___qtablewidgetitem10 = self.table_grid_analysis.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("win_guia_fertil", u"Sistema de Plantio", None));
        ___qtablewidgetitem11 = self.table_grid_analysis.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("win_guia_fertil", u"Produtividade M\u00e9dia-60kg", None));
        ___qtablewidgetitem12 = self.table_grid_analysis.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("win_guia_fertil", u"Temperatura M\u00ednima-C\u00b0", None));
        ___qtablewidgetitem13 = self.table_grid_analysis.horizontalHeaderItem(13)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("win_guia_fertil", u"Temperatura M\u00e1xima-C\u00b0", None));
        ___qtablewidgetitem14 = self.table_grid_analysis.horizontalHeaderItem(14)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("win_guia_fertil", u"Chuva-Vegetativo-mm", None));
        ___qtablewidgetitem15 = self.table_grid_analysis.horizontalHeaderItem(15)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("win_guia_fertil", u"Chuva-Reprodutivo-mm", None));
        ___qtablewidgetitem16 = self.table_grid_analysis.horizontalHeaderItem(16)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("win_guia_fertil", u"Profundidade Inicial-cm", None));
        ___qtablewidgetitem17 = self.table_grid_analysis.horizontalHeaderItem(17)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("win_guia_fertil", u"Profundidade Final-cm", None));
        ___qtablewidgetitem18 = self.table_grid_analysis.horizontalHeaderItem(18)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("win_guia_fertil", u"pH H2O-1:2,5", None));
        ___qtablewidgetitem19 = self.table_grid_analysis.horizontalHeaderItem(19)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("win_guia_fertil", u"pH CaCl2-1:2,5", None));
        ___qtablewidgetitem20 = self.table_grid_analysis.horizontalHeaderItem(20)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("win_guia_fertil", u"Argila-g kg", None));
        ___qtablewidgetitem21 = self.table_grid_analysis.horizontalHeaderItem(21)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("win_guia_fertil", u"MO-dag kg", None));
        ___qtablewidgetitem22 = self.table_grid_analysis.horizontalHeaderItem(22)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("win_guia_fertil", u"CO-dag kg", None));
        ___qtablewidgetitem23 = self.table_grid_analysis.horizontalHeaderItem(23)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("win_guia_fertil", u"K-cmolc dm3", None));
        ___qtablewidgetitem24 = self.table_grid_analysis.horizontalHeaderItem(24)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("win_guia_fertil", u"Ca-cmolc dm3", None));
        ___qtablewidgetitem25 = self.table_grid_analysis.horizontalHeaderItem(25)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("win_guia_fertil", u"Mg-cmolc dm3", None));
        ___qtablewidgetitem26 = self.table_grid_analysis.horizontalHeaderItem(26)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("win_guia_fertil", u"Al-cmolc dm3", None));
        ___qtablewidgetitem27 = self.table_grid_analysis.horizontalHeaderItem(27)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("win_guia_fertil", u"H + Al-cmolc dm3", None));
        ___qtablewidgetitem28 = self.table_grid_analysis.horizontalHeaderItem(28)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("win_guia_fertil", u"SB-cmolc dm3", None));
        ___qtablewidgetitem29 = self.table_grid_analysis.horizontalHeaderItem(29)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("win_guia_fertil", u"t-cmol dm3", None));
        ___qtablewidgetitem30 = self.table_grid_analysis.horizontalHeaderItem(30)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("win_guia_fertil", u"T-cmolc dm3", None));
        ___qtablewidgetitem31 = self.table_grid_analysis.horizontalHeaderItem(31)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("win_guia_fertil", u"V-%", None));
        ___qtablewidgetitem32 = self.table_grid_analysis.horizontalHeaderItem(32)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("win_guia_fertil", u"m-%", None));
        ___qtablewidgetitem33 = self.table_grid_analysis.horizontalHeaderItem(33)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("win_guia_fertil", u"P meh-mg dm3", None));
        ___qtablewidgetitem34 = self.table_grid_analysis.horizontalHeaderItem(34)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("win_guia_fertil", u"P rem-mg dm3", None));
        ___qtablewidgetitem35 = self.table_grid_analysis.horizontalHeaderItem(35)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("win_guia_fertil", u"Na-mg dm3", None));
        ___qtablewidgetitem36 = self.table_grid_analysis.horizontalHeaderItem(36)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("win_guia_fertil", u"K-mg dm3", None));
        ___qtablewidgetitem37 = self.table_grid_analysis.horizontalHeaderItem(37)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("win_guia_fertil", u"S-SO-mg dm3", None));
        ___qtablewidgetitem38 = self.table_grid_analysis.horizontalHeaderItem(38)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("win_guia_fertil", u"B-mg dm3", None));
        ___qtablewidgetitem39 = self.table_grid_analysis.horizontalHeaderItem(39)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("win_guia_fertil", u"Cu-mg dm3", None));
        ___qtablewidgetitem40 = self.table_grid_analysis.horizontalHeaderItem(40)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("win_guia_fertil", u"Fe-mg dm3", None));
        ___qtablewidgetitem41 = self.table_grid_analysis.horizontalHeaderItem(41)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("win_guia_fertil", u"Mn-mg dm3", None));
        ___qtablewidgetitem42 = self.table_grid_analysis.horizontalHeaderItem(42)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("win_guia_fertil", u"Zn-mg dm3", None));
        ___qtablewidgetitem43 = self.table_grid_analysis.horizontalHeaderItem(43)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("win_guia_fertil", u"Calc\u00e1rio", None));
        ___qtablewidgetitem44 = self.table_grid_analysis.horizontalHeaderItem(44)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("win_guia_fertil", u"PRNT", None));
        ___qtablewidgetitem45 = self.table_grid_analysis.horizontalHeaderItem(45)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("win_guia_fertil", u"Gesso", None));
        ___qtablewidgetitem46 = self.table_grid_analysis.horizontalHeaderItem(46)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("win_guia_fertil", u"T-Ca", None));
        ___qtablewidgetitem47 = self.table_grid_analysis.horizontalHeaderItem(47)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("win_guia_fertil", u"Pr\u00e9-Sem. NPK-kg/ha", None));
        ___qtablewidgetitem48 = self.table_grid_analysis.horizontalHeaderItem(48)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("win_guia_fertil", u"N-%", None));
        ___qtablewidgetitem49 = self.table_grid_analysis.horizontalHeaderItem(49)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("win_guia_fertil", u"P2O5-%", None));
        ___qtablewidgetitem50 = self.table_grid_analysis.horizontalHeaderItem(50)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("win_guia_fertil", u"K2O-%", None));
        ___qtablewidgetitem51 = self.table_grid_analysis.horizontalHeaderItem(51)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("win_guia_fertil", u"N-kg/ha", None));
        ___qtablewidgetitem52 = self.table_grid_analysis.horizontalHeaderItem(52)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("win_guia_fertil", u"P2O5-kg/ha", None));
        ___qtablewidgetitem53 = self.table_grid_analysis.horizontalHeaderItem(53)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("win_guia_fertil", u"K2O-kg/ha", None));
        ___qtablewidgetitem54 = self.table_grid_analysis.horizontalHeaderItem(54)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("win_guia_fertil", u"Plantio NPK-kg/ha", None));
        ___qtablewidgetitem55 = self.table_grid_analysis.horizontalHeaderItem(55)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("win_guia_fertil", u"N%", None));
        ___qtablewidgetitem56 = self.table_grid_analysis.horizontalHeaderItem(56)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("win_guia_fertil", u"P2O5-%", None));
        ___qtablewidgetitem57 = self.table_grid_analysis.horizontalHeaderItem(57)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("win_guia_fertil", u"K2O-%", None));
        ___qtablewidgetitem58 = self.table_grid_analysis.horizontalHeaderItem(58)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("win_guia_fertil", u"N-kg/ha", None));
        ___qtablewidgetitem59 = self.table_grid_analysis.horizontalHeaderItem(59)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("win_guia_fertil", u"P2O5-kg/ha", None));
        ___qtablewidgetitem60 = self.table_grid_analysis.horizontalHeaderItem(60)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("win_guia_fertil", u"K2O-kg/ha", None));
        ___qtablewidgetitem61 = self.table_grid_analysis.horizontalHeaderItem(61)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("win_guia_fertil", u"Cobertura NPK-kg/ha", None));
        ___qtablewidgetitem62 = self.table_grid_analysis.horizontalHeaderItem(62)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("win_guia_fertil", u"N-%", None));
        ___qtablewidgetitem63 = self.table_grid_analysis.horizontalHeaderItem(63)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("win_guia_fertil", u"P2O5-%", None));
        ___qtablewidgetitem64 = self.table_grid_analysis.horizontalHeaderItem(64)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("win_guia_fertil", u"K2O-%", None));
        ___qtablewidgetitem65 = self.table_grid_analysis.horizontalHeaderItem(65)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("win_guia_fertil", u"N-kg/ha", None));
        ___qtablewidgetitem66 = self.table_grid_analysis.horizontalHeaderItem(66)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("win_guia_fertil", u"P2O5-kg/ha", None));
        ___qtablewidgetitem67 = self.table_grid_analysis.horizontalHeaderItem(67)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("win_guia_fertil", u"K2O-kg/ha", None));
        ___qtablewidgetitem68 = self.table_grid_analysis.horizontalHeaderItem(68)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("win_guia_fertil", u"Micros-kg/ha", None));
        ___qtablewidgetitem69 = self.table_grid_analysis.horizontalHeaderItem(69)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("win_guia_fertil", u"Zn-%", None));
        ___qtablewidgetitem70 = self.table_grid_analysis.horizontalHeaderItem(70)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("win_guia_fertil", u"B-%", None));
        ___qtablewidgetitem71 = self.table_grid_analysis.horizontalHeaderItem(71)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("win_guia_fertil", u"Cu-%", None));
        ___qtablewidgetitem72 = self.table_grid_analysis.horizontalHeaderItem(72)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("win_guia_fertil", u"Mn-%", None));
        ___qtablewidgetitem73 = self.table_grid_analysis.horizontalHeaderItem(73)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("win_guia_fertil", u"Mo-%", None));
        ___qtablewidgetitem74 = self.table_grid_analysis.horizontalHeaderItem(74)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("win_guia_fertil", u"Co-%", None));
        ___qtablewidgetitem75 = self.table_grid_analysis.horizontalHeaderItem(75)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("win_guia_fertil", u"Ca-%", None));
        ___qtablewidgetitem76 = self.table_grid_analysis.horizontalHeaderItem(76)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("win_guia_fertil", u"S-%", None));
        ___qtablewidgetitem77 = self.table_grid_analysis.horizontalHeaderItem(77)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("win_guia_fertil", u"Zn-kg/ha", None));
        ___qtablewidgetitem78 = self.table_grid_analysis.horizontalHeaderItem(78)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("win_guia_fertil", u"B-kg/ha", None));
        ___qtablewidgetitem79 = self.table_grid_analysis.horizontalHeaderItem(79)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("win_guia_fertil", u"Cu-kg/ha", None));
        ___qtablewidgetitem80 = self.table_grid_analysis.horizontalHeaderItem(80)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("win_guia_fertil", u"Mn-kg/ha", None));
        ___qtablewidgetitem81 = self.table_grid_analysis.horizontalHeaderItem(81)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("win_guia_fertil", u"Mo-kg/ha", None));
        ___qtablewidgetitem82 = self.table_grid_analysis.horizontalHeaderItem(82)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("win_guia_fertil", u"Co-kg/ha", None));
        ___qtablewidgetitem83 = self.table_grid_analysis.horizontalHeaderItem(83)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("win_guia_fertil", u"Ca-kg/ha", None));
        ___qtablewidgetitem84 = self.table_grid_analysis.horizontalHeaderItem(84)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("win_guia_fertil", u"S-kg/ha", None));
        ___qtablewidgetitem85 = self.table_grid_analysis.horizontalHeaderItem(85)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("win_guia_fertil", u"Nome do Usu\u00e1rio", None));
        self.btn_search_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Buscar \n"
" (F2)", None))
#if QT_CONFIG(shortcut)
        self.btn_search_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_excel_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Gerar Excel\n"
" (F11)", None))
#if QT_CONFIG(shortcut)
        self.btn_excel_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.btn_pdf_report_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Relat\u00f3rio\n"
"(F12)", None))
#if QT_CONFIG(shortcut)
        self.btn_pdf_report_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_analysis.setText(QCoreApplication.translate("win_guia_fertil", u"Excluir\n"
"(Shift+Del)", None))
#if QT_CONFIG(shortcut)
        self.btn_delete_analysis.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Del", None))
#endif // QT_CONFIG(shortcut)
        self.tab_register_analysis.setTabText(self.tab_register_analysis.indexOf(self.tab_register_analysis02), QCoreApplication.translate("win_guia_fertil", u"Atributos de Solo, Clima e Produtividade", None))
        self.lbl_logo_home.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><img src=\":/soon/images/soon/GuiaFertil-01.png\"/></p></body></html>", None))
        self.lbl_epochs.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-weight:600;\">\u00c9pocas de treinamento...........:</span></p></body></html>", None))
        self.edt_epochs.setText(QCoreApplication.translate("win_guia_fertil", u"160", None))
        self.label_5.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Batch size :</span></p></body></html>", None))
        self.edt_batch_size.setText(QCoreApplication.translate("win_guia_fertil", u"5", None))
        self.label_6.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-weight:600;\">% dados para treinamento....:</span></p></body></html>", None))
        self.edt_training.setText(QCoreApplication.translate("win_guia_fertil", u"80", None))
        self.label_8.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">N\u00b0 de Folds (C.V.) :</span></p></body></html>", None))
        self.edt_cv.setText(QCoreApplication.translate("win_guia_fertil", u"10", None))
        self.label_12.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-weight:600;\">Taxa de aprendizagem...........:</span></p></body></html>", None))
        self.edt_learning_rate.setText(QCoreApplication.translate("win_guia_fertil", u"0,0001", None))
        self.lbl_list_network.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Regressores da salvos--&gt;</span></p></body></html>", None))
        self.btn_neural_network.setText(QCoreApplication.translate("win_guia_fertil", u"Rede Neural (F9)", None))
#if QT_CONFIG(shortcut)
        self.btn_neural_network.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F9", None))
#endif // QT_CONFIG(shortcut)
        self.btn_linear_regression.setText(QCoreApplication.translate("win_guia_fertil", u"Regress\u00e3o Linear (F10)", None))
#if QT_CONFIG(shortcut)
        self.btn_linear_regression.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F10", None))
#endif // QT_CONFIG(shortcut)
        self.btn_SVR.setText(QCoreApplication.translate("win_guia_fertil", u"S V R (F11)", None))
#if QT_CONFIG(shortcut)
        self.btn_SVR.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.btn_random_forest.setText(QCoreApplication.translate("win_guia_fertil", u"Floresta aleat\u00f3ria (F12)", None))
#if QT_CONFIG(shortcut)
        self.btn_random_forest.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.label_13.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Valida\u00e7\u00e3o Cruzada</span></p></body></html>", None))
        self.label_14.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Semente:</span></p></body></html>", None))
        self.edt_seed_neural_network.setText(QCoreApplication.translate("win_guia_fertil", u"42", None))
        self.label_15.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Semente:</span></p></body></html>", None))
        self.edt_seed_linear_regression.setText(QCoreApplication.translate("win_guia_fertil", u"42", None))
        self.label_16.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Semente:</span></p></body></html>", None))
        self.edt_seed_SVR.setText(QCoreApplication.translate("win_guia_fertil", u"42", None))
        self.label_17.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Semente:</span></p></body></html>", None))
        self.edt_seed_random_forest.setText(QCoreApplication.translate("win_guia_fertil", u"42", None))
        self.btn_cross_validation_neural_network.setText(QCoreApplication.translate("win_guia_fertil", u"Rede Neural (F1)", None))
#if QT_CONFIG(shortcut)
        self.btn_cross_validation_neural_network.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F1", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cross_validation_linear_regression.setText(QCoreApplication.translate("win_guia_fertil", u"Regress\u00e3o Linear (F2)", None))
#if QT_CONFIG(shortcut)
        self.btn_cross_validation_linear_regression.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.label_10.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Kernel:</span></p></body></html>", None))
        self.cbx_kernel.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"linear", None))
        self.cbx_kernel.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"poly", None))
        self.cbx_kernel.setItemText(2, QCoreApplication.translate("win_guia_fertil", u"rbf", None))
        self.cbx_kernel.setItemText(3, QCoreApplication.translate("win_guia_fertil", u"sigmoid", None))

        self.label_11.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">Degree:</span></p></body></html>", None))
        self.edt_degree.setText(QCoreApplication.translate("win_guia_fertil", u"1", None))
        self.label_9.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"right\"><span style=\" font-weight:600;\">\u00c1rvores:</span></p></body></html>", None))
        self.edt_n_tree.setText(QCoreApplication.translate("win_guia_fertil", u"400", None))
        self.btn_cross_validation_SVR.setText(QCoreApplication.translate("win_guia_fertil", u"S V R (F3)", None))
#if QT_CONFIG(shortcut)
        self.btn_cross_validation_SVR.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F3", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cross_validation_random_forest.setText(QCoreApplication.translate("win_guia_fertil", u"Random Forest (F4)", None))
#if QT_CONFIG(shortcut)
        self.btn_cross_validation_random_forest.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F4", None))
#endif // QT_CONFIG(shortcut)
        self.btr_delete_regressor.setText(QCoreApplication.translate("win_guia_fertil", u"Apagar Regressor (Shift+Del)", None))
#if QT_CONFIG(shortcut)
        self.btr_delete_regressor.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Del", None))
#endif // QT_CONFIG(shortcut)
        self.btn_correlation_between_attributes.setText(QCoreApplication.translate("win_guia_fertil", u"Correla\u00e7\u00e3o entre Atributos (Ctrl+Space)", None))
#if QT_CONFIG(shortcut)
        self.btn_correlation_between_attributes.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Ctrl+Space", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_regressor.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar modelo da Rede Neural (F5)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_regressor.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_regressor_RL.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar modelo da Regress\u00e3o Linear (F6)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_regressor_RL.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F6", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_regressor_SVM.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar modelo da SVR (F7)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_regressor_SVM.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F7", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_regressor_RF.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar modelo da Floresta aleat\u00f3ria (F8)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_regressor_RF.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F8", None))
#endif // QT_CONFIG(shortcut)
        self.lbl_title_register_producer01.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Produtor Rural</span></p></body></html>", None))
        self.lbl_cep_producer.setText(QCoreApplication.translate("win_guia_fertil", u"CEP", None))
        self.lbl_neighborhood_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Bairro", None))
        self.edt_phone_producer.setInputMask(QCoreApplication.translate("win_guia_fertil", u"(99) 9-9999-9999", None))
        self.lbl_title_user_producer.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-weight:600;\">Usu\u00e1rio</span></p></body></html>", None))
        self.cbx_state_producer.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"AC", None))
        self.cbx_state_producer.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"AL", None))
        self.cbx_state_producer.setItemText(2, QCoreApplication.translate("win_guia_fertil", u"AP", None))
        self.cbx_state_producer.setItemText(3, QCoreApplication.translate("win_guia_fertil", u"AM", None))
        self.cbx_state_producer.setItemText(4, QCoreApplication.translate("win_guia_fertil", u"BA", None))
        self.cbx_state_producer.setItemText(5, QCoreApplication.translate("win_guia_fertil", u"CE", None))
        self.cbx_state_producer.setItemText(6, QCoreApplication.translate("win_guia_fertil", u"DF", None))
        self.cbx_state_producer.setItemText(7, QCoreApplication.translate("win_guia_fertil", u"ES", None))
        self.cbx_state_producer.setItemText(8, QCoreApplication.translate("win_guia_fertil", u"GO", None))
        self.cbx_state_producer.setItemText(9, QCoreApplication.translate("win_guia_fertil", u"MA", None))
        self.cbx_state_producer.setItemText(10, QCoreApplication.translate("win_guia_fertil", u"MT", None))
        self.cbx_state_producer.setItemText(11, QCoreApplication.translate("win_guia_fertil", u"MS", None))
        self.cbx_state_producer.setItemText(12, QCoreApplication.translate("win_guia_fertil", u"MG", None))
        self.cbx_state_producer.setItemText(13, QCoreApplication.translate("win_guia_fertil", u"PA", None))
        self.cbx_state_producer.setItemText(14, QCoreApplication.translate("win_guia_fertil", u"PB", None))
        self.cbx_state_producer.setItemText(15, QCoreApplication.translate("win_guia_fertil", u"PR", None))
        self.cbx_state_producer.setItemText(16, QCoreApplication.translate("win_guia_fertil", u"PE", None))
        self.cbx_state_producer.setItemText(17, QCoreApplication.translate("win_guia_fertil", u"PI", None))
        self.cbx_state_producer.setItemText(18, QCoreApplication.translate("win_guia_fertil", u"RJ", None))
        self.cbx_state_producer.setItemText(19, QCoreApplication.translate("win_guia_fertil", u"RN", None))
        self.cbx_state_producer.setItemText(20, QCoreApplication.translate("win_guia_fertil", u"RS", None))
        self.cbx_state_producer.setItemText(21, QCoreApplication.translate("win_guia_fertil", u"RO", None))
        self.cbx_state_producer.setItemText(22, QCoreApplication.translate("win_guia_fertil", u"RR", None))
        self.cbx_state_producer.setItemText(23, QCoreApplication.translate("win_guia_fertil", u"SC", None))
        self.cbx_state_producer.setItemText(24, QCoreApplication.translate("win_guia_fertil", u"SP", None))
        self.cbx_state_producer.setItemText(25, QCoreApplication.translate("win_guia_fertil", u"SE", None))
        self.cbx_state_producer.setItemText(26, QCoreApplication.translate("win_guia_fertil", u"TO", None))

        self.cbx_state_producer.setCurrentText(QCoreApplication.translate("win_guia_fertil", u"MG", None))
        self.lbl_name_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Nome", None))
        self.lbl_address_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Endere\u00e7o", None))
        self.edt_cpf_cnpj_producer.setText("")
        self.edt_cpf_cnpj_producer.setPlaceholderText("")
        self.edt_name_producer.setText("")
        self.edt_name_producer.setPlaceholderText("")
        self.lbl_code_producer.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-weight:600;\"><br/></span></p></body></html>", None))
        self.edt_neighborhood_producer.setPlaceholderText("")
        self.lbl_cpf_cnpj_producer.setText(QCoreApplication.translate("win_guia_fertil", u"CPF / CNPJ", None))
        self.edt_number_producer.setText("")
        self.edt_number_producer.setPlaceholderText("")
        self.lbl_state_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Estado", None))
        self.lbl_phone_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Telefone", None))
        self.edt_address_producer.setText("")
        self.edt_address_producer.setPlaceholderText("")
        self.lbl_number_producer.setText(QCoreApplication.translate("win_guia_fertil", u"N\u00famero", None))
        self.edt_cep_producer.setInputMask(QCoreApplication.translate("win_guia_fertil", u"99.999-999", None))
        self.edt_cep_producer.setPlaceholderText("")
        self.edt_city_producer.setPlaceholderText("")
        self.lbl_complement_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Complemento", None))
        self.lbl_email_producer.setText(QCoreApplication.translate("win_guia_fertil", u"e-mail", None))
        self.edt_complement_producer.setPlaceholderText("")
        self.edt_email_producer.setText("")
        self.edt_email_producer.setPlaceholderText("")
        self.lbl_city_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Munic\u00edpio", None))
        self.lbl_name_user_producer.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><br/></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.btn_insert_producer.setToolTip(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p>Pressione o bot\u00e3o ou tecla \u201cInsert\u201d para abrir a janela de cadastra do Produtor.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_insert_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Inserir\n"
"(Ins)", None))
#if QT_CONFIG(shortcut)
        self.btn_insert_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Ins", None))
#endif // QT_CONFIG(shortcut)
        self.btn_update_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Alterar \n"
"(Shift+Ins)", None))
#if QT_CONFIG(shortcut)
        self.btn_update_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Ins", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancelar_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Cancelar\n"
"(Ctrl+Space)", None))
#if QT_CONFIG(shortcut)
        self.btn_cancelar_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Ctrl+Space", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_change_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar Altera\u00e7\u00f5es \n"
"(Shift+Enter)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_change_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar\n"
" (Enter)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tab_register_producer.setTabText(self.tab_register_producer.indexOf(self.tab_register_producer01), QCoreApplication.translate("win_guia_fertil", u"Cadastro", None))
        self.lbl_title_register_producer02.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Produtores Rurais</span></p></body></html>", None))
        ___qtablewidgetitem86 = self.table_grid_producer.horizontalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("win_guia_fertil", u"C\u00f3digo", None));
        ___qtablewidgetitem87 = self.table_grid_producer.horizontalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("win_guia_fertil", u"Nome", None));
        ___qtablewidgetitem88 = self.table_grid_producer.horizontalHeaderItem(2)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("win_guia_fertil", u"CPF/CNPJ", None));
        ___qtablewidgetitem89 = self.table_grid_producer.horizontalHeaderItem(3)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("win_guia_fertil", u"Endere\u00e7o", None));
        ___qtablewidgetitem90 = self.table_grid_producer.horizontalHeaderItem(4)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("win_guia_fertil", u"N\u00famero", None));
        ___qtablewidgetitem91 = self.table_grid_producer.horizontalHeaderItem(5)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("win_guia_fertil", u"Complemento", None));
        ___qtablewidgetitem92 = self.table_grid_producer.horizontalHeaderItem(6)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("win_guia_fertil", u"Bairro", None));
        ___qtablewidgetitem93 = self.table_grid_producer.horizontalHeaderItem(7)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("win_guia_fertil", u"Munic\u00edpio", None));
        ___qtablewidgetitem94 = self.table_grid_producer.horizontalHeaderItem(8)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("win_guia_fertil", u"Estado", None));
        ___qtablewidgetitem95 = self.table_grid_producer.horizontalHeaderItem(9)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("win_guia_fertil", u"CEP", None));
        ___qtablewidgetitem96 = self.table_grid_producer.horizontalHeaderItem(10)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("win_guia_fertil", u"Telefone", None));
        ___qtablewidgetitem97 = self.table_grid_producer.horizontalHeaderItem(11)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("win_guia_fertil", u"e-mail", None));
        ___qtablewidgetitem98 = self.table_grid_producer.horizontalHeaderItem(12)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("win_guia_fertil", u"C\u00f3digo", None));
        ___qtablewidgetitem99 = self.table_grid_producer.horizontalHeaderItem(13)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("win_guia_fertil", u"Nome do Usu\u00e1rio", None));
        self.btn_search_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Buscar \n"
" (F2)", None))
#if QT_CONFIG(shortcut)
        self.btn_search_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_excel_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Gerar Excel\n"
" (F11)", None))
#if QT_CONFIG(shortcut)
        self.btn_excel_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.btn_pdf_report_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Relat\u00f3rio\n"
"(F12)", None))
#if QT_CONFIG(shortcut)
        self.btn_pdf_report_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_producer.setText(QCoreApplication.translate("win_guia_fertil", u"Excluir\n"
"(Shift+Del)", None))
#if QT_CONFIG(shortcut)
        self.btn_delete_producer.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Del", None))
#endif // QT_CONFIG(shortcut)
        self.tab_register_producer.setTabText(self.tab_register_producer.indexOf(self.tab_register_producer02), QCoreApplication.translate("win_guia_fertil", u"Produtores Rurais", None))
        self.lbl_about.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Sobre</span></p></body></html>", None))
        self.txt_about.setHtml(QCoreApplication.translate("win_guia_fertil", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">	O sistema tem como objetivo realizar uma an\u00e1lise explorat\u00f3ria utilizando t\u00e9cnicas de intelig\u00eancia artificial para compreender a influ\u00eancia dos atributos qu\u00edmicos do solo, das condi\u00e7\u00f5es clim\u00e1ticas e das pr\u00e1ticas de aduba\u00e7\u00e3o na produtividade da cultura da soja, permitindo, assim, prever o limiar de produtividade com base nesses atributos preditores.</span></p></body></html>", None))
        self.lbl_contact.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Contato:</span></p></body></html>", None))
        self.lbl_email.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><img src=\":/Contacts/images/contacts/email.png\"/><span style=\" font-size:16pt; font-weight:600; vertical-align:super;\">dariosilvamelo@gmail.com</span></p></body></html>", None))
        self.lbl_linkedin.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><img src=\":/Contacts/images/contacts/linkedin.png\"/><span style=\" font-size:16pt; font-weight:600; vertical-align:super;\">https://www.linkedin.com/in/dariosilvamelo/</span></p></body></html>", None))
        self.lbl_phone.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><img src=\":/Contacts/images/contacts/whats.png\"/><span style=\" font-size:16pt; font-weight:600; vertical-align:super;\">(034) 9-9199-8303</span></p></body></html>", None))
        self.lbl_title_register_user.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Usu\u00e1rio</span></p></body></html>", None))
        self.lbl_code_user.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p><br/></p></body></html>", None))
        self.lbl_name_user.setText(QCoreApplication.translate("win_guia_fertil", u"Nome", None))
        self.lbl_cpf_user.setText(QCoreApplication.translate("win_guia_fertil", u"CPF / CNPJ", None))
        self.edt_name_user.setText("")
        self.edt_name_user.setPlaceholderText("")
        self.edt_cpf_user.setText("")
        self.edt_cpf_user.setPlaceholderText("")
        self.lbl_address_user.setText(QCoreApplication.translate("win_guia_fertil", u"Endere\u00e7o", None))
        self.lbl_number_user.setText(QCoreApplication.translate("win_guia_fertil", u"N\u00famero", None))
        self.lbl_complement_user.setText(QCoreApplication.translate("win_guia_fertil", u"Complemento", None))
        self.lbl_neighborhood_user.setText(QCoreApplication.translate("win_guia_fertil", u"Bairro", None))
        self.edt_address_user.setText("")
        self.edt_address_user.setPlaceholderText("")
        self.edt_number_user.setText("")
        self.edt_number_user.setPlaceholderText("")
        self.edt_complement_user.setPlaceholderText("")
        self.edt_neighborhood_user.setPlaceholderText("")
        self.lbl_city_user.setText(QCoreApplication.translate("win_guia_fertil", u"Munic\u00edpio", None))
        self.lbl_state_uer.setText(QCoreApplication.translate("win_guia_fertil", u"Estado", None))
        self.lbl_cep_user.setText(QCoreApplication.translate("win_guia_fertil", u"CEP", None))
        self.lbl_phone_user.setText(QCoreApplication.translate("win_guia_fertil", u"Telefone", None))
        self.edt_city_user.setPlaceholderText("")
        self.cbx_state_user.setItemText(0, QCoreApplication.translate("win_guia_fertil", u"AC", None))
        self.cbx_state_user.setItemText(1, QCoreApplication.translate("win_guia_fertil", u"AL", None))
        self.cbx_state_user.setItemText(2, QCoreApplication.translate("win_guia_fertil", u"AP", None))
        self.cbx_state_user.setItemText(3, QCoreApplication.translate("win_guia_fertil", u"AM", None))
        self.cbx_state_user.setItemText(4, QCoreApplication.translate("win_guia_fertil", u"BA", None))
        self.cbx_state_user.setItemText(5, QCoreApplication.translate("win_guia_fertil", u"CE", None))
        self.cbx_state_user.setItemText(6, QCoreApplication.translate("win_guia_fertil", u"DF", None))
        self.cbx_state_user.setItemText(7, QCoreApplication.translate("win_guia_fertil", u"ES", None))
        self.cbx_state_user.setItemText(8, QCoreApplication.translate("win_guia_fertil", u"GO", None))
        self.cbx_state_user.setItemText(9, QCoreApplication.translate("win_guia_fertil", u"MA", None))
        self.cbx_state_user.setItemText(10, QCoreApplication.translate("win_guia_fertil", u"MT", None))
        self.cbx_state_user.setItemText(11, QCoreApplication.translate("win_guia_fertil", u"MS", None))
        self.cbx_state_user.setItemText(12, QCoreApplication.translate("win_guia_fertil", u"MG", None))
        self.cbx_state_user.setItemText(13, QCoreApplication.translate("win_guia_fertil", u"PA", None))
        self.cbx_state_user.setItemText(14, QCoreApplication.translate("win_guia_fertil", u"PB", None))
        self.cbx_state_user.setItemText(15, QCoreApplication.translate("win_guia_fertil", u"PR", None))
        self.cbx_state_user.setItemText(16, QCoreApplication.translate("win_guia_fertil", u"PE", None))
        self.cbx_state_user.setItemText(17, QCoreApplication.translate("win_guia_fertil", u"PI", None))
        self.cbx_state_user.setItemText(18, QCoreApplication.translate("win_guia_fertil", u"RJ", None))
        self.cbx_state_user.setItemText(19, QCoreApplication.translate("win_guia_fertil", u"RN", None))
        self.cbx_state_user.setItemText(20, QCoreApplication.translate("win_guia_fertil", u"RS", None))
        self.cbx_state_user.setItemText(21, QCoreApplication.translate("win_guia_fertil", u"RO", None))
        self.cbx_state_user.setItemText(22, QCoreApplication.translate("win_guia_fertil", u"RR", None))
        self.cbx_state_user.setItemText(23, QCoreApplication.translate("win_guia_fertil", u"SC", None))
        self.cbx_state_user.setItemText(24, QCoreApplication.translate("win_guia_fertil", u"SP", None))
        self.cbx_state_user.setItemText(25, QCoreApplication.translate("win_guia_fertil", u"SE", None))
        self.cbx_state_user.setItemText(26, QCoreApplication.translate("win_guia_fertil", u"TO", None))

        self.cbx_state_user.setCurrentText(QCoreApplication.translate("win_guia_fertil", u"MG", None))
        self.edt_cep_user.setInputMask(QCoreApplication.translate("win_guia_fertil", u"99.999-999", None))
        self.edt_cep_user.setPlaceholderText("")
        self.edt_phone_user.setInputMask(QCoreApplication.translate("win_guia_fertil", u"(99) 9-9999-9999", None))
        self.lbl_email_user.setText(QCoreApplication.translate("win_guia_fertil", u"e-mail", None))
        self.edt_email_user.setPlaceholderText("")
        self.lbl_email_user_2.setText(QCoreApplication.translate("win_guia_fertil", u"Usu\u00e1rio de login", None))
        self.edt_authentication_name_user.setPlaceholderText("")
        self.edt_password_user.setText("")
        self.edt_password_user.setPlaceholderText("")
        self.lbl_email_user_3.setText(QCoreApplication.translate("win_guia_fertil", u"Senha", None))
#if QT_CONFIG(tooltip)
        self.btn_insert_user.setToolTip(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p>Pressione o bot\u00e3o ou tecla \u201cInsert\u201d para abrir a janela de cadastra do Produtor.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_insert_user.setText(QCoreApplication.translate("win_guia_fertil", u"Inserir\n"
"(Ins)", None))
#if QT_CONFIG(shortcut)
        self.btn_insert_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Ins", None))
#endif // QT_CONFIG(shortcut)
        self.btn_update_user.setText(QCoreApplication.translate("win_guia_fertil", u"Alterar \n"
"(Shift+Ins)", None))
#if QT_CONFIG(shortcut)
        self.btn_update_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Ins", None))
#endif // QT_CONFIG(shortcut)
        self.btn_cancelar_user.setText(QCoreApplication.translate("win_guia_fertil", u"Cancelar\n"
"(Ctrl+Space)", None))
#if QT_CONFIG(shortcut)
        self.btn_cancelar_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Ctrl+Space", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_change_user.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar Altera\u00e7\u00f5es \n"
"(Shift+Enter)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_change_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Return", None))
#endif // QT_CONFIG(shortcut)
        self.btn_save_user.setText(QCoreApplication.translate("win_guia_fertil", u"Salvar\n"
" (Enter)", None))
#if QT_CONFIG(shortcut)
        self.btn_save_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.tab_user.setTabText(self.tab_user.indexOf(self.tab_register_user), QCoreApplication.translate("win_guia_fertil", u"Cadastro", None))
        self.lbl_title_consult_user.setText(QCoreApplication.translate("win_guia_fertil", u"<html><head/><body><p align=\"center\"><span style=\" font-size:12pt; font-weight:600;\">Usu\u00e1rios</span></p></body></html>", None))
        ___qtablewidgetitem100 = self.table_grid_user.horizontalHeaderItem(0)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("win_guia_fertil", u"C\u00f3digo", None));
        ___qtablewidgetitem101 = self.table_grid_user.horizontalHeaderItem(1)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("win_guia_fertil", u"Nome", None));
        ___qtablewidgetitem102 = self.table_grid_user.horizontalHeaderItem(2)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("win_guia_fertil", u"CPF/CNPJ", None));
        ___qtablewidgetitem103 = self.table_grid_user.horizontalHeaderItem(3)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("win_guia_fertil", u"Endere\u00e7o", None));
        ___qtablewidgetitem104 = self.table_grid_user.horizontalHeaderItem(4)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("win_guia_fertil", u"N\u00famero", None));
        ___qtablewidgetitem105 = self.table_grid_user.horizontalHeaderItem(5)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("win_guia_fertil", u"Complemento", None));
        ___qtablewidgetitem106 = self.table_grid_user.horizontalHeaderItem(6)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("win_guia_fertil", u"Bairro", None));
        ___qtablewidgetitem107 = self.table_grid_user.horizontalHeaderItem(7)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("win_guia_fertil", u"Munic\u00edpio", None));
        ___qtablewidgetitem108 = self.table_grid_user.horizontalHeaderItem(8)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("win_guia_fertil", u"Estado", None));
        ___qtablewidgetitem109 = self.table_grid_user.horizontalHeaderItem(9)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("win_guia_fertil", u"CEP", None));
        ___qtablewidgetitem110 = self.table_grid_user.horizontalHeaderItem(10)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("win_guia_fertil", u"Telefone", None));
        ___qtablewidgetitem111 = self.table_grid_user.horizontalHeaderItem(11)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("win_guia_fertil", u"e-mail", None));
        ___qtablewidgetitem112 = self.table_grid_user.horizontalHeaderItem(12)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("win_guia_fertil", u"Usu\u00e1rio de login", None));
        ___qtablewidgetitem113 = self.table_grid_user.horizontalHeaderItem(13)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("win_guia_fertil", u"Senha", None));
        self.btn_search_user.setText(QCoreApplication.translate("win_guia_fertil", u"Buscar \n"
" (F2)", None))
#if QT_CONFIG(shortcut)
        self.btn_search_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.btn_excel_user.setText(QCoreApplication.translate("win_guia_fertil", u"Gerar Excel\n"
" (F11)", None))
#if QT_CONFIG(shortcut)
        self.btn_excel_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F11", None))
#endif // QT_CONFIG(shortcut)
        self.btn_pdf_report_user.setText(QCoreApplication.translate("win_guia_fertil", u"Relat\u00f3rio\n"
"(F12)", None))
#if QT_CONFIG(shortcut)
        self.btn_pdf_report_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"F12", None))
#endif // QT_CONFIG(shortcut)
        self.btn_delete_user.setText(QCoreApplication.translate("win_guia_fertil", u"Excluir\n"
"(Shift+Del)", None))
#if QT_CONFIG(shortcut)
        self.btn_delete_user.setShortcut(QCoreApplication.translate("win_guia_fertil", u"Shift+Del", None))
#endif // QT_CONFIG(shortcut)
        self.tab_user.setTabText(self.tab_user.indexOf(self.tab_consult_user), QCoreApplication.translate("win_guia_fertil", u"Usu\u00e1rios", None))
    # retranslateUi

