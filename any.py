from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QVBoxLayout, QWidget
from PySide6.QtGui import QStandardItemModel, QStandardItem

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("عرض جدول باستخدام QTableView")
        self.setGeometry(100, 100, 600, 400)

        # إعداد الـ TableView
        table = QTableView(self)

        # إنشاء النموذج
        model = QStandardItemModel(3, 3)  # 3 صفوف و 3 أعمدة
        model.setHorizontalHeaderLabels(['الاسم', 'العمر', 'المدينة'])

        # إضافة البيانات للنموذج
        data = [
            ['أحمد', '25', 'بغداد'],
            ['سارة', '30', 'البصرة'],
            ['محمد', '22', 'الموصل']
        ]

        for row in range(3):
            for col in range(3):
                item = QStandardItem(data[row][col])
                model.setItem(row, col, item)

        # تعيين النموذج للـ TableView
        table.setModel(model)

        # وضع الـ TableView في الـ Layout
        layout = QVBoxLayout()
        layout.addWidget(table)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

# تشغيل التطبيق
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
