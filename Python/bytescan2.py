import sys
import os
import mmap
import re

bytestr = b'\x48\x8d\x45\xf0\x4c\x39\xf8\x72'

def scanfiles(path):
    for entry in os.scandir(path):
        if entry.is_file():
            filename = os.path.join(path, entry.name)
            with open(filename, "rb") as f:
                if os.fstat(f.fileno()).st_size > 0:
                    with mmap.mmap(f.fileno(), 0, 
                           access=mmap.ACCESS_READ) as m:
                        match = re.search(bytestr, m)
                        if match:
                            print(bytestr.hex() + " found in " + filename)
        else:
            scanfiles(entry.path)


""" Main Program """

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <path>")
    exit(0)

rootpath = sys.argv[1]
scanfiles(rootpath)
