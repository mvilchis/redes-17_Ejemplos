#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from SimpleXMLRPCServer import SimpleXMLRPCServer
from threading import Thread
from AuxiliarFunctions import * 
from Constants import *
class MyApiServer(Thread):

    def __init__(self, my_port = None):
        super(MyApiServer, self).__init__()
        port = my_port if my_port else CHAT_PORT
        self.server = SimpleXMLRPCServer(("localhost", int(port)), allow_none = True)
        self.server.register_introspection_functions()
        self.server.register_multicall_functions()
        self.funtionWrapper = FunctionWrapper()
        self.server.register_instance(self.funtionWrapper)

    def run(self):
        self.server.serve_forever()

    def stop_server(self):
        self.server.shutdown()
        self.server.server_close()

class FunctionWrapper:
    """ **************************************************
    Constructor de la clase
    ************************************************** """
    def __init__(self):
        print "Se construye las funciones"
   
    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para mostrar el texto en nuestra pantalla.
    ************************************************** """
    def sendMessage_wrapper(self, message):
        print "El:"+ message+"\n"
    """ **************************************************
    Procedimiento que ofrece nuestro servidor, este metodo sera llamado
    por el cliente con el que estamos hablando, debe de
    hacer lo necesario para regresar el texto
    ************************************************** """
    def echo(self, message):
        return message


def main(args):
   myPort = int(args[0])
   api_server_thread = MyApiServer(myPort)
   api_server_thread.start()
   import time
   #Que se ejecute 2 segundos el servidor
   time.sleep(2)
   #Detenemos el thread del servidor
   print "Fin del servidor"
   api_server_thread.stop_server()
   api_server_thread.join()
   print "Fin del programa"
if __name__ == '__main__':
   main(sys.argv[1:])
