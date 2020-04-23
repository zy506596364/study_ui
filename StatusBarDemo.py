# coding=utf-8
# author:yi.zhang

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class StatusBarDemo(QMainWindow):
    def __init__(self):
        super(StatusBarDemo, self).__init__()
        self.setWindowTitle("状态栏")
        self.resize(400, 300)
        self.set_menu_bar()
        self.set_tool_bar()
        self.set_status_bar()
        self.btn1 = QPushButton("save", self)
        self.btn1.setGeometry(20,100,50,20)

    def set_menu_bar(self):
        self.menu_bar = self.menuBar()
        file = self.menu_bar.addMenu("File")
        file.addAction("show")
        file.triggered.connect(self.status_bar_show)

    def set_tool_bar(self):

        self.bar = self.addToolBar("File")
        new = QAction(QIcon("./timg.jpg"),"NEW", self)
        self.bar.addAction(new)
        self.bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.bar2 = self.addToolBar("close")
        close_ = QAction("关闭", self)
        self.bar2.addAction(close_)
        self.bar2.actionTriggered.connect(self.close)
        self.bar.actionTriggered.connect(self.toolbarpressed)

    def set_status_bar(self):
        self.statusBar_ = QStatusBar()
        self.setStatusBar(self.statusBar_)

    def toolbarpressed(self, bar):
        print("按下的工具栏是： {}".format(bar.text()))

    def status_bar_show(self, a):
        self.statusBar_.showMessage(a.text(), 5000)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = StatusBarDemo()
    window.show()
    sys.exit(app.exec_())