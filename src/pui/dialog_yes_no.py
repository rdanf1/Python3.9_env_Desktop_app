# Form implementation generated from reading ui file 'src/gui/dialog_yes_no.ui'
#
# Created by: PyQt6 UI code generator 6.1.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(492, 216)
        Dialog.setToolTip("")
        Dialog.setAutoFillBackground(False)
        self.no_btn = QtWidgets.QPushButton(Dialog)
        self.no_btn.setGeometry(QtCore.QRect(370, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(6)
        self.no_btn.setFont(font)
        self.no_btn.setToolTip("")
        self.no_btn.setAutoFillBackground(True)
        self.no_btn.setObjectName("no_btn")
        self.yes_btn = QtWidgets.QPushButton(Dialog)
        self.yes_btn.setGeometry(QtCore.QRect(10, 80, 471, 131))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.yes_btn.setFont(font)
        self.yes_btn.setToolTip("")
        self.yes_btn.setObjectName("yes_btn")
        self.content = QtWidgets.QLabel(Dialog)
        self.content.setGeometry(QtCore.QRect(70, 40, 401, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.content.setFont(font)
        self.content.setObjectName("content")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.no_btn.setText(_translate("Dialog", "Non Chui pas sûr à 100%..."))
        self.yes_btn.setText(_translate("Dialog", "OUI"))
        self.content.setText(_translate("Dialog", "Etes-vous bien SÛR ? ( à 100% )"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
