#! /usr/bin/env python

""" Ejemplo de clase servidor xmlrpc
para intercambio de audio """
from ServerGui import *
from signals import *
import pickle
import socket
import threading
from   PyQt4.QtGui import QApplication
import sys
import struct
import numpy

"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
BUFFER_SIZE = 1024
class Server:
    def __init__(self, signalManager):
        self.signalManager = signalManager
        self.my_socket = socket.socket(socket.AF_INET,  socket.SOCK_DGRAM,socket.IPPROTO_UDP)
        self.my_socket.bind((IP, CHAT_PORT))
        self.listening = True
        self.thread_connections = []
        self.play_video = True


    def run(self):
        queue = []
        split = int(self.my_socket.recvfrom(BUFFER_SIZE)[0])
        imstr = [""] * split
        self.signalManager.create_window_signal(self,queue,None)

        while self.listening:
            for i in range(split):
                imstr[i], addr = self.my_socket.recvfrom(BUFFER_SIZE * 872)

            jpgstring = "".join(imstr)

            queue.append(jpgstring)

    def stop_server(self):
        self.listening = False
        self.my_socket.close()


class ClientConectionThread(threading.Thread):

    def __init__(self, socket,signalManager,queue,split):
        threading.Thread.__init__(self)
        self.signalManager = signalManager
        self.split = split
        self.socket = socket
        self.queue = queue
        print "[+] New thread started for "
        self.listening = True

    def run(self):
        data = ""
        imstr = [""] * self.split
        while self.listening:
            for i in range(self.split):
                imstr[i], addr = self.socket.recvfrom(BUFFER_SIZE * 872)

            jpgstring = "".join(imstr)

            self.queue.append(jpgstring)


    def finish_call(self):
        self.listening = False

def main ():
    print "Construyendo el servidor"
    signalManager = SignalManager()
    server = Server(signalManager)
    api_server_thread = threading.Thread(target=server.run)
    api_server_thread.start()
    app = QApplication(sys.argv)
    mainWindow = DummyClass()
    app.exec_()



if __name__ == '__main__':
    main()
