import sys
from PySide6.QtWidgets import QApplication
from controller import Controller

if __name__ == '__main__':
    app = QApplication(sys.argv)  # قم بإنشاء كائن واحد فقط
    controller = Controller()
    controller.view.show()
    sys.exit(app.exec())






