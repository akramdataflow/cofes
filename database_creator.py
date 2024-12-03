from tortoise.models import Model
from tortoise import fields, Tortoise, run_async











async def init_db():
    await Tortoise.init(
        db_url = "sqlite://C:/Users/Kstore/Documents/GitHub/cofes/data.db",  # مسار قاعدة البيانات
        modules={"models": ["__main__"]}  # تحديد موقع النماذج
    )
    await Tortoise.generate_schemas()  # إنشاء الجداول
    print("Database initialized!")

run_async(init_db())