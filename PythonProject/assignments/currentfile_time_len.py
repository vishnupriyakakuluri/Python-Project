import os
from datetime import datetime

directory='.'
files=os.listdir(directory)
print(files)
print(len(files))
file_info = []

for filename in files:
    filepath = os.path.join(directory, filename)
    if os.path.isfile(filepath):
        creation_time = os.path.getctime(filepath)
        creation_time_str = datetime.fromtimestamp(creation_time).strftime('%Y-%m-%d %H:%M:%S')
        file_info.append((filename, creation_time_str))

for filename, creation_time in file_info:
    print(f"Filename: {filename}, Created: {creation_time}")

print(f"\nTotal number of files: {len(file_info)}")