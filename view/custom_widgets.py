from PyQt5.QtCore import QEvent, Qt
from PyQt5.QtWidgets import QInputDialog, QStyledItemDelegate, QToolTip


class CustomInputDialog(QInputDialog):
    def __init__(self):
        super(CustomInputDialog, self).__init__()

        self.setStyleSheet("QLineEdit {\n"
                           "    border: 2px solid #8f8f91;\n"
                           "    border-radius: 10px;\n"
                           "    padding: 0 0;\n"
                           "    background: white;\n"
                           "    selection-background-color: darkgray;\n"
                           "}\n"
                           "QPushButton {\n"
                           "    height: 30px;\n"
                           "    width: 60px;\n"
                           "    margin: 0px 0px;\n"
                           "    border: 1px solid #8f8f91;\n"
                           "    border-radius: 5px;\n"
                           "    background-color: transparent;\n"
                           "    color: rgba(0, 0, 0, 0.87);\n"
                           "}\n"
                           "QPushButton:hover, QPushButton:focus {\n"
                           "    background-color: rgba(208,208,208,1);\n"
                           "}")

    @staticmethod
    def get_text(title, label, input_text=""):
        dialog = CustomInputDialog()
        dialog.setTextValue(input_text)
        if dialog.__show_input__(title, label):
            return tuple([dialog.textValue(), True])
        else:
            return tuple(['', False])

    def __show_input__(self, title, label):
        self.setWindowTitle(title)
        self.setLabelText(label)
        return self.exec_()


class CustomToolTipDelegate(QStyledItemDelegate):
    def helpEvent(self, event, view, option, index):
        if not event or not view:
            return False

        if event.type() == QEvent.ToolTip:
            rect = view.visualRect(index)
            size = self.sizeHint(option, index)

            if rect.width() < size.width():
                tooltip = index.data(Qt.DisplayRole)

                QToolTip.showText(event.globalPos(), tooltip)
                return True

            if not QStyledItemDelegate.helpEvent(self, event, view, option, index):
                QToolTip.hideText()

            return True

        return QStyledItemDelegate.helpEvent(self, event, view, option, index)