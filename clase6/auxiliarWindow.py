#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
class AuxiliarWindow(QtGui.QWidget):
    def __init__(self):
        super(AuxiliarWindow, self).__init__()
        self.setGeometry(200, 200, 200,200)
        self.setWindowTitle('Ventana auxiliar')

