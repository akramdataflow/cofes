from model import Model
from view import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = MyApp(self)

    def add_order_button_clicked(self):
        # عند النقر على زر "إضافة طلب" نعرض نافذة جديدة
        self.add_order_window = AddOrderPage(self)
        self.add_order_window.show()

        

    def show_orders_page(self):
        # نافذة جديدة لصفحة إضافة الطلب
        self.add_order_window = Orders(self)
        self.add_order_window.show()

    def show_halls_page(self):
        # نافذة جديدة لصفحة إضافة الطلب
        self.add_order_window = Halls(self)
        self.add_order_window.show()
    
    
    def show_tabelles_page(self):
        # نافذة جديدة لصفحة إضافة الطلب
        self.add_order_window = Tabelles(self)
        self.add_order_window.show()

    def add_prudact(self):
        self.add_prudact_window = AddProdect(self)
        self.add_prudact_window.show()

    def storeg(self):
        self.storeg_show = Storeg(self)
        self.storeg_show.show()

    def data_show(self):
        self.data = Data(self)
        self.data.show()


        
    def data_ana(self):
        self.data = Data_ana(self)
        self.data.show()

    
    def kitchen (self):
        self.data = Kitchen(self)
        self.data.show()
