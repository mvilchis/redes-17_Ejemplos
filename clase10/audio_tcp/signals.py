from PyQt4.QtCore import SIGNAL, QObject,QThread, Qt
from PyQt4.QtGui import QApplication
from call_window import *
import sys


def create_call_GUI(server,client_thread):
    mainWindow = CallWindow(server, client_thread)


class SignalManager(QThread):
    def __init__(self):
        QThread.__init__(self)

        #Ligamos la signal de create_call_window a la interfaz grafica
        QObject.connect(self, SIGNAL('audio_signal'),create_call_GUI, Qt.QueuedConnection)

    def create_window_signal(self,server,client_thread):
        self.emit(SIGNAL('audio_signal'), server, client_thread)
