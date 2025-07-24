from logs import c_logger as logger
import sys
from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QFrame, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget, QMainWindow, QMessageBox)
import os, sys
def resource_path(relative_path):
    """Get absolute path to resource, works for dev and PyInstaller .exe"""
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except AttributeError:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
class Ui_MainWindow(object):
    def copy_cell_content(self, row, column):
        print("cell double-clicked to copy", row, column)
        item = self.search_result_table.item(row, column)
        if item:
            clipboard = QApplication.clipboard()
            clipboard.setText(item.text())
            # Show alert
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Icon.Information)
            msg.setText(f"Copied: {item.text()}")
            msg.setWindowTitle("Cell Copied")
            msg.setStandardButtons(QMessageBox.StandardButton.Ok)
            msg.exec()

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1288, 883)
        Form.setMinimumSize(QSize(1288, 883))
        self.vboxLayout = QVBoxLayout(Form)
        self.vboxLayout.setSpacing(0)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.vboxLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Search_sale_btn = QPushButton(Form)
        self.Search_sale_btn.setObjectName(u"Search_sale_btn")
        self.Search_sale_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Search_sale_btn.setStyleSheet(u" background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(247, 198, 56, 255), stop:1 rgba(255, 81, 81, 255));\n"
"color: rgb(0, 0, 255);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 0;")
        icon = QIcon()
        icon.addFile(resource_path(u"gui/images/icons/search/icons8-search-property-50.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Search_sale_btn.setIcon(icon)
        self.Search_sale_btn.setIconSize(QSize(45, 39))

        self.verticalLayout_2.addWidget(self.Search_sale_btn)

        self.New_Sales_btn = QPushButton(Form)
        self.New_Sales_btn.setObjectName(u"New_Sales_btn")
        self.New_Sales_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.New_Sales_btn.setStyleSheet(u" background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0518135 rgba(99, 100, 161, 255), stop:0.948187 rgba(255, 128, 128, 255));\n"
"color: white;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 0;")
        icon1 = QIcon()
        icon1.addFile(resource_path(u"gui/images/icons/add/icons8-writer-male-50.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.New_Sales_btn.setIcon(icon1)
        self.New_Sales_btn.setIconSize(QSize(45, 45))

        self.verticalLayout_2.addWidget(self.New_Sales_btn)

        self.Report_btn = QPushButton(Form)
        self.Report_btn.setObjectName(u"Report_btn")
        self.Report_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.Report_btn.setStyleSheet(u" background-color:rgb(85, 255, 127);\n"
"selection-color: rgb(0, 0, 255);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 0;")
        icon2 = QIcon()
        icon2.addFile(resource_path(u"gui\images\pdf_logo.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.Report_btn.setIcon(icon2)
        self.Report_btn.setIconSize(QSize(45, 50))

        self.verticalLayout_2.addWidget(self.Report_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.Developer_label = QLabel(Form)
        self.Developer_label.setObjectName(u"Developer_label")
        self.Developer_label.setCursor(QCursor(Qt.CursorShape.ForbiddenCursor))

        self.verticalLayout_2.addWidget(self.Developer_label)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.today_date_label = QLabel(Form)
        self.today_date_label.setObjectName(u"today_date_label")
        self.today_date_label.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.today_date_label.setStyleSheet(u"    background-color: rgb(80, 120, 200);\n"
"    text-align: center;\n"
"    padding: 20px;\n"
"    font-weight: bold;\n"
"    font-size: 24px;\n"
"   color:white;")

        self.gridLayout.addWidget(self.today_date_label, 0, 0, 1, 1)

        self.company_name_label = QLabel(Form)
        self.company_name_label.setObjectName(u"company_name_label")
        self.company_name_label.setCursor(QCursor(Qt.CursorShape.IBeamCursor))
        self.company_name_label.setStyleSheet(u"    background-color:rgb(19, 141, 255);\n"
"    text-align: center;\n"
"    padding: 20px;\n"
"    font-weight: bold;\n"
"    font-size: 24px;\n"
"    color:rgb(255, 213, 88);")

        self.gridLayout.addWidget(self.company_name_label, 0, 1, 1, 1)

        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page1 = QWidget()
        self.page1.setObjectName(u"page1")
        self.verticalLayout = QVBoxLayout(self.page1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.page1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u" background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0777202 rgba(61, 119, 135, 255), stop:0.896373 rgba(179, 198, 255, 255));\n"
"color:rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 50% ;\n"
"margin-right:750%")

        self.verticalLayout.addWidget(self.label_2)

        self.frame = QFrame(self.page1)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.name_search = QLineEdit(self.frame)
        self.name_search.setObjectName(u"name_search")
        self.name_search.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        self.name_search.setMaxLength(200)
        self.name_search.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.name_search, 0, 0, 1, 1)

        self.search_btn_action = QPushButton(self.frame)
        self.search_btn_action.setObjectName(u"search_btn_action")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_btn_action.sizePolicy().hasHeightForWidth())
        self.search_btn_action.setSizePolicy(sizePolicy)
        self.search_btn_action.setMinimumSize(QSize(0, 0))
        self.search_btn_action.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_btn_action.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.search_btn_action.setAutoFillBackground(False)
        self.search_btn_action.setStyleSheet(u"background-color:rgb(135, 144, 108);\n"
"color: white;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 18px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 0;\n"
"  margin-left: 50%;\n"
"")
        icon3 = QIcon()
        icon3.addFile(resource_path(u"gui/images/icons/search/icons8-search-50.png"), QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.search_btn_action.setIcon(icon3)
        self.search_btn_action.setIconSize(QSize(54, 35))

        self.gridLayout_2.addWidget(self.search_btn_action, 0, 4, 1, 1)

        self.serial_no_search = QLineEdit(self.frame)
        self.serial_no_search.setObjectName(u"serial_no_search")
        self.serial_no_search.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        self.serial_no_search.setMaxLength(300)
        self.serial_no_search.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.serial_no_search, 0, 1, 1, 1)

        self.mobile_search = QLineEdit(self.frame)
        self.mobile_search.setObjectName(u"mobile_search")
        self.mobile_search.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        self.mobile_search.setInputMethodHints(Qt.InputMethodHint.ImhDialableCharactersOnly|Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.mobile_search.setMaxLength(11)
        self.mobile_search.setClearButtonEnabled(True)

        self.gridLayout_2.addWidget(self.mobile_search, 1, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.month_search_inp = QComboBox(self.frame)
        months = [
            "Select-Month",
            "JANUARY",
            "FEBRUARY",
            "MARCH",
            "APRIL",
            "JUNE",
            "JULY",
            "AUGUST",
            "SEPTEMBER",
            "OCTOBER",
            "NOVEMBER",
            "DECEMBER",
        ]
        self.month_search_inp.addItems(months)
        self.month_search_inp.setObjectName(u"month_search_inp")
        self.month_search_inp.setMinimumSize(QSize(190, 0))
        self.month_search_inp.setMaximumSize(QSize(1000, 16777215))
        self.month_search_inp.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")

        self.horizontalLayout.addWidget(self.month_search_inp)

        self.year_search_inp = QLineEdit(self.frame)
        self.year_search_inp.setObjectName(u"year_search_inp")
        self.year_search_inp.setMaximumSize(QSize(250, 16777215))
        self.year_search_inp.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        self.year_search_inp.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhPreferNumbers)
        self.year_search_inp.setMaxLength(4)
        self.year_search_inp.setPlaceholderText("YYYY")
        self.year_search_inp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.year_search_inp.setClearButtonEnabled(True)

        self.horizontalLayout.addWidget(self.year_search_inp)


        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.total_search_label = QLabel(self.page1)
        self.total_search_label.setObjectName(u"total_search_label")
        self.total_search_label.setStyleSheet(u" background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0518135 rgba(99, 100, 161, 255), stop:0.948187 rgba(255, 128, 128, 255));\n"
"color: white;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 5% 5% 5% 5%;")

        self.horizontalLayout_4.addWidget(self.total_search_label)

        self.pag_back_search_btn = QPushButton(self.page1)
        self.pag_back_search_btn.setObjectName(u"pag_back_search_btn")
        self.pag_back_search_btn.setStyleSheet(u" background-color:rgb(0, 170, 0);\n"
"color: white;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 25px;\n"
"border-radius: 10px;\n"
"   padding: 5% 15% 5% 15%;")

        self.horizontalLayout_4.addWidget(self.pag_back_search_btn)

        self.pag_count_label = QLabel(self.page1)
        self.pag_count_label.setObjectName(u"pag_count_label")
        self.pag_count_label.setStyleSheet(u" background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0518135 rgba(99, 100, 161, 255), stop:0.948187 rgba(255, 128, 128, 255));\n"
"color: white;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 5% 5% 5% 5%;")

        self.horizontalLayout_4.addWidget(self.pag_count_label)

        self.pag_forward_search_btn = QPushButton(self.page1)
        self.pag_forward_search_btn.setObjectName(u"pag_forward_search_btn")
        self.pag_forward_search_btn.setStyleSheet(u" background-color:rgb(0, 170, 0);\n"
"color: white;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 25px;\n"
"border-radius: 10px;\n"
"   padding: 5% 15% 5% 15%;")

        self.horizontalLayout_4.addWidget(self.pag_forward_search_btn)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.search_result_table = QTableWidget(self.page1)
        if (self.search_result_table.columnCount() < 7):
            self.search_result_table.setColumnCount(7)
        # __qtablewidgetitem = QTableWidgetItem()
        # self.search_result_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.search_result_table.setHorizontalHeaderItem(0, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.search_result_table.setHorizontalHeaderItem(1, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.search_result_table.setHorizontalHeaderItem(2, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.search_result_table.setHorizontalHeaderItem(3, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.search_result_table.setHorizontalHeaderItem(4, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.search_result_table.setHorizontalHeaderItem(5, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.search_result_table.setHorizontalHeaderItem(6, __qtablewidgetitem7)

        self.search_result_table.horizontalHeader().setSectionResizeMode(6, QHeaderView.ResizeMode.ResizeToContents) 
        self.search_result_table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.ResizeToContents) 
        self.search_result_table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents) 
        self.search_result_table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)

        self.search_result_table.setObjectName(u"search_result_table")
        self.search_result_table.viewport().setProperty("cursor", QCursor(Qt.CursorShape.PointingHandCursor))
        self.search_result_table.setStyleSheet(u"")
        self.search_result_table.setAutoScrollMargin(16)

        self.search_result_table.setEditTriggers(QTableWidget.EditTrigger.NoEditTriggers)
        self.search_result_table.cellDoubleClicked.connect(self.copy_cell_content)

        self.verticalLayout.addWidget(self.search_result_table)

        self.stackedWidget.addWidget(self.page1)
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.gridLayout_3 = QGridLayout(self.page2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.product_combo_list = QComboBox(self.page2)
        self.product_combo_list.addItem(u"select product")
        self.product_combo_list.addItem(u"Battery")
        self.product_combo_list.addItem(u"Others")
        self.product_combo_list.setObjectName(u"comboBox")
        self.product_combo_list.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        self.product_combo_list.setCurrentText(u"Select a Product")
        self.product_combo_list.setEditable(True)  # Enable text editing
        self.gridLayout_3.addWidget(self.product_combo_list, 5, 1, 1, 1)

        self.label_9 = QLabel(self.page2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u" background-color:rgb(170, 170, 255);\n"
"color: Black;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 20%;")

        self.gridLayout_3.addWidget(self.label_9, 6, 0, 1, 1)

        self.label_7 = QLabel(self.page2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u" background-color:rgb(170, 170, 255);\n"
"color: Black;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 10% 10% 18%;")

        self.gridLayout_3.addWidget(self.label_7, 4, 0, 1, 1)

        self.mobile_ns_input = QLineEdit(self.page2)
        self.mobile_ns_input.setObjectName(u"mobile_ns_input")
        self.mobile_ns_input.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        self.mobile_ns_input.setInputMethodHints(Qt.InputMethodHint.ImhDialableCharactersOnly|Qt.InputMethodHint.ImhDigitsOnly|Qt.InputMethodHint.ImhFormattedNumbersOnly)
        self.mobile_ns_input.setMaxLength(11)
        self.mobile_ns_input.setCursorMoveStyle(Qt.CursorMoveStyle.VisualMoveStyle)
        self.mobile_ns_input.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.mobile_ns_input, 3, 1, 1, 1)

        self.price_ns_input = QSpinBox(self.page2)
        self.price_ns_input.setObjectName(u"price_ns_input")
        self.price_ns_input.setMinimum(0)          # Set minimum as needed
        self.price_ns_input.setMaximum(99999999)   # Increase maximum to allow more digits
        self.price_ns_input.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")

        self.gridLayout_3.addWidget(self.price_ns_input, 6, 1, 1, 1)

        self.label_4 = QLabel(self.page2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u" background-color:rgb(170, 170, 255);\n"
"color: Black;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 20%;")

        self.gridLayout_3.addWidget(self.label_4, 3, 0, 1, 1)
        
        self.new_sale_date_label = QLabel(self.page2)
        self.new_sale_date_label.setObjectName(u"new_sale_date_label")
        self.new_sale_date_label.setStyleSheet(u" background-color:rgb(170, 170, 255);\n"
"color: Black;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 20%;")

        self.gridLayout_3.addWidget(self.new_sale_date_label, 7, 0, 1, 1)

        self.date_pick_new_sale = QDateEdit(self.page2)
        self.date_pick_new_sale.setCalendarPopup(True)
        self.date_pick_new_sale.setObjectName(u"date_pick_new_sale")
        self.date_pick_new_sale.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")

        self.gridLayout_3.addWidget(self.date_pick_new_sale, 7, 1, 1, 1)

        self.clear_new_sale_record_btn = QPushButton(self.page2)
        self.clear_new_sale_record_btn.setObjectName(u"clear_new_sale_record_btn")
        self.clear_new_sale_record_btn.setStyleSheet(u" background-color:rgb(199, 0, 100);\n"
"color: white;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;")

        self.gridLayout_3.addWidget(self.clear_new_sale_record_btn, 0, 4, 1, 1)

        self.name_ns_input = QLineEdit(self.page2)
        self.name_ns_input.setObjectName(u"name_ns_input")
        self.name_ns_input.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.name_ns_input.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        self.name_ns_input.setInputMask(u"")
        self.name_ns_input.setMaxLength(100)
        self.name_ns_input.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.name_ns_input, 2, 1, 1, 1)

        self.label_8 = QLabel(self.page2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u" background-color:rgb(170, 170, 255);\n"
"color: Black;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 20%;")

        self.gridLayout_3.addWidget(self.label_8, 5, 0, 1, 1)

        self.snumber_ns_input = QLineEdit(self.page2)
        self.snumber_ns_input.setObjectName(u"snumber_ns_input")
        self.snumber_ns_input.setStyleSheet(u" background-color:rgb(234, 234, 234);\n"
"color: rgb(0, 0, 0);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;\n"
"border:2px solid black;")
        self.snumber_ns_input.setMaxLength(200)
        self.snumber_ns_input.setClearButtonEnabled(True)

        self.gridLayout_3.addWidget(self.snumber_ns_input, 4, 1, 1, 1)

        self.label = QLabel(self.page2)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u" background-color:rgb(170, 170, 255);\n"
"color: Black;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 0 10% 20%;")

        self.gridLayout_3.addWidget(self.label, 2, 0, 1, 1)

        self.save_new_sale_record_btn = QPushButton(self.page2)
        self.save_new_sale_record_btn.setObjectName(u"save_new_sale_record_btn")
        self.save_new_sale_record_btn.setStyleSheet(u" background-color:rgb(20, 216, 99);\n"
"color: rgb(243, 255, 23);\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 50% 10% 50%;")

        self.gridLayout_3.addWidget(self.save_new_sale_record_btn, 0, 3, 1, 1)

        self.label_3 = QLabel(self.page2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u" background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.0518135 rgba(99, 100, 161, 255), stop:0.948187 rgba(255, 128, 128, 255));\n"
"color: white;\n"
"    text-align: center;\n"
"    font-weight: bold;\n"
"    font-size: 20px;\n"
"border-radius: 15px;\n"
"   padding: 10% 20% 10% 25%;")

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page2)

        self.gridLayout.addWidget(self.stackedWidget, 1, 1, 1, 1)


        self.vboxLayout.addLayout(self.gridLayout)


        self.retranslateUi(Form)

        # self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Record Managment", None))
        Form.setWindowIcon(QIcon(resource_path("gui/images/icons/search/icons8-search-property-100.png")))
        self.Search_sale_btn.setText(QCoreApplication.translate("Form", u"Search Sales", None))
        self.New_Sales_btn.setText(QCoreApplication.translate("Form", u"New Sales", None))
        self.Report_btn.setText(QCoreApplication.translate("Form", u"Report", None))
        self.Developer_label.setText(QCoreApplication.translate("Form", u"Present by: Adesh Dangi", None))
        self.today_date_label.setText(QCoreApplication.translate("Form", u"20 July 2025", None))
        self.company_name_label.setText(QCoreApplication.translate("Form", u"Company Name", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Search Sales", None))
        self.name_search.setText("")
        self.name_search.setPlaceholderText(QCoreApplication.translate("Form", u"Search By Name....", None))
        self.search_btn_action.setText(QCoreApplication.translate("Form", u"Search", None))
        self.serial_no_search.setText("")
        self.serial_no_search.setPlaceholderText(QCoreApplication.translate("Form", u"Search by Serial Number....", None))
        self.mobile_search.setText("")
        self.mobile_search.setPlaceholderText(QCoreApplication.translate("Form", u"Search by Mobile no...", None))
        self.total_search_label.setText(QCoreApplication.translate("Form", u"Total:----", None))
        self.pag_back_search_btn.setText(QCoreApplication.translate("Form", u"<", None))
        self.pag_count_label.setText(QCoreApplication.translate("Form", u"X-Y", None))
        self.pag_forward_search_btn.setText(QCoreApplication.translate("Form", u">", None))
        # ___qtablewidgetitem = self.search_result_table.horizontalHeaderItem(0)
        # ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"Sr No.", None));

        ___qtablewidgetitem1 = self.search_result_table.horizontalHeaderItem(0)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Name", None));

        ___qtablewidgetitem2 = self.search_result_table.horizontalHeaderItem(1)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Mobile", None));

        ___qtablewidgetitem3 = self.search_result_table.horizontalHeaderItem(2)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Serial Number", None));

        ___qtablewidgetitem4 = self.search_result_table.horizontalHeaderItem(3)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Date", None));

        ___qtablewidgetitem5 = self.search_result_table.horizontalHeaderItem(4)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Product", None));

        ___qtablewidgetitem6 = self.search_result_table.horizontalHeaderItem(5)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Price", None));

        ___qtablewidgetitem7 = self.search_result_table.horizontalHeaderItem(6)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"Actions", None));

        self.product_combo_list.setPlaceholderText(QCoreApplication.translate("Form", u"Choose Product", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Price", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"Serial Number", None))
        self.mobile_ns_input.setPlaceholderText(QCoreApplication.translate("Form", u"Enter 10 digit Mobile Number ......", None))
        self.price_ns_input.setSuffix("")
        self.price_ns_input.setPrefix(QCoreApplication.translate("Form", u"Rs. ", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Mobile", None))
        self.clear_new_sale_record_btn.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.name_ns_input.setText("")
        self.name_ns_input.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Buyer Name......", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Product", None))
        self.snumber_ns_input.setPlaceholderText(QCoreApplication.translate("Form", u"Enter Order Serial Number for product ......", None))
        self.label.setText(QCoreApplication.translate("Form", u"Name", None))
        self.new_sale_date_label.setText(QCoreApplication.translate("Form", u"Select Date -", None))
        self.save_new_sale_record_btn.setText(QCoreApplication.translate("Form", u"Save", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Save New Sales", None))
    # retranslateUi


# Minimal Runner
if __name__ == "__main__":
    logger.info("Starting the application...from gui_screens.py")
    app = QApplication(sys.argv)
    MainWindow = QWidget()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
