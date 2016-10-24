#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import xmlrpclib

CHAT_PORT = 5000
IP = '127.0.0.1'
def main(argv):
    mensaje = argv[0]
    proxy_server = xmlrpclib.Server('http://' + IP + ':' + str(CHAT_PORT), allow_none=True)
    proxy_server.sendMessage_remote(mensaje)


if __name__ == '__main__':
    #El primer parametro es el nombre del programa
    main(sys.argv[1:])
