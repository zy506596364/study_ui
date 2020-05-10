# coding=utf-8
# author:yi.zhang
"""
选项卡控件：QTabWidget
"""

import sys
from PyQt5.QtWidgets import *


class QTabWidgetDemo(QTabWidget):
    def __init__(self):
        super(QTabWidgetDemo, self).__init__()
        self.setWindowTitle("选项卡控件例子")
        self.resize(500, 300)
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.set_ui()
        self.tab1_ui()
        self.tab2_ui()

    def set_ui(self):
        self.addTab(self.tab1, "单个信息")
        self.addTab(self.tab2, "全部名单")

    def tab1_ui(self):
        _layout = QFormLayout()
        _layout.addRow("昵称: ", QLineEdit("zy01"))
        _layout.addRow("等级: ", QLineEdit("80"))
        self.tab1.setLayout(_layout)

    def tab2_ui(self):
        _layout = QVBoxLayout()
        _table_widget = QTableWidget()
        _table_widget.setRowCount(5)
        _table_widget.setColumnCount(3)
        _table_widget.setHorizontalHeaderLabels(["昵称", "登录名", "等级"])
        _layout.addWidget(_table_widget)
        self.tab2.setLayout(_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTabWidgetDemo()
    window.show()
    sys.exit(app.exec_())
