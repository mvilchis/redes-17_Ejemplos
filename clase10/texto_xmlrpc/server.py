#! /usr/bin/env python

""" Ejemplo de clase servidor xmlrpc
para intercambio de mensajes """
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)
class Server:
    def __init__(self, signalManager):
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

    """Funcion que ofrece el servidor esta funcion agregara a la interfaz
    grafica el texto que el cliente envie """
    def sendMessage_remote(self, message):
        text = message
        self.signalManager.add_message_signal("Mandaron: " + text + "\n")
