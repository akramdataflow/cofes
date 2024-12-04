import sqlite3
from model import Model
from view import *

class Controller:
    def __init__(self):
        self.model = Model()
        self.view = MyApp(self)
        self.halls = Halls(self)

    def add_order_button_clicked(self):
        # عند النقر على زر "إضافة طلب" نعرض نافذة جديدة
        self.add_order_window = AddOrderPage(self)
        self.add_order_window.show()

        

    def show_orders_page(self):
        # نافذة جديدة لصفحة إضافة الطلب
        self.add_order_window = Addprodact(self)
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

    def add_hall(self):
        hall_name = self.halls.hall_name.text()
        # الاتصال بقاعدة البيانات
        conn = sqlite3.connect('C:/Users/Kstore/Documents/GitHub/cofes/data.db')
        cursor = conn.cursor()

        # إدخال بيانات في جدول Hall
        cursor.execute("INSERT INTO Hall (name) VALUES (?)", (hall_name,))

        # حفظ التغييرات وإغلاق الاتصال
        conn.commit()
        conn.close()
        print(f"Hall '{hall_name}' added successfully!")
