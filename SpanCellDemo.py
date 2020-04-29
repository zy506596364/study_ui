# coding=utf-8
# author:yi.zhang

"""
合并单元格

setSpan(row, column, 要合并的行数，要合并的列数)
"""

import sys
from PyQt5.QtWidgets import *


class SpanCellDemo(QWidget):
    def __init__(self):
        super(SpanCellDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("合并单元格")
        self.resize(400, 300)
        _layout = QHBoxLayout()
        _table_widget = QTableWidget()
        _table_widget.setRowCount(5)
        _table_widget.setColumnCount(3)
        _table_widget.setHorizontalHeaderLabels(["姓名", "性别", "年龄"])
        _table_widget.verticalHeader().setVisible(False)
        name_item = QTableWidgetItem("张三丰")
        _table_widget.setItem(0, 0, name_item)
        _table_widget.setSpan(0, 0, 3, 1)

        sex_item = QTableWidgetItem("男")
        _table_widget.setItem(0, 1, sex_item)

        age_item = QTableWidgetItem("100")
        _table_widget.setItem(0, 2, age_item)

        _layout.addWidget(_table_widget)

        self.setLayout(_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpanCellDemo()
    window.show()
    sys.exit(app.exec_())