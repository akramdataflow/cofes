from PySide6.QtGui import QScreen, QIcon, QPixmap, QIntValidator
from PySide6.QtWidgets import QGridLayout, QMainWindow, QApplication, QFrame, QPushButton, QSizePolicy, QLabel, QLineEdit,  QComboBox, QSpinBox, QVBoxLayout, QTableWidget, QTableWidgetItem, QVBoxLayout
from PySide6.QtCore import Qt, QSize
import sqlite3


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
        button1.clicked.connect(self.controller.add_prudact)
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/اضافة مواد.png');
               font-size: 16px;
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
        button2.clicked.connect(self.controller.show_orders_page)
        button2.setStyleSheet(
            '''QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/Group 24.png');
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
        button3.clicked.connect(self.controller.add_order_button_clicked)
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
        button4.clicked.connect(self.controller.data_show)
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
        button5.clicked.connect(self.controller.kitchen)
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
        button6.clicked.connect(self.controller.show_halls_page)
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
        button7.clicked.connect(self.controller.show_tabelles_page)
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
        button8.clicked.connect(self.controller.storeg)
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


class AddOrderPage(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("إضافة طلب")
        self.resize(500, 500)

        pixmap = QPixmap('./static/اضافة طلب/ايقونة اضافة الطلبات.png')
        pixmap = pixmap.scaled(32, 32)
        self.setWindowIcon(QIcon(pixmap))

        main_frame = QFrame()
        main_frame.setStyleSheet(
            """
            QFrame {
                background-color: #1A3654; 
            }
            """
        )
        layout = QGridLayout(main_frame)

        # Set the central widget properly
        self.setCentralWidget(main_frame)
    

        header_frame = QFrame()

        header_frame.setStyleSheet("""
            QFrame {
                background-color: #50F296; 
                border-radius: 6px;
                background-image: url('./static/اضافة طلب/اضافة الطلبات.png');
                background-repeat: no-repeat;
                background-position: right;
                padding: 100px; 
            }
            """)


        header_frame.setFixedHeight(40)
        layout.addWidget(header_frame,0,0,1,0)




######################################################################################################        
        view_frame = QFrame()

        view_frame.setStyleSheet("""
            QFrame {
                background-color: #fff; 
                border-radius: 6px;  
                padding: 10px;              
            }
            """)
        

        view_frame_layout = QGridLayout(view_frame)

        label = QLabel('البحث')
        label.setStyleSheet('''
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        view_frame_layout.addWidget(label,0,3)


        self.serch_line = QLineEdit()
        self.serch_line.setStyleSheet('''
                border-radius: 10px;
                background: #BEB8B8;
            ''')
        view_frame_layout.addWidget(self.serch_line,0,2)

        button1 = QPushButton('المأكولات')
        button1.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        
        view_frame_layout.addWidget(button1,0,1)

        button2 = QPushButton('المشروبات')
        button2.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        
        view_frame_layout.addWidget(button2,0,0)
        
        data_frame = QFrame()
        data_frame.setStyleSheet('''
                border-radius: 10px;
                background: rgba(0, 0, 0, 0.10);
            ''')
        view_frame_layout.addWidget(data_frame,1,0,1,4)

        layout.addWidget(view_frame, 1, 0, 1, 3)




######################################################################################################
        add_frame = QFrame()
        add_frame.setStyleSheet("""
            QFrame {
                background-color: #fff; 
                border-radius: 6px; 
                padding: 10px;               
            }
            """)
        
        layout.addWidget(add_frame,1,3)

        add_frame_layout = QGridLayout(add_frame)

        name_food_drinck_label = QLabel('اسم الأكلة او المشروب')
        name_food_drinck_label.setStyleSheet('''

                color: #1A3654;
                text-align: right;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;

            ''')
        add_frame_layout.addWidget(name_food_drinck_label,0,1)


        self.name_food_drinck_combo = QComboBox()
        self.name_food_drinck_combo.setEditable(True)
        self.name_food_drinck_combo.setStyleSheet('''
                border-radius: 4px; 
                background: #1A3654;
                color: #fff;

            ''')
        
        options = ["بيتزا", "شاورما", "برجر", "عصير مانجو", "عصير برتقال", "فاهيتا"]
        self.name_food_drinck_combo.addItems(options)
        add_frame_layout.addWidget(self.name_food_drinck_combo, 0, 0)


        label = QLabel('نوع الطلب')
        label.setStyleSheet('''
                color: #1A3654;
                text-align: right;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        add_frame_layout.addWidget(label,1,1)

        self.order_tayp = QComboBox()
        self.order_tayp.setStyleSheet('''
                border-radius: 4px; 
                background: #1A3654;
                color: #fff;

            ''')
        add_frame_layout.addWidget(self.order_tayp,1,0)

        label = QLabel('الصالة')
        label.setStyleSheet('''
                color: #1A3654;
                text-align: right;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        add_frame_layout.addWidget(label,2,1)
        
        self.order_to_hall = QComboBox()
        self.order_to_hall.setStyleSheet('''
                border-radius: 4px; 
                background: #1A3654;
                color: #fff;

            ''')
        add_frame_layout.addWidget(self.order_to_hall,2,0)


        label = QLabel('الطاولة')
        label.setStyleSheet('''
                color: #1A3654;
                text-align: right;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        add_frame_layout.addWidget(label,3,1)
        
        self.order_to_tabel = QComboBox()
        self.order_to_tabel.setStyleSheet('''
                border-radius: 4px; 
                background: #1A3654;
                color: #fff;

            ''')
        add_frame_layout.addWidget(self.order_to_tabel,3,0)


        button1 = QPushButton()
        button1.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                background-image: url('./static/حفظ.png');
                background-repeat: no-repeat;
                background-position: center;
            ''')
        
        add_frame_layout.addWidget(button1,4,0,1,2)


        button2 = QPushButton()
        button2.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                background-image: url('./static/جديد.png');
                background-repeat: no-repeat;
                background-position: center;
            ''')
        
        add_frame_layout.addWidget(button2,5,0,1,2)


        button2 = QPushButton()
        button2.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                background-image: url('./static/حذف.png');
                background-repeat: no-repeat;
                background-position: center;
            ''')
        
        add_frame_layout.addWidget(button2,6,0,1,2)


class Addprodact(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("الطلبات")
        self.resize(750, 750)
        # pixmap = QPixmap('./static/الطلبات.png')
        # pixmap = pixmap.scaled(32, 32)
        # self.setWindowIcon(QIcon(pixmap))

        main_frame = QFrame()
        main_frame.setStyleSheet(
            """
            QFrame {
                background-color: #1A3654; 
            }
            """
        )

        layout = QGridLayout(main_frame)

        # Set the central widget properly
        self.setCentralWidget(main_frame)

        header_frame = QFrame()

        header_frame.setStyleSheet("""
            QFrame {
                background-color: #50F296; 
                border-radius: 6px;
                background-image: url('./static/منتج جديد/Group 23.png');
                background-repeat: no-repeat;
                background-position: right;
                padding: 100px; 
            }
            """)


        header_frame.setFixedHeight(60)
        layout.addWidget(header_frame,0,0)

        frame = QFrame()
        layout.addWidget(frame,1,0)

        add_frame_layout = QGridLayout(frame)
        label = QLabel('اسم المنتج')
        label.setStyleSheet('''
                color: #FFF;
                font-family: Inter;
                font-size: 14px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        add_frame_layout.addWidget(label,0,1)

        self.product_name = QLineEdit()
        self.product_name.setStyleSheet('''
                border-radius: 4px; 
                background: #fff;
                color: #000;
            ''')
        add_frame_layout.addWidget(self.product_name,0,0)

        label = QLabel('المطبخ')
        label.setStyleSheet('''
                color: #FFF;
                font-family: Inter;
                font-size: 14px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        add_frame_layout.addWidget(label,1,1)

        self.kitchen = QComboBox()
        self.kitchen.setStyleSheet('''
                border-radius: 4px; 
                background: #fff;
                color: #000;
            ''')
        add_frame_layout.addWidget(self.kitchen,1,0)

        label = QLabel('السعر')
        label.setStyleSheet('''
                color: #FFF;
                font-family: Inter;
                font-size: 14px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        
        add_frame_layout.addWidget(label,2,1)

        self.price = QSpinBox()
        self.price.setStyleSheet('''
                    border-radius: 4px;
                    background: #fff;
                ''')
        add_frame_layout.addWidget(self.price,2,0)


        save_frame = QFrame()
        save_frame_layout = QGridLayout(save_frame)

        button1 = QPushButton()
        button1.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/حفظ.png');
                    background-repeat: no-repeat;
                    background-position: center;
            ''')
        save_frame_layout.addWidget(button1,0,0)

        button2 = QPushButton()
        button2.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                background-image: url('./static/جديد.png');
                background-repeat: no-repeat;
                background-position: center;
            ''')
        save_frame_layout.addWidget(button2,1,0)

        add_frame_layout.addWidget(save_frame,3,0,1,2)


class Halls(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("الصالات")
        self.resize(500, 500)
        pixmap = QPixmap('./static/الصالات/ايقونة الصالات.png')
        pixmap = pixmap.scaled(32, 32)
        self.setWindowIcon(QIcon(pixmap))

        main_frame = QFrame()
        main_frame.setStyleSheet(
            """
            QFrame {
                background-color: #1A3654; 
            }
            """
        )

        layout = QGridLayout(main_frame)

        # Set the central widget properly
        self.setCentralWidget(main_frame)

        header_frame = QFrame()

        header_frame.setStyleSheet("""
            QFrame {
                background-color: #50F296; 
                border-radius: 6px;
                background-image: url('./static/الصالات/الصالات.png');
                background-repeat: no-repeat;
                background-position: right;
                padding: 100px; 
            }
            """)


        header_frame.setFixedHeight(40)
        layout.addWidget(header_frame,0,0,1,0)


        frame = QFrame()
        layout.addWidget(frame,1,1)

        frame_layout = QGridLayout(frame)

        label = QLabel('اسم الصالة')
        label.setStyleSheet('''
                color: #FFF;
                font-family: Inter;
                font-size: 14px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
            ''')
        frame_layout.addWidget(label,0,1)

        self.hall_name = QLineEdit(self)
        self.hall_name.setStyleSheet('''
                border-radius: 4px;
                background: #fff;
            ''')
        frame_layout.addWidget(self.hall_name,0,0)


        button1 = QPushButton()
        button1.clicked.connect(self.send_hall_name_to_controller)
        button1.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                background-image: url('./static/حفظ.png');
                background-repeat: no-repeat;
                background-position: center;
            ''')
        frame_layout.addWidget(button1,1,0,1,2)


        button2 = QPushButton()
        button2.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                background-image: url('./static/حذف.png');
                background-repeat: no-repeat;
                background-position: center;
            ''')
        frame_layout.addWidget(button2,3,0,1,2)




        data_frame = QFrame()
        data_frame_layout = QGridLayout(data_frame)

        data_frame.setStyleSheet('''
                border-radius: 5px;
                background: #FFF;
            ''')

        layout.addWidget(data_frame,1,0)

        self.hall_name_count = self.controller.get_hall_name_from_model()
        for index, hall_name in enumerate(self.hall_name_count):
            # إنشاء الإطار
            frame_iner = QFrame(self)
            frame_iner.setStyleSheet(
                """
                border-radius: 5px;
                background: #50F296;
                """
            )

            # إعداد التخطيط العمودي داخل الإطار
            frame_layout = QVBoxLayout(frame_iner)

            # إنشاء النص (اسم الصالة)
            label = QLabel(hall_name, frame_iner)
            label.setStyleSheet("font-size: 14px; font-weight: bold; text-align: center;")
            label.setAlignment(Qt.AlignCenter)  # محاذاة النص في منتصف الإطار

            # إضافة النص إلى التخطيط داخل الإطار
            frame_layout.addWidget(label)

            # تحديد الصف والعمود
            row = index // 4  # حساب الصف بناءً على العدد
            col = index % 4   # حساب العمود بناءً على العدد

            # إضافة الإطار إلى التخطيط الشبكي
            data_frame_layout.addWidget(frame_iner, row, col)


        layout.setColumnStretch(0,2)
        layout.setColumnStretch(1,1)

    def send_hall_name_to_controller(self):
        hall_name = self.hall_name.text()
        self.controller.add_hall(hall_name)


class Tabelles(QMainWindow):
        def __init__(self, controller):
            super().__init__()
            self.controller = controller
            self.setWindowTitle("الطاولات")
            self.resize(500, 500)
            pixmap = QPixmap('./static/الصالات/ايقونة الصالات.png')
            pixmap = pixmap.scaled(32, 32)
            self.setWindowIcon(QIcon(pixmap))
    
            main_frame = QFrame()
            main_frame.setStyleSheet(
                """
                QFrame {
                    background-color: #1A3654; 
                }
                """
            )
    
            layout = QGridLayout(main_frame)
    
            # Set the central widget properly
            self.setCentralWidget(main_frame)
    
            header_frame = QFrame()
    
            header_frame.setStyleSheet("""
                QFrame {
                    background-color: #50F296; 
                    border-radius: 6px;
                    background-image: url('./static/الطاولات/الطاولات.png');
                    background-repeat: no-repeat;
                    background-position: right;
                    padding: 100px; 
                }
                """)
    
    
            header_frame.setFixedHeight(40)
            layout.addWidget(header_frame,0,0,1,0)
    
    
            frame = QFrame()
            layout.addWidget(frame,1,1)
    
            frame_layout = QGridLayout(frame)
    
            label = QLabel('رقم الطاولة')
            label.setStyleSheet('''
                    color: #FFF;
                    font-family: Inter;
                    font-size: 14px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                ''')
            frame_layout.addWidget(label,0,1)
    
            self.taebal_name = QLineEdit(self)
            self.taebal_name.setStyleSheet('''
                    border-radius: 4px;
                    background: #fff;
                ''')
            frame_layout.addWidget(self.taebal_name,0,0)
    

            label = QLabel('اسم الصالة')
            label.setStyleSheet('''
                    color: #FFF;
                    font-family: Inter;
                    font-size: 14px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                ''')
            frame_layout.addWidget(label,1,1)
    
            
    
            self.hall_name = QComboBox()
            self.hall_name.setEditable(True)
            self.hall_name.setStyleSheet('''
                    border-radius: 4px;
                    background: #fff;
                ''')
            self.hall_name.addItems(self.controller.get_hall_name_from_model())
            frame_layout.addWidget(self.hall_name,1,0)
    
            button1 = QPushButton()
            button1.clicked.connect(self.send_tabel_name_to_controller)
            button1.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/حفظ.png');
                    background-repeat: no-repeat;
                    background-position: center;
                ''')
            frame_layout.addWidget(button1,2,0,1,2)
    
    
            button2 = QPushButton()
            button2.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/جديد.png');
                    background-repeat: no-repeat;
                    background-position: center;
                ''')
            frame_layout.addWidget(button2,3,0,1,2)
    
    
            button3 = QPushButton()
            button3.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/حذف.png');
                    background-repeat: no-repeat;
                    background-position: center;
                ''')
            frame_layout.addWidget(button3,4,0,1,2)
    
    
    
    
            data_frame = QFrame()
            data_frame_layout = QGridLayout(data_frame)

            data_frame.setStyleSheet('''
                    border-radius: 5px;
                    background: #FFF;
                ''')

            layout.addWidget(data_frame,1,0)

            # جلب أسماء الطاولات وترتيبها
            self.tabel_name_count = sorted(self.controller.get_tabel_name_from_model())
            
            # إنشاء الإطارات وترتيبها داخل التخطيط
            for index, tabel_name in enumerate(self.tabel_name_count):
                # إنشاء الإطار
                frame_iner = QFrame(self)
                frame_iner.setStyleSheet(
                    """
                    border-radius: 5px;
                    background: #50F296;
                    """
                )
            
                # إعداد التخطيط العمودي داخل الإطار
                frame_layout = QVBoxLayout(frame_iner)
            
                # إنشاء النص (اسم الطاولة)
                label = QLabel(tabel_name, frame_iner)
                label.setStyleSheet("font-size: 14px; font-weight: bold; text-align: center;")
                label.setAlignment(Qt.AlignCenter)  # محاذاة النص في منتصف الإطار
            
            
                # إضافة النص إلى التخطيط داخل الإطار
                frame_layout.addWidget(label)
            
                # تحديد الصف والعمود
                row = index // 4  # حساب الصف بناءً على العدد
                col = index % 4   # حساب العمود بناءً على العدد
            
                # إضافة الإطار إلى التخطيط الشبكي
                data_frame_layout.addWidget(frame_iner, row, col)



            layout.setColumnStretch(0,2)
            layout.setColumnStretch(1,1)

        

        def send_tabel_name_to_controller(self):
            tabel_name = self.taebal_name.text()
            hall_name = self.hall_name.currentText()
            self.controller.add_tabel(tabel_name,hall_name)
            self.taebal_name.clear()


