#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QWidget, QLabel, QPixmap
import cv2
import numpy
### Video
CAM_NUMBER= 0
VIDEO_WIDTH = 320
VIDEO_HEIGTH = 240
#**************************************************
#Clase que representa la ventana de audio y proximamente
#de video
#**************************************************
class CallWindow(QtGui.QWidget):
    # **************************************************
    #Constructor de la clase
    #**************************************************

    def __init__(self, server, queue, client_thread):
        super(CallWindow, self).__init__()
        self.client_thread = client_thread
        self.queue = queue
        self.server = server
        self.video_size = QtCore.QSize(VIDEO_WIDTH, VIDEO_HEIGTH)
        self.server_side()
        self.initUI()


    # **************************************************
    #Metodo Auxiliar que agrega todos los widget a la interfaz
    #**************************************************

    def initUI(self):
        self.image_label = QLabel()
        self.image_label.setFixedSize(self.video_size)
        finish_button = QtGui.QPushButton('Finalizar llamada')
        finish_button.clicked.connect(lambda: self.close())
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.addWidget(self.image_label)
        self.main_layout.addWidget(finish_button)
        self.setLayout(self.main_layout)
        self.setGeometry(350, 350, 500, 500)
        self.setWindowTitle('Servidor llamada')
        self.show()

    def closeEvent(self, event):
        #self.chat_channel.close_call()
        self.server.stop_server()
        event.accept()

    def server_side(self):
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start()

    def display_video_stream(self):
        if len(self.queue) > 0:
            frame = self.queue.pop(0)
            narray = numpy.fromstring(frame, dtype="uint8")
            decimg = cv2.imdecode(narray, 1)
            try:
                cv2.imshow("camara servidor", decimg)
            except Exception as e:
                print "show error"

class DummyClass(QWidget):
        def __init__(self):
            super(DummyClass, self).__init__()
