#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""**************************************************
Clase que genera un proxy para poder hacer uso de los 
procedimientos remotos que ofrece la api del contacto
 **************************************************"""
import xmlrpclib
import sys
sys.path.insert(0, './servidor')
from Constants import *
from AuxiliarFunctions import *
class MyApiClient:
    def __init__(self, contact_port = None):
        if contact_port:
            self.server = xmlrpclib.Server('http://localhost' +':'+str(contact_port), allow_none = True)


def main(args):
   contact_port = int(args[0])
   api_client = MyApiClient(contact_port = contact_port).server
   api_client.sendMessage_wrapper("Mensaje de cliente a Servidor")
if __name__ == '__main__':
   main(sys.argv[1:])

