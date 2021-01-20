import librosa
import soundfile as sf

filepath = 'result.wav'
analyzed_filepath = 'modified_result.wav'

speed = 0.80    # The higher, the faster and vice-versa
                # speed > 1.0 is faster and speed < 1.0 is slower

y, sr = librosa.load(filepath, sr=None)
y_duration = y.shape[0] / sr
y_stretched = librosa.effects.time_stretch(y, speed)
y_stretched_samples = y_stretched.shape[0]
y_stretched_duration = y_duration / speed
y_stretched_sr = y_stretched_samples / y_stretched_duration

# print(y_duration, y_stretched_duration, y_stretched_samples, y_stretched_sr)

sf.write(analyzed_filepath, y_stretched, sr, format='wav')