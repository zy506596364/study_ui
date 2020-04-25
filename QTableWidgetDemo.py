# coding=utf-8
# author:yi.zhang

"""
扩展的表格控件（QTableWidget）
"""

import sys
from PyQt5.QtWidgets import *


class QTableWidgetDemo(QWidget):
    def __init__(self):
        super(QTableWidgetDemo, self).__init__()
        self.setWindowTitle("扩展的表格控件")
        self.resize(400, 300)
        self._layout = QHBoxLayout()
        self._table_widget = QTableWidget()
        self.set_ui()

    def set_ui(self):
        self._table_widget.setRowCount(3)
        self._table_widget.setColumnCount(3)
        self._table_widget.setHorizontalHeaderLabels(["id", "name", "age"])
        self._table_widget.setItem(0, 0, QTableWidgetItem("1"))
        self._table_widget.setItem(0, 1, QTableWidgetItem("小明"))
        self._table_widget.setItem(0, 2, QTableWidgetItem("18"))

        # 设置单元格为不可编辑
        self._table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)

        # 设置为整行选择
        self._table_widget.setSelectionBehavior(QAbstractItemView.SelectRows)

        # 隐藏水平表头
        self._table_widget.horizontalHeader().setVisible(False)

        # 隐藏列表头
        self._table_widget.verticalHeader().setVisible(False)

        # 隐藏表格线
        self._table_widget.setShowGrid(False)

        self._layout.addWidget(self._table_widget)
        self.setLayout(self._layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTableWidgetDemo()
    window.show()
    sys.exit(app.exec_())
