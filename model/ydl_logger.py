from PyQt5.QtCore import QObject


class YDLLogger(QObject):
    def debug(self, msg):
        print(msg)

    def warning(self, msg):
        print('warning')

    def error(self, msg):
        print('error')
