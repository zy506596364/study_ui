# coding=utf-8
# author:yi.zhang

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class WinSignal(QWidget):
    _signal = pyqtSignal()

    def __init__(self):
        super(WinSignal, self).__init__()
        self.setWindowTitle("为窗口添加信号")
        self.resize(500, 300)
        self.btn = QPushButton("点击关闭窗口", self)
        self.btn.clicked.connect(self.on_click)
        self._signal.connect(self._close)
        self.set_ui()

    def set_ui(self):
        self.btn.move(10, 30)
        # pass

    def on_click(self):
        self._signal.emit()

    def _close(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WinSignal()
    window.show()
    sys.exit(app.exec_())
