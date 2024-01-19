import sys
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel, QLineEdit,QPushButton,QMessageBox
from PyQt5.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Input Output")
        self.setGeometry(500, 300, 500, 300)

        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)

        self.label1 = QLabel("Enter Your Name")
        self.label1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label1.setFixedSize(500, 30)
        self.mainLayout.addWidget(self.label1, alignment=Qt.AlignmentFlag.AlignCenter)

        # Add QLineEdit for username input
        self.addTextBox()
        self.addButton()

    def addTextBox(self):
        self.textbox = QLineEdit(self)
        self.textbox.setPlaceholderText("Enter username...")
        self.textbox.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textbox.setFixedSize(200, 30)
        self.mainLayout.addWidget(self.textbox, alignment=Qt.AlignmentFlag.AlignCenter)

    def addButton(self):
        self.ok_button = QPushButton("Ok", self)
        self.ok_button.clicked.connect(self.on_ok_button_clicked)
        self.ok_button.setFixedSize(50, 30)
        self.mainLayout.addWidget(self.ok_button, alignment=Qt.AlignmentFlag.AlignCenter)

    def on_ok_button_clicked(self):
        username = self.textbox.text()
        if username:
            QMessageBox.information(self, "Information", f"Username entered: {username}")
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_Window = MainWindow()
    main_Window.show()
    sys.exit(app.exec_())
