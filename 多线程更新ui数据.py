# coding=utf-8
# author:yi.zhang
"""
多线程更新UI数据
"""

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import time


class UpdatTime(QThread):
    update_time = pyqtSignal(str)

    def run(self):
        while True:
            _date = QDateTime.currentDateTime()
            current_date_time = _date.toString("yyyy-MM-dd hh:mm:ss")
            self.update_time.emit(str(current_date_time))
            time.sleep(1)


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self._update_time = UpdatTime()

        self._label = QLabel("asasf", self)
        self.btn = QPushButton("点击计时", self)
        self.btn.clicked.connect(self.on_click)
        self._init_ui()

    def _init_ui(self):
        self.setWindowTitle("多线程更新UI数据")
        self.resize(500, 500)
        self._label.move(30, 30)
        self._label.resize(300, 30)
        self.btn.move(30, 80)
        self._update_time.start()

    def on_click(self):
        self._update_time.update_time.connect(self.show_time)

    def show_time(self, _data):

        self._label.setText(_data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
