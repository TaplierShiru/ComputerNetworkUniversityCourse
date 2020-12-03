from PySide2.QtCore import Signal, QObject


class WorkerSender(QObject):

    error = Signal(object)
    finish = Signal()

