from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QDialog
from PyQt5.QtCore import pyqtSlot

from controller.url_enter import AddUrl
from view.ui_ydl import Ui_Dialog


class YoutubeDLGui(QDialog):
    def __init__(self):
        super(YoutubeDLGui, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.model = QStandardItemModel(0, 5, self)
        self.model.setHeaderData(0, QtCore.Qt.Horizontal, 'Name')
        self.model.setHeaderData(1, QtCore.Qt.Horizontal, 'Progress')
        self.model.setHeaderData(2, QtCore.Qt.Horizontal, 'Size')
        self.model.setHeaderData(3, QtCore.Qt.Horizontal, 'ETA')
        self.model.setHeaderData(4, QtCore.Qt.Horizontal, 'Speed')
        self.ui.downloadView.setModel(self.model)

    @pyqtSlot()
    def on_addBtn_clicked(self):
        self.add_url = AddUrl()
        self.add_url.show()

