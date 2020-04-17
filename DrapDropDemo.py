# coding=utf-8
# author:yi.zhang

"""
让控件支持拖拽
A控件拖动到B
A

B 需要设置为可接收控件 setAcceptDrops(True)
  A拖到B时触发  drapEnterEvent
  在B的区域放下A时触发 dropEvent
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MyComboBox(QComboBox):
    def __init__(self):
        super(MyComboBox, self).__init__()
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasText():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        self.addItem(event.mimeData().text())


class DrapDropDemo(QWidget):
    def __init__(self):
        super(DrapDropDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("拖拽控件演示")
        self.resize(400, 300)
        layout = QFormLayout()
        layout.addRow(QLabel("拖拽下面的内容"))
        btn = QPushButton("拖拽下面的内容")
        layout.addRow(btn)
        lineEdit = QLineEdit()
        lineEdit.setDragEnabled(True)
        self.comboBox = MyComboBox()
        layout.addRow(lineEdit, self.comboBox)
        self.setLayout(layout)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrapDropDemo()
    window.show()
    sys.exit(app.exec_())