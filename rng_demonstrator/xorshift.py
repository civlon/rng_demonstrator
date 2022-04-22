import random
import struct
import sys

# =====================================================
# base algorithm for xorshift for generatin 32-bit number


def xorshift(seed):
    seed ^= seed << 13  # 13
    seed ^= seed >> 17  # 17
    seed ^= seed << 5  # 5
    # seed ^= seed << 7   # 5
    # The modulus limits it to a 32-bit number
    seed %= int("ffffffff", 16)
    return seed

# =====================================================
# =====================================================
# functions for testing dieharder
# with raw unsigned 32 integer input
# and changing seed


def rawInputChangingSeed():
    seed = random.randint(0, 2**32)
    while True:
        generate_numbers(seed)


def generate_numbers(seed):
    for _ in range(1000000):  # 1 mio
        seed = xorshift(seed)
        sys.stdout.buffer.write(struct.pack('>I', seed))

# =====================================================
# =====================================================
# functions for testing dieharder
# with raw unsigned 32 integer input
# and non changing seed


def rawInputStaticSeed():
    seed = 2463534242
    while True:
        seed = xorshift(seed)
        sys.stdout.buffer.write(struct.pack('>I', seed))

# =====================================================
# =====================================================
# main


def main():
    # rawInputStaticSeed()
    rawInputChangingSeed()


if __name__ == '__main__':
    main()

# =====================================================
