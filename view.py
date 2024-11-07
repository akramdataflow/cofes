from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QTextEdit



class MyApp(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle('Testing')
        self.setWindowIcon(QIcon('google-maps.png'))
        self.resize(300, 200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputField = QLineEdit()
        button = QPushButton('&Say Hello')
        button.clicked.connect(self.controller.sayHello)
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        delet_button = QPushButton('&Delet')
        delet_button.clicked.connect(self.controller.delet)


        button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50; /* Green background */
                color: white; /* White text */
                border: none; /* No border */
                padding: 10px 20px; /* Some padding */
                text-align: center; /* Center text */
                text-decoration: none; /* No underline */
                display: inline-block; /* Inline-block display */
                font-size: 16px; /* Font size */
                margin: 4px 2px; /* Margin */
                cursor: pointer; /* Pointer cursor on hover */
                border-radius: 5px; /* Rounded corners */
            }
            QPushButton:hover {
                background-color: #45a049; /* Darker green on hover */
            }
        """)

        delet_button.setStyleSheet("""
            QPushButton {
                background-color: #47D685; /* Green background */
                color: white; /* White text */
                border: none; /* No border */
                padding: 10px 20px; /* Some padding */
                text-align: center; /* Center text */
                text-decoration: none; /* No underline */
                display: inline-block; /* Inline-block display */
                font-size: 16px; /* Font size */
                margin: 4px 2px; /* Margin */
                cursor: pointer; /* Pointer cursor on hover */
                border-radius: 5px; /* Rounded corners */
            }
            QPushButton:hover {
                background-color: #435160; /* Darker green on hover */
            }
        """)

        layout.addWidget(self.inputField)
        layout.addWidget(button)
        layout.addWidget(self.output)
        layout.addWidget(delet_button)

    def display_greeting(self, greeting):
        self.output.setText(greeting)