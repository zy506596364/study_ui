# coding=utf-8
# author:yi.zhang

"""
显示上下文菜单
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QTableWidgetContextMenuDemo(QWidget):
    def __init__(self):
        super(QTableWidgetContextMenuDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("显示上下文菜单")
        self.resize(500, 300)
        _layout = QHBoxLayout()
        self._table_widget = QTableWidget()
        self._table_widget.setRowCount(5)
        self._table_widget.setColumnCount(3)
        self._table_widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        _name_item = QTableWidgetItem("HAHA1")
        _name_item.setTextAlignment(Qt.AlignCenter)
        self._table_widget.setItem(0, 0, _name_item)
        _name_item = QTableWidgetItem("HAHA2")
        _name_item.setTextAlignment(Qt.AlignCenter)
        self._table_widget.setItem(1, 0, _name_item)
        _name_item = QTableWidgetItem("HAHA3")
        _name_item.setTextAlignment(Qt.AlignCenter)
        self._table_widget.setItem(2, 0, _name_item)

        self._table_widget.setContextMenuPolicy(Qt.CustomContextMenu)
        self._table_widget.customContextMenuRequested.connect(self.contextMenu)

        _layout.addWidget(self._table_widget)

        self.setLayout(_layout)

    def contextMenu(self, _pos):
        print(_pos)
        screenPos = self._table_widget.mapToGlobal(_pos)
        _y = screenPos.y() + 25
        _x = screenPos.x() + 20
        # for i in self._table_widget.selectionModel().selection().indexes():
        #     rowNum = i.row()
        menu = QMenu()
        item1 = menu.addAction("菜单1")
        item1.triggered.connect(self.selectMenu)
        item2 = menu.addAction("菜单2")
        item3 = menu.addAction("菜单3")
        action = menu.exec(QPoint(_x, _y))

    def selectMenu(self):
        info = self.sender().text()
        QMessageBox.information(self, "菜单", info)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTableWidgetContextMenuDemo()
    window.show()
    sys.exit(app.exec_())