#! /usr/bin/env python
# -*- coding: utf-8 -*-


#####################################################
# PURPOSE:Funciones auxiliares                      #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
#                                                   #
# Copyright   16-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################
import socket


"""**************************************************
Metodo auxiliar que se conecta a internet para
conocer nuestra ip actual
**************************************************"""

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return "%s"% (s.getsockname()[0]) 
