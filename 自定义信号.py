# coding=utf-8
# author:yi.zhang

"""
自定义信号
pyqtSignal()
"""

from PyQt5.QtCore import pyqtSignal, QObject


class MyTypeSignal(QObject):
    # 定义一个信号
    send_msg = pyqtSignal(object)
    # 定义一个发送三个参数的信号
    send_msg1 = pyqtSignal(str, int, int)

    def run_(self):
        self.send_msg.emit("Hello PyQt5")

    def run_1(self):
        self.send_msg1.emit("hello", 2, 3)


class MySlot(QObject):

    def get(self,  msg):
        print("信息：" + msg)

    def get_1(self, msg, a, b):
        print(msg)
        print(a, b)


if __name__ == '__main__':
    send_ = MyTypeSignal()
    slot_ = MySlot()
    send_.send_msg.connect(slot_.get)
    send_.run_()
    print("-"*50)
    send_.send_msg1.connect(slot_.get_1)
    send_.run_1()