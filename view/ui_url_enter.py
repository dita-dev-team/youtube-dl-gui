# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_url_enter.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(557, 146)
        Dialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        Dialog.setStyleSheet("QLineEdit {\n"
                             "    border: 2px solid #8f8f91;\n"
                             "    border-radius: 10px;\n"
                             "    padding: 0 0;\n"
                             "    background: white;\n"
                             "    selection-background-color: darkgray;\n"
                             "}\n"
                             "QPushButton {\n"
                             "    height: 30px;\n"
                             "    width: 30px;\n"
                             "    margin: 0px 0px;\n"
                             "    border: 1px solid #8f8f91;\n"
                             "    border-radius: 5px;\n"
                             "    background-color: transparent;\n"
                             "    color: rgba(0, 0, 0, 0.87);\n"
                             "}\n"
                             "QPushButton:hover, QPushButton:focus {\n"
                             "    background-color: rgba(208,208,208,1);\n"
                             "}\n"
                             "QProgressBar {\n"
                             "    border: 2px solid grey;\n"
                             "    border-radius: 10px;\n"
                             "    margin: 5px 5px;\n"
                             "    padding: 0 0;\n"
                             "}\n"
                             "QProgressBar::chunk {\n"
                             "    background-color: grey;\n"
                             "    width: 25px;\n"
                             "    radius: 5px;\n"
                             "}")
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/ydl_icon/link.svg"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.goBtn = QtWidgets.QPushButton(Dialog)
        self.goBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ydl_icon/go.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goBtn.setIcon(icon)
        self.goBtn.setObjectName("goBtn")
        self.horizontalLayout.addWidget(self.goBtn)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        self.progressBar.setMaximumSize(QtCore.QSize(16777215, 30))
        self.progressBar.setMaximum(0)
        self.progressBar.setProperty("value", -1)
        self.progressBar.setOrientation(QtCore.Qt.Horizontal)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_2.addWidget(self.progressBar)
        spacerItem1 = QtWidgets.QSpacerItem(78, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Enter Url"))
        self.lineEdit.setPlaceholderText(_translate("Dialog", "Download Link..."))

