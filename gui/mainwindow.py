# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(493, 466)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../assets/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.globalMessage = QtWidgets.QFrame(self.centralwidget)
        self.globalMessage.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.globalMessage.setFrameShadow(QtWidgets.QFrame.Raised)
        self.globalMessage.setObjectName("globalMessage")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.globalMessage)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.globalMessageTitle = QtWidgets.QLabel(self.globalMessage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.globalMessageTitle.setFont(font)
        self.globalMessageTitle.setText("")
        self.globalMessageTitle.setObjectName("globalMessageTitle")
        self.verticalLayout_2.addWidget(self.globalMessageTitle)
        self.globalMessageText = QtWidgets.QLabel(self.globalMessage)
        self.globalMessageText.setText("")
        self.globalMessageText.setOpenExternalLinks(True)
        self.globalMessageText.setObjectName("globalMessageText")
        self.verticalLayout_2.addWidget(self.globalMessageText)
        self.verticalLayout.addWidget(self.globalMessage)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.South)
        self.tabWidget.setObjectName("tabWidget")
        self.programmingTab = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.programmingTab.sizePolicy().hasHeightForWidth())
        self.programmingTab.setSizePolicy(sizePolicy)
        self.programmingTab.setObjectName("programmingTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.programmingTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.programmingTab)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 3, 0, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.programmingTab)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout_2.addWidget(self.progressBar, 5, 0, 1, 2)
        self.versionBox = QtWidgets.QComboBox(self.programmingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.versionBox.sizePolicy().hasHeightForWidth())
        self.versionBox.setSizePolicy(sizePolicy)
        self.versionBox.setEditable(True)
        self.versionBox.setObjectName("versionBox")
        self.gridLayout_2.addWidget(self.versionBox, 3, 1, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uploadButton = QtWidgets.QPushButton(self.programmingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.uploadButton.sizePolicy().hasHeightForWidth())
        self.uploadButton.setSizePolicy(sizePolicy)
        self.uploadButton.setObjectName("uploadButton")
        self.horizontalLayout.addWidget(self.uploadButton)
        self.eraseButton = QtWidgets.QPushButton(self.programmingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.eraseButton.sizePolicy().hasHeightForWidth())
        self.eraseButton.setSizePolicy(sizePolicy)
        self.eraseButton.setObjectName("eraseButton")
        self.horizontalLayout.addWidget(self.eraseButton)
        self.expertModeBox = QtWidgets.QCheckBox(self.programmingTab)
        self.expertModeBox.setCheckable(True)
        self.expertModeBox.setObjectName("expertModeBox")
        self.horizontalLayout.addWidget(self.expertModeBox)
        self.gridLayout_2.addLayout(self.horizontalLayout, 6, 0, 1, 2)
        self.boardBox = QtWidgets.QComboBox(self.programmingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.boardBox.sizePolicy().hasHeightForWidth())
        self.boardBox.setSizePolicy(sizePolicy)
        self.boardBox.setObjectName("boardBox")
        self.gridLayout_2.addWidget(self.boardBox, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.programmingTab)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.expertForm = QtWidgets.QWidget(self.programmingTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.expertForm.sizePolicy().hasHeightForWidth())
        self.expertForm.setSizePolicy(sizePolicy)
        self.expertForm.setObjectName("expertForm")
        self.formLayout_2 = QtWidgets.QFormLayout(self.expertForm)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_3 = QtWidgets.QLabel(self.expertForm)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.comboBox = QtWidgets.QComboBox(self.expertForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox)
        self.textBrowser = QtWidgets.QTextBrowser(self.expertForm)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.textBrowser.sizePolicy().hasHeightForWidth())
        self.textBrowser.setSizePolicy(sizePolicy)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.textBrowser)
        self.gridLayout_2.addWidget(self.expertForm, 7, 0, 1, 2)
        self.gridLayout_2.setRowStretch(7, 1)
        self.tabWidget.addTab(self.programmingTab, "")
        self.discoveryTab = QtWidgets.QWidget()
        self.discoveryTab.setObjectName("discoveryTab")
        self.gridLayout = QtWidgets.QGridLayout(self.discoveryTab)
        self.gridLayout.setObjectName("gridLayout")
        self.discoveryList = QtWidgets.QListWidget(self.discoveryTab)
        self.discoveryList.setObjectName("discoveryList")
        self.gridLayout.addWidget(self.discoveryList, 3, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.discoveryTab)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 2)
        self.label_4 = QtWidgets.QLabel(self.discoveryTab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)
        self.discoveryRefreshButton = QtWidgets.QPushButton(self.discoveryTab)
        self.discoveryRefreshButton.setObjectName("discoveryRefreshButton")
        self.gridLayout.addWidget(self.discoveryRefreshButton, 1, 1, 1, 1)
        self.tabWidget.addTab(self.discoveryTab, "")
        self.serialTab = QtWidgets.QWidget()
        self.serialTab.setObjectName("serialTab")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.serialTab)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.serialTextEdit = QtWidgets.QTextEdit(self.serialTab)
        self.serialTextEdit.setObjectName("serialTextEdit")
        self.gridLayout_4.addWidget(self.serialTextEdit, 2, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.serialTab)
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName("label_9")
        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 1)
        self.serialConnectButton = QtWidgets.QPushButton(self.serialTab)
        self.serialConnectButton.setCheckable(True)
        self.serialConnectButton.setObjectName("serialConnectButton")
        self.gridLayout_4.addWidget(self.serialConnectButton, 1, 0, 1, 1)
        self.tabWidget.addTab(self.serialTab, "")
        self.aboutTab = QtWidgets.QWidget()
        self.aboutTab.setObjectName("aboutTab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.aboutTab)
        self.gridLayout_3.setSpacing(12)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.buildLabel = QtWidgets.QLabel(self.aboutTab)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.buildLabel.setFont(font)
        self.buildLabel.setObjectName("buildLabel")
        self.gridLayout_3.addWidget(self.buildLabel, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.aboutTab)
        self.label_6.setMaximumSize(QtCore.QSize(64, 64))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../assets/logo.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.aboutTab)
        self.label_8.setTextFormat(QtCore.Qt.RichText)
        self.label_8.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_8.setWordWrap(True)
        self.label_8.setOpenExternalLinks(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 2, 0, 1, 2)
        self.tabWidget.addTab(self.aboutTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 493, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sensor.Community - Airrohr Flasher (v{version})"))
        self.label_2.setText(_translate("MainWindow", "Firmware version:"))
        self.uploadButton.setText(_translate("MainWindow", "Upload"))
        self.eraseButton.setText(_translate("MainWindow", "Erase Flash"))
        self.expertModeBox.setText(_translate("MainWindow", "Expert mode"))
        self.label.setText(_translate("MainWindow", "Board:"))
        self.label_3.setText(_translate("MainWindow", "Baudrate:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.programmingTab), _translate("MainWindow", "Flashing"))
        self.label_5.setText(_translate("MainWindow", "Double-click to open configuration page."))
        self.label_4.setText(_translate("MainWindow", "Sensors detected in local network:"))
        self.discoveryRefreshButton.setText(_translate("MainWindow", "Refresh"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.discoveryTab), _translate("MainWindow", "Discovery"))
        self.label_9.setText(_translate("MainWindow", "In case of sensor issues, Serial Monitor can be used to review logs sent by the sensor over USB cable."))
        self.serialConnectButton.setText(_translate("MainWindow", "Connect"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.serialTab), _translate("MainWindow", "Serial Monitor"))
        self.buildLabel.setText(_translate("MainWindow", "<b>Sensor.Community Airrohr Flasher</b><br/>Build {build_id}"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Developed by <a href=\"https://inf.re/\"><span style=\" text-decoration: underline; color:#0000ff;\">Piotr Dobrowolski</span></a>.</p><p>This software is released under the terms of MIT license. No warranty is provided.</p><p>For newest release see: <a href=\"https://d.inf.re/luftdaten/\"><span style=\" text-decoration: underline; color:#0000ff;\">https://d.inf.re/luftdaten/</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aboutTab), _translate("MainWindow", "About"))
