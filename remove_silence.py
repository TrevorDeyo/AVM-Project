import os
import subprocess
from alive_progress import alive_bar
import time

# Import required libraries
from pydub.silence import split_on_silence
from pydub import AudioSegment, effects 
from scipy.io.wavfile import read, write
            

root = r"C:\Users\tdeyo\Desktop\Code\AVM Project\clear_untrimed_voices"

file_count = sum([len(files) for path, subdirs, files in os.walk(root)])

with alive_bar(file_count, title="Processing audio files") as bar:
    for path, subdirs, files in os.walk(root):
        for file in files:
            # Pass audio path
            path = os.path.join(path, file)

            rate, audio = read(path)
            # make the audio in pydub audio segment format
            aud = AudioSegment(audio.tobytes(),frame_rate = rate, sample_width = audio.dtype.itemsize, channels = 1)
            # use split on sience method to split the audio based on the silence, 
            # here we can pass the min_silence_len as silent length threshold in ms and intensity thershold
            audio_chunks = split_on_silence(aud, min_silence_len = 2000, silence_thresh = -45, keep_silence = 500,)
            #audio chunks are combined here
            audio_processed = sum(audio_chunks)
            audio_processed = np.array(audio_processed.get_array_of_samples())
            #Note the processed audio rate is not the same - it would be 1K
            bar()