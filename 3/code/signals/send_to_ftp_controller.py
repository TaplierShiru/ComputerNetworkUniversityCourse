from PySide2.QtCore import QObject, Signal


class SendToFtpController(QObject):

    send = Signal(str, int, str, str) # host, port, user_name, password

