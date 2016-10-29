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
import cv2.cv as cv

import pickle
import sys
import struct
import base64
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,QtCore

##Uso de https://docs.python.org/2/library/struct.html

""" Constantes de tpc """
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

my_socket = ''
def get_cap_size(capture):
    img = cv.QueryFrame(capture)

    jpgstring = cv.EncodeImage(".jpeg", img).tostring()
    jpglen = len(jpgstring)
    split = jpglen/BUFFER_SIZE
    return split
def main ():
    global my_socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM,socket.IPPROTO_UDP)#socket.SOCK_STREAM)
    my_socket.connect((TCP_IP, TCP_PORT))
    capture = cv.CaptureFromCAM(0)


    address = (TCP_IP,TCP_PORT)
    split = get_cap_size(capture)
    splittedstr = [""]*split
    my_socket.sendto(str(split),address)
    while(True):
        img = cv.QueryFrame(capture)

        jpgstring = cv.EncodeImage(".jpeg", img).tostring()
        jpglen = len(jpgstring)
        for i in range(split-1):
            splittedstr[i] = jpgstring[jpglen/split*i:jpglen/split*(i+1)]

        splittedstr[split-1] = jpgstring[jpglen/split*(split-1):]
        for i in range(split):
            my_socket.sendto(splittedstr[i],address)
        if cv.WaitKey(10) == 27:
            break


    cap.release()
    cv2.destroyAllWindows()
    my_socket.close()



main()
