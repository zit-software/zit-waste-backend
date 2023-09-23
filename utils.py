import os
import zipfile
import time
import io

if not os.path.exists("tmp"):
    os.mkdir("tmp")


def zipdir(path: str, ziph: zipfile.ZipFile) -> None:
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file),
                       os.path.relpath(os.path.join(root, file),
                                       os.path.join(path, '..')))


def zip(path: str) -> io.BufferedReader:
    filename = f'tmp/{time.time()}.zip'

    with zipfile.ZipFile(filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        zipdir(path, zipf)

    zipf.close()

    zipf = open(filename, 'rb')

    os.remove(filename)

    return zipf
