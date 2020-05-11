# coding=utf-8
# author:yi.zhang

"""
停靠窗口控件(QDcokWidget)
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class QDockWidgetDemo(QMainWindow):
    def __init__(self, parent=None):
        super(QDockWidgetDemo, self).__init__(parent)
        self.setWindowTitle("停靠窗口控件")
        self.resize(500, 300)
        self.list_widget = QListWidget()
        self.list_widget.addItem("item1")
        self.list_widget.addItem("item2")
        self.list_widget.addItem("item3")
        self.items = QDockWidget("停靠", self)
        self.items.setWidget(self.list_widget)
        self.setCentralWidget(QTextEdit())
        self.addDockWidget(Qt.RightDockWidgetArea, self.items)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDockWidgetDemo()
    window.show()
    sys.exit(app.exec_())