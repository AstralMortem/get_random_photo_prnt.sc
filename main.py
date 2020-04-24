#!-*-coding:utf-8-*-
import sys

# import PyQt5 QtCore and QtGui modules
from PyQt5 import QtWidgets
from main_window import Ui_Form # импорт нашего сгенерированного файла


class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)


app = QtWidgets.QApplication([])
application = MyWindow()
application.show()

sys.exit(app.exec())
