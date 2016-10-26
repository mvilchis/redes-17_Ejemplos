#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Ejemplo de cliente  xmlrpc
para intercambio de audio """
import sys
import socket
import pyaudio
import time
import numpy as np
"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
BUFFER_SIZE = 1024

WIDTH_FORMAT = 2
CHUNK = 1024
CHANNELS = 1
RATE = 44100

my_socket = None

""" Funcion que sera llamada para enviar audio de manera continua """
def callback(in_data, frame_count, time_info, flag):
    global my_socket
    audio_data = np.fromstring(in_data, dtype=np.float32)
    #Aqui manda audio
    my_socket.sendall(audio_data)
    #Termina de mandar audio
    return (audio_data, pyaudio.paContinue)

def main():
    global my_socket
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((IP, CHAT_PORT))
    pyaudio_instance = pyaudio.PyAudio()
    pyaudio_format = pyaudio_instance.get_format_from_width(2)
    stream = pyaudio_instance.open(format=pyaudio_format,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        stream_callback = callback)
    stream.start_stream()
    while True:
        time.sleep(0.1)
    my_socket.close()


if __name__ == '__main__':
    main()
