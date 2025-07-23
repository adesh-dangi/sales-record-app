import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from gui_screens import Ui_MainWindow #comment this if running this file is start point
from logs import c_logger as logger
from crud_op.crud_operation import get_bs_by_filter_keys
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
        self.ui.year_search_inp.clear()

         # Connect buttons to page switch functions
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.month_search_inp.setCurrentIndex(0)

        
        self.current_page = 1
        self.search_query_data= {
            "name":"", "mobile":"", "order_id":"", "date_search_month":"","date_search_year":""
        }
        self.buttons_clicked_connect()

    def buttons_clicked_connect(self):
        # navigation buttons
        self.ui.Search_sale_btn.clicked.connect(self.show_search_page)
        self.ui.New_Sales_btn.clicked.connect(self.show_new_sales_page)

        #load table on opening app
        self.load_table_data(self.current_page)
        self.ui.pag_back_search_btn.setDisabled(True)
        self.back_grey_out_button_disabled("grey")
        self.ui.pag_back_search_btn.clicked.connect(self.go_back_page)
        self.ui.pag_forward_search_btn.clicked.connect(self.go_next_page)

        #search by name, mobile, order id, date
        self.ui.search_btn_action.clicked.connect(self.search_sales_record_button_clicked)

    def search_sales_record_button_clicked(self):
        print("search_sales_record_button_clicked")
        print("name = ", self.ui.name_search.text(),len(self.ui.name_search.text()),
              "mobile = ", self.ui.mobile_search.text(),len(self.ui.mobile_search.text()),
              "order_id = ", self.ui.serial_no_search.text(),
              "date_search_month = ",self.ui.month_search_inp.currentText(),
              "date_search_year = ",self.ui.year_search_inp.text())
        self.search_query_data = {
            "name": self.ui.name_search.text(),
            "mobile": self.ui.mobile_search.text(),
            "order_id": self.ui.serial_no_search.text(),
            "date_search_month":self.ui.month_search_inp.currentText() if self.ui.month_search_inp.currentIndex!=0 else "",
            "date_search_year":self.ui.year_search_inp.text() 
        }
        self.current_page = 1
        self.load_table_data(self.current_page)

    def set_today_date(self):
        # 20 July 2025
        today_ = datetime.now()
        date_ = today_.strftime("%d %B %Y")
        self.ui.today_date_label.setText(QCoreApplication.translate("Form", f"{date_}", None))
        self.ui.year_search_inp.setText(f"{today_.year}")

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
        data, total_records = get_bs_by_filter_keys(name=self.search_query_data["name"],
                                                    mobile=self.search_query_data["mobile"],
                                                    date_search_month=self.search_query_data["date_search_month"],
                                                    date_search_year=self.search_query_data["date_search_year"],
                                                    order_id=self.search_query_data["order_id"],
                                                    page=page, per_page=limit)
        print("total data", len(data), total_records)
        self.ui.search_result_table.setRowCount(len(data))
        columns = ["name", "mobile", "order_id", "created_at", "price","Action"]
        for row_num, row_data in enumerate(data):
            # Set vertical header item (row number)
            self.ui.search_result_table.setVerticalHeaderItem(row_num, QTableWidgetItem(str(offset + row_num + 1)))
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
        # total_records = get_all_battery_sales_count_active_only()  # if you have it
        end_record = offset + len(data)
        self.ui.total_search_label.setText(f"Total: {total_records}")
        self.ui.pag_count_label.setText(f"{offset+1}-{end_record}")

        print("checking when to disabled forward button :", (self.current_page - 1) * limit, total_records-200)
        if self.current_page > 1:
            self.ui.pag_back_search_btn.setDisabled(False)
            self.back_grey_out_button_disabled("rgb(0, 170, 0)")
        elif self.current_page == 1:
            self.ui.pag_back_search_btn.setDisabled(True)
            self.back_grey_out_button_disabled("grey")
        if self.current_page!=1 and (self.current_page - 1) * limit > total_records-200:
            self.ui.pag_forward_search_btn.setDisabled(True)
            self.forward_grey_out_button_disabled("grey")
        else:
            self.ui.pag_forward_search_btn.setDisabled(False)
            self.forward_grey_out_button_disabled("rgb(0, 170, 0)")
            

    def back_grey_out_button_disabled(self, color_bg):
        self.ui.pag_back_search_btn.setStyleSheet(f" background-color:{color_bg};\n"
            "color: white;\n"
            "    text-align: center;\n"
            "    font-weight: bold;\n"
            "    font-size: 25px;\n"
            "border-radius: 10px;\n"
            "   padding: 5% 15% 5% 15%;")
        
    def forward_grey_out_button_disabled(self, color_bg):
        self.ui.pag_forward_search_btn.setStyleSheet(f" background-color:{color_bg};\n"
            "color: white;\n"
            "    text-align: center;\n"
            "    font-weight: bold;\n"
            "    font-size: 25px;\n"
            "border-radius: 10px;\n"
            "   padding: 5% 15% 5% 15%;")

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