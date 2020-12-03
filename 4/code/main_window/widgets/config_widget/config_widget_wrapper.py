import traceback

from logic.config_controller import ConfigController
from PySide2.QtWidgets import QWidget
from .config_widget import Ui_Config_widget
from main_window.utils import LOG_IN_INDEX


class ConfigWidget(QWidget):

    __TIME = 3200

    def __init__(self, parent):
        super(ConfigWidget, self).__init__(parent)
        self.ui = Ui_Config_widget()
        self.ui.setupUi(self)
        self.setLayout(self.ui.gridLayout)
        self.index = None

        self.ui.pushButton_back_to_default.clicked.connect(self.__back_to_default)
        self.ui.pushButton_back_to_menu.clicked.connect(lambda: parent.set_widget_by_index(LOG_IN_INDEX))
        self.ui.pushButton_save.clicked.connect(self.__try_save_changes)
        self.__config_controller = ConfigController()
        self.__status_bar = parent.get_status_bar()

        self.__back_to_current()

    def set_index(self, index: int):
        self.index = index

    def get_index(self):
        return self.index

    def change_receiver(self, port: int) -> bool:
        good_params = True

        try:
            self.__config_controller.change_receiver(port)
        except Exception as exc:
            print(exc)
            traceback.print_exc()
            good_params = False

        return good_params

    def change_sender(self, port: int) -> bool:
        good_params = True

        try:
            self.__config_controller.change_sender(port)
        except Exception as exc:
            print(exc)
            traceback.print_exc()
            good_params = False

        return good_params

    def change_host(self, host: str) -> bool:
        good_params = True

        try:
            self.__config_controller.change_host(host)
        except Exception as exc:
            print(exc)
            traceback.print_exc()
            good_params = False

        return good_params

    def __bad_args(self):
        self.__status_bar.showMessage("Bad arguments, check out input data", self.__TIME)

    def __good_args(self):
        self.__status_bar.showMessage("Saved", self.__TIME)

    def __back_to_current(self):
        host, port = ConfigController.get_current_params_for_receiver()
        self.ui.lineEdit_port_receiver.setText(str(port))

        host, port = ConfigController.get_current_params_for_sender()
        self.ui.lineEdit_host.setText(host)
        self.ui.lineEdit_port_sender.setText(str(port))

    def __back_to_default(self):
        self.__config_controller.reset_params()
        self.__back_to_current()

    def __try_save_changes(self):
        try:
            # Change host
            host = self.ui.lineEdit_host.text()
            if not self.change_host(host):
                raise Exception("Bad Args")

            # Change receiver
            port = int(self.ui.lineEdit_port_receiver.text())

            if not self.change_receiver(port):
                raise Exception("Bad Args")

            # Change sender
            port = int(self.ui.lineEdit_port_sender.text())

            if not self.change_sender(port):
                raise Exception("Bad Args")

        except Exception as exc:
            traceback.print_exc()
            print(exc)
            self.__bad_args()
        else:
            self.__good_args()
        finally:
            self.__back_to_current()
