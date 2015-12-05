import logging

import validators
from PyQt5.QtWidgets import QDialog, QMessageBox
from PyQt5.QtCore import pyqtSlot

from controller.worker import WorkerBuilder

from controller.info_parser import InfoParser
from view.ui_url_enter import Ui_Dialog


class AddUrl(QDialog):
    def __init__(self):
        super(AddUrl, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.progressBar.setVisible(False)
        self.worker = WorkerBuilder.build(bool)
        self.parser = None

    @pyqtSlot()
    def on_goBtn_clicked(self):
        url = self.ui.lineEdit.text()

        if not validators.url(url):
            QMessageBox.information(self, "Invalid Url", "Please enter a valid url")
            return

        ydl_opt = {
            'logging', logging.getLogger('ydl')
        }
        self.parser = InfoParser(url)
        self.worker.set_up(self.parser.generate_info, self.on_background_done)
        # self.worker.done.connect(self.on_background_done)
        self.worker.start()
        self.ui.progressBar.setVisible(True)

    def on_background_done(self, success):
        self.ui.progressBar.setVisible(False)
        if success:
            QMessageBox.information(self, "Success", "Success!!")
        else:
            QMessageBox.information(self, "Invalid Url", "Unable to parse url")



