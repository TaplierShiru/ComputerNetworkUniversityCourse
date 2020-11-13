from PySide2.QtWidgets import QWidget, QStatusBar
from PySide2.QtCore import QThreadPool, QCoreApplication
from .main_widget import Ui_MainWidget
from link_reader import LinkWorker
from main_window.main_widget.signals.prograss_bar_signal import PrograssBarSignalSender
from main_window.main_widget.signals.label_process_signal import LabelProcessSignalSender


class MainWidget(QWidget):

    def __init__(self, parent, status_bar: QStatusBar):
        super(MainWidget, self).__init__(parent=parent)

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)
        self.status_bar=status_bar
        self.setLayout(self.ui.gridLayout)
        self.pool = QThreadPool()
        #print("Multithreading with maximum %d threads" % self.pool.maxThreadCount())

        self.__connect_buttons_and_signals()

        self.ui.lineEdit_port.setText(str(443))
        self.ui.lineEdit_adress.setText('https://ssau.ru/')
        self.ui.lineEdit_depth.setText(str(2))
        self.ui.lineEdit_max_depth.setText(str(30))

        self.__finish_progress_bar()

    def __connect_buttons_and_signals(self):
        self.ui.pushButton_search.clicked.connect(self.take_images)
        self.ui.pushButton_quit.clicked.connect(QCoreApplication.quit)

        self._progress_bar_signal = PrograssBarSignalSender()
        self._progress_bar_signal.finish.connect(self.__finish_progress_bar)
        self._progress_bar_signal.maximum.connect(self.__set_maximum_to_progress_bar)
        self._progress_bar_signal.progress.connect(self.__update_progress_bar)

        self._label_process_signal = LabelProcessSignalSender()
        self._label_process_signal.whatProcess.connect(self.ui.label_what_process.setText)

    def take_images(self):
        self.status_bar.showMessage("")
        self.ui.plainTextEdit_by_other_sites.setPlainText("")
        self.ui.plainTextEdit_by_adress.setPlainText("")

        adress = self.ui.lineEdit_adress.text()

        try:
            port = int(self.ui.lineEdit_port.text())
        except ValueError as ex:
            self.status_bar.showMessage("Wrong address")
            return
        try:
            depth = int(self.ui.lineEdit_depth.text())
        except ValueError as ex:
            self.status_bar.showMessage("Wrong address")
            return
        try:
            max_number_links = int(self.ui.lineEdit_max_depth.text())
        except ValueError as ex:
            self.status_bar.showMessage("Wrong address")
            return

        # Show progress
        self.ui.label_what_process.setHidden(False)
        self.ui.label_process.setHidden(False)

        worker = LinkWorker(
            adress,
            port,
            depth,
            max_number_links,
            self._progress_bar_signal,
            self._label_process_signal
        )

        worker.signals.result.connect(self.__write_found_links)
        worker.signals.finished.connect(self.__finish_pool)
        self.pool.start(worker)

    def __write_found_links(self, worker: LinkWorker):
        first_names = ""
        for elem in worker.main_images_set:
            first_names += elem + '\n'

        second_names = ""
        for elem in worker.second_images_set:
            second_names += elem + '\n'

        self.ui.plainTextEdit_by_adress.setPlainText(first_names)
        self.ui.plainTextEdit_by_other_sites.setPlainText(second_names)

    def __finish_pool(self):
        self._progress_bar_signal.finish.emit()

    def __update_progress_bar(self, value: int):
        self.ui.progressBar_of_found.setValue(value)

    def __set_maximum_to_progress_bar(self, value: int):
        self.ui.progressBar_of_found.setHidden(False)
        self.ui.label_progress.setHidden(False)

        self.ui.progressBar_of_found.setMaximum(value)
        self.ui.progressBar_of_found.setValue(0)

        self.ui.label_what_process.setText("")
        self.ui.label_what_process.setHidden(True)
        self.ui.label_process.setHidden(True)

    def __finish_progress_bar(self):
        self.ui.progressBar_of_found.setHidden(True)
        self.ui.label_progress.setHidden(True)
