# DR - 26/06/2022 - Python Studi's Course (Desktop Interface with Python)
#
# !! dependency pyqt6-plugins required by pyqt6-tools is for Python3.9 MAXIMUM !!
# NB: Installed Python3.9 instead of 3.10 ( $ sudo dnf install python3.9 )
#     Then installed a new Python 3.9 venv,
#     then installed PyQt6 and pyqt6-tools packages : ( venv ) $ pip install PyQt6 pyqt6-tools
#
# Pre-requesite :
#   1.  Using at the console : $ pyqt6-tools designer ( GUI tool for creating a user interface / ui )
#       For creating Windows canvas : windows with 2 onglets and a list in onglet 1
#   2.  Compile .ui file of gui designer to .py file ready to use (ie) :
#       $ pyuic6 -x gui/interface_file.ui -o pui/interface_file.py
#
# NB2: Renamed (within "$ pyqt6-tool designer interface_Restau_Carte_ou_Menus_V1.1.ui")
#      initialy called "treeWidget" to "tree".

from PyQt6.QtWidgets import QApplication, QMainWindow, \
     QTreeWidgetItem
from PyQt6.QtCore import Qt

import os
import sys

import time
# Importing the Timer subclass from the threading Class
from threading import Timer

from pui.interface_Restau_Carte_ou_Menus_V1 import Ui_MainWindow

from config_Grand_Restau import ALL_ITEMS

DataRole = Qt.ItemDataRole.UserRole


class PuiWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        # Mandatory for PUI Object to work !!!
        self.setupUi(self)

        # Some modifications
        self.load_items()

    def load_items(self):
        for category_name, item_list in ALL_ITEMS.items():
            category = QTreeWidgetItem()
            category.setText(0, category_name)
            category.setData(0, DataRole, None)
            for item_name, item_price in item_list:
                item = QTreeWidgetItem()
                item.setText(0, item_name)
                item.setText(1, str(item_price))
                item.setData(0, DataRole, item_price)
                category.addChild(item)
            self.tree.addTopLevelItem(category)


def main():
    # Once
    app = QApplication(sys.argv)

    restau_ui = PuiWindow()
    restau_ui.show()

    # Starting UI
    app.exec()

    # Exit code 137 forced (always) !
    print(os.getpid())
    os.kill(os.getpid(), 9)


if __name__ == "__main__":
    main()
