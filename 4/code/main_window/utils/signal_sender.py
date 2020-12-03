from PySide2.QtCore import Signal, QObject


class SignalSender(QObject):

    signal_newWindowIndx2MainWindow = Signal(int)
    signal_goto_settings = Signal()

    signal_send_user_data_receiver = Signal(str, str) # login and pass
    signal_send_user_data_sender = Signal(str, str)   # login and pass


