import sys

from PyQt5.QtWidgets import QApplication
from controller.test_ydl import test_ydl

from controller.ydl import YoutubeDLGui


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ydl = YoutubeDLGui()
    ydl.show()
    sys.exit(app.exec_())
    # test_ydl()
