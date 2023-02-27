import requests
import zipfile
import shutil
import io
import os


def dl(name, href):
    print(f"\n> import {name}")
    r = requests.get(href)
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall('')
    if os.path.exists('SFML'):
        shutil.rmtree('SFML')
    os.rename('SFML-2.5.1','SFML')
    exit()


# Main loop
while True:
    cmd = input()
    if cmd == 'exit':
        exit()
    elif cmd == 'win':
        dl('GCC 7.3.0 MinGW (DW2) - 32-bit', 'https://www.sfml-dev.org/files/SFML-2.5.1-windows-gcc-7.3.0-mingw-32-bit.zip')
    elif cmd == 'lin':
        print("\n> No.\n") # TODO
    elif cmd == 'mac':
        print("\n> No.\n") # TODO
    else:
        print("\n> No.\n")
