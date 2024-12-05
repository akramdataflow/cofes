import sqlite3
conn = sqlite3.connect('data.db')  
cursor = conn.cursor()

cursor.execute('SELECT name FROM Hall')

halls_name = [row[0] for row in cursor.fetchall()]

conn.commit()
