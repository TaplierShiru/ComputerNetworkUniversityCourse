
import os

START_FOLDER = ''.join(os.path.abspath(os.getcwd()).replace('\\', '/'))

print('start fodler: ', START_FOLDER)

from .main_window_wrapper import MainWindow

