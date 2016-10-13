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
import pyaudio
import numpy
CHUNK = 1024
CHANNELS = 1
RATE = 44100
DELAY_SECONDS = 5

frames = []


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
p = pyaudio.PyAudio()
FORMAT = p.get_format_from_width(2)
stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    output=True,
                    frames_per_buffer=CHUNK)


while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    stream.write(data)
 
conn.close()
