from model import Model
from view import MyApp, Main

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = MyApp(self)

    def sayHello(self):
        input_text = self.view.inputField.text()
        self.model.set_text(input_text)
        greet = f'Hello {self.model.get_text()}'
        self.view.display_greeting(greet)

    def delet(self):
        self.view.output.clear()



class Controller_main:
    def __init__(self):
        self.view = Main(self)

    def greet(self, data):
        print('button is clicked', data)