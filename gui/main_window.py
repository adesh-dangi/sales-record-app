import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

class MainPage(QWidget):
    def __init__(self, stacked_widget):
        super().__init__()
        self.stacked_widget = stacked_widget

        layout = QVBoxLayout()

        # Company label (full width)
        company_label = QLabel("My Company Pvt Ltd")
        company_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        company_label.setFixedHeight(50)
        company_label.setStyleSheet("background-color: green; color: white; font-size: 24px; font-weight: bold;")
        layout.addWidget(company_label)

        layout.addStretch()

        # Three buttons
        self.buttons = []
        for i in range(1, 4):
            btn = QPushButton(f"Button {i}")
            btn.setFont(QFont("Arial", 26))
            btn.setFixedHeight(70)
            btn.clicked.connect(lambda checked, idx=i: self.open_page(idx))
            layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)
            self.buttons.append(btn)

        layout.addStretch()
        self.setLayout(layout)

    def resizeEvent(self, event):
        # Dynamically adjust button width to 10% of window width
        window_width = self.width()
        btn_width = max(150, int(window_width * 0.10))  # minimum width safeguard
        for btn in self.buttons:
            btn.setFixedWidth(btn_width)

    def open_page(self, idx):
        self.stacked_widget.setCurrentIndex(idx)

class SubPage(QWidget):
    def __init__(self, stacked_widget, page_number):
        super().__init__()
        self.stacked_widget = stacked_widget
        layout = QVBoxLayout()

        label = QLabel(f"You are on Page {page_number}")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        label.setFont(QFont("Arial", 26))
        layout.addWidget(label)

        back_btn = QPushButton("Go Back")
        back_btn.setFont(QFont("Arial", 20))
        back_btn.setFixedSize(200, 60)
        back_btn.clicked.connect(self.go_back)
        layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def go_back(self):
        self.stacked_widget.setCurrentIndex(0)

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Company App with Pages")

        self.stacked_widget = QStackedWidget()
        self.main_page = MainPage(self.stacked_widget)
        self.stacked_widget.addWidget(self.main_page)

        # Add subpages for each button
        for i in range(1, 4):
            subpage = SubPage(self.stacked_widget, i)
            self.stacked_widget.addWidget(subpage)

        layout = QVBoxLayout()
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)
        self.resize(800, 600)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
