# coding=utf-8
# author:yi.zhang

"""
输入对话框： QInputDialog

QInputDialog.getItem
QInputDialog.getText
QInputDialog.getInt

"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QInputDialogDemo(QWidget):
    def __init__(self):
        super(QInputDialogDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("输入对话框")
        self.resize(400, 300)
        layout = QFormLayout()

        btn1 = QPushButton("获取列表")
        btn1.clicked.connect(self.getItem)
        self.lineEdit1 = QLineEdit()
        layout.addRow(btn1, self.lineEdit1)

        btn2 = QPushButton("获取文本")
        btn2.clicked.connect(self.getText)
        self.lineEdit2 = QLineEdit()
        layout.addRow(btn2, self.lineEdit2)

        btn3 = QPushButton("获取整数")
        btn3.clicked.connect(self.getInt)
        self.lineEdit3 = QLineEdit()
        layout.addRow(btn3, self.lineEdit3)

        self.setLayout(layout)

    def getItem(self):
        items = (("c",), ("c++", ), ("python",), ("ruby",), ("java",))
        item, ok = QInputDialog.getItem(self, "语言选择", "请选择语言", (i[0] for i in items))
        if item and ok:
            self.lineEdit1.setText(item)

    def getText(self):
        text, ok = QInputDialog.getText(self, "信息", "名字")
        if text and ok:
            self.lineEdit2.setText(text)

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "整数", "输入数字")
        if num and ok:
            self.lineEdit3.setText(str(num))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QInputDialogDemo()
    window.show()
    sys.exit(app.exec_())