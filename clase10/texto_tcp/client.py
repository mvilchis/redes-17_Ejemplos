#! /usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import xmlrpclib
import socket

CHAT_PORT = 5000
IP = '127.0.0.1'
BUFFER_SIZE = 20
def main(argv):
    mensaje = argv[0]
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, CHAT_PORT))
    counter = 0
    for _ in range(len(mensaje) / BUFFER_SIZE):
        base = counter*BUFFER_SIZE
        my_socket.sendall(mensaje[base: base +BUFFER_SIZE])
        counter += 1

    base = counter*BUFFER_SIZE
    my_socket.sendall(mensaje[base:])
    my_socket.close()


if __name__ == '__main__':
    #El primer parametro es el nombre del programa
    main(sys.argv[1:])
