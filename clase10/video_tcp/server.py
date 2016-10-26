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


"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
BUFFER_SIZE = 1024
class Server:
    def __init__(self, signalManager):
        self.signalManager = signalManager
        self.my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.my_socket.bind((IP, CHAT_PORT))
        self.my_socket.listen(0)
        self.listening = True
        self.thread_connections = []


    def run(self):
        while self.listening:
            (clientsock, (ip, port)) = self.my_socket.accept()
            queue = []
            newthread = ClientConectionThread(ip, port, clientsock,self.signalManager,queue)
            newthread.start()
            self.thread_connections.append(newthread)
            self.signalManager.create_window_signal(queue,newthread)

    def stop_server(self):
        self.listening = False
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((IP, CHAT_PORT))
        my_socket.sendall('')
        my_socket.close()
        for thread in self.thread_connections:
            thread.join()

class ClientConectionThread(threading.Thread):

    def __init__(self, ip, port, socket,signalManager,queue):
        threading.Thread.__init__(self)
        self.signalManager = signalManager
        self.ip = ip
        self.port = port
        self.socket = socket
        self.queue = queue
        print "[+] New thread started for "+ip+":"+str(port)
        self.listening = True

    def run(self):
        data = ""
        payload_size = struct.calcsize("L")

        while self.listening:
            while len(data) < payload_size:
                data += self.socket.recv(BUFFER_SIZE)
            packed_msg_size = data[:payload_size]

            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]

            while len(data) < msg_size:
                data += self.socket.recv(BUFFER_SIZE)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frame=pickle.loads(frame_data)
            self.queue.append(frame)
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
