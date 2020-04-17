# coding=utf-8
# author:yi.zhang

"""
剪贴板
"""

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ClipBoardDemo(QWidget):
    def __init__(self):
        super(ClipBoardDemo, self).__init__()
        self.clipboard = QApplication.clipboard()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("剪贴板使用")
        self.resize(400, 300)
        layout = QGridLayout()
        self.copyTextButton = QPushButton("复制文本")
        self.copyTextButton.clicked.connect(self.copyText)
        self.pasteTextButton = QPushButton("粘贴文本")
        self.pasteTextButton.clicked.connect(self.pasteText)
        self.textLabel = QLabel()

        self.copyHtmlButton = QPushButton("复制HTML")
        self.copyHtmlButton.clicked.connect(self.copyHtml)
        self.pasteHtmlButton = QPushButton("粘贴HTML")
        self.pasteHtmlButton.clicked.connect(self.pasteHtml)
        self.copyImageButton = QPushButton("复制图片")
        self.copyImageButton.clicked.connect(self.copyImage)
        self.pasteImageButton = QPushButton("粘贴图片")
        self.pasteImageButton.clicked.connect(self.pasteImage)
        self.htmlLabel = QLabel()
        self.htmlLabel.setAlignment(Qt.AlignCenter)
        self.imageLbel = QLabel()
        layout.addWidget(self.copyTextButton, 0, 0)
        layout.addWidget(self.copyHtmlButton,0,1)
        layout.addWidget(self.copyImageButton,0,2)
        layout.addWidget(self.pasteTextButton, 1, 0)
        layout.addWidget(self.pasteHtmlButton,1,1)
        layout.addWidget(self.pasteImageButton,1,2)
        layout.addWidget(self.textLabel, 2, 0, 1, 3)
        layout.addWidget(self.htmlLabel,3,0,1,3)
        layout.addWidget(self.imageLbel,4,0,3,3)


        self.setLayout(layout)

    def copyText(self):
        self.clipboard.setText("hello python")

    def pasteText(self):
        self.textLabel.setText(self.clipboard.text())

    def copyImage(self):
        self.clipboard.setPixmap(QPixmap("./timg.jpg"))

    def pasteImage(self):
        self.imageLbel.setPixmap(QPixmap(self.clipboard.pixmap()))

    def copyHtml(self):
        mimeData = QMimeData()
        mimeData.setHtml("<b>Bold and <font color='red'>Red</font></b>")
        self.clipboard.setMimeData(mimeData)

    def pasteHtml(self):
        mimeData = self.clipboard.mimeData()
        if mimeData.hasHtml():
            self.htmlLabel.setText(mimeData.html())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ClipBoardDemo()
    window.show()
    sys.exit(app.exec_())