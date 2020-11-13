from PySide2.QtWidgets import QTreeWidget, QTreeWidgetItem
from ftp_controller import FTPController
from signals import DataSender


class CustomQTreeWidget(QTreeWidget):

    def __init__(self, parent, size_sender: DataSender):
        super().__init__(parent)

        self.send_to_widget_size_sender = size_sender

    def connect_and_write(self, host: str, port: int, user: str, passwd: str):
        self.clear()
        file_system, size, size_to_each_type = FTPController.get_directory_list_and_size(
            host, port, user, passwd
        )

        self.send_to_widget_size_sender.send_TO_main_widget.emit(float(size))
        self.send_to_widget_size_sender.send_TO_tableview.emit(size_to_each_type)

        self.setHeaderLabels(['Files'])
        file_system_tree = {}

        for single_system_path in file_system:
            squeeze = single_system_path.split("\\")[1:]
            cur_directory = file_system_tree

            for single_squeeze in squeeze:
                if cur_directory.get(single_squeeze) is None:
                    # add
                    cur_directory.update({ single_squeeze: {}})
                else:
                    # already exist, jump into
                    cur_directory = cur_directory[single_squeeze]

        def deep_create_tree(came_from: QTreeWidgetItem, collections_tree: dict):
            for single_name in collections_tree:
                single_value = collections_tree[single_name]
                qtree = QTreeWidgetItem(came_from, 'zame')
                qtree.setText(0, single_name)
                deep_create_tree(qtree, single_value)

        deep_create_tree(self, file_system_tree)
