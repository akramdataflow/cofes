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
        name_tabel TEXT UNIQUE NOT NULL,
        hall_name TEXT,
        FOREIGN KEY(hall_name) REFERENCES Hall(name)
    )
    ''')

    # حفظ التغييرات وإغلاق الاتصال
    conn.commit()
    conn.close()

# استدعاء الدالة لإنشاء قاعدة البيانات والجداول
if __name__ == "__main__":
    init_db()
