# Hacking With Monads:
# Functional Programming for the Blue Team
# A Def Con 27 Workshop August 10, 2019

# Recursively compute file hashes using scandir
# Modeled after bytescan2.py

import sys
import os
import mmap
import hashlib


def hashfiles(path):
    for entry in os.scandir(path):
        if entry.is_file():
            filename = os.path.join(path, entry.name)
            with open(filename, "rb") as f:
                if os.fstat(f.fileno()).st_size > 0:
                    with mmap.mmap(f.fileno(), 0, 
                           access=mmap.ACCESS_READ) as m:
                        h = hashlib.sha256()
                        h.update(m)
                        print(filename + " sha256: " + h.hexdigest())
        else:
            hashfiles(entry.path)


if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <path>")
    exit(0)

rootpath = sys.argv[1]
hashfiles(rootpath)
