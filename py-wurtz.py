#!/usr/bin/python3

import pyaudio

CHUNK = 1024
WIDTH = 2
CHANNELS = 2
RATE = 44200
RECORD_SECONDS = 5


p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(WIDTH),
                channels=CHANNELS,
                rate=RATE,
                input=True,
                output=True,
                frames_per_buffer=CHUNK
)

print("* recording")

while True:
    data = stream.read(CHUNK)
    stream.write(data, CHUNK)

print("* done")
stream.stop_stream()
stream.close()
p.terminate()
