import sys 
import random
from PySide2 import QtCore, QtWidgets, QtGui

class Widgetini (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.hei = "Hei maailma"
        self.hello = "Hello World"

        self.button = QtWidgets.QPushButton("For your clicking pleausre")
        self.text = QtWidgets.QLabel(self.hello)
        self.text.setAlignment(QtCore.Qt.AlignCenter)


        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        #klikkaus kutsuu magic fuktiota
        self.button.clicked.connect(self.magic)

        
        # tehdään muuttuja jolla saadaan vaihdettua fuktion sisällä boolia / true / falsea 
        self.valinta = False

    # magic fuktio sisältää 2 vaihtoehtoa siitä mitä napin painalluksesta tapahtuu, riippuen siitä mikä testi on näkyvillä
    def magic(self):

        # jos valinta on False niin vaihda tekstiksi (self.hei)
        if self.valinta == False:
            self.text.setText(self.hei)

        # jos valinta on True niin vaihda tekstiksi (self.hello)    
        elif self.valinta == True:
            self.text.setText(self.hello)
            
        # self valinta vaihtuu, joka kerta päin vastaiseksi. NOT komento sisältää itsessään vaihdon.
        self.valinta = not(self.valinta)      


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Widgetini()
    widget.resize (1920, 1080)
    widget.show()

    sys.exit(app.exec_())

'''
     self.button.clicked.connect(self.magic)
        
        self.valinta = False

    def magic(self):
        if self.valinta == False:
            self.text.setText(self.hei)
        elif self.valinta == True:
            self.text.setText(self.hello)

        self.valinta = not(self.valinta) 
'''