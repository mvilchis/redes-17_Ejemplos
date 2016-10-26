#! /usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import QMainWindow, QWidget, QLabel, QPixmap,QWidget,QApplication
import cv2
import sys
import xmlrpclib
import pickle
"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
### Video
CAM_NUMBER= 0
VIDEO_WIDTH = 320
VIDEO_HEIGTH = 240
#**************************************************
#Clase que representa la ventana de audio y proximamente
#de video
#**************************************************
class CallWindow(QWidget):
    # **************************************************
    #Constructor de la clase
    #**************************************************

    def __init__(self,proxy_server):
        super(CallWindow, self).__init__()
        self.proxy_server = proxy_server
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
        self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, VIDEO_WIDTH)
        self.capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT,VIDEO_HEIGTH)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.display_video_stream)
        self.timer.start()


    def display_video_stream(self):
            """Read frame from camera and repaint QLabel widget.
            """
            _, frame = self.capture.read()
            data = pickle.dumps(frame)
            self.proxy_server.play_video_remote(data)
            frame = cv2.cvtColor(frame, cv2.cv.CV_BGR2RGB)
            frame = cv2.flip(frame, 1)
            image = QtGui.QImage(frame, frame.shape[1], frame.shape[0],
                           frame.strides[0], QtGui.QImage.Format_RGB888)
            self.image_label.setPixmap(QPixmap.fromImage(image))


def main():
    proxy_server = xmlrpclib.Server('http://' + IP + ':' + str(CHAT_PORT), allow_none=True)
    app = QApplication(sys.argv)
    mainWindow = CallWindow(proxy_server)
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
