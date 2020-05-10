# coding=utf-8
# author:yi.zhang

"""
堆栈窗口控件（QStackedWidget）

"""

import sys
from PyQt5.QtWidgets import (QApplication, QStackedWidget, QHBoxLayout,
                             QWidget, QListWidget, QFormLayout, QLineEdit,
                             QTableWidget, QWidgetItem, QTableWidgetItem
                             )


class QStackedWidgetDemo(QWidget):
    def __init__(self):
        super(QStackedWidgetDemo, self).__init__()
        self.setWindowTitle("堆栈窗口控件")
        self.resize(500, 300)
        self.list_widget = QListWidget()
        self.stack1 = QWidget()
        self.stack2 = QWidget()
        # self.stack3 = QWidget()
        self.stack = QStackedWidget()
        self.list_widget.currentRowChanged.connect(self.display)
        self.set_ui()
        self.stack1_ui()
        self.stack2_ui()

    def set_ui(self):
        self.list_widget.insertItem(0, "个人信息")
        self.list_widget.insertItem(1, "账户信息")
        self.stack.addWidget(self.stack1)
        self.stack.addWidget(self.stack2)
        _layout = QHBoxLayout()
        _layout.addWidget(self.list_widget)
        _layout.addWidget(self.stack)
        self.setLayout(_layout)

    def stack1_ui(self):
        _layout = QFormLayout()
        _layout.addRow("昵称： ", QLineEdit("zy01"))
        _layout.addRow("等级： ", QLineEdit("80"))
        self.stack1.setLayout(_layout)

    def stack2_ui(self):
        _layout = QHBoxLayout()
        _table = QTableWidget()
        _table.setRowCount(5)
        _table.setColumnCount(3)
        _table.setHorizontalHeaderLabels(["昵称", "登录名", "等级"])
        item1 = QTableWidgetItem("zy01")
        item2 = QTableWidgetItem("zy01")
        item3 = QTableWidgetItem("80")
        _table.setItem(0, 0, item1)
        _table.setItem(0, 1, item2)
        _table.setItem(0, 2, item3)
        _layout.addWidget(_table)
        self.stack2.setLayout(_layout)


    def display(self, _index):
        self.stack.setCurrentIndex(_index)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QStackedWidgetDemo()
    window.show()
    sys.exit(app.exec_())



