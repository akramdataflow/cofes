from model import Model
from view import MyApp

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = MyApp(self)

    def sayHello(self):
        input_text = self.view.inputField.text()
        self.model.set_text(input_text)
        greet = f'Hello {self.model.get_text()}'
        self.view.display_greeting(greet)
