'''
This is a GUI base for Cythames
Functionality will be added later
VERSION 0.11

'''


import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget
from PySide2.QtGui import *
from PySide2.QtCore import *


class Widget(QWidget):
    def __init__(self):
        QWidget.__init__(self)


class MainWindow(QMainWindow):
    def __init__(self, widget):
        QMainWindow.__init__(self)

        self.setWindowTitle("Cythames")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")


if __name__ == "__main__":

    app = QApplication(sys.argv)

    widget = Widget()
    window = MainWindow(widget)
    window.showMaximized()
    window.show()


    sys.exit(app.exec_())