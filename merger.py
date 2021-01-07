import os
import librosa
import numpy as np
import librosa.display
import soundfile as sf

# Assuming there is a folder in current directory named "static" that contains the .wav files
# This will join all the files in the default sorting order and create "result.wav"
# I believe the sample rate should be the same for each file

files = os.listdir("static")

z = None

for file in files:
    x, sr = librosa.load("static/" + file)
    if z is None:
        z = x
    else:
        z = np.append(z, x)
    
sf.write('result.wav', z, sr)