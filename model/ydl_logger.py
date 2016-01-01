from PyQt5.QtCore import QObject, pyqtSignal
import re


class YDLLogger(QObject):
    debug_message = pyqtSignal(str)

    def debug(self, msg):
        new_msg = re.findall(': (\D+)', msg)[0]
        self.debug_message.emit(new_msg)

    def warning(self, msg):
        print('warning')

    def error(self, msg):
        print('error')
