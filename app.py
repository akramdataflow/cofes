import sys
from PySide6.QtWidgets import QApplication
from controller import Controller, Controller_main

if __name__ == '__main__':
    app = QApplication(sys.argv)
    controller = Controller_main()
    controller.view.show()
    sys.exit(app.exec())
