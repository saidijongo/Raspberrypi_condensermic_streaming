import pyaudio
import numpy as np

# Constants
FORMAT = pyaudio.paFloat32
CHANNELS = 1
RATE = 44100
CHUNK_SIZE = 1024

# Initialize PyAudio
audio = pyaudio.PyAudio()

# pyaudio.PyAudio().get_device_info_by_index()
#pyaudio.PyAudio().get_device_info_by_name()

#audio stream for input and output
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, output=True, frames_per_buffer=CHUNK_SIZE)

#reading audio data from the microphone and output it to the speaker
while True:
    # Read audio data from the input stream
    input_data = stream.read(CHUNK_SIZE)

    # Processing the audio data
    processed_data = np.frombuffer(input_data, dtype=np.float32)
    
    # Output the processed audio data to the output stream
    stream.write(processed_data.tobytes())

# Cleanup
stream.stop_stream()
stream.close()
audio.terminate()
