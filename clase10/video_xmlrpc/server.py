#! /usr/bin/env python

""" Ejemplo de clase servidor xmlrpc
para intercambio de audio """
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from ServerGui import *
from signals import *
import pickle
import threading
from   PyQt4.QtGui import QApplication
import sys


"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
WIDTH_FORMAT = 1
CHUNK = 1024
CHANNELS = 1
RATE = 44100

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
class Server:
    def __init__(self, signalManager):
        self.signalManager = signalManager
        self.server = SimpleXMLRPCServer((IP, CHAT_PORT), requestHandler=RequestHandler, allow_none=True)
        # Agregamos las funciones al servidor xmlrpc
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.functionWrapper = FunctionWrapper(signalManager)
        self.server.register_instance(self.functionWrapper)

    def run(self):
        self.server.serve_forever()

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()

class FunctionWrapper:
    def __init__(self, signalManager):
        self.signalManager = signalManager
         #Inicializacion de video
        self.is_record = False
        self.queue = []

    def play_video_remote(self,data):
        frame = pickle.loads(data)
        self.queue.append(frame)
        if not self.is_record:
            self.is_record = True
            self.signalManager.create_window_signal(self.queue)


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
