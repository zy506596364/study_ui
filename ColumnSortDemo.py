# coding=utf-8
# author:yi.zhang
"""
按列排序

1. 按哪一列排序
2. 排序类型：升序或者降序

sortItem(columnIndex, orderType)
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class ColumnSortDemo(QWidget):
    def __init__(self):
        super(ColumnSortDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("排序例子")
        self.resize(500, 300)
        _layout = QHBoxLayout()
        self._table_widget = QTableWidget()
        self._table_widget.setRowCount(5)
        self._table_widget.setColumnCount(3)
        self._table_widget.setHorizontalHeaderLabels(["姓名", "年龄", "身高"])
        self._table_widget.verticalHeader().setVisible(False)
        self._table_widget.setItem(0, 0, QTableWidgetItem("小明"))
        self._table_widget.setItem(0, 1, QTableWidgetItem("20"))
        self._table_widget.setItem(0, 2, QTableWidgetItem("180"))

        self._table_widget.setItem(1, 0, QTableWidgetItem("小芳"))
        self._table_widget.setItem(1, 1, QTableWidgetItem("22"))
        self._table_widget.setItem(1, 2, QTableWidgetItem("170"))

        self._table_widget.setItem(2, 0, QTableWidgetItem("小王"))
        self._table_widget.setItem(2, 1, QTableWidgetItem("20"))
        self._table_widget.setItem(2, 2, QTableWidgetItem("185"))

        _layout.addWidget(self._table_widget)

        btn_asc = QPushButton("升序")
        btn_asc.clicked.connect(self._sort)
        _layout.addWidget(btn_asc)

        btn_desc = QPushButton("降序")
        btn_desc.clicked.connect(self._sort)
        _layout.addWidget(btn_desc)

        self.setLayout(_layout)

    def _sort(self):
        if self.sender().text() == "升序":
            self._table_widget.sortItems(2, Qt.AscendingOrder)

        elif self.sender().text() == "降序":
            self._table_widget.sortItems(2, Qt.DescendingOrder)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColumnSortDemo()
    window.show()
    sys.exit(app.exec_())
