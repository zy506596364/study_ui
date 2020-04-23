# coding=utf-8
# author:yi.zhang

"""
扩展的列表控件（QListWidget）
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class QListWidgetDemo(QWidget):
    def __init__(self):
        super(QListWidgetDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("列表数据")
        self.resize(400, 300)
        list_widget = QListWidget()
        list_widget.addItem("item1")
        list_widget.addItem("item2")
        list_widget.addItem("item3")
        list_widget.addItem("item4")
        list_widget.addItem("item5")
        list_widget.itemClicked.connect(self.clicke_Event)
        layout = QVBoxLayout()
        layout.addWidget(list_widget)
        self.setLayout(layout)

    def clicke_Event(self, item):
        QMessageBox.information(self, "提示", "你选择了{}".format(item.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QListWidgetDemo()
    window.show()
    sys.exit(app.exec_())