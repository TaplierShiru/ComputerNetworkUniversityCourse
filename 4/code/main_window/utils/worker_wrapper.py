import sys
import traceback

from PySide2.QtCore import QRunnable, Slot

from main_window.utils.worker_sender import WorkerSender


class WorkerWrapper(QRunnable):

    def __init__(self, function_execute, params: dict):
        super(WorkerWrapper, self).__init__()
        self.function_execute = function_execute
        self.params = params

        self.signals = WorkerSender()

    @Slot()
    def run(self):
        try:
            self.function_execute(**self.params)
        except:
            tracer = traceback.print_exc()
            print(tracer)
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype, value, traceback.format_exc(), tracer))
        else:
            self.signals.finish.emit()

