import logging

import validators

from PyQt5 import QtCore
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QComboBox, QMessageBox, QMainWindow, QProgressBar, QLabel, QWidget, QHBoxLayout, QFrame
from PyQt5.QtCore import pyqtSlot, QItemSelectionModel

from controller.center import Center
from controller.info_parser import InfoParser
from controller.worker import WorkerBuilder
from model.ydl_logger import YDLLogger
from view.custom_widgets import CustomInputDialog, CustomToolTipDelegate
from view.ui_ydl import Ui_MainWindow
import view.ydl_qui


class YoutubeDLGui(QMainWindow):
    def __init__(self):
        super(YoutubeDLGui, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        Center(self)
        self.download_model = QStandardItemModel(0, 5, self)
        self.download_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Name')
        self.download_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Progress')
        self.download_model.setHeaderData(2, QtCore.Qt.Horizontal, 'Size')
        self.download_model.setHeaderData(3, QtCore.Qt.Horizontal, 'ETA')
        self.download_model.setHeaderData(4, QtCore.Qt.Horizontal, 'Speed')
        self.ui.downloadView.setModel(self.download_model)
        self.pending_model = QStandardItemModel(0, 2, self)
        self.pending_model.setHeaderData(0, QtCore.Qt.Horizontal, 'Name')
        self.pending_model.setHeaderData(1, QtCore.Qt.Horizontal, 'Quality')
        self.ui.pendingView.setModel(self.pending_model)
        self.ui.pendingView.setItemDelegate(CustomToolTipDelegate(self.ui.pendingView))
        self.init_status_bar()
        self.parsing_worker = WorkerBuilder.build(bool)
        self.pending_list = []

    def init_status_bar(self):
        self.pending_progressbar = QProgressBar()
        self.pending_progressbar.setFixedHeight(20)
        self.pending_progressbar.setFixedWidth(150)
        self.pending_progressbar.setMaximum(0)
        self.pending_progressbar.setMinimum(0)
        self.pending_label = QLabel("")
        self.pending_label.setAlignment(QtCore.Qt.AlignLeading)
        self.pending_label.setFixedWidth(220)
        font = self.pending_label.font()
        font.setPointSize(10)
        self.pending_label.setFont(font)
        self.pending_label.setStyleSheet("padding-left: 5px")
        self.pending_progressbar.setVisible(False)

        self.statusBar().addPermanentWidget(self.pending_progressbar)
        self.statusBar().addWidget(self.pending_label)

    @pyqtSlot()
    def on_addBtn_clicked(self):
        url = CustomInputDialog.get_text("Url", "Enter Url")

        if not url[1]:
            return

        if not validators.url(url[0]):
            QMessageBox.information(self, "Invalid Url", "Please enter a valid url")
            self.on_addBtn_clicked()

        ydl_logger = YDLLogger()
        ydl_logger.debug_message.connect(self.on_debug_message_emitted)
        ydl_opt = {
            'logger': ydl_logger
        }
        self.ui.addBtn.setEnabled(False)
        self.parser = InfoParser(url[0], ydl_opt)
        self.parsing_worker.set_up(self.parser.generate_info, self.on_parsing_done)
        self.parsing_worker.start()
        self.pending_progressbar.setVisible(True)

    @pyqtSlot(int)
    def on_combobox_currentIndexChanged(self, index):
        list_index = self.ui.pendingView.currentIndex().row()
        self.pending_list[list_index].current_format = self.pending_list[list_index].format_info[index]

    @pyqtSlot(str)
    def on_debug_message_emitted(self, msg):
        self.pending_label.setText(msg)

    def add_to_pending(self, ydl_obj):
        if ydl_obj in self.pending_list:
            return

        index = len(self.pending_list)
        self.pending_list.append(ydl_obj)

        self.pending_model.insertRow(index)
        self.pending_model.setData(self.pending_model.index(index, 0), ydl_obj.title)
        model_index = self.pending_model.index(index, 0)
        self.ui.pendingView.setCurrentIndex(model_index)
        self.ui.pendingView.selectionModel().select(model_index, QItemSelectionModel.ClearAndSelect)

        combobox = QComboBox()
        combobox.currentIndexChanged[int].connect(self.on_combobox_currentIndexChanged)
        for ydl_format in ydl_obj.info:
            format_text = "%s, %s, %s" % (ydl_format['extension'], ydl_format['resolution'], ydl_format['filesize'])
            combobox.addItem(format_text)
        self.ui.pendingView.setIndexWidget(self.pending_model.index(index, 1), combobox)

        self.ui.tabWidget.setCurrentIndex(1)

    def on_parsing_done(self, success):
        self.pending_progressbar.setVisible(False)
        self.pending_label.setText("")
        self.ui.addBtn.setEnabled(True)
        if success:
            self.add_to_pending(self.parser.ydl_object)
        else:
            self.parsing_worker.quit()
            self.ui.addBtn.setEnabled(True)
            QMessageBox.information(self, "Invalid Url", "Unable to parse url")




