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
Cliente por localhost que después de conectarse
una peticion de conexión y recibe una imagen.
"""
import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send("Me puedo conectar?")
data = s.recv(BUFFER_SIZE)
s.close()

print "El servidor me dijo:", data
