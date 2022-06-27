
from PyQt6.QtWidgets import QApplication
import sys

from Grand_Restaurant_final import MenuWindow


def main():
    app = QApplication(sys.argv)
    win = MenuWindow()
    win.show()
    app.exec()


if __name__ == '__main__':
    main()
