# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!


# Code within sections was not generated from qtdesigner, it will have to be added
# back in if a new file is generated

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):   
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        
        self.mainVerticalLayout = QtWidgets.QVBoxLayout()
        self.mainVerticalLayout.setObjectName("mainVerticalLayout")
        
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(450, 300))
        self.widget.setObjectName("widget")        
        self.mainVerticalLayout.addWidget(self.widget)
        
        self.verticalLayoutVariablesConsole = QtWidgets.QVBoxLayout()
        self.verticalLayoutVariablesConsole.setObjectName("verticalLayoutVariablesConsole")
        
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setMaximumSize(QtCore.QSize(16777215, 1677215))
        self.textBrowser.setObjectName("textBrowser")
        
        self.verticalLayoutVariablesConsole.addWidget(self.textBrowser)
        
        self.horizontalLayoutSettings = QtWidgets.QHBoxLayout()
        self.horizontalLayoutSettings.setObjectName("horizontalLayoutSettings")
        
        self.loadDatabasesButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadDatabasesButton.setObjectName("loadDatabasesButton")
        self.horizontalLayoutSettings.addWidget(self.loadDatabasesButton)

        
        self.setVariablesButton = QtWidgets.QPushButton(self.centralwidget)
        self.setVariablesButton.setObjectName("setVariablesButton")
        self.horizontalLayoutSettings.addWidget(self.setVariablesButton)
        
        
        self.verticalLayoutVariablesConsole.addLayout(self.horizontalLayoutSettings)
        self.mainVerticalLayout.addLayout(self.verticalLayoutVariablesConsole)
        
        self.horizontalLayoutGraphics = QtWidgets.QHBoxLayout()
        self.horizontalLayoutGraphics.setObjectName("horizontalLayoutGraphics")
        self.mainVerticalLayout.addLayout(self.horizontalLayoutGraphics)
        self.horizontalLayoutProgress = QtWidgets.QHBoxLayout()
        self.horizontalLayoutProgress.setObjectName("horizontalLayoutProgress")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayoutProgress.addWidget(self.progressBar)
        
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        self.startButton.setObjectName("startButton")
        
        
        self.horizontalLayoutProgress.addWidget(self.startButton)
        self.mainVerticalLayout.addLayout(self.horizontalLayoutProgress)
        self.verticalLayout_3.addLayout(self.mainVerticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGitHub = QtWidgets.QAction(MainWindow)
        self.actionGitHub.setObjectName("actionGitHub")
        self.actionTeam_Site = QtWidgets.QAction(MainWindow)
        self.actionTeam_Site.setObjectName("actionTeam_Site")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionLoad_Settings = QtWidgets.QAction(MainWindow)
        self.actionLoad_Settings.setObjectName("actionLoad_Settings")
        self.actionSave_Settings = QtWidgets.QAction(MainWindow)
        self.actionSave_Settings.setObjectName("actionSave_Settings")
        self.actionLoad_Databases = QtWidgets.QAction(MainWindow)
        self.actionLoad_Databases.setObjectName("actionLoad_Databases")
        self.actionSet_Variables = QtWidgets.QAction(MainWindow)
        self.actionSet_Variables.setObjectName("actionSet_Variables")
        self.menuFile.addAction(self.actionLoad_Settings)
        self.menuFile.addAction(self.actionSave_Settings)
        self.menuFile.addAction(self.actionLoad_Databases)
        self.menuFile.addAction(self.actionSet_Variables)
        self.menuAbout.addAction(self.actionGitHub)
        self.menuAbout.addAction(self.actionTeam_Site)
        self.menuAbout.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "OpenThrust"))
        self.loadDatabasesButton.setText(_translate("MainWindow", "Load Datbases"))
        self.setVariablesButton.setText(_translate("MainWindow", "Set Variables"))
        self.startButton.setText(_translate("MainWindow", "Start"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.actionGitHub.setText(_translate("MainWindow", "GitHub"))
        self.actionTeam_Site.setText(_translate("MainWindow", "Team Site"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionLoad_Settings.setText(_translate("MainWindow", "Load Settings"))
        self.actionSave_Settings.setText(_translate("MainWindow", "Save Settings"))
        self.actionLoad_Databases.setText(_translate("MainWindow", "Load Databases"))
        self.actionSet_Variables.setText(_translate("MainWindow", "Set Variables"))
