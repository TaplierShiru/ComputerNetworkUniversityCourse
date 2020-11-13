from PySide2.QtWidgets import QMainWindow, QDesktopWidget
from .main_window import Ui_MainWindow
from .main_widget import MainWidget


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.main_widget = MainWidget(self)
        self.setCentralWidget(self.main_widget)

        self.resize(800, 500)
        self.center()
        self.setWindowTitle("Main window")
        self.show()

    def center(self):
        """
        Centers the window on the screen

        """

        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            int((screen.width() - size.width()) / 2),
            int((screen.height() - size.height()) / 2)
        )
