# coding=utf-8
# author:yi.zhang


import sys
from PyQt5.QtWidgets import QApplication, QFormLayout, QLayout, QWidget, QLineEdit, QGridLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp


class Demo_(QWidget):
    def __init__(self):
        super(Demo_, self).__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle("校验器")
        formlayout = QFormLayout()
        gridlayout = QGridLayout()
        # intlineEdit = QIntValidator()
        # doublelineEdit = QDoubleValidator()
        # reglineEdit = QRegExpValidator()

        intlineEdit = QLineEdit()
        doublelineEdit = QLineEdit()
        reglineEdit = QLineEdit()

        # 设定校验器
        IntValidator = QIntValidator(self)
        IntValidator.setRange(1,99)
        DoubleValidator = QDoubleValidator(self)
        DoubleValidator.setDecimals(2)
        RegExpValidator = QRegExpValidator(self)
        reg = QRegExp("[A-Za-z0-9]+")
        RegExpValidator.setRegExp(reg)

        intlineEdit.setValidator(IntValidator)
        doublelineEdit.setValidator(DoubleValidator)
        reglineEdit.setValidator(RegExpValidator)

        formlayout.addRow("int", intlineEdit)
        formlayout.addRow("double", doublelineEdit)
        formlayout.addRow("reg", reglineEdit)


        self.setLayout(formlayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = Demo_()
    myWindow.show()
    sys.exit(app.exec_())
