# coding=utf-8
# author:yi.zhang

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ToolBarDemo(QMainWindow):
    def __init__(self):
        super(ToolBarDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("工具栏")
        self.resize(400, 300)
        self.bar = self.addToolBar("File")
        new = QAction(QIcon("./timg.jpg"),"NEW", self)
        self.bar.addAction(new)
        self.bar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.bar2 = self.addToolBar("close")
        close_ = QAction("关闭", self)
        self.bar2.addAction(close_)
        self.bar2.actionTriggered.connect(self.close)
        self.bar.actionTriggered.connect(self.toolbarpressed)

    def toolbarpressed(self, bar):
        print("按下的工具栏是： {}".format(bar.text()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ToolBarDemo()
    window.show()
    sys.exit(app.exec_())