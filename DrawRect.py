# coding=utf-8
# author:yi.zhang

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DrawFill(QWidget):
    def __init__(self):
        super(DrawFill, self).__init__()
        self.resize(400, 600)
        self.setWindowTitle("画刷填充")

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        brush = QBrush(Qt.SolidPattern)
        painter.setBrush(brush)
        painter.drawRect(10,15,90,60)

        brush = QBrush(Qt.Dense2Pattern)
        painter.setBrush(brush)
        painter.drawRect(120, 15, 90, 60)


        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawFill()
    window.show()
    sys.exit(app.exec_())