# coding=utf-8
# author:yi.zhang
"""
下拉列表控件
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QComboBoxDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("下拉列表控件")
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.lable = QLabel()
        self.lable.setText("请选择编程语言")
        self.cb = QComboBox()
        self.cb.addItem("python")
        self.cb.addItem("c#")
        self.cb.addItems(["c++", "java", "php"])
        self.cb.currentIndexChanged.connect(self.index_changed)


        layout.addWidget(self.lable)
        layout.addWidget(self.cb)
        self.setLayout(layout)

    def index_changed(self, i):
        print(self.cb.currentText(), i)
        self.lable.setText(self.cb.currentText())
        self.lable.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QComboBoxDemo()
    window.show()
    sys.exit(app.exec_())