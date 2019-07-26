import sys
import os
import mmap
import hashlib


def gethash(hashtype='sha256'):
    hashfunc = hashlib.sha256()

    if hashtype == 'md5':
        hashfunc = hashlib.md5()
    elif hashtype == 'sha1':
        hashfunc = hashlib.sha1()
    elif hashtype == 'blake2b':
        hashfunc = hashlib.blake2b()
    elif hashtype == 'blake2s':
        hashfunc = hashlib.blake2s()

    return hashfunc



def hashfiles(path, hashtype):
    for entry in os.scandir(path):
        if entry.is_file():
            filename = os.path.join(path, entry.name)
            with open(filename, "rb") as f:
                if os.fstat(f.fileno()).st_size > 0:
                    with mmap.mmap(f.fileno(), 0, 
                           access=mmap.ACCESS_READ) as m:
                        h = gethash(hashtype)
                        h.update(m)
                        print(filename + " hash: " + h.hexdigest())
        else:
            hashfiles(entry.path)


if len(sys.argv) < 3:
    print("Usage: " + sys.argv[0] + " <path> <hashtype>")
    exit(0)

rootpath = sys.argv[1]
hashtype = sys.argv[2]
hashfiles(rootpath, hashtype)
