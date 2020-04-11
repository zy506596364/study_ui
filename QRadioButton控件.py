# coding=utf-8
# author:yi.zhang

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QRadioButtonDemo(QWidget):
    def __init__(self):
        super(QRadioButtonDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("QRadioButton控件")
        self.resize(400, 300)
        layout = QHBoxLayout()
        self.button1 = QRadioButton("第一个选项")
        self.button1.setChecked(True)
        self.button1.toggled.connect(self.whichButton)
        self.button2 = QRadioButton("第二个选项")
        self.button2.toggled.connect(self.whichButton)

        self.button3 = QRadioButton("第3个选项")
        # self.button3.setChecked(True)
        self.button3.toggled.connect(self.whichButton)
        self.button4 = QRadioButton("第4个选项")
        self.button4.toggled.connect(self.whichButton)


        layout.addWidget(self.button1)
        layout.addWidget(self.button2)
        layout.addWidget(self.button3)
        layout.addWidget(self.button4)

        self.setLayout(layout)

    def whichButton(self):
        radiobutton = self.sender()
        if radiobutton.isChecked():
            print(radiobutton.text() + "被选中")
        else:
            print(radiobutton.text() + "被取消")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    my_window = QRadioButtonDemo()
    my_window.show()
    sys.exit(app.exec_())