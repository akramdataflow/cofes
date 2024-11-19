from PySide6.QtGui import QScreen, QIcon
from PySide6.QtWidgets import QGridLayout, QMainWindow, QApplication, QFrame, QPushButton, QSizePolicy, QLabel
from PySide6.QtCore import Qt, QSize


class MyApp(QMainWindow):
    def __init__(self, controller=None):
        super().__init__()
        self.controller = controller
        self.setWindowTitle('لنكيدو')

        # الحصول على أبعاد الشاشة
        screen = QApplication.primaryScreen()
        screen_geometry = screen.geometry()
        screen_width = screen_geometry.width()
        screen_height = screen_geometry.height()

        self.resize(screen_width, screen_height)

        # إنشاء إطار رئيسي وإضافة التخطيط عليه
        main_frame = QFrame(self)
        layout = QGridLayout(main_frame)
        self.setCentralWidget(main_frame)

        # إنشاء فريم علوي
        frame = QFrame()
        layout_frame = QGridLayout(frame)  # إنشاء تخطيط خاص بالفريم
        frame.setStyleSheet("""
            QFrame {
                background-color: #1A3654; 
            }
        """)

        # إنشاء التسمية وإضافتها إلى التخطيط الخاص بالفريم
        label = QLabel('لنكيدو')
        label.setStyleSheet("""
            QLabel {
                color: #50F296; /* تغيير لون النص */
                font-size: 50px; /* تغيير حجم النص */
                font-weight: bold; /* جعل النص عريضًا */
            }
        """)
        label.setAlignment(Qt.AlignCenter)  # محاذاة النص إلى المنتصف
        layout_frame.addWidget(label, 0, 0)


        label = QLabel('RESTAURANT <span style="color: #50F296;">&</span> CAFE')
        label.setStyleSheet("""
            QLabel {
                color: #fff; /* تغيير لون النص الافتراضي */
                font-size: 50px; /* تغيير حجم النص */
                font-weight: bold; /* جعل النص عريضًا */
            }
        """)
        label.setAlignment(Qt.AlignCenter)  # محاذاة النص إلى المنتصف
        layout_frame.addWidget(label, 1, 0)

        
        

        # إضافة الفريم العلوي إلى التخطيط الرئيسي
        layout.addWidget(frame, 0, 0)
        # تمديد الفريم العلوي بنسبة 1
        layout.setRowStretch(0, 1)

        # إنشاء فريم يحتوي على شبكة الأزرار
        frame1 = QFrame()
        layout_frame1 = QGridLayout(frame1)
        frame1.setStyleSheet("""
            QFrame {
                background-color: #fff; /* لون خلفية الفريم */
            }
        """)

        # تقليل المسافات بين الأزرار
        layout_frame1.setSpacing(10)
        layout_frame1.setContentsMargins(10, 10, 10, 10)

        # إنشاء الأزرار يدويًا
        icon = QIcon('./static/Polygon 7.svg')  # Replace with your icon path

        button1 = QPushButton()
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/اضافة مواد.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button1.setIcon(icon)
        button1.setIconSize(QSize(250, 250))
        button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button1, 0, 0)

        button2 = QPushButton()
        button2.setStyleSheet(
            '''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/الطلبات.png');
                background-repeat: no-repeat;
                background-position: center;
    }
    QPushButton:hover {
        background-color: #E9FDF2;
    }'''
        )
        button2.setIcon(icon)
        button2.setIconSize(QSize(250, 250))
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button2, 0, 1)

        button3 = QPushButton()
        button3.setStyleSheet(
            '''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/اضافة طلب.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }'''
        )
        button3.setIcon(icon)
        button3.setIconSize(QSize(250, 250))
        button3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        layout_frame1.addWidget(button3, 0, 2)

        button4 = QPushButton()
        button4.setStyleSheet('''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/تحليل المبيعات.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }''')
        button4.setIcon(icon)
        button4.setIconSize(QSize(250, 250))
        button4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button4, 1, 0)

        button5 = QPushButton()
        button5.setStyleSheet(
            '''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/المطبخ.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }'''
        )
        button5.setIcon(icon)
        button5.setIconSize(QSize(250, 250))
        button5.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button5, 1, 1)

        button6 = QPushButton()
        button6.setStyleSheet(
            '''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/الصالات.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }'''
        )
        button6.setIcon(icon)
        button6.setIconSize(QSize(250, 250))
        button6.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button6, 1, 2)

        button7 = QPushButton()
        button7.setStyleSheet(
            '''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/الطاولات.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }'''
        )
        button7.setIcon(icon)
        button7.setIconSize(QSize(250, 250))
        button7.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button7, 2, 0)

        button8 = QPushButton()
        button8.setStyleSheet(
            '''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/المخزن.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }'''
        )
        button8.setIcon(icon)
        button8.setIconSize(QSize(250, 250))
        button8.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button8, 2, 1)

        button9 = QPushButton()
        button9.setStyleSheet(
            '''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/الضبط.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }'''
        )
        button9.setIcon(icon)
        button9.setIconSize(QSize(250, 250))
        button9.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button9, 2, 2)

        # إضافة فريم الأزرار إلى التخطيط الرئيسي
        layout.addWidget(frame1, 1, 0)

        # تمديد فريم الأزرار بنسبة 5
        layout.setRowStretch(1, 5)
        layout.setColumnStretch(0, 1)


