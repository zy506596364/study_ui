# coding=utf-8
# author:yi.zhang
"""
QCheckBox控件
3种状态
0 未选中
1 半选中
2 选中
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class CheckBoxDemo(QWidget):
    def __init__(self):
        super(CheckBoxDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("复选框演示")
        self.resize(400, 300)
        layout1 = QVBoxLayout()

        self.button1 = QCheckBox()
        self.button1.setText("第一个选项")
        self.button1.setChecked(True)
        self.button1.stateChanged.connect(self.stateChanged)


        self.button2 = QCheckBox("第二个选项")
        self.button2.stateChanged.connect(self.stateChanged)

        self.button3 = QCheckBox("半选择状态")
        self.button3.setTristate(True)
        self.button3.setCheckState(Qt.PartiallyChecked)

        layout1.addWidget(self.button1)
        layout1.addWidget(self.button2)
        layout1.addWidget(self.button3)


        self.button4 = QCheckBox("第二区1项")
        self.button5 = QCheckBox("第二区2项")
        self.button6 = QCheckBox("第二区3项")
        layout1.addWidget(self.button4)
        layout1.addWidget(self.button5)
        layout1.addWidget(self.button6)


        self.setLayout(layout1)

    def stateChanged(self):
        state1 = str(self.button1.isChecked()) + " " + str(self.button1.checkState())
        state2 = str(self.button2.isChecked()) + " " + str(self.button2.checkState())
        print(state1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = CheckBoxDemo()
    window.show()
    sys.exit(app.exec_())