# coding=utf-8
# author:yi.zhang

"""
文件对话框：QFileDialog
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QFileDialogDemo(QWidget):
    def __init__(self):
        super(QFileDialogDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("文件对话框")
        self.resize(400, 300)
        self.btn1 = QPushButton("打开图像文件")
        self.btn1.clicked.connect(self.loadImage)
        self.label = QLabel()
        layout = QVBoxLayout()
        layout.addWidget(self.btn1)
        layout.addWidget(self.label)

        self.btn2 = QPushButton("打开文件")
        self.btn2.clicked.connect(self.loadFile)
        self.textEdit = QTextEdit()
        self.textEdit.setReadOnly(True)
        layout.addWidget(self.btn2)
        layout.addWidget(self.textEdit)

        self.setLayout(layout)

    def loadImage(self):
        fname, _ = QFileDialog.getOpenFileName(self, "打开图片", ".", "图像文件(*.jpg *.png)")
        self.label.setPixmap(QPixmap(fname))

    def loadFile(self):

        fileDialog = QFileDialog()

        fileDialog.setFileMode(QFileDialog.AnyFile)

        fileDialog.setFilter(QDir.Files)
        # print("=" * 50)
        if fileDialog.exec():
            filenames = fileDialog.selectedFiles()
            print(filenames)
            # f = open(filenames[0], encoding="utf-8", mode="r")
            f = open(filenames[0], "r")
            with f:
                data = f.read()
                self.textEdit.setText(data)
            # print(filenames)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QFileDialogDemo()
    window.show()
    sys.exit(app.exec_())