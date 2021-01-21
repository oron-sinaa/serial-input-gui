# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_serialtBQouX.ui'
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
        self.drop_shadow_frame.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(42, 44, 111, 255), stop:0.583916 rgba(28, 29, 73, 255));\n"
"border-radius:15px;")
        self.drop_shadow_frame.setFrameShape(QFrame.NoFrame)
        self.drop_shadow_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.drop_shadow_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.title_bar = QFrame(self.drop_shadow_frame)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMaximumSize(QSize(16777215, 45))
        font = QFont()
        font.setStyleStrategy(QFont.PreferAntialias)
        self.title_bar.setFont(font)
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
        self.verticalLayout_5 = QVBoxLayout(self.frame_title)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(12, 0, 0, 0)
        self.label_title = QLabel(self.frame_title)
        self.label_title.setObjectName(u"label_title")
        font1 = QFont()
        font1.setFamily(u"Roboto Condensed")
        font1.setPointSize(12)
        font1.setStyleStrategy(QFont.PreferAntialias)
        self.label_title.setFont(font1)
        self.label_title.setStyleSheet(u"color:rgb(60, 231, 195)")

        self.verticalLayout_5.addWidget(self.label_title)

        self.line = QFrame(self.frame_title)
        self.line.setObjectName(u"line")
        self.line.setStyleSheet(u"border: 1px solid grey;")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)


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
        self.content_bar.setStyleSheet(u"")
        self.content_bar.setFrameShape(QFrame.StyledPanel)
        self.content_bar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.content_bar)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.group_serial_settings = QGroupBox(self.content_bar)
        self.group_serial_settings.setObjectName(u"group_serial_settings")
        self.group_serial_settings.setMaximumSize(QSize(16777215, 125))
        font2 = QFont()
        font2.setFamily(u"Lucida Console")
        font2.setPointSize(7)
        font2.setBold(False)
        font2.setWeight(50)
        font2.setStyleStrategy(QFont.PreferAntialias)
        self.group_serial_settings.setFont(font2)
        self.group_serial_settings.setStyleSheet(u"border: 2px solid rgb(85, 150, 127);\n"
"color: rgb(255, 170, 255);\n"
"border-radius:12px;\n"
"background-color: none;\n"
"")
        self.group_serial_settings.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.verticalLayout_4 = QVBoxLayout(self.group_serial_settings)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(20, 20, 20, 20)
        self.frame_for_settings = QFrame(self.group_serial_settings)
        self.frame_for_settings.setObjectName(u"frame_for_settings")
        self.frame_for_settings.setMaximumSize(QSize(16777215, 500))
        self.frame_for_settings.setStyleSheet(u"border:none; border-radius: 20px;background-color: none")
        self.frame_for_settings.setFrameShape(QFrame.StyledPanel)
        self.frame_for_settings.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_for_settings)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_com = QFrame(self.frame_for_settings)
        self.frame_com.setObjectName(u"frame_com")
        self.frame_com.setStyleSheet(u"background-color:none")
        self.frame_com.setFrameShape(QFrame.StyledPanel)
        self.frame_com.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_com)
        self.horizontalLayout_5.setSpacing(20)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, 25, -1)
        self.label_com_port = QLabel(self.frame_com)
        self.label_com_port.setObjectName(u"label_com_port")
        font3 = QFont()
        font3.setFamily(u"Dosis Light")
        font3.setPointSize(11)
        font3.setBold(False)
        font3.setWeight(50)
        self.label_com_port.setFont(font3)
        self.label_com_port.setStyleSheet(u"color: white")

        self.horizontalLayout_5.addWidget(self.label_com_port)

        self.combo_com_port = QComboBox(self.frame_com)
        self.combo_com_port.setObjectName(u"combo_com_port")
        self.combo_com_port.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_5.addWidget(self.combo_com_port)


        self.horizontalLayout_2.addWidget(self.frame_com, 0, Qt.AlignHCenter)

        self.frame_baud = QFrame(self.frame_for_settings)
        self.frame_baud.setObjectName(u"frame_baud")
        self.frame_baud.setStyleSheet(u"background-color:none")
        self.frame_baud.setFrameShape(QFrame.StyledPanel)
        self.frame_baud.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_baud)
        self.horizontalLayout_6.setSpacing(20)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, 25, -1)
        self.label_com_port_2 = QLabel(self.frame_baud)
        self.label_com_port_2.setObjectName(u"label_com_port_2")
        self.label_com_port_2.setFont(font3)
        self.label_com_port_2.setStyleSheet(u"background-color:none; color: white;")

        self.horizontalLayout_6.addWidget(self.label_com_port_2)

        self.combo_com_port_2 = QComboBox(self.frame_baud)
        self.combo_com_port_2.setObjectName(u"combo_com_port_2")
        self.combo_com_port_2.setMinimumSize(QSize(120, 0))

        self.horizontalLayout_6.addWidget(self.combo_com_port_2)


        self.horizontalLayout_2.addWidget(self.frame_baud, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.frame_for_settings)


        self.verticalLayout_3.addWidget(self.group_serial_settings)

        self.button_frame = QFrame(self.content_bar)
        self.button_frame.setObjectName(u"button_frame")
        self.button_frame.setMaximumSize(QSize(16777215, 40))
        self.button_frame.setStyleSheet(u"background:none")
        self.button_frame.setFrameShape(QFrame.StyledPanel)
        self.button_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.button_frame)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(50, 0, 50, 0)
        self.dummy_frame_2 = QFrame(self.button_frame)
        self.dummy_frame_2.setObjectName(u"dummy_frame_2")
        self.dummy_frame_2.setFrameShape(QFrame.StyledPanel)
        self.dummy_frame_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.dummy_frame_2)

        self.start_stop_button = QPushButton(self.button_frame)
        self.start_stop_button.setObjectName(u"start_stop_button")
        self.start_stop_button.setMaximumSize(QSize(200, 16777215))
        font4 = QFont()
        font4.setFamily(u"Bahnschrift SemiBold")
        font4.setPointSize(8)
        self.start_stop_button.setFont(font4)
        self.start_stop_button.setStyleSheet(u"border-color: rgb(60, 231, 195);\n"
"border-style: outset;\n"
"color:lightgrey;\n"
"border-width:2px;\n"
"border-radius: 12px;\n"
"background-color: rgb(50, 50, 100);\n"
"padding: 6px;")

        self.horizontalLayout_7.addWidget(self.start_stop_button)

        self.dummy_frame = QFrame(self.button_frame)
        self.dummy_frame.setObjectName(u"dummy_frame")
        self.dummy_frame.setFrameShape(QFrame.StyledPanel)
        self.dummy_frame.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.dummy_frame)


        self.verticalLayout_3.addWidget(self.button_frame)

        self.group_output = QGroupBox(self.content_bar)
        self.group_output.setObjectName(u"group_output")
        self.group_output.setMaximumSize(QSize(16777215, 400))
        self.group_output.setFont(font2)
        self.group_output.setStyleSheet(u"border: 1px solid rgb(85, 150, 127); ; color: rgb(255, 170, 255);border-radius:12px;\n"
"background-color: rgb(30, 30, 30);")
        self.group_output.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)
        self.group_output.setFlat(False)
        self.group_output.setCheckable(False)
        self.verticalLayout_6 = QVBoxLayout(self.group_output)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(15, 15, 15, 15)
        self.console_output = QTextBrowser(self.group_output)
        self.console_output.setObjectName(u"console_output")
        self.console_output.setStyleSheet(u"border: none;")

        self.verticalLayout_6.addWidget(self.console_output)


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
        font5 = QFont()
        font5.setFamily(u"Roboto Condensed Light")
        self.label_credits.setFont(font5)
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
        self.label_com_port.setText(QCoreApplication.translate("MainWindow", u"Set  Com  Port", None))
        self.label_com_port_2.setText(QCoreApplication.translate("MainWindow", u"Set  Baud  Rate", None))
        self.start_stop_button.setText(QCoreApplication.translate("MainWindow", u"START LISTENING", None))
        self.group_output.setTitle(QCoreApplication.translate("MainWindow", u"  OUTPUT WINDOW  ", None))
        self.console_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label_credits.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Orbit Technologies", None))
    # retranslateUi

