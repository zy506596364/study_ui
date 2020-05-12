# coding=utf-8
# author:yi.zhang

"""
容纳多文档窗口
"""

import sys
from PyQt5.QtWidgets import *


class MultiWindowsDemo(QMainWindow):
    num = 0

    def __init__(self, parent=None):
        super(MultiWindowsDemo, self).__init__(parent)
        self.setWindowTitle("容纳多文档窗口")
        self.mid = QMdiArea()
        self.setCentralWidget(self.mid)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("new")
        file.addAction("cascade")
        file.addAction("Tiled")
        file.triggered.connect(self.window_action)

    def window_action(self, p):
        if p.text() == "new":
            MultiWindowsDemo.num += 1
            _widget = QWidget()
            _from = QFormLayout()
            _from.addRow("姓名", QLineEdit())
            _sex = QHBoxLayout()
            _sex.addWidget(QRadioButton("男"))
            _sex.addWidget(QRadioButton("女"))
            _from.addRow("性别", _sex)
            _widget.setLayout(_from)
            sub = QMdiSubWindow()
            sub.setWidget(_widget)
            sub.setWindowTitle("子窗口{}".format(MultiWindowsDemo.num))
            self.mid.addSubWindow(sub)
            sub.show()

        elif p.text() == "cascade":
            self.mid.cascadeSubWindows()

        elif p.text() == "Tiled":
            self.mid.tileSubWindows()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MultiWindowsDemo()
    window.show()
    sys.exit(app.exec_())