class Addmaterial(QMainWindow):
        def __init__(self, controller):
            super().__init__()
            self.controller = controller
            self.setWindowTitle("الطاولات")
            self.resize(500, 500)
            pixmap = QPixmap('./static/اضافة مواد/noun-add-7163783-1A3654 1.png')
            pixmap = pixmap.scaled(32, 32)
            self.setWindowIcon(QIcon(pixmap))

            self.controller.get_material_from_maoel()
    
            main_frame = QFrame()
            main_frame.setStyleSheet(
                """
                QFrame {
                    background-color: #1A3654; 
                }
                """
            )
    
            layout = QGridLayout(main_frame)
    
            # Set the central widget properly
            self.setCentralWidget(main_frame)
    
            header_frame = QFrame()
    
            header_frame.setStyleSheet("""
                QFrame {
                    background-color: #50F296; 
                    border-radius: 6px;
                    background-image: url('./static/اضافة مواد/Group 11.png');
                    background-repeat: no-repeat;
                    background-position: right;
                    padding: 100px; 
                }
                """)
    
    
            header_frame.setFixedHeight(40)
            layout.addWidget(header_frame,0,0,1,0)    

            frame = QFrame()
            

            layout.addWidget(frame,1,0)
            layout_frame = QGridLayout(frame)

            add_frame = QFrame()

            add_frame_layout = QGridLayout(add_frame)

            label = QLabel('اسم المادة')
            label.setStyleSheet(
                 """color: #FFF;
                    font-family: Inter;
                    font-size: 14px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;""")
            
            add_frame_layout.addWidget(label,0,1)


            self.material_name = QLineEdit()
            self.material_name.setStyleSheet(
                 """
                    background: #FFF;
                """
            )
            add_frame_layout.addWidget(self.material_name,0,0)

            label = QLabel("العدد")
            label.setStyleSheet(
                 """color: #FFF;
                    font-family: Inter;
                    font-size: 14px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;""")

            add_frame_layout.addWidget(label,1,1)


            self.spin = QSpinBox()
            self.spin.setStyleSheet('''
                    border-radius: 4px;
                    background: #fff;
                ''')            

            add_frame_layout.addWidget(self.spin, 1, 0)


            button1 = QPushButton()
            button1.clicked.connect(self.send_material_to_controller)
            button1.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/حفظ.png');
                    background-repeat: no-repeat;
                    background-position: center;
                ''')
            add_frame_layout.addWidget(button1,2,0,1,2)
    
    
            button2 = QPushButton()
            button2.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/جديد.png');
                    background-repeat: no-repeat;
                    background-position: center;
                ''')
            add_frame_layout.addWidget(button2,3,0,1,2)
    
    
            button3 = QPushButton()
            button3.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/حذف.png');
                    background-repeat: no-repeat;
                    background-position: center;
                ''')
            add_frame_layout.addWidget(button3,4,0,1,2)




            
            data_frame = QFrame()
            data_frame_layout = QVBoxLayout(data_frame)
            
            data_tabel = self.controller.get_material_from_maoel()
            
            # Create the table widget
            self.table = QTableWidget()

            self.table.setGeometry(data_frame.geometry())

            
            # Configure the table
            self.table.setColumnCount(2)
            self.table.setHorizontalHeaderLabels(['Name', 'Count'])
            
            # Populate the table with data
            if data_tabel:
                row_count = len(data_tabel[0])  # Assuming name and count have the same length
                self.table.setRowCount(row_count)
            
                for row in range(row_count):
                    self.table.setItem(row, 0, QTableWidgetItem(data_tabel[0][row]))  # Insert Name
                    self.table.setItem(row, 1, QTableWidgetItem(str(data_tabel[1][row])))  # Insert Count)
            
            # Resize columns to fit content
            self.table.resizeColumnsToContents()
            
            # Add the table to the frame's layout
            data_frame_layout.addWidget(self.table)
            data_frame.setLayout(data_frame_layout)





            



            data_frame.setStyleSheet(
                """
                QFrame {
                    background-color: #fff; 
                    border-radius: 6px;
                }
                """
            )
            

            layout_frame.addWidget(data_frame, 0, 0)
            layout_frame.addWidget(add_frame, 0, 1)

            layout_frame.setColumnStretch(0,4)
            layout_frame.setColumnStretch(1,1)

        def send_material_to_controller(self):
            self.controller.add_Material_to_storeg(self.material_name.text(),self.spin.value())


class Storeg(QMainWindow):
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("المخزن")
        pixmap = QPixmap('./static/المخزن/المخزن.png')
        pixmap = pixmap.scaled(32, 32)
        self.setWindowIcon(QIcon(pixmap))
        self.resize(500,500)


        main_frame = QFrame()
        main_frame.setStyleSheet("""background-color: #1A3654;""")
        self.setCentralWidget(main_frame)


        main_frame_layout = QGridLayout(main_frame)
         
        header = QFrame()
        header.setStyleSheet(
             """border-radius: 6px;
                background: #50F296;
                background-image: url('./static/المخزن/Group 15.png');
                background-repeat: no-repeat;
                background-position: right;
                """
        )

        header.setFixedHeight(40)
        main_frame_layout.addWidget(header,0,0,1,2)


        add_frame = QFrame()
        main_frame_layout.addWidget(add_frame,1,1)

        add_frame_layout = QGridLayout(add_frame)


        lable = QLabel("القسم")
        lable.setStyleSheet(
             """color: #FFF;
                font-family: Inter;
                font-size: 14px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;"""
                        )
        add_frame_layout.addWidget(lable,0,1)

        self.class_food = QComboBox()
        self.class_food.setStyleSheet('''
                border-radius: 4px; 
                background: #fff;
                color: #000;

            ''')
        add_frame_layout.addWidget(self.class_food,0,0)



        


        lable = QLabel("البحث")
        lable.setStyleSheet(
             """color: #FFF;
                font-family: Inter;
                font-size: 14px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;"""
                        )
        add_frame_layout.addWidget(lable,1,1)


        self.serch = QComboBox()
        self.serch.setStyleSheet('''
                border-radius: 4px; 
                background: #fff;
                color: #000;

            ''')
        add_frame_layout.addWidget(self.serch,1,0)


        button1 = QPushButton()
        button1.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/حذف.png');
                    background-repeat: no-repeat;
                    background-position: center;
                ''')
        
        add_frame_layout.addWidget(button1,2,0,1,2)




        frame = QFrame()
        frame.setStyleSheet(
                """
                QFrame {
                    background-color: #fff; 
                    border-radius: 6px;
                }
                """
            )
        main_frame_layout.addWidget(frame,1,0)
        main_frame_layout.setColumnStretch(0,4)
        main_frame_layout.setColumnStretch(1,1)


