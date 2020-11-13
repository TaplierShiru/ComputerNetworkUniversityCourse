from PySide2.QtCore import QObject, Signal


class PrograssBarSignalSender(QObject):

    progress = Signal(int)
    maximum = Signal(int)
    finish = Signal()

