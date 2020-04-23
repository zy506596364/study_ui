# coding=utf-8
# author:yi.zhang

"""
显示二维表数据 （QTableView控件）

需要创建QTableView实例和一个数据源（Model），然后将两者关联

MVC ：Model  Viewer  Controller

MVC的目的是将后端的数据和前段页面的耦合度降低
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class TableViewDemo(QWidget):
    def __init__(self):
        super(TableViewDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("二维表数据")
        self.resize(600, 400)
        layout = QVBoxLayout()
        tableView = self.set_tableView()

        layout.addWidget(tableView)
        self.setLayout(layout)

    def set_tableView(self):
        _model = QStandardItemModel(4, 3)
        _model.setHorizontalHeaderLabels(["id", "name", "age"])
        a = ["10", "雷神", "1000"]
        for i in range(3):
            for j in a:
                _model.setItem(i, a.index(j), QStandardItem(j))
        _tableView = QTableView()
        # 关联tableview控件
        _tableView.setModel(_model)
        return _tableView


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TableViewDemo()
    window.show()
    sys.exit(app.exec_())