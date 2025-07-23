import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from gui_screens import Ui_MainWindow #comment this if running this file is start point
from logs import c_logger as logger
from crud_op.crud_operation import *
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
        # self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.month_search_inp.setCurrentIndex(0)
        
        self.current_page = 1
        self.search_query_data= {
            "name":"", "mobile":"", "order_id":"", "date_search_month":"","date_search_year":""
        }
        self.save_new_sale_error=False
        self.buttons_clicked_connect()

    def handle_input_product_list_edit(self):
        text = self.ui.product_combo_list.currentText()
        if text and self.ui.product_combo_list.findText(text) == -1:
            self.ui.product_combo_list.addItem(text)  # Add if it's a new value
            logger.info("New option saved:", text)
            save_new_product_item(text)
        
    def notifocation_popup(self,title, text):
        # Show alert
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(f" Message : {text}")
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

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
        self.search_query_data = {
            "name": self.ui.name_search.text(),
            "mobile": self.ui.mobile_search.text(),
            "order_id": self.ui.serial_no_search.text(),
            "date_search_month":self.ui.month_search_inp.currentText() if self.ui.month_search_inp.currentIndex!=0 else "",
            "date_search_year":self.ui.year_search_inp.text() 
        }
        if not self.ui.year_search_inp.text() or not self.ui.month_search_inp.currentText():
            self.notifocation_popup("Mssing Search Value","Month and Year both required to search in month")
        else:
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
        # print("total data", total_records)
        self.ui.search_result_table.setRowCount(len(data))
        columns = ["name", "mobile", "order_id", "created_at", "product", "price","Action"]
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
        end_record = offset + len(data)
        self.ui.total_search_label.setText(f"Total: {total_records}")
        self.ui.pag_count_label.setText(f"{offset+1}-{end_record}")

        # logger.debug("checking when to disabled forward button :", self.current_page * limit, total_records)
        if self.current_page > 1:
            self.ui.pag_back_search_btn.setDisabled(False)
            self.back_grey_out_button_disabled("rgb(0, 170, 0)")
        elif self.current_page == 1:
            self.ui.pag_back_search_btn.setDisabled(True)
            self.back_grey_out_button_disabled("grey")
        if self.current_page!=1 and self.current_page * limit > total_records:
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
        self.current_page = 1
        self.clear_search_filter()
        self.load_table_data(self.current_page)
        self.ui.stackedWidget.setCurrentIndex(0)  # Page 1 index
        logger.info("Switched to Search Page")
    
    def clear_search_filter(self):
        self.ui.name_search.clear()
        self.ui.mobile_search.clear()
        self.ui.serial_no_search.clear()
        self.ui.month_search_inp.setCurrentIndex(0)
        self.ui.year_search_inp.clear() 

    def load_products_list(self):
        products = get_products_list()
        if products:
            for product in products:
                # print(product.name, type(product.name))
                self.ui.product_combo_list.addItem(str(product.name))

    def show_new_sales_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)  # Page 2 index
        logger.info("Switched to New Sales Page")
        self.load_products_list()
        self.ui.product_combo_list.setEditable(True)
        self.ui.product_combo_list.lineEdit().editingFinished.connect(self.handle_input_product_list_edit)
        self.link_form_new_sales_button()
    
    def link_form_new_sales_button(self):
        self.ui.clear_new_sale_record_btn.clicked.connect(self.clear_new_sale_form)
        self.ui.save_new_sale_record_btn.clicked.connect(self.save_new_sales_record)
    
    def save_new_sales_record(self):
        print("save clicked for new record")

        # Get values from inputs
        name = self.ui.name_ns_input.text().strip()
        mobile = self.ui.mobile_ns_input.text().strip()
        product = self.ui.product_combo_list.currentText().strip()
        serial_num = self.ui.snumber_ns_input.text().strip()
        price = self.ui.price_ns_input.value()  # assuming QSpinBox or QDoubleSpinBox
        # Validation and red border logic
        def mark_invalid(widget, is_valid):
            if not is_valid:
                widget.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border: 2px solid red;")
                self.save_new_sale_error = True
            else: 
                widget.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")

        mark_invalid(self.ui.name_ns_input, bool(name))
        mark_invalid(self.ui.mobile_ns_input, bool(mobile and mobile.isdigit() and len(mobile)==10))
        mark_invalid(self.ui.snumber_ns_input, bool(serial_num))
        mark_invalid(self.ui.product_combo_list, bool(product and product!="select product"))
        mark_invalid(self.ui.price_ns_input, price > 0)

        if all([name, mobile, product, serial_num]) and price > 0:
            add_battery_sale(
                name=name,
                mobile=mobile,
                price=price,
                order_id=serial_num,
                product=product
            )
            logger.info("Record saved successfully!")
            self.save_new_sale_error = False
            self.notifocation_popup("Record Update", "New sales record saved successfully ✅")
        else:
            self.save_new_sale_error = True
            logger.info("Please fill in all required fields.")

    
    def clear_new_sale_form(self):
        self.ui.name_ns_input.clear()
        self.ui.price_ns_input.clear()
        self.ui.mobile_ns_input.clear()
        self.ui.product_combo_list.setCurrentIndex(0)
        self.ui.snumber_ns_input.clear()

        def reset_border(widget):
            widget.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        if self.save_new_sale_error==True:
            reset_border(self.ui.name_ns_input)
            reset_border(self.ui.mobile_ns_input)
            reset_border(self.ui.snumber_ns_input)
            reset_border(self.ui.product_combo_list)
            reset_border(self.ui.price_ns_input)


def run_app():
    app = QApplication(sys.argv)
    window = Start_App()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    run_app()