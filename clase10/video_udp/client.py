#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QWidget, QLabel, QPixmap,QWidget,QApplication
import cv2
import cv2.cv as cv
import sys
import pickle
import socket
import struct

"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
### Video
CAM_NUMBER= 0
VIDEO_WIDTH = 320
VIDEO_HEIGTH = 240
BUFFER_SIZE = 1024


#**************************************************
#Clase que representa la ventana de audio y proximamente
#de video
#**************************************************
class CallWindow(QWidget):
    # **************************************************
    #Constructor de la clase
    #**************************************************

    def __init__(self,my_socket):
        super(CallWindow, self).__init__()
        self.my_socket = my_socket
        self.video_size = QtCore.QSize(VIDEO_WIDTH, VIDEO_HEIGTH)
        self.client_side()
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
        self.setWindowTitle('Llamada')
        self.show()

    def closeEvent(self, event):
        event.accept()

    def client_side(self):
        self.capture = cv2.VideoCapture(0)
        #self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, VIDEO_WIDTH)
        #self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,VIDEO_HEIGTH)

        self.split = self.get_image_size(self.capture)
        splittedstr = [""]*self.split
        self.my_socket.sendto(str(self.split),(IP, CHAT_PORT))

        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start()

    def get_image_size(self,capture):
        _, frame = self.capture.read() #cv.QueryFrame(self.capture)
        jpgstring = frame.flatten().tostring ()
        #img = cv.fromarray(frame)
        #jpgstring = cv.EncodeImage(".jpeg", img).tostring()
        jpglen = len(jpgstring)
        split = jpglen/BUFFER_SIZE
        return split

    def display_video_stream(self):
            """Read frame from camera and repaint QLabel widget.
            """
            _, frame = self.capture.read() #cv.QueryFrame(self.capture)
            img = cv.fromarray(frame)
            jpg_instance = cv.EncodeImage(".jpeg", img)
            jpg_string = jpg_instance.tostring()

            jpglen = len(jpg_string)
            splittedstr = [""]*self.split
            for i in range(self.split-1):
                splittedstr[i] = jpg_string[BUFFER_SIZE*i:BUFFER_SIZE*(i+1)]
            splittedstr[self.split-1] = jpg_string[BUFFER_SIZE*(self.split-1):]
            for i in range(self.split):
                my_socket.sendto(splittedstr[i],(IP,CHAT_PORT))

            frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
            frame = cv2.flip(frame, 1)
            image = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                           frame.strides[0], QtGui.QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(image))


def main():
    global my_socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)#socket.SOCK_STREAM)
    my_socket.connect((IP, CHAT_PORT))
    app = QApplication(sys.argv)
    mainWindow = CallWindow(my_socket)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
