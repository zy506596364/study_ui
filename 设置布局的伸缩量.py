# coding=utf-8
# author:yi.zhang

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("设置伸缩量")
        # btn1 = QPushButton("按钮1")
        # btn2 = QPushButton("按钮2")
        # btn3 = QPushButton("按钮3")
        # btn4 = QPushButton("按钮4")
        # btn5 = QPushButton("按钮5")
        # layout = QVBoxLayout()
        # layout.addStretch(1)
        #
        # layout.addWidget(btn1)
        # layout.addStretch(1)
        # layout.addWidget(btn2)
        # layout.addStretch(1)
        # layout.addWidget(btn3)
        #
        # layout1 = QHBoxLayout()
        # layout1.addStretch(1)
        # layout1.addWidget(btn4)
        # # layout1.addWidget(btn5)
        # layout.addLayout(layout1)
        v_box = QVBoxLayout()
        v_box.setSpacing(30)
        v_box.addStretch(0)
        h_box1 = QHBoxLayout()
        h_box1.addWidget(QLabel("初始价格"))
        h_box1.addWidget(QLineEdit())

        v_box.addLayout(h_box1)

        v_box1 = QVBoxLayout()
        # v_box1.addStretch(0)
        v_box1.addWidget(QLabel("期望价格"))
        v_box1.addWidget(QLineEdit())
        v_box2 = QVBoxLayout()
        # v_box2.addStretch(0)
        v_box2.addWidget(QLabel("投入金额"))
        v_box2.addWidget(QLineEdit())
        h_box2 = QHBoxLayout()
        h_box2.addLayout(v_box1)
        h_box2.addLayout(v_box2)

        v_box.addLayout(h_box2)

        h_box3 = QHBoxLayout()
        h_box3.addStretch(1)
        h_box3.addWidget(QPushButton("确定"))
        v_box.addStretch(1)
        v_box.addLayout(h_box3)
        self.setLayout(v_box)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec_())