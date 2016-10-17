#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE:Ejemplo de video con tpc                  #
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
de reproduce el video
"""

import socket
import cv2
import numpy
import pickle
import struct

""" Constantees de tpc """
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
my_socket = ''

def main():
    global my_socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)#socket.SOCK_STREAM)
    my_socket.bind((TCP_IP, TCP_PORT))
    #my_socket.listen(10)
    #conn, addr = my_socket.accept()
    payload_size = struct.calcsize("L")
    data = ""
    while True:
        #Recibimos el frame completo
        while len(data) < payload_size:
            #data += conn.recv(BUFFER_SIZE)
            data+= my_socket.recvfrom(BUFFER_SIZE)[0]
        packed_msg_size = data[:payload_size]

        data = data[payload_size:]
        msg_size = struct.unpack("L", packed_msg_size)[0]

        while len(data) < msg_size:
            #data += conn.recv(BUFFER_SIZE)
            data += my_socket.recvfrom(BUFFER_SIZE)[0]

        frame_data = data[:msg_size]
        data = data[msg_size:]

        frame=pickle.loads(frame_data)
        cv2.imshow('Servidor',frame)
        cv2.waitKey(10)

    cv2.destroyAllWindows()

main()
