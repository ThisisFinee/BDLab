import MyInterface
from PyQt5 import QtCore, QtGui, QtWidgets
import os

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = MyInterface.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.MainDirectoryExists()
    MainWindow.show()
    sys.exit(app.exec_())