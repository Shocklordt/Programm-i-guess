'''
This is a gui base for CYTHAMES
Functionality will be added later

VERSION 0.01

'''



import sys 
import random
from PySide2 import QtCore, QtWidgets, QtGui

class Widgetini (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.hello = ["Hei maailma"]

        self.button = QtWidgets.QPushButton("For your clicking pleausre") 
        self.text = QtWidgets.QLabel("Hello World")
<<<<<<< HEAD
        self.text.setAlignment(QtCore.Qt.AlignHCenter)
=======
        self.text.setAlignment(QtCore.Qt.AlignRCenter)
>>>>>>> f29719ee02fce502c4edfda0320bad25697ecfd8


        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    def magic(self):
        self.text.setText(random.choice(self.hello))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Widgetini()
    widget.resize (800, 600)
    widget.show()

    sys.exit(app.exec_())
