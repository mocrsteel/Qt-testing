# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Testing-GUIgkDZcT.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 450)
        MainWindow.setMinimumSize(QSize(700, 450))
        MainWindow.setMaximumSize(QSize(700, 450))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("/*\n"
"Color palette:\n"
"Main: #F2F2F2\n"
"Main-shade: #A6A6A6\n"
"Accent-base: #F29F05\n"
"Accent-light: #F2A341\n"
"Accent-shade: #D9863D\n"
"Text: #545454\n"
"*/\n"
"\n"
"QMainWindow {\n"
"	color: #545454;\n"
"	background-color: #F2F2F2;\n"
"	border-radius: 50px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid #A6A6A6;\n"
"	border-radius: 16px;	\n"
"	padding: 6px;\n"
"	font: 12pt \"Calibri Light\";\n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"	border-color: #D9863D;\n"
"}\n"
"QLineEdit:focus {\n"
"	border-color: #D9863D;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #F29F05;\n"
"	border-radius: 16px;\n"
"	padding: 8px;\n"
"	font: 12pt \"Calibri Light\";\n"
"	color: #3D3D3D;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: #F2A341;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: #3D3D3D;\n"
"	font: 12pt \"Calibri Light\";\n"
"}\n"
"")
        MainWindow.setDocumentMode(True)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(True)
        self.actionSettings = QAction(MainWindow)
        self.actionSettings.setObjectName(u"actionSettings")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"Calibri Light")
        font.setPointSize(12)
        self.centralwidget.setFont(font)
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, -3, 701, 281))
        self.ContentVertical = QVBoxLayout(self.verticalLayoutWidget)
        self.ContentVertical.setObjectName(u"ContentVertical")
        self.ContentVertical.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.ContentVertical.setContentsMargins(60, 50, 60, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lblSelectedFile = QLabel(self.verticalLayoutWidget)
        self.lblSelectedFile.setObjectName(u"lblSelectedFile")

        self.horizontalLayout.addWidget(self.lblSelectedFile)

        self.btnSelectFile = QPushButton(self.verticalLayoutWidget)
        self.btnSelectFile.setObjectName(u"btnSelectFile")

        self.horizontalLayout.addWidget(self.btnSelectFile)


        self.ContentVertical.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.lblOutputFolder = QLabel(self.verticalLayoutWidget)
        self.lblOutputFolder.setObjectName(u"lblOutputFolder")

        self.horizontalLayout_3.addWidget(self.lblOutputFolder)

        self.btnSelectFolder = QPushButton(self.verticalLayoutWidget)
        self.btnSelectFolder.setObjectName(u"btnSelectFolder")

        self.horizontalLayout_3.addWidget(self.btnSelectFolder)


        self.ContentVertical.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.lineEditOutputFileName = QLineEdit(self.verticalLayoutWidget)
        self.lineEditOutputFileName.setObjectName(u"lineEditOutputFileName")

        self.horizontalLayout_2.addWidget(self.lineEditOutputFileName)


        self.ContentVertical.addLayout(self.horizontalLayout_2)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(-1, 280, 701, 121))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(100, -1, 100, -1)
        self.label_6 = QLabel(self.verticalLayoutWidget_2)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_4.addWidget(self.label_6, 0, Qt.AlignLeft)

        self.lblReportStatus = QLabel(self.verticalLayoutWidget_2)
        self.lblReportStatus.setObjectName(u"lblReportStatus")

        self.horizontalLayout_4.addWidget(self.lblReportStatus)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.ButtonsHorizontal = QHBoxLayout()
        self.ButtonsHorizontal.setObjectName(u"ButtonsHorizontal")
        self.ButtonsHorizontal.setContentsMargins(100, -1, 100, -1)
        self.btnLoadFile = QPushButton(self.verticalLayoutWidget_2)
        self.btnLoadFile.setObjectName(u"btnLoadFile")

        self.ButtonsHorizontal.addWidget(self.btnLoadFile)

        self.btnPreviewOutput = QPushButton(self.verticalLayoutWidget_2)
        self.btnPreviewOutput.setObjectName(u"btnPreviewOutput")

        self.ButtonsHorizontal.addWidget(self.btnPreviewOutput)

        self.btnSaveReport = QPushButton(self.verticalLayoutWidget_2)
        self.btnSaveReport.setObjectName(u"btnSaveReport")

        self.ButtonsHorizontal.addWidget(self.btnSaveReport)


        self.verticalLayout.addLayout(self.ButtonsHorizontal)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 700, 22))
        self.menuProgram = QMenu(self.menubar)
        self.menuProgram.setObjectName(u"menuProgram")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuProgram.menuAction())
        self.menuProgram.addAction(self.actionSettings)
        self.menuProgram.addAction(self.actionAbout)
        self.menuProgram.addSeparator()
        self.menuProgram.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", "Test Application", None))
        self.actionSettings.setText(QCoreApplication.translate("MainWindow", "Preferences...", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", "Exit", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", "About", None))
        self.label.setText(QCoreApplication.translate("MainWindow", "Currently selected input file: ", None))
        self.lblSelectedFile.setText(QCoreApplication.translate("MainWindow", "No file selected...", None))
        self.btnSelectFile.setText(QCoreApplication.translate("MainWindow", "Select File", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", "Current output folder:", None))
        self.lblOutputFolder.setText(QCoreApplication.translate("MainWindow", "output/folder/from/config", None))
        self.btnSelectFolder.setText(QCoreApplication.translate("MainWindow", "Select Output Folder", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", "File Output file name: ", None))
        self.lineEditOutputFileName.setPlaceholderText(QCoreApplication.translate("MainWindow", "Please enter the desired file name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", "Report status: ", None))
        self.lblReportStatus.setText(QCoreApplication.translate("MainWindow", "Input file not loaded.", None))
        self.btnLoadFile.setText(QCoreApplication.translate("MainWindow", "Load File", None))
        self.btnPreviewOutput.setText(QCoreApplication.translate("MainWindow", "Preview output", None))
        self.btnSaveReport.setText(QCoreApplication.translate("MainWindow", "Save Report", None))
        self.menuProgram.setTitle(QCoreApplication.translate("MainWindow", "Program", None))
    # retranslateUi

