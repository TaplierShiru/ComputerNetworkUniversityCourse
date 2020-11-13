from PySide2.QtCore import QObject, Signal


class SignalSender(QObject):

    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)

