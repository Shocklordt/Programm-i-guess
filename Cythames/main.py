'''
This is a gui base for CYTHAMES
Functionality will be added later

VERSION 0.03

'''



import sys 
import random
from PySide2 import QtCore, QtWidgets, QtGui

class Widgetini (QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # määritetään funktiot, jotka sisältää pelkästään tekstin
        self.hello = "Hello World"
        self.hei = "Hei Maailma"

        # luodaan nappi
        self.button = QtWidgets.QPushButton("Button 1") 
        self.text = QtWidgets.QLabel(self.hello)
        self.text.setAlignment(QtCore.Qt.AlignHCenter)

        # luodaan layout ohjelmalle
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic) # klikatessa nappia kutsuu magic funktiota
        self.valinta = False # Boolean muuttuja, muuttaa painalluksen lopputulosta

    def magic(self): # määritetään magic funktiota jossa on 2 vaihtoehtoa klikkauksen lopputuloksesta
        if self.valinta == False: # jos valinta on False niin vaihda tekstiksi (self.hei)
            self.text.setText(self.hei)

        elif self.valinta == True: # jos valinta on True niin vaihda tekstiksi (self.hello)
            self.text.setText(self.hello)

        self.valinta = not(self.valinta) # self valinta vaihtuu, joka kerta päin vastaiseksi. Not komento sisältää itsessään vaihdon.

        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = Widgetini()
    widget.showMaximized() # Ikkuna avautuu näytön resoluutiossa
    widget.show()

    sys.exit(app.exec_())
