#! /usr/bin/env python

""" Ejemplo de clase servidor xmlrpc
para intercambio de audio """
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
from call_window import *
from signals import *
import pyaudio
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
        self.pyaudio_instance = pyaudio.PyAudio()
        FORMAT = self.pyaudio_instance.get_format_from_width(WIDTH_FORMAT)
        self.stream = self.pyaudio_instance.open(format=FORMAT,
                                                 channels=CHANNELS,
                                                 rate=RATE,
                                                 output=True,
                                                 frames_per_buffer=CHUNK)
        self.flag_play_audio= True
        self.show_window = False
    def can_play_audio(self):
        return self.flag_play_audio


    def play_audio_remote(self, audio):

        if self.flag_play_audio:
            if not self.show_window:
                self.show_window = True
                self.signalManager.create_window_signal(self)
            data = audio.data
            self.stream.write(data)

    def finish_call(self):
        self.stream.stop_stream()
        self.stream.close()
        self.flag_play_audio= False


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
