# coding=utf-8
# author:yi.zhang
"""
QLineEdit控件的回显

有4中回显
1. Normal
2. NoEcho
3. Password
4. PasswordEchoOnEdit
"""
import sys
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLayout


class QlineEditDemo(QWidget):
    def __init__(self):
        super(QlineEditDemo, self).__init__()
        self.setUI()

    def setUI(self):
        self.setWindowTitle("QLineEdit 回显模式")
        normal_line_edit = QLineEdit()
        noecho_line_edit = QLineEdit()
        password_line_edit = QLineEdit()
        password_echo_onedit = QLineEdit()

        QForm = QFormLayout()
        QForm.addRow("normal", normal_line_edit)
        QForm.addRow("noecho", noecho_line_edit)
        QForm.addRow("password", password_line_edit)
        QForm.addRow("password_echo", password_echo_onedit)

        normal_line_edit.setEchoMode(QLineEdit.Normal)
        noecho_line_edit.setEchoMode(QLineEdit.NoEcho)
        password_line_edit.setEchoMode(QLineEdit.Password)
        password_echo_onedit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        normal_line_edit.setPlaceholderText("Normal")
        noecho_line_edit.setPlaceholderText("NoEcho")
        password_line_edit.setPlaceholderText("Password")
        password_echo_onedit.setPlaceholderText("PasswordEchoOnEdit")
        self.setLayout(QForm)

        # normal_line_edit.set

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWindow = QlineEditDemo()
    myWindow.show()
    sys.exit(app.exec_())