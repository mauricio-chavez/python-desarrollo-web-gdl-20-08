import os
import datetime
import json

directory = './archivos'
dirfiles = os.listdir(directory)
files = []

for file in dirfiles:
    filepath = os.path.join(directory, file)

    name = file
    size = '{} bytes'.format(os.path.getsize(filepath))

    timestamp = os.path.getmtime(filepath)
    date = datetime.datetime.fromtimestamp(timestamp).strftime('%c')

    files.append({
        'name': name,
        'size': size,
        'date': date
    })

with open('files.json', 'w') as jsonfile:
    json.dump(files, jsonfile, indent=2)
