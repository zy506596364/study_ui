# coding=utf-8
# author:yi.zhang
"""
日历控件

"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class CalendarWidgetDemo(QWidget):
    def __init__(self):
        super(CalendarWidgetDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("日历控件演示")
        self.resize(300, 300)
        layout = QVBoxLayout()
        self.cal = QCalendarWidget()
        self.cal.setGridVisible(True)
        self.cal.clicked.connect(self.changeDate)
        self.datelabel = QLabel(self.cal.selectedDate().toString("yyyy-MM-dd dddd"))
        layout.addWidget(self.cal)
        layout.addWidget(self.datelabel)

        self.setLayout(layout)

    def changeDate(self):
        self.datelabel.setText(self.cal.selectedDate().toString("yyyy-MM-dd dddd"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CalendarWidgetDemo()
    window.show()
    sys.exit(app.exec_())