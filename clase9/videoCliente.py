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
Cliente por localhost que después de conectarse
manda video
"""
import socket
import cv2
import pickle
import sys
import struct

##Uso de https://docs.python.org/2/library/struct.html
""" Constantes de tpc """
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

my_socket = ''

def main ():
    global my_socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((TCP_IP, TCP_PORT))
    cap = cv2.VideoCapture(0)

    while(True):
        ret, frame = cap.read()
        cv2.imshow('Cliente',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        data = pickle.dumps(frame)
        my_socket.sendall(struct.pack("L", len(data)) + data)
    cap.release()
    cv2.destroyAllWindows()
    my_socket.close()



main()
