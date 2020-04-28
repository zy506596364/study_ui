# coding=utf-8
# author:yi.zhang

"""
在表格中快速定位到特定的行
1. 数据的定位：findItems
2. 如果找到了满足条件的单元格，会定位单元格所在的行： setSliderPosition(row)
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DataLocationDemo(QWidget):
    def __init__(self):
        super(DataLocationDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("快速定位到行")
        self.resize(600, 300)
        layout = QHBoxLayout()
        table_widget = QTableWidget()
        table_widget.setRowCount(40)
        table_widget.setColumnCount(4)
        for i in range(40):
            for j in range(4):
                table_widget.setItem(i, j, QTableWidgetItem("({0},{1})".format(i, j)))

        item1 = "(31,2)"
        items = table_widget.findItems(item1, Qt.MatchExactly)
        if len(items) > 0:
            item = items[0]
            item.setBackground(QBrush(QColor("blue")))
            item.setForeground(QBrush(QColor("red")))
            item.setFont(QFont("Times", 20, QFont.Thin))
            row_ = item.row()
            table_widget.verticalScrollBar().setSliderPosition(row_)
        layout.addWidget(table_widget)
        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DataLocationDemo()
    window.show()
    sys.exit(app.exec_())
