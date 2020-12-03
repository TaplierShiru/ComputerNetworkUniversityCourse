from main_window.widgets import FileReceiverWidget, FileSenderWidget, LogInWidget, ConfigWidget
from main_window.utils import SignalSender
from PySide2.QtWidgets import QWidget, QStackedWidget, QGridLayout


class ControlWidget(QWidget):

    def __init__(self, status_bar):
        super().__init__()
        self.statusBar = status_bar
        self.initUI()

    def initUI(self):
        """
        Init app

        """
        self._stacked_widget = QStackedWidget()
        signal_controller = SignalSender()
        signal_controller.signal_newWindowIndx2MainWindow.connect(self.set_widget_by_index)
        signal_controller.signal_goto_settings.connect(self.set_widget_settings)

        self.grid = QGridLayout()
        self.grid.addWidget(self._stacked_widget)

        # Create log in widget
        self._log_in_widget = LogInWidget(self.statusBar, signal_controller)
        self._log_in_widget.set_index(self._stacked_widget.addWidget(self._log_in_widget))

        # Create file receiver
        self._file_receiver = FileReceiverWidget(self, signal_controller)
        self._file_receiver.set_index(self._stacked_widget.addWidget(self._file_receiver))

        # Create file sender
        self._file_sender = FileSenderWidget(self, signal_controller)
        self._file_sender.set_index(self._stacked_widget.addWidget(self._file_sender))

        # Create settings
        self._config_widget= ConfigWidget(self)
        self._config_widget.set_index(self._stacked_widget.addWidget(self._config_widget))

        self.setLayout(self.grid)
        self._stacked_widget.setCurrentIndex(self._log_in_widget.get_index())
        self.setWindowTitle("Main menu")

    def set_widget_settings(self):
        self.set_widget_by_index(self._config_widget.get_index())

    def set_widget_by_index(self, index: int):
        self._stacked_widget.setCurrentIndex(index)

    def get_status_bar(self):
        return self.statusBar

