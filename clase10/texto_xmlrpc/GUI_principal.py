#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import threading
from PyQt4.QtGui import QMainWindow, QWidget, QLabel, QApplication, QGridLayout,QTextEdit
import PyQt4.QtGui as QtGui
from server import *
from signals import *


class CentralWindow(QMainWindow):
    def __init__(self):
        super(CentralWindow, self).__init__()
        #Creamos el objeto que se encargara de emitir signals
        self.signalManager = SignalManager(self)
        #Creamos el servidor de xmlrpc
        self.server = Server(self.signalManager)
        self.api_server_thread = threading.Thread(target=self.server.run)
        self.api_server_thread.start()

        self.initUI()

    def initUI(self):
        self.conversation_widget = QtGui.QTextEdit(self)
        self.setCentralWidget(self.conversation_widget)
        self.conversation_widget.setReadOnly(True)

        self.setGeometry(350, 350, 500, 500)
        self.setWindowTitle('Despliega texto de cliente')
        self.show()


    """ Metodo que sera llamado desde el servidor
    para agregar el texto que el cliente mande """
    def insert_text_window(self, text):
        self.conversation_widget.insertPlainText(text)


    """Evento llamado cuando se cierra la ventana
       Detendremos el thread para el servidor de xmlrpc
    """
    def closeEvent(self, event):
        self.server.stop_server()
        event.accept()


def main():
    app = QApplication(sys.argv)
    mainWindow = CentralWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
