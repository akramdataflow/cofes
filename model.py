import sqlite3

class Model:
    def get_hall_name(self):
        conn = sqlite3.connect('data.db')  
        cursor = conn.cursor()

        cursor.execute('SELECT name FROM Hall')

        halls_name = [row[0] for row in cursor.fetchall()]

        conn.commit()
        conn.close()
    
        return halls_name