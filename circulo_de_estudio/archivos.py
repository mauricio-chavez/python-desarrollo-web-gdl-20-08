import os
import datetime

if __name__ == '__main__':
    size = os.path.getsize('./args_kwargs.py')
    print('El tamaño en bytes es', size)

    last_modified_timestamp = os.path.getmtime('./args_kwargs.py')
    last_modified = datetime.datetime.fromtimestamp(last_modified_timestamp)
    print('La última modificación fue', last_modified)
