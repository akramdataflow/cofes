from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton

# Model
class Model:
    def __init__(self):
        self.name = ""

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name


# View
class View(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("MVC تطبيق")
        self.setGeometry(100, 100, 300, 150)

        self.layout = QVBoxLayout()

        # Create input field for name
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("أدخل اسمك هنا")
        self.layout.addWidget(self.name_input)

        # Label to display greeting
        self.greeting_label = QLabel("", self)
        self.layout.addWidget(self.greeting_label)

        # Button to trigger the greeting
        self.show_button = QPushButton("عرض الاسم", self)
        self.layout.addWidget(self.show_button)

        self.setLayout(self.layout)


# Controller
class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.show_button.clicked.connect(self.update_greeting)

    def update_greeting(self):
        # Get the name from the input field
        name = self.view.name_input.text()
        self.model.set_name(name)

        # Update the label with the greeting message
        self.view.greeting_label.setText(f"أهلاً {self.model.get_name()}")


if __name__ == "__main__":
    app = QApplication([])

    # Initialize Model, View, and Controller
    model = Model()
    view = View()
    controller = Controller(model, view)

    view.show()
    app.exec()
