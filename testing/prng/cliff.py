from random import randrange
import random
import struct
from sys import stdout
import sys
from numpy import log
from scipy.optimize import bisect

# Link: https://www.johndcook.com/blog/2019/08/11/cliff-dieharder/

# r = bisect(lambda x: -100*log(x) - x - 20, 0, 0.999)
# print(r)

N = 1000000000

while True:
    # seed = random.uniform(0.0, 0.8)
    seed = 0.1
    r = bisect(lambda x: -100*log(x) - x - 20, seed, 0.999)
    for _ in range(1000000):
        r = abs(-100*log(r)) % 1
        sys.stdout.buffer.write(struct.pack('>I', int(r * 2**32)))
