from PySide2.QtCore import QObject, Signal


class LabelProcessSignalSender(QObject):

    whatProcess = Signal(str)

