import sqlite3
from controller import *

class Model:
    def __init__(self):
        self.conn = sqlite3.connect('data.db')  
        self.cursor = self.conn.cursor()
        


    def get_hall_name(self):
        self.cursor.execute('SELECT name FROM Hall')
        halls_name = [row[0] for row in self.cursor.fetchall()]
        self.conn.commit()
        return halls_name
    
    def save_tabel_name(self,tabel_name,hall_name):
        self.cursor.execute(
            """INSERT INTO Tabel (name_tabel,hall_name)
               VALUES (?, ?)
            """, (tabel_name,hall_name))
        self.conn.commit()

    def get_tabel_name(self):
        self.cursor.execute('SELECT name_tabel FROM Tabel')
        tabel_name = [row[0] for row in self.cursor.fetchall()]
        self.conn.commit()
        return tabel_name
    
    def get_Material(self):
        self.cursor.execute('SELECT * FROM Material')
        rows = self.cursor.fetchall()
        name = [row[0] for row in rows]
        count = [row[1] for row in rows]
        return name,count

    def add_material(self,name,cuont):
        self.cursor.execute(
        """INSERT INTO Material (name,count)
           VALUES (?, ?)
        """, (name,cuont))
        self.conn.commit()

