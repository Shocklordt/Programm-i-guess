'''
This is a gui base for CYTHAMES
Functionality will be added later
VERSION 0.03
'''
import sys 
from PySide2 import QtCore, QtWidgets, QtGui

class MainWindow (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cythames") # lisää ikkunalle tittelin
        self.initGui()

    def initGui(self):
        menuBar = self.window.menuBar()
        

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.showMaximized() # Ikkuna avautuu näytön resoluutiossa
    widget.show()
    sys.exit(app.exec_())