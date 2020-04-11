# coding=utf-8
# author:yi.zhang

"""
QSlider控件
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QSliderDemo(QWidget):
    def __init__(self):
        super(QSliderDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(800, 400)
        self.setWindowTitle("滑块控件演示")
        layout = QVBoxLayout()
        self.label = QLabel("你好，python !")
        layout.addWidget(self.label)
        self.slider1 = QSlider(Qt.Horizontal)  # 设置滑块为水平方向
        self.slider1.setValue(18)  # 设置滑块的当前值
        self.slider1.setMinimum(10)  # 设置滑块最小值
        self.slider1.setMaximum(50)  # 设置滑块最大值
        self.slider1.setSingleStep(3)  # 设置滑块的步长
        self.slider1.setTickPosition(QSlider.TicksBelow)  # 设置滑块的刻度，且显示在下方
        self.slider1.setTickInterval(5)  # 设置滑块刻度的间隔
        self.slider1.valueChanged.connect(self.valuechanged)

        layout.addWidget(self.slider1)
        self.setLayout(layout)

    def valuechanged(self):
        size = self.sender().value()
        self.label.setFont(QFont("Arial", size))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSliderDemo()
    window.show()
    sys.exit(app.exec_())
