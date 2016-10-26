from PyQt4.QtCore import SIGNAL, QObject,QThread, Qt
from PyQt4.QtGui import QApplication
from ServerGui import *
import sys


def create_call_GUI(queue):
    mainWindow = CallWindow(queue)


class SignalManager(QThread):
    def __init__(self):
        QThread.__init__(self)

        #Ligamos la signal de create_call_window a la interfaz grafica
        QObject.connect(self, SIGNAL('video_signal'),create_call_GUI, Qt.QueuedConnection)

    def create_window_signal(self,queue):
        self.emit(SIGNAL('video_signal'), queue)
