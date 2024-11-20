from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QDialog

from succession_planting_ui import Ui_succession_planting


class SuccessionPlanting(QDialog, Ui_succession_planting):

    def __init__(self):
        super(SuccessionPlanting, self).__init__()
        self.setupUi(self)
        icon = QIcon('./images/soon/guiafertil.png')
        self.setWindowIcon(icon)
        self.center_window()
        self.confirm_registration = False
        self.btn_confirm.clicked.connect(lambda: self.confirm())
        self.btn_cancel.clicked.connect(lambda: self.exit())

    def confirm(self):
        self.confirm_registration = True
        self.close()

    def exit(self):
        self.confirm_registration = False
        self.close()

    def center_window(self):
        window_geometry = self.frameGeometry()
        screens = QApplication.screens()
        if screens:
            primary_screen = screens[0]
            screen_geometry = primary_screen.availableGeometry().center()
            window_geometry.moveCenter(screen_geometry)
            self.move(window_geometry.topLeft())
