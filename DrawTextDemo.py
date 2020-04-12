# coding=utf-8
# author:yi.zhang
"""
绘图API: 绘制文本
1. 文本
2. 各种图形（直线，点，椭圆，弧形，扇形，多边形）
3. 图像
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *


class DrawTextDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("在窗口上绘制文本")
        self.resize(400, 300)
        self.text = "恭喜中得大奖！！！"

    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setPen(QColor("red"))
        painter.setFont(QFont("SimSun", 25))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DrawTextDemo()
    window.show()
    sys.exit(app.exec_())