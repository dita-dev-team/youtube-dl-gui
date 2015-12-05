from PyQt5 import QtCore


'''class Worker(QtCore.QThread):

    def __init__(self):
        super(Worker, self).__init__()
        self.__i_process = None
        self.__f_process = None
        self.__done = None

    def set_up(self, i_process):
        self.__i_process = i_process

    def run(self):
        return_value = self.__i_process()
        self.__done.emit(return_value)

    @property
    def done(self):
        return self.__done

    @done.setter
    def done(self, done):
        self.__done = done'''


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


'''
class Worker(QtCore.QObject):
    return_type = None
    done = QtCore.pyqtSignal(return_type)

    def __init__(self, i_process, f_process, f_return_type):
        super(Worker, self).__init__()
        self.__process = i_process
        #self.__done = QtCore.pyqtSignal(f_return_type)

    def run(self):
        return_value = self.__process()
        self.__done.emit(return_value)

    @property
    def done(self):
        return self.__done


class WorkerBuilder(QtCore.QObject):

    def __init__(self):
        super(WorkerBuilder, self).__init__()
        self.__i_process = None
        self.__f_process = None
        self.__f_return_type = None

    def initial_process(self, process):
        self.__i_process = process
        return self

    def final_process(self, process, return_type):
        self.__f_process = process
        self.__f_return_type = return_type
        return self

    def build(self):
        self.thread = QtCore.QThread()
        self.worker = Worker(self.__i_process, self.__f_process, self.__f_return_type)
        self.worker.moveToThread(self.thread)
        self.worker.done.connect(self.__f_process)
        self.worker.done.connect(self.thread.quit)
        self.thread.started.connect(self.worker.run)
        self.thread.start()
'''