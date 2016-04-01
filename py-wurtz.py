#!/usr/bin/python3

import pyaudio
import numpy as np

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44200
RECORD_SECONDS = 5

def createStream():
    p = pyaudio.PyAudio()
    stream = p.open(
        format=p.get_format_from_width(WIDTH),
        channels=CHANNELS,
        rate=RATE,
        input=True,
        output=True,
        frames_per_buffer=CHUNK
    )
    return stream, p

stream, p = createStream()
print("* listening")
try:
    while True:
        data = stream.read(CHUNK)
        signal = np.array([np.fromstring(data, 'Float32')], dtype=float)
        fourier = np.fft.fft(signal)
        freq = np.fft.fftfreq(signal.size, d = 1 / RATE)
        stream.write(data, CHUNK)
except (KeyboardInterrupt, SystemExit):
    print("* done")
    stream.stop_stream()
    stream.close()
    p.terminate()
