from PySide2.QtCore import QObject, Signal


class DataSender(QObject):

    send_TO_main_widget = Signal(float)
    send_TO_tableview = Signal(dict)

