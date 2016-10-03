#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE:                                          #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes:                                            #
#                                                   #
# Copyright   28-09-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

"""
Servidor que por localhost al recibir una peticion 
de conexión regresa que si se puede conectar, al recibir
una imagen la despliega.
"""

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    if data == "Me puedo conectar?":
        conn.send("Si te puedes conectar") 
conn.close()
