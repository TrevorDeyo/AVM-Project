import os
from alive_progress import alive_bar; import time

import soundfile as sf
import pyloudnorm as pyln


directory_path = r'C:\Users\tdeyo\Desktop\Code\AVM-Project\2trimmed_audio'

with alive_bar() as bar:
    for filename in os.listdir(directory_path):
        data, rate = sf.read(filename) # load audio (with shape (samples, channels))
        

        if len(data.shape) > 1:
        
            print(filename)
            print(data.shape)
            print('wavfile.read data:', data)
        
            meter = pyln.Meter(rate)                   # create BS.1770 meter
            loudness = meter.integrated_loudness(data) # measure loudness
        
            print('sf.read data: ', data)

            print(loudness)
        
        
        bar()