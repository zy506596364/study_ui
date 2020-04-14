# coding=utf-8
# author:yi.zhang
"""
绘制各种图形
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class DrawAllDemo(QWidget):
    def __init__(self):
        super(DrawAllDemo, self).__init__()
        self.resize(400, 600)
        self.setWindowTitle("绘制各种图形")

    def paintEvent(self, event):

        painter = QPainter()

        painter.begin(self)
        pen = QPen()
        pen.setColor(Qt.blue)
        painter.setPen(pen)
        # 绘制弧形
        rect = QRect(10, 10, 100, 100)
        # alen: 1个alen等于1/16度
        painter.drawArc(rect, 0, 90 * 16)

        # 绘制圆形
        painter.drawArc(120, 10, 100, 100, 0, 360 * 16)

        # 绘制椭圆
        painter.drawArc(10, 120, 100, 150, 0, 360 * 16)

        # 绘制椭圆
        painter.drawEllipse(200, 200, 100, 150)

        # 绘制一个太极图

        painter.drawArc(120, 120, 100, 100, 0, 360 * 16)
        painter.drawArc(145, 120, 50, 50, -90*16, 180 * 16)
        painter.drawArc(145, 170, 50, 50, 90 * 16, 180 * 16)
        # 绘制带弦的扇形
        painter.drawChord(250, 10, 100, 100, 12, 130*16)

        # 绘制扇形
        painter.drawPie(10, 300, 100, 100, 0, 60*16)

        # 绘制多边形
        point1 = QPoint(140, 380)
        point2 = QPoint(190, 300)
        point3 = QPoint(280, 330)
        point4 = QPoint(150, 280)
        point5 = QPoint(160, 180)
        polygon = QPolygon([point1,point2,point3,point4,point5])
        painter.drawPolygon(polygon)
        painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DrawAllDemo()
    window.show()
    sys.exit(app.exec_())