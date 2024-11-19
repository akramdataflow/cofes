from model import Model
from view import MyApp

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = MyApp(self)





