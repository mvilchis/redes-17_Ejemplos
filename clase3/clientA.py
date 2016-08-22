#! /usr/bin/env python


#####################################################
# PURPOSE:                                          #
#                                                   #
# Vilchis Dominguez Miguel Alonso                   #
#       <mvilchis@ciencias.unam.mx>                 #
#                                                   #
# Notes: installar pyaudio (python-pyaudio)         #
#        installar  jackd qjackctl                  #
#                                                   #
# Copyright   31-08-2015                            #
#                                                   #
# Distributed under terms of the MIT license.       #
#####################################################

"""
Graba audio y manda el stream

"""

import multiprocessing as mp
import time
import xmlrpclib
CHUNK = 1024
CHANNELS = 1
RATE = 44100
RECORD_SECONDS = 2


def feed_queue(q):
    import pyaudio
    import numpy

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
        q.put(data_ar)


queue = mp.Queue()
p = mp.Process(target=feed_queue, args=(queue,))
p.start()

proxy = xmlrpclib.ServerProxy("http://localhost:8000/",allow_none = False)
import numpy
while True:
    d = queue.get()
    data = xmlrpclib.Binary(d)
    proxy.playAudio(data)
