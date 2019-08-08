import sys
import os
import mmap
import re
import hashlib
import pymonad


def hashfile(filename):
    try:
        with open(filename, "rb") as f:
            if os.fstat(f.fileno()).st_size > 0:
                with mmap.mmap(f.fileno(), 0, 
                 access=mmap.ACCESS_READ) as m:
                    h = hashlib.sha256()
                    h.update(m)
                    result = pymonad.Just(filename + " sha256: " + h.hexdigest())
    except:
        result = pymonad.Nothing
    finally:
        return result


bytestr = b'\x6f\x73\x2e\x70\x61\x74\x68\x2e'

def scanfile(filename):
    result = pymonad.Nothing
    try:
        with open(filename, "rb") as f:
            if os.fstat(f.fileno()).st_size > 0:
                with mmap.mmap(f.fileno(), 0, 
                 access=mmap.ACCESS_READ) as m:
                    match = re.search(bytestr, m)
                    if match:
                        found = bytestr.hex() + " found in " + filename
        result = pymonad.Just(found)
    except:
        pass
    finally:
        return result


def scanfiles(path, fn):
    for entry in os.scandir(path):
        if entry.is_file():
            fn(os.path.join(path, entry.name)).fmap(lambda n: print(n))
        elif entry.is_dir:
            scanfiles(entry.path, fn)


""" Main Program """

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <path>")
    exit(0)

rootpath = sys.argv[1]
scanfiles(rootpath, scanfile)
