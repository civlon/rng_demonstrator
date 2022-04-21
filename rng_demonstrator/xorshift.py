import random
import struct
from sys import stdout
import sys


def xorshift(seed):
    xorshift_seed = seed
    xorshift_seed ^= xorshift_seed << 11  # 13
    xorshift_seed ^= xorshift_seed >> 21  # 17
    xorshift_seed ^= xorshift_seed << 15  # 5
    xorshift_seed ^= xorshift_seed >> 7  # 5
    # The modulus limits it to a 32-bit number
    xorshift_seed %= int("ffffffff", 16)
    sys.stdout.buffer.write(struct.pack('>I', xorshift_seed))
    return xorshift_seed


def rotation(seed):
    for _ in range(10000000):
        seed = xorshift(seed)


def main():
    seed = random.randint(0, 2**32)
    N = 1000000  # 1 mio

    while True:
        seed = int(random.randint(0, 2**32))
        rotation(seed)
        #seed = xorshift(seed)


if __name__ == '__main__':
    main()
