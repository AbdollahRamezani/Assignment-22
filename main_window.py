# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        if not mainWindow.objectName():
            mainWindow.setObjectName(u"mainWindow")
        mainWindow.resize(517, 563)
        mainWindow.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.grid_tasks = QGridLayout()
        self.grid_tasks.setObjectName(u"grid_tasks")

        self.verticalLayout.addLayout(self.grid_tasks)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textbox_newtask_title = QLineEdit(self.centralwidget)
        self.textbox_newtask_title.setObjectName(u"textbox_newtask_title")
        self.textbox_newtask_title.setStyleSheet(u"background-color: rgb(75, 150, 225);\n"
"color: rgb(240, 240, 240);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"")

        self.horizontalLayout.addWidget(self.textbox_newtask_title)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.textbox_newtask_description = QTextEdit(self.centralwidget)
        self.textbox_newtask_description.setObjectName(u"textbox_newtask_description")
        self.textbox_newtask_description.setStyleSheet(u"background-color: rgb(75, 150, 225);\n"
"color: rgb(240, 240, 240);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"")

        self.verticalLayout.addWidget(self.textbox_newtask_description)

        self.textbox_newtask_time = QLineEdit(self.centralwidget)
        self.textbox_newtask_time.setObjectName(u"textbox_newtask_time")
        self.textbox_newtask_time.setStyleSheet(u"background-color: rgb(75, 150, 225);\n"
"color: rgb(240, 240, 240);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"")

        self.verticalLayout.addWidget(self.textbox_newtask_time)

        self.textbox_newtask_date = QLineEdit(self.centralwidget)
        self.textbox_newtask_date.setObjectName(u"textbox_newtask_date")
        self.textbox_newtask_date.setStyleSheet(u"background-color: rgb(75, 150, 225);\n"
"color: rgb(240, 240, 240);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 7px;\n"
"")

        self.verticalLayout.addWidget(self.textbox_newtask_date)

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Snap ITC"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: rgb(85, 0, 127);")

        self.verticalLayout.addWidget(self.label)

        self.radioButton_important = QRadioButton(self.centralwidget)
        self.radioButton_important.setObjectName(u"radioButton_important")
        font1 = QFont()
        font1.setFamilies([u"Snap ITC"])
        self.radioButton_important.setFont(font1)
        self.radioButton_important.setStyleSheet(u"color: rgb(85, 85, 127);")
        self.radioButton_important.setChecked(False)

        self.verticalLayout.addWidget(self.radioButton_important)

        self.radioButton_normal = QRadioButton(self.centralwidget)
        self.radioButton_normal.setObjectName(u"radioButton_normal")
        self.radioButton_normal.setFont(font1)
        self.radioButton_normal.setStyleSheet(u"color: rgb(85, 85, 127);")
        self.radioButton_normal.setChecked(True)

        self.verticalLayout.addWidget(self.radioButton_normal)

        self.btn_newtask = QPushButton(self.centralwidget)
        self.btn_newtask.setObjectName(u"btn_newtask")
        self.btn_newtask.setFont(font)
        self.btn_newtask.setStyleSheet(u"background-color: rgb(75, 150, 225);\n"
"color: rgb(255, 255, 255);\n"
"border: 2px solid rgba(172, 172, 172, 0.33);\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 12px;")

        self.verticalLayout.addWidget(self.btn_newtask)

        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(mainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 517, 22))
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(mainWindow)
        self.statusbar.setObjectName(u"statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    # setupUi

    def retranslateUi(self, mainWindow):
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", u"ToDoList", None))
        self.textbox_newtask_title.setPlaceholderText(QCoreApplication.translate("mainWindow", u"insert Title", None))
        self.textbox_newtask_description.setPlaceholderText(QCoreApplication.translate("mainWindow", u"insert description", None))
        self.textbox_newtask_time.setPlaceholderText(QCoreApplication.translate("mainWindow", u"insert Time", None))
        self.textbox_newtask_date.setPlaceholderText(QCoreApplication.translate("mainWindow", u"insert Date", None))
        self.label.setText(QCoreApplication.translate("mainWindow", u"Priority", None))
        self.radioButton_important.setText(QCoreApplication.translate("mainWindow", u"Important", None))
        self.radioButton_normal.setText(QCoreApplication.translate("mainWindow", u"Normal", None))
        self.btn_newtask.setText(QCoreApplication.translate("mainWindow", u"Add Task", None))
    # retranslateUi

