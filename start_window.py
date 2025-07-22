import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from gui_screens import Ui_MainWindow #comment this if running this file is start point
from logs import c_logger as logger

# QMainWindow  to use when main window with toolbar
# Qwidget when first form is present
class Start_App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        print("Start_App class initialized")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # print("ui object : ", self.ui.__dict__)
         # Connect buttons to page switch functions
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Search_sale_btn.clicked.connect(self.show_search_page)
        self.ui.New_Sales_btn.clicked.connect(self.show_new_sales_page)

    def show_search_page(self):
        self.ui.stackedWidget.setCurrentIndex(0)  # Page 1 index
        logger.info("Switched to Search Page")

    def show_new_sales_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)  # Page 2 index
        logger.info("Switched to New Sales Page")
       

def run_app():
    app = QApplication(sys.argv)
    window = Start_App()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()