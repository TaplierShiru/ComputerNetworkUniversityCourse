from PySide2.QtWidgets import QApplication
from main_window import MainWindow
import sys


def main():
    app = QApplication(sys.argv)
    _ = MainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
