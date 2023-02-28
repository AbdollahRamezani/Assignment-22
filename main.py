import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from functools import partial
from main_window import Ui_mainWindow  # فایل یوآی که تبدیل به فایل پایتونی کردیم
from database import Database


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_mainWindow()  # همون فایل پایتونی بالااست
        self.ui.setupUi(self)

        self.db = Database()
        self.read_from_database()   
               
        self.ui.btn_newtask.clicked.connect(self.add_newtask) 
    
    
    def add_newtask(self):  
        new_title = self.ui.textbox_newtask_title.text()  
        new_time = self.ui.textbox_newtask_time.text()
        new_date = self.ui.textbox_newtask_date.text()
        if self.ui.radioButton_normal.isChecked():
             priority = 0
        elif self.ui.radioButton_important.isChecked():
             priority = 1
        new_description = self.ui.textbox_newtask_description.toPlainText()  
        if new_title and new_description != "": #شرط اگر تکست باگس خالی باشد رکورد خالی ذخیره نکند
            feedback = self.db.add_newtasks(new_title, new_time, new_date, new_description, priority)
            if feedback == True:
                self.read_from_database()
                self.ui.textbox_newtask_title.setText("")
                self.ui.textbox_newtask_time.setText("")
                self.ui.textbox_newtask_date.setText("")
                self.ui.textbox_newtask_description.setText("")
            else:
                msg_box = QMessageBox()
                msg_box.setText("مشکلی رخ داده است")    
                msg_box.exec_()

    def read_from_database(self):
        tasks = self.db.get_tasks()  #تابع گت تسکس در فایل دیتابیس موجود است
        for i in range(len(tasks)):
            new_checkbox = QCheckBox()
            new_label1 = QLabel()
            new_label1.setText(tasks[i][1])
            new_label2 = QLabel()
            new_label2.setText(tasks[i][2])
            # new_label2.setVisible(False)  #مخفی کردن دیسکریپشن
            new_label_time = QLabel()
            new_label_time.setText(tasks[i][5])
            new_label_date = QLabel()
            new_label_date.setText(tasks[i][6])
            remove_btn = QPushButton()
            remove_btn.setText("❌")
            remove_btn.setStyleSheet("background-color: red; border: 2px solid black; border-radius: 10px; width :2px")
            


            self.ui.grid_tasks.addWidget(new_checkbox, i, 0)

            if tasks[i][3] == 1:   #چک کردن تسک انجام شده یا انجام نشده
                new_checkbox.setChecked(True)
                new_label1.setStyleSheet("text-decoration: line-through")
                new_label2.setStyleSheet("text-decoration: line-through")
            else :
                new_checkbox.setChecked(False) 

            if tasks[i][4] == 1:   #چک کردن اولویت تسک  ها
                new_label1.setStyleSheet("color:red")
            else :
                new_label1.setStyleSheet("color:white")


                
            self.ui.grid_tasks.addWidget(new_label1, i, 1)
            self.ui.grid_tasks.addWidget(new_label2, i, 2)
            self.ui.grid_tasks.addWidget(new_label_time, i, 3)
            self.ui.grid_tasks.addWidget(new_label_date, i, 4)
            self.ui.grid_tasks.addWidget(remove_btn, i, 5)
            
            remove_btn.clicked.connect(partial(self.db.remove_task, tasks[i][0]))  # برای حذف تسک ها
            new_checkbox.clicked.connect(partial(self.db.task_done, tasks[i][0]))   #  تیک خوردن و برداشتن تیک تسک ها    
               
if __name__ == "__main__"  :      
    app = QApplication(sys.argv)    

    main_window = MainWindow()
    main_window.show()



app.exec()