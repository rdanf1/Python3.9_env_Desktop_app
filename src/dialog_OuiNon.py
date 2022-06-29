
from PyQt6.QtWidgets import QDialog

from pui.dialog_yes_no import Ui_Dialog


class DialogWindow(Ui_Dialog, QDialog):
    def __init__(self, text):
        super().__init__()

        # Enable UI file parameters
        self.setupUi(self)
        # Fill the Warning msg
        self.content.setText(text)
        # Case a button is pressed
        self.yes_btn.clicked.connect(self.accept)
        self.no_btn.clicked.connect(self.reject)
