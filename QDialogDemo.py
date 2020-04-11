# coding=utf-8
# author:yi.zhang
"""
对话框： QDialog
QMessageBox 消息对话框
QColorDialog 颜色对话框
QFileDialog 保存对话框
QFontDialog 字体对话框
QInputDialog 输入对话框
"""
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys


class QDialogDemo(QMainWindow):
    def __init__(self):
        super(QDialogDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("对话框演示")
        self.resize(300, 200)
        self.button = QPushButton("点击显示对话框", self)
        self.button.move(50,50)
        self.button.clicked.connect(self.showdialog)

    def showdialog(self):
        dialog = QDialog()
        dialog.setWindowTitle("子对话框")
        button1 = QPushButton("确定", dialog)
        button1.move(50,50)
        button1.clicked.connect(dialog.close)
        button1.clicked.connect(self.close)
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QDialogDemo()
    window.show()
    sys.exit(app.exec_())