# coding=utf-8
# author:yi.zhang
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt



class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.set_ui()

    def set_ui(self):
        formlayout = QFormLayout()
        edit1 = QLineEdit()
        edit1.setValidator(QIntValidator())
        edit1.setMaxLength(4)

        edit1.setAlignment(Qt.AlignRight)
        formlayout.addRow("整数", edit1)

        edit2 = QLineEdit()
        edit2.setValidator(QDoubleValidator( 99,99,2))
        formlayout.addRow("浮点数", edit2)

        edit3 = QLineEdit()
        edit3.setInputMask("000.000.000.000.000;0")

        formlayout.addRow("ip",edit3)

        edit4 = QLineEdit()
        edit4.textChanged.connect(self.textchange)
        formlayout.addRow("  ", edit4)

        self.text = QTextEdit()
        formlayout.addRow("  ", self.text)
        self.btn = QPushButton("获取内容")
        formlayout.addRow("    ",self.btn)
        self.btn.clicked.connect(self.gettex)

        self.text2 = QLineEdit()
        formlayout.addRow("  ", self.text2)
        self.btn2 = QPushButton("获取内容")
        formlayout.addRow("    ", self.btn2)
        self.btn2.clicked.connect(self.get_line_text)



        self.setWindowTitle("综合案例")
        self.setLayout(formlayout)

    def textchange(self, text):
        print(text)

    def gettex(self):
        print(self.text.toPlainText())

    def get_line_text(self):
        print(self.text2.text())



if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    myWindow.show()
    sys.exit(app.exec_())


