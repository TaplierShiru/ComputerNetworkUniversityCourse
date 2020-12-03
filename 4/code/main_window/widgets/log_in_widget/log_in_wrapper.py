from main_window.utils import FILE_RECEIVER_INDEX, FILE_SENDER_INDEX, SignalSender
from logic.account_checker import AccountChecker
from .log_in_widget import Ui_Form
from PySide2.QtWidgets import QWidget, QStatusBar


class LogInWidget(QWidget):

    def __init__(self, status_bar: QStatusBar, signal_sender: SignalSender):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setLayout(self.ui.gridLayout)

        self.ui.pushButton_enter.clicked.connect(self.__enter_into_prof)
        self.ui.pushButton_settings.clicked.connect(lambda: signal_sender.signal_goto_settings.emit())
        self.index = None

        self.__status_bar = status_bar
        self.__signal_sender = signal_sender

    def get_user_data(self):
        return self.login, self.password

    def set_index(self, index: int):
        self.index = index

    def get_index(self):
        return self.index

    def __enter_into_prof(self):
        login = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_pass.text()

        if not AccountChecker.password_check(login, password):
            self.__status_bar.showMessage("Wrong login/password or bad host/port values!", 5000)
            return

        self.__signal_sender.signal_send_user_data_receiver.emit(login, password)
        self.__signal_sender.signal_send_user_data_sender.emit(login, password)

        self.__signal_sender.signal_newWindowIndx2MainWindow.emit(FILE_RECEIVER_INDEX)


