from model import Model
from view import MyApp, AddOrderPage, Orders, Halls, Tabelles

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = MyApp(self)

    def add_order_button_clicked(self):
        # عند النقر على زر "إضافة طلب" نعرض نافذة جديدة
        self.show_add_order_page()


    def show_add_order_page(self):
        # نافذة جديدة لصفحة إضافة الطلب
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
    