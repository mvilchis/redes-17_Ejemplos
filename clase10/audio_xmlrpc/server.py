#! /usr/bin/env python

""" Ejemplo de clase servidor xmlrpc
para intercambio de audio """
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import pyaudio
import threading
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
    def __init__(self):
        self.server = SimpleXMLRPCServer((IP, CHAT_PORT), requestHandler=RequestHandler, allow_none=True)
        # Agregamos las funciones al servidor xmlrpc
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.functionWrapper = FunctionWrapper()
        self.server.register_instance(self.functionWrapper)

    def run(self):
        self.server.serve_forever()

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()

class FunctionWrapper:
    def __init__(self):
        self.pyaudio_instance = pyaudio.PyAudio()
        FORMAT = self.pyaudio_instance.get_format_from_width(WIDTH_FORMAT)
        self.stream = self.pyaudio_instance.open(format=FORMAT,
                                                 channels=CHANNELS,
                                                 rate=RATE,
                                                 output=True,
                                                 frames_per_buffer=CHUNK)

    def play_audio_remote(self, audio):
        if not self.stream.is_active():
            self.stream.start_stream()
        data = audio.data
        self.stream.write(data)

def main ():
    print "Construyendo el servidor"
    server = Server()
    api_server_thread = threading.Thread(target=server.run)
    api_server_thread.start()



if __name__ == '__main__':
    main()
