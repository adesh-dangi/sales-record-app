import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QColor, QPalette

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple PyQt6 Window with Header")

        layout = QVBoxLayout()

        # Company Name Label - full width with green background
        company_label = QLabel("My Company Pvt Ltd")
        company_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        company_label.setFixedHeight(50)

        # Styling for green background and white text
        company_label.setStyleSheet("""
            background-color: green;
            color: white;
            font-size: 20px;
            font-weight: bold;
        """)

        layout.addWidget(company_label)

        # Create buttons
        button1 = QPushButton("Button 1")
        button2 = QPushButton("Button 2")
        button3 = QPushButton("Button 3")

        # Optional: bigger font for buttons
        for btn in [button1, button2, button3]:
            btn.setFont(QFont("Arial", 14))

        # Center buttons with vertical stretch
        layout.addStretch()
        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button3)
        layout.addStretch()

        self.setLayout(layout)
        self.resize(400, 400)  # Start with a decent size window

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SimpleWindow()
    window.show()
    sys.exit(app.exec())
