#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from SimpleXMLRPCServer import SimpleXMLRPCServer
from threading import Thread
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import SIGNAL, QObject
class MyApiServer:
    def __init__(self, simpleWindow):
        self.server = SimpleXMLRPCServer(("localhost", 8000), allow_none = True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.funtionWrapper = FunctionWrapper(simpleWindow)
        self.server.register_instance(self.funtionWrapper)
        print "Servidor escuchando en el puerto 8000"

class FunctionWrapper(QtCore.QThread):
    """ **************************************************
    Constructor de la clase
    ************************************************** """
    def __init__(self, simpleWindow):
        QtCore.QThread.__init__(self)
        print "Se construye las funciones"
        self.simpleWindow = simpleWindow
   
    def create_remote_window(self):
        self.emit(SIGNAL('some_signal'))
        #self.simpleWindow.openNewWindow()
        print "Hola mundo"
