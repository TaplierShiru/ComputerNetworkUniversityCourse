from PySide2.QtGui import QStandardItemModel, QStandardItem
from PySide2.QtWidgets import QWidget, QHeaderView, QAbstractItemView
from PySide2.QtCore import QThreadPool, QCoreApplication, Qt
from .custom_widget import CustomQTreeWidget
from .main_widget import Ui_Form as Ui_MainWidget
from signals import SendToFtpController, DataSender


class MainWidget(QWidget):

    def __init__(self, parent):
        super(MainWidget, self).__init__(parent=parent)

        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)
        self._init_additional_widgets()
        self.setLayout(self.ui.gridLayout)
        #self.pool = QThreadPool()
        #print("Multithreading with maximum %d threads" % self.pool.maxThreadCount())

        self.ui.lineEdit_port.setText(str(8080))
        self.ui.lineEdit_adress.setText('localhost')
        self.ui.lineEdit_password.setText("123")
        self.ui.lineEdit_login.setText("lokesh")

    def _init_additional_widgets(self):

        send_size_to_main_widget_sender = DataSender()
        send_size_to_main_widget_sender.send_TO_main_widget.connect(self.__set_size)
        send_size_to_main_widget_sender.send_TO_tableview.connect(self.__set_tableview)

        self.treeWidget_file_system = CustomQTreeWidget(self.ui.gridLayoutWidget, send_size_to_main_widget_sender)
        self.treeWidget_file_system.setObjectName(u"treeWidget_file_system")
        self.treeWidget_file_system.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.gridLayout.addWidget(self.treeWidget_file_system, 3, 3, 1, 3)

        self.sender_to_ftp = SendToFtpController()
        self.sender_to_ftp.send.connect(self.treeWidget_file_system.connect_and_write)
        self.ui.pushButton_connect.clicked.connect(self.__send_to_ftp)

    def __send_to_ftp(self):
        host = self.ui.lineEdit_adress.text()
        port = self.ui.lineEdit_port.text()
        user_name = self.ui.lineEdit_login.text()
        password = self.ui.lineEdit_password.text()

        self.sender_to_ftp.send.emit(host, int(port), user_name, password)

    def __set_size(self, string):
        self.ui.label_size.setText(str(string))

    def __set_tableview(self, data:dict):
        model = QStandardItemModel()
        model.setColumnCount(2)
        model.setHorizontalHeaderLabels(["Name", "Type"])

        for single_name_data in data:
            item_name = QStandardItem(single_name_data)
            item_name.setEditable(False)

            item_value = QStandardItem(str(data[single_name_data]))
            item_value.setEditable(False)

            model.appendRow([item_name, item_value])

        self.ui.tableView_result_type_and_size.setModel(model)
