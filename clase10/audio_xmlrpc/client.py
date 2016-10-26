#! /usr/bin/env python
# -*- coding: utf-8 -*-

""" Ejemplo de cliente  xmlrpc
para intercambio de audio """
import sys
import xmlrpclib
import pyaudio
import time
import numpy as np
"""        Area de constantes      """
CHAT_PORT = 5000
IP = '127.0.0.1'
WIDTH_FORMAT = 1
CHUNK = 1024
CHANNELS = 1
RATE = 44100

proxy_server = None

""" Funcion que sera llamada para enviar audio de manera continua """
def callback(in_data, frame_count, time_info, flag):
    global proxy_server
    audio_data = np.fromstring(in_data, dtype=np.float32)
    #Aqui manda audio
    #Revisamos si podemos mandar audio
    if proxy_server.can_play_audio():
        binary_data = xmlrpclib.Binary(audio_data)
        proxy_server.play_audio_remote(binary_data)
    else:
        sys.exit(0)
    #Termina de mandar audio
    return (audio_data, pyaudio.paContinue)

def main():
    global proxy_server
    proxy_server = xmlrpclib.Server('http://' + IP + ':' + str(CHAT_PORT), allow_none=True)
    pyaudio_instance = pyaudio.PyAudio()
    pyaudio_format = pyaudio_instance.get_format_from_width(WIDTH_FORMAT)
    stream = pyaudio_instance.open(format=pyaudio_format,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK,
                        stream_callback = callback)
    stream.start_stream()
    while True:
        time.sleep(0.1)


if __name__ == '__main__':
    main()
