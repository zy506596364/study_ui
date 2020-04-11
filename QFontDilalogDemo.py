# coding=utf-8
# author:yi.zhang
"""
字体对话框：QFontDialog
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class QFontDialogDemo(QWidget):
    def __init__(self):
        super(QFontDialogDemo, self).__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("字体对话框")
        self.resize(400, 300)
        layout = QVBoxLayout()
        self.btn = QPushButton("选择字体按钮")
        self.btn.clicked.connect(self.getFont)
        self.label = QLabel()
        self.label.setText("HELLO, Python !")
        self.label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.btn)
        layout.addWidget(self.label)
        self.setLayout(layout)

    def getFont(self):
        text = self.sender().text()
        if text == "选择字体按钮":
            Font, ok = QFontDialog.getFont()
            if ok:
                self.label.setFont(Font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QFontDialogDemo()
    window.show()
    sys.exit(app.exec_())