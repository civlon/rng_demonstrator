import struct
from sys import stdout
import sys
from numpy import log
from scipy.optimize import bisect

# Link: https://www.johndcook.com/blog/2019/08/11/cliff-dieharder/

r = bisect(lambda x: -100*log(x) - x - 20, 0.4, 0.999)
# print(r)

N = 1000000000

while True:
    r = abs(-100*log(r)) % 1
    print(int(r * 2**32))
    sys.stdout.buffer.write(struct.pack('>I', r))
