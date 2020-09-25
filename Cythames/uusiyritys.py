from PySide2.QtWidgets import QApplication,QMainWindow, QAction, QVBoxLayout
import sys
from PySide2.QtGui import QIcon
 
class Window(QMainWindow):
    def __init__(self):
        super().__init__()
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
            QMenuBar {
                background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                                            stop:0 lightgray, stop:1 darkgray);
            }
            QMenuBar::item {
                spacing: 3px;           
                padding: 2px 10px;
                background-color: rgb(210,105,30);
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
                background-color: #654321;
                color: rgb(255,255,255);
            }
            """
        
        self.setStyleSheet(self.stylesheet)
        self.setWindowTitle("Cythames")
        self.showMaximized()
        self.create_menu()
        self.show()
 
    def create_menu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
 
        exitAction = QAction(QIcon('exit.png'), "Exit", self)
        exitAction.setShortcut("Ctrl+X")
 
        exitAction.triggered.connect(self.exit_app)
 
        fileMenu.addAction(exitAction)
 

    def exit_app(self):
        self.close()
 
myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)