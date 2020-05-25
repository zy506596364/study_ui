# coding=utf-8
# author:yi.zhang

"""
为类添加多个信号
"""

from PyQt5.QtCore import *


class MySignal(QObject):

    signal1 = pyqtSignal()
    signal2 = pyqtSignal(int)
    signal3 = pyqtSignal(int, str)
    signal4 = pyqtSignal(list)
    signal5 = pyqtSignal(dict)
    signal6 = pyqtSignal([int, str], [str])

    def __init__(self):
        super(MySignal, self).__init__()
        self.signal1.connect(self.signal_call1)
        self.signal2.connect(self.signal_call2)
        self.signal3.connect(self.signal_call3)
        self.signal4.connect(self.signal_call4)
        self.signal5.connect(self.signal_call5)
        self.signal6[str].connect(self.signal_call6_overload)
        self.signal6[int, str].connect(self.signal_call6)

        self.signal1.emit()
        self.signal2.emit(10)
        self.signal3.emit(20, "hello !")
        self.signal4.emit([1, 2, 3, 4, 5])
        self.signal5.emit({"name": "ruby", "age": "30"})
        self.signal6[str].emit("hello python !")
        self.signal6[int, str].emit(20, "Hi !")

    def signal_call1(self):
        print("signal emit")

    def signal_call2(self, val):
        print("signal emit {}".format(val))

    def signal_call3(self, val, test):
        print("signal emit {1} {0:f}".format(val, test))

    def signal_call4(self, val):
        print("signal emit ", val)

    def signal_call5(self, val):
        print("signal emit ", val)

    def signal_call6(self, val, text):
        print("signal emit", val, text)

    def signal_call6_overload(self, text):
        print("signal_call6_overload", text)


if __name__ == '__main__':
    MySignal()