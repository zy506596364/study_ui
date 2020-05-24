# coding=utf-8
# author:yi.zhang

"""
控件之间的边界(QSplitter)
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("控件边界控件")
        self.resize(500, 300)
        edit1 = QTextEdit("哈哈哈")
        edit2 = QTextEdit("呵呵呵")
        edit3 = QTextEdit("嘿嘿嘿")
        splitter = QSplitter()
        splitter.addWidget(edit1)
        splitter.addWidget(edit2)
        splitter.addWidget(edit3)
        layout = QHBoxLayout()
        layout.addWidget(splitter)
        self.setLayout(layout)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec_())