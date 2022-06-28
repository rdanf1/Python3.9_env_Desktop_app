
from PyQt6.QtWidgets import QDialog

from pui.dialog_yes_no import Ui_Dialog


class DialogWindow(Ui_Dialog, QDialog):
    def __init__(self, text):
        super().__init__()

        # Enable UI file parameters
        self.setupUI(self)
