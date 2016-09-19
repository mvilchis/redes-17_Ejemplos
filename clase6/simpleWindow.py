#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
from auxiliarWindow import AuxiliarWindow
from myServer import MyApiServer
from threading import Thread
class SimpleWindow(QtGui.QWidget):
   def __init__(self):
       super(SimpleWindow, self).__init__()
       self.setGeometry(400, 400, 400,400)
       self.setWindowTitle('Ventana principal')
       self.show()
   def openNewWindow(self):
       self.new_window = AuxiliarWindow()
       self.new_window.show()


def main():
    app = QtGui.QApplication(sys.argv)
    mainWindow = SimpleWindow()
    apiServer = MyApiServer(mainWindow).server
    api_server_thread = Thread(target=apiServer.serve_forever)
    api_server_thread.start()

    sys.exit(app.exec_())

if __name__=='__main__':
    main()
    
