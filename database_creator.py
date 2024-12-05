import sqlite3

# دالة لإنشاء قاعدة البيانات والجداول
def init_db():
    # الاتصال بقاعدة البيانات (إذا لم تكن موجودة، سيتم إنشاؤها)
    conn = sqlite3.connect('data.db')  # تحديد مسار قاعدة البيانات
    cursor = conn.cursor()  # إنشاء كائن المؤشر

    # إنشاء جدول Hall
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Hall (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    )
    ''')

    # إنشاء جدول Tabel
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Tabel (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number_of_tabel INTEGER NOT NULL,
        hall_id INTEGER,
        FOREIGN KEY(hall_id) REFERENCES Hall(id)
    )
    ''')

    # حفظ التغييرات وإغلاق الاتصال
    conn.commit()
    conn.close()

# استدعاء الدالة لإنشاء قاعدة البيانات والجداول
if __name__ == "__main__":
    init_db()
