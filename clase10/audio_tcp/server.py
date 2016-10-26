#! /usr/bin/env python

""" Ejemplo de clase servidor xmlrpc
para intercambio de mensajes """
import socket
import threading
import pyaudio
from   PyQt4.QtGui import QApplication
import sys

from signals import *
from call_window import *
"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
BUFFER_SIZE = 1024
CHUNK = 1024
CHANNELS = 1
RATE = 44100

class Server:
    def __init__(self, signalManager):
        self.signalManager = signalManager
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.bind((IP, CHAT_PORT))
        self.my_socket.listen(0)
        pyaudio_instance = pyaudio.PyAudio()
        FORMAT = pyaudio_instance.get_format_from_width(2)
        self.stream = pyaudio_instance.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        output=True,
                        frames_per_buffer=CHUNK)

        self.listening = True
        self.thread_connections = []


    def run(self):
        while self.listening:
            (clientsock, (ip, port)) = self.my_socket.accept()
            newthread = ClientConectionThread(ip, port, clientsock,self.signalManager,self.stream)
            newthread.start()
            self.thread_connections.append(newthread)
            self.signalManager.create_window_signal(self,newthread)

    def stop_server(self):
        self.listening = False
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((IP, CHAT_PORT))
        my_socket.sendall('')
        my_socket.close()
        for thread in self.thread_connections:
            thread.join()

class ClientConectionThread(threading.Thread):

    def __init__(self, ip, port, socket,signalManager,stream):
        threading.Thread.__init__(self)
        self.signalManager = signalManager
        self.ip = ip
        self.port = port
        self.socket = socket
        self.stream = stream
        print "[+] New thread started for "+ip+":"+str(port)
        self.listening = True

    def run(self):
        while self.listening:
            data = self.socket.recv(BUFFER_SIZE)
            if not data: break
            self.stream.write(data)
        self.socket.close()

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
