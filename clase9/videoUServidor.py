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
    data = ""
    split = int(my_socket.recvfrom(BUFFER_SIZE)[0])
    imstr = [""] * split
    while True:
        for i in range(split):
            imstr[i], addr = my_socket.recvfrom(BUFFER_SIZE * 32)
        jpgstring = "".join(imstr)
        narray = numpy.fromstring(jpgstring, dtype="uint8")
        decimg = cv2.imdecode(narray, 1)

        try:
            cv2.imshow("camara servidor", decimg)
        except Exception as e:
            print "show error"
            continue
        if  cv2.waitKey(10) == 27:
            break

    cv2.destroyAllWindows()

main()
