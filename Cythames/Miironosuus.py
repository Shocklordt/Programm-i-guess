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
                color: #ffffff
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