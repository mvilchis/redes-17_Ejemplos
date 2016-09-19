#! /usr/bin/env python
# -*- coding: utf-8 -*-
import xmlrpclib
import sys
class MyApiClient:
    def __init__(self):
        self.server = xmlrpclib.ServerProxy('http://localhost:8000', allow_none = True)

def main(args):
    api_client = MyApiClient().server
    api_client.create_remote_window()
if __name__ == '__main__':
    main(sys.argv[1:])


