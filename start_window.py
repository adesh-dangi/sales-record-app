import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from gui_screens import Ui_MainWindow #comment this if running this file is start point
from logs import c_logger as logger

class Start_App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        print("Start_App class initialized")
        self.ui = Ui_MainWindow()
        print("Ui_MainWindow class initialized")
        self.ui.setupUi(self)
        print("setupUi class initialized")
        # print("ui object : ", self.ui.__dict__)
       

    


def run_app():
    app = QApplication(sys.argv)
    window = Start_App()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()