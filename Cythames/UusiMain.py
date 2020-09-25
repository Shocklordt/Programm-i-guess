'''
This is a GUI base for Cythames
Functionality will be added later
VERSION 0.11

'''


import sys
from PySide2 import QtWidgets, QtGui, QtCore


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.setWindowTitle("Cythames")

        # Menu
        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu("File")

        # Exit QAction käyttäen Ctrl+Q shortcuttia
        exit_action = QtWidgets.QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")

        self.file_menu.addAction(exit_action)

        element.signal_name.connect(slot_name)
        exit_action.triggered.connect(slot_name)











if __name__ == "__main__":

    app = QtWidgets.QApplication([])

    window = MainWindow()
    window.showMaximized()
    window.show()


    sys.exit(app.exec_())