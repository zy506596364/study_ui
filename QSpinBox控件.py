# coding=utf-8
# author:yi.zhang
"""
计数器控件
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QSpinBoxDemo(QWidget):
    def __init__(self):
        super(QSpinBoxDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("计数器控件")
        self.resize(300, 200)
        layout = QVBoxLayout()
        self.lable = QLabel("当前值：")
        self.lable.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.lable)

        self.spb = QSpinBox()
        self.spb.setValue(18)
        self.spb.setSingleStep(3)
        self.spb.setRange(10, 20)
        self.spb.valueChanged.connect(lambda: self.valuechanged(self.spb))

        layout.addWidget(self.spb)

        self.setLayout(layout)

    def valuechanged(self, _spb):
        self.lable.setText(str(_spb.value()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QSpinBoxDemo()
    window.show()
    sys.exit(app.exec_())