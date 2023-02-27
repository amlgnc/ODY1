import requests
import zipfile
import io
import os


def help():
    print("todo")


def dlSFML():
    print("dl GCC 7.3.0 MinGW (DW2) - 32-bit")
    r = requests.get("https://www.sfml-dev.org/files/SFML-2.5.1-windows-gcc-7.3.0-mingw-32-bit.zip")
    z = zipfile.ZipFile(io.BytesIO(r.content))
    z.extractall("")
    os.rename("SFML-2.5.1","SFML")


while True:
    cmd = input()
    if cmd == 'exit':
        exit()
    elif cmd == "help":
        help()
    elif cmd == "dl":
        dlSFML()
