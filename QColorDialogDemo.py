# coding=utf-8
# author:yi.zhang
"""
颜色对话框：QColorDialog
"""

import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class QColorDialogDemo(QWidget):
    def __init__(self):
        super(QColorDialogDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("颜色设置对话框")
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.btn = QPushButton("字体颜色设置按钮")
        self.btn.clicked.connect(self.changeColor)
        self.label = QLabel()
        self.label.setText("颜色设置演示。。。")
        self.label.setAlignment(Qt.AlignRight | Qt.AlignCenter)
        layout.addWidget(self.btn)
        layout.addWidget(self.label)
        self.btnBG = QPushButton("设置字体背景色按钮")
        self.btnBG.clicked.connect(self.changeBGColor)
        layout.addWidget(self.btnBG)
        self.setLayout(layout)

    def changeColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.WindowText, color)
        self.label.setPalette(p)

    def changeBGColor(self):
        color = QColorDialog.getColor()
        p = QPalette()
        p.setColor(QPalette.Window, color)
        self.label.setAutoFillBackground(True)
        self.label.setPalette(p)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QColorDialogDemo()
    window.show()
    sys.exit(app.exec_())