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
     QTreeWidgetItem, QListWidgetItem
from PyQt6.QtCore import Qt

import os
import sys

import time
# Importing the Timer subclass from the threading Class
from threading import Timer

from pui.interface_Restau_Carte_ou_Menus_V1 import Ui_MainWindow

from config_Grand_Restau_carte import ALL_ITEMS

DataRole = Qt.ItemDataRole.UserRole


class PuiWindow(Ui_MainWindow, QMainWindow):


    def __init__(self):
        super().__init__()

        # Mandatory for PUI Object to work !!!
        self.setupUi(self)

        # Some modifications
        self.load_items()
        self.setup_links()

        # subtotal: float
        self.subtotal = 0.00
        self.gain = 0.00

    def load_items(self):
        for category_name, item_list in ALL_ITEMS.items():
            category = QTreeWidgetItem()
            category.setText(0, category_name)
            category.setData(0, DataRole, None)
            # item_price: float
            for item_name, item_price in item_list:
                item = QTreeWidgetItem()
                item.setText(0, item_name)
                item.setText(1, str('{:.02f}'.format(item_price)))
                item.setData(0, DataRole, item_price)

                category.addChild(item)

            self.tree.addTopLevelItem(category)

    def setup_links(self):
        self.tree.itemDoubleClicked.connect(self.order_item)
        self.order_summarize.itemDoubleClicked.connect(self.cancel_item)
        self.pay_btn.clicked.connect(self.pay)
        self.cancel_btn.clicked.connect(self.cancel)

    def add_to_order(self, title, price):
        item = QListWidgetItem()
        item.setText(title)
        item.setData(DataRole, price)
        self.subtotal += price
        self.refresh_price()
        self.order_summarize.addItem(item)

    def order_item(self, item: QTreeWidgetItem):
        # price: float
        price = item.data(0, DataRole)
        if price is None:
            return
        item_name = item.text(0)
        pricetxt = '{:.02f}'.format(price)
        title = f'{item_name} -- ({pricetxt})'
        self.add_to_order(title, price)

    def cancel_item(self, item: QListWidgetItem):
        price = item.data(DataRole)
        row = self.order_summarize.row(item)
        self.order_summarize.takeItem(row)
        self.subtotal -= price
        self.refresh_price()

    def refresh_price(self):
        # self.subtotal_label.setText(str(self.subtotal))
        self.subtotal_label.setText('{:.02f}'.format(self.subtotal))
        total = self.subtotal * 1.10
        # self.total_label.setText(str(total))
        self.total_label.setText('{:.02f}'.format(total))

    def pay(self):
        self.gain += self.subtotal
        self.gain_label.setText('{:.02f}'.format(self.gain))
        self.cancel()

    def cancel(self):
        self.order_summarize.clear()
        self.subtotal = 0.00
        self.refresh_price()


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
