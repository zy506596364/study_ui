# coding=utf-8
# author:yi.zhang
"""
按钮控件（pushbutton）

所有的控件都有一个父类QAbstractButton

QPushButton
AToolButton
QRadioButton
QCheckBox
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class PushButtonDemo(QDialog):
    def __init__(self):
        super(PushButtonDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("PushButton控件")
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.button1 = QPushButton("第一个按钮")
        # self.button1.setChecked(True)
        # self.button1.toggle()
        self.button1.clicked.connect(lambda: self.whichbutton(self.button1))
        self.button1.clicked.connect(lambda: self.buttonstate(self.button1))

        self.button2 = QPushButton("第2个按钮")
        # self.button2.setChecked(True)
        # self.button2.toggle()
        self.button2.setIcon(QIcon(QPixmap("./logo.png")))
        self.button2.clicked.connect(lambda: self.whichbutton(self.button2))
        self.button2.clicked.connect(lambda: self.buttonstate(self.button2))

        self.button3 = QPushButton("不可用按钮")
        self.button3.setEnabled(False)

        self.button4 = QPushButton("默认按钮")
        self.button4.setDefault(True)
        self.button4.clicked.connect(lambda: self.whichbutton(self.button4))

        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)
        self.setLayout(layout)

    def whichbutton(self, btn):
        print(btn.text())

    def buttonstate(self, btn):
        print(btn)
        if btn.isChecked():
            print(btn.text() + "已经被选中")
        else:
            print(btn.text() + "没有被选中")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = PushButtonDemo()
    myWindow.show()
    sys.exit(app.exec_())