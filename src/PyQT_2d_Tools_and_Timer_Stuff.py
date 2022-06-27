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
#   2.  Compile .ui file of gui designer to .py file ready to use :
#       $ pyuic6 -x gui/interface_file.ui -o pui/interface_file.py
#
# NB2: Renamed (within "$ pyqt6-tool designer interface_file.ui")
#      initialy called "treeWidget" to "tree".

from PyQt6.QtWidgets import QApplication, QMainWindow, \
    QTreeWidgetItem

# For uic.LoadUi thing
from PyQt6 import uic
# Ds Video HS
from PyQt6.uic import loadUi

import os
import sys

import time
# Importing the Timer subclass from the threading Class
from threading import Timer

from pui.interface_file import Ui_MainWindow


class GuiWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Pff... for uic.loadUI to work with relative path...
        print(os.chdir(
            "/home/rdanf0/Bureau/Python___Environments/Python3.9_env_Desktop_app/src"))
        # print(os.path.join('gui', 'interface_file.ui'))
        uic.loadUi(os.path.join('gui', 'interface_file.ui'), self)

        # Some modifications
        self.setWindowTitle('GUI')
        self.setGeometry(60, 140, self.geometry().height(), self.geometry().width())
        item = QTreeWidgetItem()
        item.setText(0, 'Hello & GUI')
        self.tree.addTopLevelItem(item)


class PuiWindow(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()

        # Mandatory for PUI Object to work !!!
        self.setupUi(self)

        # Some modifications
        self.setGeometry(600, 310, self.geometry().width(), self.geometry().height())
        self.setWindowTitle('PUI')
        item = QTreeWidgetItem()
        item.setText(0, 'Hello & PUI')
        self.tree.addTopLevelItem(item)


def main():
    # Once
    app = QApplication(sys.argv)

    first = GuiWindow()
    first.show()

    # Simultaneous if commented (first & second Windows opened later...)
    # app.exec()

    second = PuiWindow()
    second.show()

    # Breathe a bit before launching...
    # time.sleep(1)

    # Creating an object Timer t :
    # DR : Purpose is to avoid Mouse clicks for destroying 2 Windows...
    # Here, 8.1 means that the execution of the function is after 8 seconds (almost)
    # Setting a timer with exit function of app !!!
    # ( 4 seconds is enough to see, no need to click with the mouse !!! )
    t = Timer(interval=8.1, function=app.exit)

    # starting UI destroying Timer t :
    t.start()  # after 30 seconds, "hello, world" will be printed

    # Starting UI
    app.exec()

    # Exit code 137 forced (always) !
    print(os.getpid())
    os.kill(os.getpid(), 9)


if __name__ == "__main__":
    main()
