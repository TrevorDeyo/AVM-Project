import os
import subprocess
from alive_progress import alive_bar
import time

root = r"C:\Users\tdeyo\Desktop\Code\AVM Project\clear_untrimed_voices"

file_count = sum([len(files) for path, subdirs, files in os.walk(root)])

with alive_bar(file_count, title="Processing audio files") as bar:
    for path, subdirs, files in os.walk(root):
        for file in files:
            file_path = os.path.join(path, file)
            command = f'ffmpeg -i "{file_path}" -af silenceremove=stop_periods=-1:stop_duration=2:stop_threshold=-50dB -f null -'
            subprocess.run(command, capture_output=False)
            #print(file_path)
            #print(command)
            bar()