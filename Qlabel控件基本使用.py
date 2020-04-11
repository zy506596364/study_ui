# coding=utf-8
# author:yi.zhang
"""
QLabel 控件
setAlignment() 设置文本的对齐方式
setIndent() 设置文本缩进
text() 获取文本内容
setBuddy() 设置伙伴关系
setText() 设置文本内容
selectedText() 返回所选择的字符
setWordWrap() 设置是否允许换行
---------------------------------------------
QLabel常用的信号（事件）
1. 当鼠标滑过QLabel控件时触发：LinkHovered
2. 当鼠标单击QLabel控件时触发：linkActivated

"""
from PyQt5.QtWidgets import QMainWindow, QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys


class QLabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label_1 = QLabel(self)
        label_2 = QLabel(self)
        label_3 = QLabel(self)
        label_4 = QLabel(self)

        label_1.setText("这是第一个标签")
        label_1.setAlignment(Qt.AlignCenter)

        label_2.setText("<a href=‘#’>欢迎使用python</a>")

        label_3.setAlignment(Qt.AlignCenter)
        label_3.setToolTip("这是一个图片")
        label_3.setPixmap(QPixmap("./p1.jpg"))

        label_4.setOpenExternalLinks(True)
        label_4.setText("<a href='https://www.baidu.com/'>欢迎使用python</a>")
        label_4.setToolTip("这是一个网站链接")
        label_4.setAlignment(Qt.AlignLeft)

        label_2.linkHovered.connect(self.linkHovered)
        label_4.linkActivated.connect(self.linkActivated)

        vbox = QVBoxLayout()
        vbox.addWidget(label_1)
        vbox.addWidget(label_2)
        vbox.addWidget(label_3)
        vbox.addWidget(label_4)
        self.setLayout(vbox)
        self.setWindowTitle("QLable使用")

    def linkHovered(self):
        print("滑过事件")

    def linkActivated(self):
        print("鼠标点击事件")

    def openIe(self):
        pass


if __name__ == "__main__":
     app = QApplication(sys.argv)
     myWindow = QLabelDemo()
     myWindow.show()
     sys.exit(app.exec_())
