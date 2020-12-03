import os

from PySide2.QtCore import QTimer
from logic.config_controller import ConfigController
from logic.email_sender import EmailSenderController
from main_window.utils import LOG_IN_INDEX, FILE_RECEIVER_INDEX, WorkerWrapper
from .file_sender_gui import Ui_File_sender
from PySide2.QtWidgets import QWidget, QFileDialog, QListWidgetItem
from PySide2.QtCore import QThreadPool


class FileSenderWidget(QWidget):

    __MESSAGE_TIME = 3200

    def __init__(self, parent, signal_controller):
        super().__init__()
        self.ui = Ui_File_sender()
        self.ui.setupUi(self)
        self.setLayout(self.ui.gridLayout)

        self.index = None
        self.__email_sender_controller = None
        self.__pool = QThreadPool()

        # Timer is used to handle second click
        # For correct execution of further operation
        self.__clicked_item = None
        self.__timer = QTimer()
        self.__timer.setSingleShot(True)
        self.__timer.timeout.connect(self.__item_clicked)

        # In order to show only filenames (not full path)
        # Create dict which handle filename -> full_filename
        # When file will be executed (single click) or loaded into email
        self.__filename2full_filename = {}
        self.__status_bar = parent.get_status_bar()

        # Connect events
        self.ui.commandLinkButton_to_recieve.clicked.connect(lambda: parent.set_widget_by_index(FILE_RECEIVER_INDEX))
        self.ui.pushButton_exit.clicked.connect(
            lambda: self.__back_to_log_in_menu(lambda: parent.set_widget_by_index(LOG_IN_INDEX))
        )
        self.ui.pushButton_send_message.clicked.connect(self.__send_message)
        self.ui.pushButton_attch_file.clicked.connect(self.__attach_file)

        self.ui.listWidget_attch_files.itemClicked.connect(self.__first_click_on_item)
        self.ui.listWidget_attch_files.itemDoubleClicked.connect(self.__item_remove)

        signal_controller.signal_send_user_data_receiver.connect(self.set_login)

    def set_login(self, login: str, password: str):
        host, port = ConfigController.get_current_params_for_sender()
        self.__email_sender_controller = EmailSenderController(login, password, host, port)

    def set_index(self, index: int):
        self.index = index

    def get_index(self):
        return self.index

    def __send_message(self):
        attach = list(self.__filename2full_filename.values())
        if len(attach) == 0:
            attach = None
        params = {
            'header_str': self.ui.lineEdit_header.text(),
            'text': self.ui.plainTextEdit_message_text.toPlainText(),
            'send_to': self.ui.lineEdit_to.text().split(','),
            'attachment_path': attach
        }

        runnable_th = WorkerWrapper(self.__email_sender_controller.send_message, params)
        runnable_th.signals.error.connect(self.__message_failed_send)
        runnable_th.signals.finish.connect(self.__message_send)

        self.__pool.start(runnable_th)

    def __message_send(self):
        self.__status_bar.showMessage(f'Message are sender to: {self.ui.lineEdit_to.text()}', self.__MESSAGE_TIME)

    def __message_failed_send(self, data: tuple):
        print(data[-1])
        if self.__email_sender_controller.error is not None:
            self.__status_bar.showMessage(self.__email_sender_controller.error, self.__MESSAGE_TIME)
        else:
            self.__status_bar.showMessage("Something went wrong. Check your enterted data!", self.__MESSAGE_TIME)

    def __attach_file(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self, "QFileDialog.getOpenFileNames()", "",
                                                "All Files (*);;Python Files (*.py)", options=options)
        if files:
            single_file = files[0]
            print(single_file)
            filename = single_file.split('/')[-1]
            self.__filename2full_filename[filename] = single_file
            _ = QListWidgetItem(filename, self.ui.listWidget_attch_files)

    def __first_click_on_item(self, item: QListWidgetItem):
        self.__clicked_item = item
        # To dodge second click, start timer
        # IF there is no second click - execute operation for single click
        self.__timer.start(500)

    def __item_remove(self, *args):
        self.__timer.stop()
        item_num = self.ui.listWidget_attch_files.currentRow()
        item = self.ui.listWidget_attch_files.takeItem(item_num)
        del self.__filename2full_filename[item.text()]

    def __item_clicked(self):
        item = self.__clicked_item
        if item is not None:
            # Execute file
            os.startfile(self.__filename2full_filename[item.text()])

    def __back_to_log_in_menu(self, func_back):
        self.__email_sender_controller = None
        self.__clicked_item = None
        self.__filename2full_filename.clear()

        self.ui.plainTextEdit_message_text.clear()
        self.ui.listWidget_attch_files.clear()
        self.ui.lineEdit_to.clear()
        self.ui.lineEdit_header.clear()

        func_back()

