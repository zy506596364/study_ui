# coding=utf-8
# author:yi.zhang

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from functools import partial


class LambdaDemo(QMainWindow):
    def __init__(self):
        super(LambdaDemo, self).__init__()
        self.btn1 = QPushButton("按钮1")
        self.btn1.clicked.connect(lambda: self.calc_num(3, 4))  # 使用lambda传递参数
        self.btn2 = QPushButton("按钮2")
        self.btn2.clicked.connect(partial(self.calc_num, 8, 8))  # 使用partial传递参数
        self._widget = QWidget()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("为槽函数传递参数")
        self.resize(300, 300)
        _layout = QVBoxLayout(self._widget)
        _layout.addWidget(self.btn1)
        _layout.addWidget(self.btn2)
        self.setCentralWidget(self._widget)

    def calc_num(self, a, b):
        QMessageBox.information(self, "结果", str(a+b))

    def keyPressEvent(self, e):
        print(str(e.key()))
        if e.key() == Qt.Key_Escape:
            self.close()
        elif str(e.key()) == "16777220":
            self.calc_num(20, 20)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LambdaDemo()
    window.show()
    sys.exit(app.exec_())