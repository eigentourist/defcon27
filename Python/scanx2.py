import sys
import os
import mmap
import re
import hashlib

def hashfile(filename):
    with open(filename, "rb") as f:
        if os.fstat(f.fileno()).st_size > 0:
            with mmap.mmap(f.fileno(), 0, 
             access=mmap.ACCESS_READ) as m:
                h = hashlib.sha256()
                h.update(m)
                print(filename + " sha256: " + h.hexdigest())



bytestr = b'\x6f\x73\x2e\x70\x61\x74\x68\x2e'

def scanfile(filename):
    with open(filename, "rb") as f:
        if os.fstat(f.fileno()).st_size > 0:
            with mmap.mmap(f.fileno(), 0, 
             access=mmap.ACCESS_READ) as m:
                match = re.search(bytestr, m)
                if match:
                    print(bytestr.hex() + " found in " + filename)


def scanfiles(path, fn):
    for entry in os.scandir(path):
        if entry.is_file():
            fn(os.path.join(path, entry.name))
        elif entry.is_dir:
            scanfiles(entry.path)


""" Main Program """

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <path>")
    exit(0)

rootpath = sys.argv[1]
scanfiles(rootpath, hashfile)