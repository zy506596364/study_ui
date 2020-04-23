# coding=utf-8
# author:yi.zhang

"""
显示列表数据（ListView控件）
"""


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ListViewDemo(QWidget):
    def __init__(self):
        super(ListViewDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("列表数据")
        self.resize(400, 300)
        layout = QVBoxLayout()
        _listView = self.set_listView()
        _listView.clicked.connect(self.clicke_Event)
        layout.addWidget(_listView)
        self.setLayout(layout)

    def set_listView(self):
        _listView = QListView()
        _model = QStringListModel()
        _list = ['列表项1','列表项2','列表项3','列表项3']
        _model.setStringList(_list)
        _listView.setModel(_model)
        # _listView.sender()
        return _listView

    def clicke_Event(self, item):
        QMessageBox.information(self, "提示", "你选择了{}".format(item.data()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ListViewDemo()
    window.show()
    sys.exit(app.exec_())