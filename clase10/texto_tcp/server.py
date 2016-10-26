#! /usr/bin/env python

""" Ejemplo de clase servidor xmlrpc
para intercambio de mensajes """
import socket
import threading
"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
BUFFER_SIZE = 20

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
            newthread = ClientConectionThread(ip, port, clientsock,self.signalManager)
            newthread.start()
            self.thread_connections.append(newthread)

    def stop_server(self):
        self.listening = False
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        my_socket.connect((IP, CHAT_PORT))
        my_socket.sendall('')
        my_socket.close()
        for thread in self.thread_connections:
            thread.join()

class ClientConectionThread(threading.Thread):

    def __init__(self, ip, port, socket,signalManager):
        threading.Thread.__init__(self)
        self.signalManager = signalManager
        self.ip = ip
        self.port = port
        self.socket = socket
        print "[+] New thread started for "+ip+":"+str(port)

    def run(self):
        while True:
            data = self.socket.recv(BUFFER_SIZE)
            if not data: break
            self.display_text(data)
        self.socket.close()

    def display_text(self, message):
        text = message
        self.signalManager.add_message_signal("Mandaron: " + text + "\n")
