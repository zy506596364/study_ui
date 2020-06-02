# coding=utf-8
# author:yi.zhang

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class AutoSignalSlot(QWidget):
    def __init__(self):
        super(AutoSignalSlot, self).__init__()
        self.btn = QPushButton("okbutton", self)
        self.btn.setObjectName("okbutton")
        self.btn2 = QPushButton("cancelbutton", self)
        self.btn2.setObjectName("cancelbutton")
        QMetaObject.connectSlotsByName(self)
        self.set_ui()

    def set_ui(self):
        _layout = QHBoxLayout()
        _layout.addWidget(self.btn)
        _layout.addWidget(self.btn2)

        self.setLayout(_layout)

    @pyqtSlot()
    def on_okbutton_clicked(self):
        print("点击了这个按钮")

    @pyqtSlot()
    def on_cancelbutton_clicked(self):
        print("hahaha")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AutoSignalSlot()
    window.show()
    sys.exit(app.exec_())