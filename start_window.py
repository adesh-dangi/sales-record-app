import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from gui_screens import Ui_MainWindow #comment this if running this file is start point
from logs import c_logger as logger
from crud_op.crud_operation import get_all_battery_sales_count_active_only, get_battery_sales_paginated
from datetime import datetime

# QMainWindow  to use when main window with toolbar
# Qwidget when first form is present
class Start_App(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        print("Start_App class initialized")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.company_name_label.setText(QCoreApplication.translate("Form", u"Om Sai Electronic", None))
        self.set_today_date()
        # print("ui object : ", self.ui.__dict__)
         # Connect buttons to page switch functions
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.Search_sale_btn.clicked.connect(self.show_search_page)
        self.ui.New_Sales_btn.clicked.connect(self.show_new_sales_page)
        self.current_page = 1
        self.load_table_data(self.current_page)
        self.ui.pag_back_search_btn.setDisabled(True)
        self.ui.pag_back_search_btn.clicked.connect(self.go_back_page)
        self.ui.pag_forward_search_btn.clicked.connect(self.go_next_page)

    def set_today_date(self):
        # 20 July 2025
        date_ = datetime.now().strftime("%d %B %Y")
        self.ui.today_date_label.setText(QCoreApplication.translate("Form", f"{date_}", None))

    def go_back_page(self):
        if self.current_page > 1:
            self.current_page -= 1
            self.load_table_data(self.current_page)

    def go_next_page(self):
        self.current_page += 1
        self.load_table_data(self.current_page)

    def get_table_buttons(self,row, col, order_id):
        button_widget = QWidget()
        layout = QHBoxLayout(button_widget)

        view_button = QPushButton("View")
        view_button.clicked.connect(lambda _, r=row: self.view_row(r, order_id))
        layout.addWidget(view_button)

        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(lambda _, r=row: self.edit_row(r, order_id))
        layout.addWidget(edit_button)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda _, r=row: self.delete_row(r, order_id))
        layout.addWidget(delete_button)

        layout.setContentsMargins(0, 0, 0, 0)  # Remove extra spacing around buttons
        self.ui.search_result_table.setCellWidget(row, col, button_widget)

    def view_row(self, row, order_id):
        print(f"view button clicked for row: {row, order_id}")

    def edit_row(self, row, order_id):
        print(f"Edit button clicked for row: {row, order_id}")

    def delete_row(self, row, order_id):
        print(f"Delete button clicked for row: {row, order_id}")

    def load_table_data(self, page: int, limit: int = 100):
        offset = (page - 1) * limit
        data = get_battery_sales_paginated(page, limit)
        self.ui.search_result_table.setRowCount(len(data))
        columns = ["name", "mobile", "order_id", "created_at", "price","Action"]
        for row_num, row_data in enumerate(data):
            for col_num, attr in enumerate(columns):
                if attr == "Action":
                    self.get_table_buttons(row_num, col_num, row_data.id)
                    continue
                value = getattr(row_data, attr)
                if attr=="created_at":
                    value = value.strftime("%d-%m-%Y") if value else "N/A"
                item = QTableWidgetItem(str(value))
                item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                self.ui.search_result_table.setItem(row_num, col_num, item)

        # Optional: update page label
        total_records = get_all_battery_sales_count_active_only()  # if you have it
        end_record = offset + len(data)
        self.ui.total_search_label.setText(f"Total: {total_records}")
        self.ui.pag_count_label.setText(f"{offset+1}-{end_record}")

        if self.current_page > 1:
            self.ui.pag_back_search_btn.setDisabled(False)
        if self.current_page!=1 and (self.current_page - 1) * limit >= offset:
            self.ui.pag_forward_search_btn.setDisabled(True)
        else:
            self.ui.pag_forward_search_btn.setDisabled(False)

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