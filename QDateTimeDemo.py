# coding=utf-8
# author:yi.zhang


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class DateTimeEditDemo(QWidget):
    def __init__(self):
        super(DateTimeEditDemo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("设置不同风格日期和时间")
        self.resize(300, 90)
        vlabel = QVBoxLayout()
        self.dateTimeEdit = QDateTimeEdit(QDateTime.currentDateTime())
        self.dateTimeEdit.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateTimeEdit.setMinimumDate(QDate.currentDate().addDays(-700))
        self.dateTimeEdit.setCalendarPopup(True)
        self.dateTimeEdit.dateChanged.connect(self.onDateChange)
        self.dateTimeEdit.timeChanged.connect(self.onTimeChange)
        self.dateTimeEdit.dateTimeChanged.connect(self.onDateTimeChange)
        dateEdit = QDateEdit(QDate.currentDate())
        timeEdit = QTimeEdit(QTime.currentTime())

        self.dateTimeEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        dateEdit.setDisplayFormat("yyyy.MM.dd")
        self.btn = QPushButton("点击获取时间")
        self.btn.clicked.connect(self.get_time)



        vlabel.addWidget(self.dateTimeEdit)
        vlabel.addWidget(dateEdit)
        vlabel.addWidget(timeEdit)
        vlabel.addWidget(self.btn)
        self.setLayout(vlabel)

    def onDateChange(self, date):
        print(date)

    def onTimeChange(self, time):
        print(time)

    def onDateTimeChange(self, date_time):
        print(date_time)

    def get_time(self):
        time = self.dateTimeEdit.dateTime()
        print(time)

        print(self.dateTimeEdit.maximumDateTime())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DateTimeEditDemo()
    window.show()
    sys.exit(app.exec_())
