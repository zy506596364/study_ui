# coding=utf-8
# author:yi.zhang

"""
在单元格中放置控件

setItem: 将文本放置到单元格中
setCellWidget: 将控件放置到单元格中
setStyleSheet: 设置控件的样式（QSS）
"""

import sys
import PyQt5.QtWidgets


class PlaceControlInCell(PyQt5.QtWidgets.QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("控件放置在单元格中")
        self.resize(400, 300)
        _layout = PyQt5.QtWidgets.QHBoxLayout()
        _table_widget = PyQt5.QtWidgets.QTableWidget()
        _table_widget.setRowCount(4)
        _table_widget.setColumnCount(3)
        _table_widget.setHorizontalHeaderLabels(["name", "sex", "wghite"])
        _table_widget.setItem(0, 0, PyQt5.QtWidgets.QTableWidgetItem("小明"))
        _combox = PyQt5.QtWidgets.QComboBox()
        _combox.addItem("男")
        _combox.addItem("女")
        _combox.setStyleSheet('QComboBox{margin:3px};')
        _table_widget.setCellWidget(0, 1, _combox)
        _button = PyQt5.QtWidgets.QPushButton("修改")
        _button.clicked.connect(self.masage_)
        _button.setStyleSheet("QPushButton{margin:3px};")
        _table_widget.setCellWidget(0, 2, _button)

        _layout.addWidget(_table_widget)
        self.setLayout(_layout)

    def masage_(self):
        PyQt5.QtWidgets.QMessageBox.information(self, "提示", "修改成功")


if __name__ == '__main__':
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    window = PlaceControlInCell()
    window.show()
    sys.exit(app.exec_())

