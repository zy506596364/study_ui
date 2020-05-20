# coding=utf-8
# author:yi.zhang

"""
线程类（QThread）
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


num = 0


class WorkThread(QThread):
    timer_ = pyqtSignal()
    end_ = pyqtSignal()

    def run(self):
        while True:
            self.sleep(1)
            if num == 5:
                self.end_.emit()  # 发送end信号
                break
            self.timer_.emit()  # 发送timer信号


class Counter(QWidget):
    def __init__(self):
        super(Counter, self).__init__()
        self.lcd_ = QLCDNumber()
        self.start_btn = QPushButton("计数开始")
        self.work_thread = WorkThread()
        self.work_thread.timer_.connect(self.count_timer)
        self.work_thread.end_.connect(self.end_)
        self.start_btn.clicked.connect(self.work_)
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("线程类编写计数器")
        self.resize(500, 300)
        _layout = QVBoxLayout()
        _layout.addWidget(self.lcd_)
        _layout.addWidget(self.start_btn)
        self.setLayout(_layout)

    def count_timer(self):
        global num
        num += 1
        self.lcd_.display(num)

    def end_(self):
        QMessageBox.information(self, "提示", "计数结束", QMessageBox.Ok)

    def work_(self):
        self.work_thread.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Counter()
    window.show()
    sys.exit(app.exec_())