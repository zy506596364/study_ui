# coding=utf-8
# author:yi.zhang

"""
滚动条控件
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QScrollBarDemo(QWidget):
    def __init__(self):
        super(QScrollBarDemo, self).__init__()
        self.resize(500, 500)
        self.set_ui()

    def set_ui(self):
        h_layout = QHBoxLayout()
        self._label = QLabel("拖动滚动条改变字体颜色")
        h_layout.addWidget(self._label)
        self._scroll_1 = QScrollBar()
        self._scroll_1.setMaximum(256)
        self._scroll_1.sliderMoved.connect(self.slider_move)
        h_layout.addWidget(self._scroll_1)

        self._scroll_2 = QScrollBar()
        self._scroll_2.setMaximum(100)
        self._scroll_2.sliderMoved.connect(self.slider_move2)
        h_layout.addWidget(self._scroll_2)
        self.setLayout(h_layout)

        self.y = self._label.y()


    def slider_move(self):
        print(self._scroll_1.value())
        palette = QPalette()
        c = QColor(200, 200, self._scroll_1.value(), 255)
        palette.setColor(QPalette.Foreground, c)
        self._label.setPalette(palette)

    def slider_move2(self):
        self._label.move(self._label.x(), self.y + self._scroll_2.value())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QScrollBarDemo()
    window.show()
    sys.exit(app.exec_())

