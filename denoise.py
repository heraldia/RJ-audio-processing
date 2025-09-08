import noisereduce as nr
import scipy.io.wavfile as wavfile
import os

rate, data = wavfile.read('buffer.wav')

# Apply noise reduction
reduced_noise = nr.reduce_noise(y=data, sr=rate, prop_decrease=0.5)

# Save the output file
wavfile.write('output_denoised.wav', rate, reduced_noise)
os.system("play output_denoised.wav")
