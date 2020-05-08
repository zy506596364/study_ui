# coding=utf-8
# author:yi.zhang

"""
树控件的基本用法（QTreeWidget）
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class QTreeWidgetDemo(QWidget):
    def __init__(self):
        super(QTreeWidgetDemo, self).__init__()
        self.setWindowTitle("树控件的基本使用方法")
        self.resize(400, 300)
        self._layout = QHBoxLayout()
        self.treeWidget = QTreeWidget()
        self.set_ui()

    def set_ui(self):
        self.treeWidget.setColumnCount(2)
        self.treeWidget.setHeaderLabels(["版本", "版本号"])
        root = QTreeWidgetItem(self.treeWidget)
        root.setText(0, "主干版本")

        child1 = QTreeWidgetItem(root)
        child1.setText(0, "主干")
        child1.setText(1, "75")
        child1.setCheckState(0, Qt.Unchecked)

        root_1 = QTreeWidgetItem(self.treeWidget)
        root_1.setText(0, "海外版本")

        child_1 = QTreeWidgetItem(root_1)
        child_1.setText(0, "北美")
        child_1.setText(1, "9.4")
        child_1.setCheckState(0, Qt.Unchecked)

        child_2 = QTreeWidgetItem(root_1)
        child_2.setText(0, "北美")
        child_2.setText(1, "9.3")
        child_2.setCheckState(0, Qt.Unchecked)

        self.treeWidget.clicked.connect(self.onTree)

        self._layout.addWidget(self.treeWidget)

        self.setLayout(self._layout)

    def onTree(self, index):

        item = self.treeWidget.currentItem()
        print(item.checkState(0))
        # print("{0}=====>{1}".format(index.row(), item.text(0)))
        # print(item.text(0))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTreeWidgetDemo()
    window.show()
    sys.exit(app.exec_())
