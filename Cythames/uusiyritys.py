'''
This is a gui base for CYTHAMES
Functionality will be added later

VERSION 0.11

'''
from PySide2.QtWidgets import QApplication, QMainWindow, QAction, QVBoxLayout, QWidget, QWidgetAction, QCheckBox
import sys
from PySide2.QtGui import QIcon

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        
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

        optionsAction = QAction("Options", self)
        optionsAction.triggered.connect(self.OptionsWindowOpen)
 
        fileMenu.addAction(exitAction)
        fileMenu.addAction(optionsAction)
    
    def OptionsWindowOpen(self):
        self.layout = QVBoxLayout()
        self.OptionsWindowOpen = Options()
        self.OptionsWindowOpen.show()

    def exit_app(self):
        self.close()

class Options(QWidget):
    def __init__(self):
        super().__init__()

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.setWindowTitle("Options")
        self.setGeometry(300, 300, 300, 300)

        SyleOption_checkbox = QCheckBox("Dark Theme", )




style_zero = """
"""

style = """
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






 
myApp = QApplication(sys.argv)
window = Window()
myApp.exec_()
sys.exit(0)