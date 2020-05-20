# coding=utf-8
# author:yi.zhang

"""
定时器（QTimer）
"""

import sys
from PyQt5.QtWidgets import QApplication, QGridLayout, QLabel, QPushButton, QWidget
from PyQt5.QtCore import QTimer, QDateTime


class QTimerDemo(QWidget):
    def __init__(self):
        super(QTimerDemo, self).__init__()
        self.time_label = QLabel()
        self._timer = QTimer()
        self._timer.timeout.connect(self.show_time)
        self.start_btn = QPushButton("START")
        self.start_btn.clicked.connect(self.start_stop_time)
        # self.stop_btn = QPushButton("STOP")
        # self.stop_btn.setEnabled(False)
        # self.stop_btn.clicked.connect(self.start_stop_time)
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("定时器")
        # self.resize(500, 300)
        _g_layout = QGridLayout()
        _g_layout.addWidget(self.time_label, 0, 0, 1, 2)
        _g_layout.addWidget(self.start_btn, 1, 0)
        # _g_layout.addWidget(self.stop_btn, 1, 1)

        self.setLayout(_g_layout)

    def start_stop_time(self):
        # if self.sender().text() == "START":
        #     self.start_btn.setEnabled(False)
        #     self.stop_btn.setEnabled(True)
        #     self._timer.start(1000)
        #
        # elif self.sender().text() == "STOP":
        #     self.start_btn.setEnabled(True)
        #     self.stop_btn.setEnabled(False)
        #     self._timer.stop()

        if self.sender().text() == "START":
            self.start_btn.setText("STOP")
            self._timer.start(1000)

        elif self.sender().text() == "STOP":
            self.start_btn.setText("START")
            self._timer.stop()

    def show_time(self):
        time = QDateTime.currentDateTime()
        time_display = time.toString("yyyy-MM-dd hh:mm:ss dddd")
        self.time_label.setText(time_display)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QTimerDemo()
    window.show()
    sys.exit(app.exec_())




