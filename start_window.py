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
        self.referesh_flag_on_nav_search_btn = True
        self.previous_highlighted_row = None
        self.buttons_clicked_connect()
        self.load_products_list()


    def handle_input_product_list_edit(self):
        text = self.ui.product_combo_list.currentText()
        if text and self.ui.product_combo_list.findText(text) == -1:
            self.ui.product_combo_list.addItem(text)  # Add if it's a new value
            save_new_product_item(text)
        
    def notifocation_popup(self,title, text):
        # Show alert
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText(f" Message : {text}")
        msg.setWindowTitle(title)
        msg.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg.exec()

    def confirm_action(self, confirm_message=""):
        if confirm_message=="":
            confirm_message="Are you sure you want to proceed?"
        logger.info(confirm_message)
        reply = QMessageBox.question(
            self, 
            "Confirm Action",                      # Title
            confirm_message,   # Message
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No          # Default button
        )

        if reply == QMessageBox.StandardButton.Yes:
            logger.info("User clicked Yes")
            return True
        else:
            logger.info("User clicked No")
            return False

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

        #report button
        self.ui.Report_btn.clicked.connect(self.report_button_clicked)
    
    def report_button_clicked(self):
        self.notifocation_popup("Reporting not ready", "Adesh working on reporting will be available soon ✌️")

    def search_sales_record_button_clicked(self):
        self.search_query_data = {
            "name": self.ui.name_search.text(),
            "mobile": self.ui.mobile_search.text(),
            "order_id": self.ui.serial_no_search.text(),
            "date_search_month":self.ui.month_search_inp.currentText() if self.ui.month_search_inp.currentIndex()!=0 else "",
            "date_search_year":self.ui.year_search_inp.text() 
        }
        if (self.search_query_data["date_search_year"]=="" and self.search_query_data["date_search_month"]!="") or\
            (self.search_query_data["date_search_year"]!="" and self.search_query_data["date_search_month"]==""):
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

    def get_table_buttons(self,row, col, db_id):
        button_widget = QWidget()
        layout = QHBoxLayout(button_widget)

        view_button = QPushButton("View")
        view_button.clicked.connect(lambda _, r=row: self.view_row_from_search_table(r+1, db_id))
        layout.addWidget(view_button)

        edit_button = QPushButton("Edit")
        edit_button.clicked.connect(lambda _, r=row: self.edit_row_from_search_table(r+1, db_id))
        layout.addWidget(edit_button)

        delete_button = QPushButton("Delete")
        delete_button.clicked.connect(lambda _, r=row: self.delete_row_from_search_table(r+1, db_id))
        layout.addWidget(delete_button)

        layout.setContentsMargins(0, 0, 0, 0)  # Remove extra spacing around buttons
        self.ui.search_result_table.setCellWidget(row, col, button_widget)

    def disable_view_save_button(self):
        self.ui.save_new_sale_record_btn.setVisible(False)
        self.ui.save_new_sale_record_btn.setDisabled(True)
        self.ui.save_new_sale_record_btn.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))
        self.ui.save_new_sale_record_btn.setStyleSheet(u" background-color:grey;\n"
"color: grey;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;")
        self.ui.clear_new_sale_record_btn.clicked.connect(self.clear_new_sale_form)
        
    def view_row_from_search_table(self, row, db_id, only_view=True):
        logger.info(f"view button clicked for row: {row, db_id}")
        self.referesh_flag_on_nav_search_btn = False
        data = get_battery_sales_by_id(db_id)
        if data:
            self.ui.name_ns_input.setText(data.name or "----")
            self.ui.mobile_ns_input.setText(data.mobile or "----")
            self.ui.product_combo_list.setCurrentText(data.product or "----")
            self.ui.snumber_ns_input.setText(data.mobile or "----")
            self.ui.price_ns_input.setValue(int(data.price) or 0)
            self.ui.stackedWidget.setCurrentIndex(1)
            self.ui.date_pick_new_sale.setDate(data.created_at)
            if only_view:
                self.disable_view_save_button()
            

    def edit_row_from_search_table(self, row, db_id):
        self.save_new_sale_error=False
        logger.info(f"Edit button clicked for row: {row, db_id}")
        self.show_new_sales_page()
        self.ui.save_new_sale_record_btn.setText("Save Changes")
        self.view_row_from_search_table(row, db_id, only_view=False)
        self.ui.save_new_sale_record_btn.clicked.disconnect()
        self.ui.save_new_sale_record_btn.clicked.connect(lambda: self.edit_sales_record(db_id))


    def edit_sales_record(self, db_id):
        name, mobile, product, serial_num, price,order_date = self.process_form_sale()
        if self.save_new_sale_error!=True and all([name, mobile, product, serial_num]) and price > 0:
            upd_flag = edit_batter_sale(
                db_id=db_id,
                name=name,
                mobile=mobile,
                price=price,
                order_id=serial_num,
                product=product,
                order_date=order_date
            )
            if upd_flag:
                logger.info("Record updated successfully!")
                self.save_new_sale_error = False
                self.notifocation_popup("Record Update", "Sales record Updated successfully ✅")
        else:
            self.save_new_sale_error = True
            logger.info("Please fill in all required fields for editing with correct values.")

    def delete_row_from_search_table(self, row, db_id):
        logger.info(f"Delete button clicked for row: {row, db_id}")
        ask = self.confirm_action(f"Recheck line number : {row} will be marked deleted, click Yes to proceed")
        if ask:
            deleted_ = soft_delete_sales_record(db_id)
            if deleted_:
                self.notifocation_popup("Deleted Sale",f"Sale line number : {row} is marked deleted, referesh table now")
            else:
                self.notifocation_popup("Deleted Sale",f"No Record found to delete, table will referesh now")
                self.load_table_data(self.current_page)
        else:
            self.notifocation_popup("Deleted Sale",f"nothing is deleted.")

    def load_table_data(self, page: int, limit: int = 100):
        self.referesh_flag_on_nav_search_btn=True
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

        # BACK button logic
        if self.current_page > 1:
            self.ui.pag_back_search_btn.setDisabled(False)
            self.back_grey_out_button_disabled("rgb(0, 170, 0)")
        elif self.current_page == 1:
            self.ui.pag_back_search_btn.setDisabled(True)
            self.back_grey_out_button_disabled("grey")

        # FORWARD button logic
        # Disable if we are at or beyond the last page
        if self.current_page * limit >= total_records:
            self.ui.pag_forward_search_btn.setDisabled(True)
            self.forward_grey_out_button_disabled("grey")
        else:
            self.ui.pag_forward_search_btn.setDisabled(False)
            self.forward_grey_out_button_disabled("rgb(0, 170, 0)")
        self.ui.search_result_table.cellClicked.connect(self.highlight_row_on_search_table)
            
    def highlight_row_on_search_table(self, row, column):
        if self.previous_highlighted_row != None:
            for col in range(self.ui.search_result_table.columnCount()):
                item = self.ui.search_result_table.item(self.previous_highlighted_row, col)
                if item:
                    item.setBackground(Qt.GlobalColor.white)
                    item.setForeground(Qt.GlobalColor.black)

        for col in range(self.ui.search_result_table.columnCount()):
            item = self.ui.search_result_table.item(row, col)
            if item:
                item.setBackground(Qt.GlobalColor.black)  # or use QColor
                item.setForeground(QColor("yellow"))

        self.previous_highlighted_row = row

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
        if self.referesh_flag_on_nav_search_btn:
            self.current_page = 1
            self.clear_search_filter()
            self.load_table_data(self.current_page)
            logger.info("Switched to Search Page")
        self.ui.stackedWidget.setCurrentIndex(0)  # Page 1 index
        if self.ui.stackedWidget.currentIndex()==0:
            self.referesh_flag_on_nav_search_btn=True

    def clear_search_filter(self):
        self.ui.name_search.clear()
        self.ui.mobile_search.clear()
        self.ui.serial_no_search.clear()
        self.ui.month_search_inp.setCurrentIndex(0)
        self.ui.year_search_inp.clear() 

    def load_products_list(self):
        product_list = get_products_list()
        existing_items = set(self.ui.product_combo_list.itemText(i) for i in range(self.ui.product_combo_list.count()))
        for product in product_list:
            name = str(product.name)
            if name not in existing_items:
                self.ui.product_combo_list.addItem(name)

    def show_new_sales_page(self):
        self.referesh_flag_on_nav_search_btn=True
        self.ui.save_new_sale_record_btn.setVisible(True)
        self.ui.save_new_sale_record_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.ui.save_new_sale_record_btn.setStyleSheet(u" background-color:rgb(20, 216, 99);\n"
"color: rgb(243, 255, 23);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;")
        self.ui.stackedWidget.setCurrentIndex(1)  # Page 2 index
        logger.info("Switched to New Sales Page")
        self.ui.product_combo_list.setEditable(True)
        self.ui.save_new_sale_record_btn.disconnect()
        self.clear_new_sale_form()
        self.ui.product_combo_list.lineEdit().editingFinished.connect(self.handle_input_product_list_edit)
        self.link_form_new_sales_button()
    
    def link_form_new_sales_button(self):
        self.save_new_sale_error=False
        self.ui.save_new_sale_record_btn.setDisabled(False)
        self.ui.save_new_sale_record_btn.setText("Save")
        self.ui.clear_new_sale_record_btn.clicked.connect(self.clear_new_sale_form)
        self.ui.save_new_sale_record_btn.clicked.connect(self.save_new_sales_record)
        self.ui.date_pick_new_sale.setDate(QDate.currentDate())

    
    def process_form_sale(self):
        # Get values from inputs
        name = self.ui.name_ns_input.text().strip()
        mobile = self.ui.mobile_ns_input.text().strip()
        product = self.ui.product_combo_list.currentText().strip()
        serial_num = self.ui.snumber_ns_input.text().strip()
        price = self.ui.price_ns_input.value()  # assuming QSpinBox or QDoubleSpinBox
        order_date = self.ui.date_pick_new_sale.text()
        print("date selected",order_date)

        self.tmp_flag = False
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
                self.tmp_flag = True
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
        if self.tmp_flag==False:
            self.save_new_sale_error=False
        return name, mobile, product, serial_num, price, order_date
    
    def save_new_sales_record(self):
        name, mobile, product, serial_num, price, order_date = self.process_form_sale()

        if self.save_new_sale_error!=True and all([name, mobile, product, serial_num]) and price > 0:
            add_battery_sale(
                name=name,
                mobile=mobile,
                price=price,
                order_id=serial_num,
                product=product,
                order_date=order_date
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
        self.ui.date_pick_new_sale.setDate(QDate.currentDate())

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
    from traceback import format_exc
    try:
        app = QApplication(sys.argv)
        window = Start_App()
        window.show()
        sys.exit(app.exec())
    except:
        print("start window error: ", format_exc())

if __name__ == "__main__":
    run_app()