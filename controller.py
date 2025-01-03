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
        self.add_prudact_window = Addmaterial(self)
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

    def add_hall(self, hall_name):
        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        # إدخال بيانات في جدول Hall
        cursor.execute("INSERT INTO Hall (name) VALUES (?)", (hall_name,))

        # حفظ التغييرات وإغلاق الاتصال
        conn.commit()
        conn.close()
        print(f"Hall '{hall_name}' added successfully!")

    def get_hall_name_from_model(self):
        hall_name = self.model.get_hall_name()
        return hall_name
    
    def get_tabel_name_from_model(self):
        tabel_name  = self.model.get_tabel_name()
        return tabel_name
    
    
    def add_tabel(self,tabel_name, hall_name):
        self.model.save_tabel_name(tabel_name,hall_name)

    def add_Material_to_storeg(self,name,count):
        self.model.add_material(name,count)

    def get_material_from_maoel(self):
        name, count = self.model.get_Material()
        return name,count

    def add_kitchen_to_model(self,name):
        self.model.add_kitchen(name)  

    def get_kitchen_from_model(self):
        name = self.model.get_kitchen()
        return name
    

        




    
