'''
This is a gui base for CYTHAMES
Functionality will be added later
VERSION 0.03
'''
import sys 
import random
import qdarkstyle
from PySide2 import QtCore, QtWidgets, QtGui

class MainWindow (QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Cythames") # lisää ikkunalle tittelin

        self.menu = self.menuBar()
        self.file_menu = self.menu.addMenu('File')

        # määritetään funktiot, jotka sisältää pelkästään tekstin
        self.hello = "Hello World"
        self.hei = "Hei Maailma"

        # luodaan nappi
        self.button1 = QtWidgets.QPushButton("Button 1") # !! UUSI  vaihdettu nimi 1
        self.text = QtWidgets.QLabel(self.hello)
        self.text.setAlignment(QtCore.Qt.AlignHCenter)

        # luodaan nappi
        self.button2 = QtWidgets.QPushButton("Button 2") # !! UUSI  luotu toinen nappi ja annettu nimeksi 2
        self.text = QtWidgets.QLabel() 

        self.button1.clicked.connect(self.magic) # klikatessa nappia kutsuu magic funktiota
        self.valinta = False # Boolean muuttuja, muuttaa painalluksen lopputulosta

        self.button2.clicked.connect(self.newwindow) # !! UUSI klikatessa kutsuu newwindow funktiota

    def magic(self): # määritetään magic funktiota jossa on 2 vaihtoehtoa klikkauksen lopputuloksesta
        if self.valinta == False: # jos valinta on False niin vaihda tekstiksi (self.hei)
            self.text.setText(self.hei)
        elif self.valinta == True: # jos valinta on True niin vaihda tekstiksi (self.hello)
            self.text.setText(self.hello)
        self.valinta = not(self.valinta) # self valinta vaihtuu, joka kerta päin vastaiseksi. Not komento sisältää itsessään vaihdon.

    def newwindow (self): # !! UUSI määritetään newwindow funktio, joka avaa uuden ikkunan kun nappia 2 painetaan
            self.layout = QtWidgets.QVBoxLayout()
            self.myotherwindow = OtherWindow()
            self.myotherwindow.show()
    
class OtherWindow(QtWidgets.QMainWindow, QtWidgets.QAction): # !! UUSI määrietllään toisen ikkunan aukeaminen ja se millainen ikkuna on
    def __init__(self):
        super(OtherWindow,self).__init__()
        self.setWindowTitle("Other window") # lisää ikkunalle tittelin
        self.layout = QtWidgets.QVBoxLayout()
        self.setLayout(self.layout)

        self.ikkuna = "Avasit uuden ikkunan" # !! UUSI lisätty uusi otsikko, joka tulisi uuteen ikkunaan

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MainWindow()
    widget.showMaximized() # Ikkuna avautuu näytön resoluutiossa
    widget.show()
    sys.exit(app.exec_())