'''
This is a gui base for CYTHAMES
Functionality will be added later

VERSION 0.03

'''

import sys
from PySide2 import QtCore, QtWidgets, QtGui

class Widgetini (QtWidgets.QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cythames")

        # Ohjelman CSS teema
        self.stylesheet = """
            QWidget {
                background-color: #383738;
        }
            QPushButton {
                background-color: #657e8a;
                color: #ebdddd;
                border: 2px solid #000000;
        }
            QLabel {
                color: #ebdddd;
        }
        """

        self.hello = "Hello World"
        self.hei = "Hei maailma"

        self.button1 = QtWidgets.QPushButton("Button 1")
        self.button2 = QtWidgets.QPushButton("Button 2")

        self.text = QtWidgets.QLabel(self.hello)
        self.text.setAlignment(QtCore.Qt.AlignHCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button1)
        self.layout.addWidget(self.button2)
        self.setLayout(self.layout)

        self.button1.clicked.connect(self.magic)
        self.valinta = False

        app.setStyleSheet(self.stylesheet)

    def magic(self):
        if self.valinta == False:
            self.text.setText(self.hei)
        
        elif self.valinta == True:
            self.text.setText(self.hello)

        self.valinta = not(self.valinta)

    
if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)

    widget = Widgetini()

    widget.showMaximized()

    widget.show()


    sys.exit(app.exec_())