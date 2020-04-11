# coding=utf-8
# author:yi.zhang
"""
QMessageBox

1. 关于对话框
2. 错误对话框
3. 警告对话框
4. 提问对话框
5. 消息对话框
"""

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QMessageBoxDemo(QWidget):
    def __init__(self):
        super(QMessageBoxDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("消息对话框")
        self.resize(400, 300)

        layout = QHBoxLayout()
        btn1 = QPushButton("关于对话框")
        btn1.clicked.connect(self.show_dialog)
        layout.addWidget(btn1)

        btn2 = QPushButton("错误对话框")
        btn2.clicked.connect(self.show_dialog)
        layout.addWidget(btn2)

        btn3 = QPushButton("警告对话框")
        btn3.clicked.connect(self.show_dialog)
        layout.addWidget(btn3)

        btn4 = QPushButton("提问对话框")
        btn4.clicked.connect(self.show_dialog)
        layout.addWidget(btn4)

        btn5 = QPushButton("消息对话框")
        btn5.clicked.connect(self.show_dialog)
        layout.addWidget(btn5)

        self.setLayout(layout)

    def show_dialog(self):
        text = self.sender().text()
        if text == "关于对话框":
            QMessageBox.about(self, "关于", "这是一个关于对话框ttttttttttttttttttttttt")

        elif text == "消息对话框":
            reply = QMessageBox.information(self, "消息", "这是一个消息对话框", QMessageBox.Yes | QMessageBox.No,QMessageBox.No)
            print(reply == QMessageBox.Yes)

        elif text == "错误对话框":
            QMessageBox.critical(self, "错误", "这是一个错误对话框")

        elif text == "警告对话框":
            QMessageBox.warning(self, "警告", "这是一个警告对话框")

        elif text == "提问对话框":
            QMessageBox.question(self, "提问", "这是一个提问对话框")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMessageBoxDemo()
    window.show()
    sys.exit(app.exec_())
