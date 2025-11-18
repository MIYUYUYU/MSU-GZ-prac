import struct
import sys

import random
seq = [(random.random(), bytes(random.sample(range(5), 3)), random.randrange(10000)) for i in range(10)]

with open(sys.argv[1], 'bw+') as fout:
    for t in seq:
        w = fout.write(struct.pack('f3si', *t))

with open(sys.argv[1], 'br') as fin:
    with open(sys.argv[2], 'bw+') as fout:
        size = fin.seek(0, 2)
        fin.seek(0)
        with s := fin.read(size// 10):
            w = fout.write(struct.pack('!f3si',*struct.unpack('f3si', s)))

