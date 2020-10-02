'''
This is a gui base for CYTHAMES
Functionality will be added later

VERSION 0.11

'''

# Python second party packages
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget, QWidgetAction, QCheckBox
from PySide2.QtGui import QIcon
from PySide2.QtCore import *

# Python internal packages
import sys


# Pääikkuna objektina
class Window(QMainWindow):  
    def __init__(self):
        super().__init__()
        
        
        self.setWindowTitle("Cythames") # Pääikkunan titteli
        self.showMaximized() # Avaa ikkunan näytön resoluutiossa
        self.create_menu() # Kutsuu create_menu funktiota
        self.show() # Piirtää objektin näyttöön

    # Menu-palkin def funktiona
    def create_menu(self): 

        mainMenu = self.menuBar() #Luo menu-valikko
        fileMenu = mainMenu.addMenu("File") #Luo ensimmäisen "File" palikan
 
        exitAction = QAction(QIcon('exit.png'), "Exit", self) # Luo exit toiminnan ja sille napin nimi valikossa
        exitAction.setShortcut("Ctrl+X") # Antaa pikatoiminnan exitille
        exitAction.triggered.connect(self.exit_app) # Kun exit nappia painetaan kutsuu exit_app funktiota

        optionsAction = QAction("Options", self) # Luo asetukset-napin
        optionsAction.triggered.connect(self.OptionsWindowOpen) # Kun asetukset-nappia painetaan se kutsuu OptionsWindowOpen funktiota
 
        fileMenu.addAction(exitAction) # Piirtää exit-toiminnon nappia
        fileMenu.addAction(optionsAction) # Piirtää options-toiminnon nappia
    
    # Funktio, jonka avulla avataan uusi options-ikkunaa
    def OptionsWindowOpen(self): 
        self.layout = QVBoxLayout() # Määritetään self.layout QVBox funktioksi
        self.OptionsWindow_1 = Options(self) # Muuttuja viittaa uuteen options objektiin, eli uuteen options ikkunaan
        self.OptionsWindow_1.show() # Piirtäää viitatun ikkunan

    # Funktio, joka sulkee ohjelmaa
    def exit_app(self): 
        self.close()

# Options ikkunan Objekti
class Options(QWidget):
    def __init__(self, parent):
        super().__init__()

        self.parent = parent    # Määritä objektin vanhemmaksi, jonka avulla kaikki muut ikkunan ottaa tämän ikkunan asetukset

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setWindowTitle("Options") 
        self.setGeometry(300, 300, 300, 300) # Muuttaa ikkunan geometriaa


        StyleOption_checkbox = QCheckBox("Dark Theme", self) # Luo valintaruudun ja antaa sille nimen
        StyleOption_checkbox.stateChanged.connect(self.ChangeStyle) # Kun valintaruutu painetaan, se kutsuu ChangeStyle funktiota
        
    # Funktio, joka laittaa päälle dark theme
    def ChangeStyle(self, state):
        if state == Qt.Checked: # Tarkistaa, että jos ruutu on päällä
            self.setStyleSheet(style_dark_theme) # laittaa Options classin päälle tyylin style_dark_theme 
            self.parent.setStyleSheet(style_dark_theme) # laittaa style_dark_theme tyylin kaikille muille ikkunoille

        else: # muuten 
            self.setStyleSheet(style_zero) # laittaa Options classin päälle tyylin style_zero
            self.parent.setStyleSheet(style_zero) # laittaa style_zero tyylin kaikille muille ikkunoille
            


# Määritetään ohjelman tyylit

# Tyyli oletusarvona
style_zero = """
"""

# Tumma tyyli
style_dark_theme = """
    QWidget {
        background-color: #383738;
        color: rgb(255,255,255);
}
    QPushButton {
        background-color: #657e8a;
        color: #ebdddd;
        border: 2px solid #000000;
}
    QLabel {
        color: #ebdddd;
}
    QMenuBar {
        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                    stop:0 lightgray, stop:1 darkgray);
}
    QMenuBar::item {
        spacing: 3px;           
        padding: 2px 10px;
        background-color: #294d29;
        color: rgb(255,255,255);  
        border-radius: 5px;
}
    QMenuBar::item:selected {    
        background-color: #f70000;
}
    QMenuBar::item:pressed {
        background: #0026ff;
}

/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */  

    QMenu {
        background-color: #ABABAB;   
        border: 1px solid black;
        margin: 2px;
}
    QMenu::item {
        background-color: transparent;
}
    QMenu::item:selected { 
        background-color: #1ce81c;
        color: rgb(255,255,255);
}
    QMenu::item:pressed {
        background-color: #e81cb8
        color: #00f2ff
}
"""






# Standard app loop
myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)