import os
from alive_progress import alive_bar; import time

from pydub import AudioSegment, silence

directory_path = r"C:\\Users\\tdeyo\\Desktop\\Code\\AVM-Project\\1raw"
output = "C:\\Users\\tdeyo\\Desktop\\Code\\AVM-Project\\2trimmed_audio\\"

file_count = sum(len(files) for _, _, files in os.walk(directory_path))

counter = 0


with alive_bar(file_count) as bar:
    for root, dirs, files in os.walk(directory_path):
        for file in files:

            file_path = os.path.join(root, file)
            print(file_path)
            original_sound = AudioSegment.from_file(file_path)
            audio_segments = silence.split_on_silence(original_sound,
                                                    min_silence_len = 2000,
                                                    silence_thresh = -45,
                                                    keep_silence = 500,)
            processed_sound = sum(audio_segments)

            processed_sound.export(f"{output}{counter}.wav", format="wav")
            counter += 1
            bar()