# Hacking With Monads:
# Functional Programming for the Blue Team
# A Def Con 27 Workshop August 10, 2019

# Demo of hidden functional features in Python
# Recursively search for files with a given
# byte sequence, using os.walk.

import sys
import os
import mmap
import re

if len(sys.argv) < 2:
    print("Usage: " + sys.argv[0] + " <path>")
    exit(0)

rootpath = sys.argv[1]

bytestr = b'\x6f\x73\x2e\x70\x61\x74\x68\x2e'

for root, dirs, files in os.walk(rootpath):
    for name in files:
        filename = os.path.join(root, name)
        with open(filename, "rb") as f:
            if os.fstat(f.fileno()).st_size > 0:
                with mmap.mmap(f.fileno(), 0,
                       access=mmap.ACCESS_READ) as m:
                    match = re.search(bytestr, m)
                    if match:
                        print(bytestr.hex() + " found in " + filename)