class Data(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle('لنكيدو')

        main_frame = QFrame(self)
        layout = QGridLayout(main_frame)
        self.setCentralWidget(main_frame)

        # إنشاء فريم علوي
        frame = QFrame()
        layout_frame = QGridLayout(frame)
        frame.setStyleSheet("""
            QFrame {
                background-color: #1A3654;
            }
        """)

        label = QLabel('لنكيدو')
        label.setStyleSheet("""
            QLabel {
                color: #50F296;
                font-size: 50px;
                font-weight: bold;
            }
        """)
        label.setAlignment(Qt.AlignCenter)
        layout_frame.addWidget(label, 0, 0)

        label = QLabel('RESTAURANT <span style="color: #50F296;">&</span> CAFE')
        label.setStyleSheet("""
            QLabel {
                color: #fff;
                font-size: 50px;
                font-weight: bold;
            }
        """)
        label.setAlignment(Qt.AlignCenter)
        layout_frame.addWidget(label, 1, 0)

        layout.addWidget(frame, 0, 0)
        layout.setRowStretch(0, 1)

        # إنشاء فريم يحتوي على شبكة الأزرار
        frame1 = QFrame()
        layout_frame1 = QGridLayout(frame1)
        frame1.setStyleSheet("""
            QFrame {
                background-color: #fff;
            }
        """)

        layout_frame1.setSpacing(10)
        layout_frame1.setContentsMargins(10, 10, 10, 10)

        # إنشاء الأزرار
        icon = QIcon('./static/Polygon 7.svg')  # تأكد من صحة المسار

        button1 = QPushButton()
        button1.clicked.connect(self.controller.data_ana)
        button1.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/Group 17.png');
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

        # أزرار أخرى
        button2 = QPushButton()
        button2.clicked.connect(self.controller.show_orders_page)
        button2.setStyleSheet("""
            QPushButton {
                background-color: #FFF;
                font-size: 16px;
                border-radius: 5px;
                padding: 10px;
                background-image: url('./static/Group 18.png');
                background-repeat: no-repeat;
                background-position: center;
            }
            QPushButton:hover {
                background-color: #E9FDF2;
            }
        """)
        button2.setIcon(icon)
        button2.setIconSize(QSize(250, 250))
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        layout_frame1.addWidget(button2, 0, 1)

        layout.addWidget(frame1, 1, 0)
        
        layout.setRowStretch(1, 2)


class Data_ana(QMainWindow):
        def __init__(self, controller):
            super().__init__()
            self.controller = controller
            self.setWindowTitle('لنكيدو')
         

class Kitchen(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("المخزن")
        pixmap = QPixmap('./static/المطبخ/noun-kitchen-7162636-1A3654 1.png')
        pixmap = pixmap.scaled(32, 32)
        self.setWindowIcon(QIcon(pixmap))
        self.resize(1000, 1000)

        main_frame = QFrame()
        main_frame.setStyleSheet("""background-color: #1A3654;""")
        self.setCentralWidget(main_frame)

        main_frame_layout = QGridLayout(main_frame)

        header = QFrame()
        header.setStyleSheet(
            """border-radius: 6px;
               background: #50F296;
               background-image: url('./static/المطبخ/Group 19.png');
               background-repeat: no-repeat;
               background-position: right;
            """
        )
        header.setFixedHeight(40)
        main_frame_layout.addWidget(header, 0, 0)

        frame = QFrame()
        main_frame_layout.addWidget(frame, 1, 0)
        frame_layout = QGridLayout(frame)

        # Add Frame
        add_frame = QFrame()
        add_frame_layout = QGridLayout()
        add_frame.setLayout(add_frame_layout)
        frame_layout.addWidget(add_frame, 0, 1)

        # Add Label
        label = QLabel('المطبخ')
        label.setStyleSheet("color: white; font-size: 16px;")
        add_frame_layout.addWidget(label, 0, 1)

        self.kitchen_name = QLineEdit()
        self.kitchen_name.setStyleSheet('''
                    border-radius: 4px;
                    background: #fff;
                ''')
        add_frame_layout.addWidget(self.kitchen_name, 0, 0)

        button1 = QPushButton()
        button1.clicked.connect(self.send_kitchen_name_to_controller)
        button1.setStyleSheet('''
                    border-radius: 4px;
                    background: #50F296;
                    color: #1A3654;
                    font-family: Inter;
                    font-size: 16px;
                    font-style: normal;
                    font-weight: 700;
                    line-height: normal;
                    background-image: url('./static/حفظ.png');
                    background-repeat: no-repeat;
                    background-position: center;
            ''')
        add_frame_layout.addWidget(button1, 1, 0, 1, 2)

        button2 = QPushButton()
        button2.setStyleSheet('''
                border-radius: 4px;
                background: #50F296;
                color: #1A3654;
                font-family: Inter;
                font-size: 16px;
                font-style: normal;
                font-weight: 700;
                line-height: normal;
                background-image: url('./static/حذف.png');
                background-repeat: no-repeat;
                background-position: center;
            ''')
        add_frame_layout.addWidget(button2, 2, 0, 1, 2)

        self.data_frame = QFrame()
        self.data_frame_layout = QGridLayout(self.data_frame)
        frame_layout.addWidget(self.data_frame, 0, 0)
        self.data_frame.setStyleSheet(
            """
            QFrame {
                background-color: #fff; 
                border-radius: 6px;
            }
            """
        )

        frame_layout.setColumnStretch(0, 4)
        frame_layout.setColumnStretch(1, 1)

        # Load initial data
        self.load_kitchens()

    def load_kitchens(self):
        """Load kitchen data into the data_frame."""
        # Clear previous data
        while self.data_frame_layout.count():
            item = self.data_frame_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()

        self.tabel_name_count = sorted(self.controller.get_kitchen_from_model())

        # Add kitchens to the layout
        for index, tabel_name in enumerate(self.tabel_name_count):
            # Create a frame for each kitchen
            frame_iner = QFrame(self)
            frame_iner.setStyleSheet(
                """
                border-radius: 5px;
                background: #50F296;
                """
            )
            frame_layout = QVBoxLayout(frame_iner)

            # Add the kitchen name as a label
            label = QLabel(tabel_name, frame_iner)
            label.setStyleSheet("font-size: 14px; font-weight: bold; text-align: center;")
            label.setAlignment(Qt.AlignCenter)
            frame_layout.addWidget(label)

            # Calculate row and column
            row = index // 4  # 4 kitchens per row
            col = index % 4

            self.data_frame_layout.addWidget(frame_iner, row, col)

    def send_kitchen_name_to_controller(self):
        """Add a new kitchen and reload the data."""
        new_kitchen = self.kitchen_name.text()
        if new_kitchen.strip():  # Ensure it's not empty
            self.controller.add_kitchen_to_model(new_kitchen)
            self.kitchen_name.clear()
            self.load_kitchens()



