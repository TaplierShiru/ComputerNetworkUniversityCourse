import os
import shutil

from PySide2.QtCore import QThreadPool, QTimer

from logic.config_controller import ConfigController
from main_window.utils.constans import FILE_SENDER_INDEX, LOG_IN_INDEX
from logic.email_receiver import EmailReceiverController
from .file_receiver_gui import Ui_file_reciever
from PySide2.QtWidgets import QWidget, QListWidgetItem, QFileDialog

from main_window import START_FOLDER
from main_window.utils import SignalSender, WorkerWrapper


class FileReceiverWidget(QWidget):

    __MESSAGE_TIME = 3200

    __TEMP_PATH = "main_window/widgets/file_receiver/content/temp_data"
    __CONTENT = "main_window/widgets/file_receiver/content"

    def __init__(self, parent, signal_controller: SignalSender):
        super().__init__()
        self.ui = Ui_file_reciever()
        self.ui.setupUi(self)
        self.setLayout(self.ui.gridLayout)
        self.__status_bar = parent.get_status_bar()

        self.index = None
        self.__email_receiver_controller = None
        self.__pool = QThreadPool()

        # Timer is used to handle second click
        # For correct execution of further operation
        self.__clicked_item = None
        self.__timer = QTimer()
        self.__timer.setSingleShot(True)
        self.__timer.timeout.connect(self.__item_clicked)

        self.__cur_state = -1
        self.__is_pressed = False
        self.__num_last_message = 0
        self.__IDemailname2text = {}
        self.__IDemailname2fromtxt = {}
        self.__IDemailname2date = {}
        self.__IDemailname2attach = {}
        self.__attach2fullpath = {}

        self.ui.commandLinkButton_to_sender.clicked.connect(lambda: parent.set_widget_by_index(FILE_SENDER_INDEX))
        self.ui.pushButton_exit.clicked.connect(
            lambda: self.__reset_all(lambda: parent.set_widget_by_index(LOG_IN_INDEX))
        )
        self.ui.pushButton_update_new_mess.clicked.connect(self.__update_messages)

        self.ui.listWidget_new_mess.itemClicked.connect(self.__update_text)
        self.ui.listWidget_new_mess.itemClicked.connect(self.__update_attach)

        self.ui.listWidget_attch_files.itemClicked.connect(self.__attach_clicked_open_it)
        self.ui.listWidget_attch_files.itemDoubleClicked.connect(self.__attach_double_clicked_save_it)

        signal_controller.signal_send_user_data_receiver.connect(self.set_login)

    def set_index(self, index: int):
        self.index = index

    def get_index(self):
        return self.index

    def set_login(self, login: str, password: str):
        host, port = ConfigController.get_current_params_for_receiver()
        self.__email_receiver_controller = EmailReceiverController(login, password, host, port)

    def __update_messages(self):
        self.__status_bar.showMessage(f'Update message...')

        params = {
            'save_files_to': self.__TEMP_PATH
        }

        runnable_th = WorkerWrapper(self.__email_receiver_controller.take_content_from_new_mess, params)
        runnable_th.signals.error.connect(self.__message_failed_refresh)
        runnable_th.signals.finish.connect(self.__message_refresh)

        self.__pool.start(runnable_th)

    def __message_failed_refresh(self, data: tuple):
        if self.__email_receiver_controller.error is not None:
            self.__status_bar.showMessage(self.__email_receiver_controller.error, self.__MESSAGE_TIME)
        else:
            self.__status_bar.showMessage("Something went wrong. Check your enterted data!", self.__MESSAGE_TIME)
        print(data[-1])

    def __message_refresh(self):
        self.__status_bar.showMessage("Messages updated!", self.__MESSAGE_TIME)
        for single_content in self.__email_receiver_controller.get_last_update():

            if single_content.attach is not None:
                folder_path = self.__CONTENT + '/' + str(self.__num_last_message)
                os.makedirs(
                    folder_path,
                    exist_ok=True
                )
                new_file_path = folder_path + '/' + single_content.attach.split('/')[-1]

                shutil.move(single_content.attach, new_file_path)

                self.__IDemailname2attach[self.__num_last_message] = new_file_path.split('/')[-1]
                self.__attach2fullpath[new_file_path.split('/')[-1]] = new_file_path

            self.__IDemailname2text[self.__num_last_message] = single_content.full_txt
            self.__IDemailname2fromtxt[self.__num_last_message] = single_content.from_txt
            self.__IDemailname2date[self.__num_last_message] = single_content.date

            QListWidgetItem(single_content.header_txt, self.ui.listWidget_new_mess)

            self.__num_last_message += 1

    def __update_attach(self, item: QListWidgetItem):
        if self.__cur_state == self.ui.listWidget_new_mess.currentRow() and not self.__is_pressed:
            return
        self.ui.listWidget_attch_files.clear()
        indx = self.ui.listWidget_new_mess.currentRow()

        filename = self.__IDemailname2attach.get(indx)
        if filename is not None:
            QListWidgetItem(filename, self.ui.listWidget_attch_files)
            if not self.__is_pressed:
                self.__cur_state = indx
                self.__is_pressed = True
            else:
                self.__is_pressed = False

    def __update_text(self, item: QListWidgetItem):
        if self.__cur_state == self.ui.listWidget_new_mess.currentRow() and not self.__is_pressed:
            return

        indx = self.ui.listWidget_new_mess.currentRow()
        text = self.__IDemailname2text.get(indx)
        if text is not None:
            date = self.__IDemailname2date[indx]
            from_txt = self.__IDemailname2fromtxt[indx]
            create_text = f"Date: {date}\n" + \
                          f"From: {from_txt}\n" + \
                          f"Text:\n {text}"
            self.ui.plainTextEdit_message_text.setPlainText(create_text)
            if not self.__is_pressed:
                self.__cur_state = indx
                self.__is_pressed = True
            else:
                self.__is_pressed = False

    def __attach_clicked_open_it(self, item: QListWidgetItem):
        self.__clicked_item = item
        # To dodge second click, start timer
        # IF there is no second click - execute operation for single click
        self.__timer.start(500)

    def __attach_double_clicked_save_it(self, item: QListWidgetItem):
        self.__timer.stop()
        item_num = self.ui.listWidget_attch_files.currentRow()
        item = self.ui.listWidget_attch_files.item(item_num)
        file_save_name_path = self.__attach2fullpath[item.text()]

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file, _ = QFileDialog.getSaveFileName(
            self,
            "QFileDialog.getOpenFileNames()", "",
            "All Files (*);;Python Files (*.py)",
            options=options
        )

        if file:
            shutil.copyfile(file_save_name_path, file)

    def __item_clicked(self):
        item = self.__clicked_item
        if item is not None:
            # Execute file
            os.startfile(START_FOLDER + '/' + self.__attach2fullpath[item.text()])

    def __reset_all(self, func_back):
        self.__cur_state = -1
        self.__num_last_message = 0
        self.__IDemailname2text = {}
        self.__IDemailname2attach = {}
        self.__IDemailname2fromtxt = {}
        self.__IDemailname2date = {}
        self.__attach2fullpath = {}
        self.__clicked_item = None
        self.__email_receiver_controller = None

        self.ui.listWidget_new_mess.clear()
        self.ui.listWidget_attch_files.clear()
        self.ui.plainTextEdit_message_text.clear()

        func_back()

