from PyQt5 import QtCore


class WorkerBuilder:
    @staticmethod
    def init(self):
        super(type(self), self).__init__()
        self.__i_process = None

    @staticmethod
    def set_up(self, i_process, f_process=None):
        self.__i_process = i_process
        if f_process:
            self.done.connect(f_process)

    @staticmethod
    def run(self):
        return_val = self.__i_process()
        self.done.emit(return_val)

    @staticmethod
    def build(return_type):
        worker = type('Worker', (QtCore.QThread,), {'done': QtCore.pyqtSignal(return_type),
                                                    '__init__': WorkerBuilder.init,
                                                    'set_up': WorkerBuilder.set_up,
                                                    'run': WorkerBuilder.run})
        return worker()
