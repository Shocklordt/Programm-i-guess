'''
This is a GUI base for Cythames
Functionality will be added later
VERSION 0.11

'''


import sys
from PySide2 import QtWidgets, QtGui, QtCore


class Widget(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)

        




        


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, widget):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle("Cythames")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")






if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    widget = Widget()
    window = MainWindow(widget)
    window.showMaximized()
    window.show()


    sys.exit(app.exec_())