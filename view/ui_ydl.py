# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ydl.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setStyleSheet("QPushButton {\n"
                                 "height: 30px;\n"
                                 "width: 30px;\n"
                                 "margin: 0px 0px;\n"
                                 "border: 1px solid #8f8f91;\n"
                                 "border-radius: 5px;\n"
                                 "background-color: transparent;\n"
                                 "color: rgba(0, 0, 0, 0.87);\n"
                                 "}\n"
                                 "QPushButton:hover, QPushButton:focus {\n"
                                 " background-color: rgba(208,208,208,1);\n"
                                 "}\n"
                                 "QTabWidget::pane { /* The tab widget frame */\n"
                                 "    \n"
                                 "}\n"
                                 "\n"
                                 "QTabWidget::tab-bar {\n"
                                 "    alignment: center;\n"
                                 "}\n"
                                 "\n"
                                 "/* Style the tab using the tab sub-control. Note that\n"
                                 "    it reads QTabBar _not_ QTabWidget */\n"
                                 "QTabBar::tab {\n"
                                 "    background-color: white;\n"
                                 "    border: 2px solid #C4C4C3;\n"
                                 "    border-bottom-color: #C2C7CB; /* same as the pane color */\n"
                                 "    min-width: 8ex;\n"
                                 "    padding: 2px;\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected, QTabBar::tab:hover {\n"
                                 "    background-color: rgba(208,208,208,1);\n"
                                 "}\n"
                                 "\n"
                                 "QTabBar::tab:selected {\n"
                                 "    border-color: #9B9B9B;\n"
                                 "    border-bottom-color: #C2C7CB; /* same as pane color */\n"
                                 "    margin-left: -2px;\n"
                                 "    margin-right: -2px;\n"
                                 "}\n"
                                 "QTabBar::tab:!selected {\n"
                                 "    margin-top: 3px; /* make non-selected tabs look smaller */\n"
                                 "}\n"
                                 "QTabBar::tab:first:selected {\n"
                                 "    margin-left: 0; /* the first selected tab has nothing to overlap with on the left */\n"
                                 "}\n"
                                 "QTabBar::tab:last:selected {\n"
                                 "    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
                                 "}\n"
                                 "QTabBar::tab:only-one {\n"
                                 "    margin: 0; /* if there is only one tab, we don\'t want overlapping margins */\n"
                                 "}\n"
                                 "QProgressBar {\n"
                                 "    border: 2px solid grey;\n"
                                 "    border-radius: 10px;\n"
                                 "    margin: 5px 5px;\n"
                                 "    padding: 0 0;\n"
                                 " }\n"
                                 "QProgressBar::chunk {\n"
                                 "    background-color: grey;\n"
                                 "    width: 25px;\n"
                                 "    radius: 5px;\n"
                                 "}\n"
                                 "QStatusBar::item { \n"
                                 "    border: 0px solid black };")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ydl_icon/plus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addBtn.setIcon(icon)
        self.addBtn.setAutoDefault(False)
        self.addBtn.setFlat(False)
        self.addBtn.setObjectName("addBtn")
        self.horizontalLayout.addWidget(self.addBtn)
        self.removeBtn = QtWidgets.QPushButton(self.centralwidget)
        self.removeBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/ydl_icon/minus.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.removeBtn.setIcon(icon1)
        self.removeBtn.setObjectName("removeBtn")
        self.horizontalLayout.addWidget(self.removeBtn)
        self.downloadBtn = QtWidgets.QPushButton(self.centralwidget)
        self.downloadBtn.setToolTipDuration(-1)
        self.downloadBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ydl_icon/download.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.downloadBtn.setIcon(icon2)
        self.downloadBtn.setObjectName("downloadBtn")
        self.horizontalLayout.addWidget(self.downloadBtn)
        self.refreshBtn = QtWidgets.QPushButton(self.centralwidget)
        self.refreshBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/ydl_icon/refresh.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.refreshBtn.setIcon(icon3)
        self.refreshBtn.setObjectName("refreshBtn")
        self.horizontalLayout.addWidget(self.refreshBtn)
        self.clipboardBtn = QtWidgets.QPushButton(self.centralwidget)
        self.clipboardBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/ydl_icon/clipboard-text.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clipboardBtn.setIcon(icon4)
        self.clipboardBtn.setObjectName("clipboardBtn")
        self.horizontalLayout.addWidget(self.clipboardBtn)
        self.startBtn = QtWidgets.QPushButton(self.centralwidget)
        self.startBtn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/ydl_icon/play.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.startBtn.setIcon(icon5)
        self.startBtn.setObjectName("startBtn")
        self.horizontalLayout.addWidget(self.startBtn)
        self.pauseBtn = QtWidgets.QPushButton(self.centralwidget)
        self.pauseBtn.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/ydl_icon/pause.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pauseBtn.setIcon(icon6)
        self.pauseBtn.setObjectName("pauseBtn")
        self.horizontalLayout.addWidget(self.pauseBtn)
        self.stopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.stopBtn.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/ydl_icon/stop.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.stopBtn.setIcon(icon7)
        self.stopBtn.setObjectName("stopBtn")
        self.horizontalLayout.addWidget(self.stopBtn)
        self.settingsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.settingsBtn.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/ydl_icon/settings.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.settingsBtn.setIcon(icon8)
        self.settingsBtn.setObjectName("settingsBtn")
        self.horizontalLayout.addWidget(self.settingsBtn)
        spacerItem = QtWidgets.QSpacerItem(86, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setObjectName("tabWidget")
        self.DownloadTab = QtWidgets.QWidget()
        self.DownloadTab.setObjectName("DownloadTab")
        self.gridLayout = QtWidgets.QGridLayout(self.DownloadTab)
        self.gridLayout.setObjectName("gridLayout")
        self.downloadView = QtWidgets.QTreeView(self.DownloadTab)
        self.downloadView.setObjectName("downloadView")
        self.gridLayout.addWidget(self.downloadView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.DownloadTab, "")
        self.pendingTab = QtWidgets.QWidget()
        self.pendingTab.setObjectName("pendingTab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.pendingTab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pendingView = QtWidgets.QTreeView(self.pendingTab)
        self.pendingView.setObjectName("pendingView")
        self.gridLayout_2.addWidget(self.pendingView, 0, 0, 1, 1)
        self.tabWidget.addTab(self.pendingTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.addBtn.setToolTip(_translate("MainWindow", "Add download"))
        self.removeBtn.setToolTip(_translate("MainWindow", "Remove download"))
        self.downloadBtn.setToolTip(_translate("MainWindow", "Start all Downloads"))
        self.refreshBtn.setToolTip(_translate("MainWindow", "Refresh"))
        self.clipboardBtn.setToolTip(_translate("MainWindow", "Add from Clipboard"))
        self.startBtn.setToolTip(_translate("MainWindow", "Start Download"))
        self.pauseBtn.setToolTip(_translate("MainWindow", "Pause Download"))
        self.stopBtn.setToolTip(_translate("MainWindow", "Stop Download"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DownloadTab), _translate("MainWindow", "Downloads"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.pendingTab), _translate("MainWindow", "Pending"))

