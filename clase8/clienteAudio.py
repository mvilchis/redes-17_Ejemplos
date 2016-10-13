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
import pyaudio
import numpy
CHUNK = 1024
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2



TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
p = pyaudio.PyAudio()
FORMAT = p.get_format_from_width(2)
stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

while True:
        frame = []
        for i in range(0,int(RATE/CHUNK *RECORD_SECONDS)):
            frame.append(stream.read(CHUNK))
        data_ar = numpy.fromstring(''.join(frame),  dtype=numpy.uint8)
        s.sendall(data_ar) 

s.close()

