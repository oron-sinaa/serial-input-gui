# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_serial_bkpWVfVEc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(880, 600)
        icon = QIcon()
        icon.addFile(u"img/serialplot.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.drop_shadow_layout = QVBoxLayout(self.centralwidget)
        self.drop_shadow_layout.setSpacing(0)
        self.drop_shadow_layout.setObjectName(u"drop_shadow_layout")
        self.drop_shadow_layout.setContentsMargins(10, 10, 10, 10)
        self.drop_shadow_frame = QFrame(self.centralwidget)
        self.drop_shadow_frame.setObjectName(u"drop_shadow_frame")
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 29, 48, 255), stop:1 rgba(0, 72, 116, 255));\n"
"border-radius:10px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 40))
        self.title_bar.setStyleSheet(u"background-color:none")
        self.title_bar.setFrameShape(QFrame.NoFrame)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 7, 0, 0)
        self.frame_title = QFrame(self.title_bar)
        self.frame_title.setObjectName(u"frame_title")
        self.frame_title.setFrameShape(QFrame.StyledPanel)
        self.frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_title)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font = QFont()
        font.setFamily(u"Roboto Condensed")
        font.setPointSize(12)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet(u"color:rgb(60, 231, 195)")

        self.horizontalLayout_2.addWidget(self.label_title)


        self.horizontalLayout.addWidget(self.frame_title)

        self.frame_btns = QFrame(self.title_bar)
        self.frame_btns.setObjectName(u"frame_btns")
        self.frame_btns.setMaximumSize(QSize(100, 16777215))
        self.frame_btns.setFrameShape(QFrame.StyledPanel)
        self.frame_btns.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_btns)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 10, -1, -1)
        self.btn_minimize = QPushButton(self.frame_btns)
        self.btn_minimize.setObjectName(u"btn_minimize")
        self.btn_minimize.setMinimumSize(QSize(16, 16))
        self.btn_minimize.setMaximumSize(QSize(17, 17))
        self.btn_minimize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(85, 255, 127);\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(85, 255, 127, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_minimize)

        self.btn_maximize = QPushButton(self.frame_btns)
        self.btn_maximize.setObjectName(u"btn_maximize")
        self.btn_maximize.setMinimumSize(QSize(16, 16))
        self.btn_maximize.setMaximumSize(QSize(17, 17))
        self.btn_maximize.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	\n"
"	background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(255, 170, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_maximize)

        self.btn_close = QPushButton(self.frame_btns)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(16, 16))
        self.btn_close.setMaximumSize(QSize(17, 17))
        self.btn_close.setStyleSheet(u"QPushButton {\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {\n"
"	\n"
"	background-color: rgba(255, 0, 0, 150);\n"
"}")

        self.horizontalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout.addWidget(self.frame_btns, 0, Qt.AlignVCenter)


        self.verticalLayout.addWidget(self.title_bar)

        self.content_bar = QFrame(self.drop_shadow_frame)
        self.content_bar.setObjectName(u"content_bar")
        self.content_bar.setStyleSheet(u"background-color:none")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_bar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.line = QFrame(self.content_bar)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: 1px solid grey;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line)

        self.group_serial_settings = QGroupBox(self.content_bar)
        self.group_serial_settings.setObjectName(u"group_serial_settings")
        font1 = QFont()
        font1.setFamily(u"Lucida Console")
        font1.setPointSize(7)
        font1.setBold(False)
        font1.setWeight(50)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.group_serial_settings.setFont(font1)
        self.group_serial_settings.setStyleSheet(u"border: 1px solid rgb(85, 150, 127); ; color: rgb(255, 170, 255);\n"
"border-radius:5px;\n"
"")
        self.group_serial_settings.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.com_port = QLabel(self.group_serial_settings)
        self.com_port.setObjectName(u"com_port")
        self.com_port.setGeometry(QRect(70, 60, 121, 16))
        self.com_port.setStyleSheet(u"border: none")
        self.baud_rate = QLabel(self.group_serial_settings)
        self.baud_rate.setObjectName(u"baud_rate")
        self.baud_rate.setGeometry(QRect(470, 60, 131, 16))
        self.baud_rate.setStyleSheet(u"border: none")
        self.comboBox = QComboBox(self.group_serial_settings)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(200, 60, 101, 22))
        self.comboBox_2 = QComboBox(self.group_serial_settings)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(590, 60, 101, 22))

        self.verticalLayout_3.addWidget(self.group_serial_settings)

        self.group_output = QGroupBox(self.content_bar)
        self.group_output.setObjectName(u"group_output")
        self.group_output.setFont(font1)
        self.group_output.setStyleSheet(u"border: 1px solid rgb(85, 150, 127); ; color: rgb(255, 170, 255);border-radius:5px;")
        self.group_output.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.group_output.setFlat(False)
        self.group_output.setCheckable(False)

        self.verticalLayout_3.addWidget(self.group_output)


        self.verticalLayout.addWidget(self.content_bar)

        self.credits_bar = QFrame(self.drop_shadow_frame)
        self.credits_bar.setObjectName(u"credits_bar")
        self.credits_bar.setMaximumSize(QSize(16777215, 30))
        self.credits_bar.setStyleSheet(u"background-color:none")
        self.credits_bar.setFrameShape(QFrame.NoFrame)
        self.credits_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.credits_bar)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_label_credits = QFrame(self.credits_bar)
        self.frame_label_credits.setObjectName(u"frame_label_credits")
        self.frame_label_credits.setFrameShape(QFrame.StyledPanel)
        self.frame_label_credits.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_label_credits)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(15, 0, 0, 0)
        self.label_credits = QLabel(self.frame_label_credits)
        self.label_credits.setObjectName(u"label_credits")
        font2 = QFont()
        font2.setFamily(u"Roboto Condensed Light")
        self.label_credits.setFont(font2)
        self.label_credits.setStyleSheet(u"color: rgb(140, 112, 184);")

        self.verticalLayout_2.addWidget(self.label_credits)


        self.horizontalLayout_4.addWidget(self.frame_label_credits)

        self.frame_grip = QFrame(self.credits_bar)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(30, 30))
        self.frame_grip.setMaximumSize(QSize(30, 30))
        self.frame_grip.setStyleSheet(u"padding: 5px;")
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.credits_bar)


        self.drop_shadow_layout.addWidget(self.drop_shadow_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Serial Reader", None))
        self.label_title.setText(QCoreApplication.translate("MainWindow", u"Serial Reader", None))
#if QT_CONFIG(tooltip)
        self.btn_minimize.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_minimize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_maximize.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.btn_maximize.setText("")
#if QT_CONFIG(tooltip)
        self.btn_close.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.btn_close.setText("")
        self.group_serial_settings.setTitle(QCoreApplication.translate("MainWindow", u"  SERIAL SETTINGS  ", None))
        self.com_port.setText(QCoreApplication.translate("MainWindow", u"Set COM Port", None))
        self.baud_rate.setText(QCoreApplication.translate("MainWindow", u"Set Baud Rate", None))
        self.group_output.setTitle(QCoreApplication.translate("MainWindow", u"  OUTPUT WINDOW  ", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Orbit Technologies", None))
    # retranslateUi

