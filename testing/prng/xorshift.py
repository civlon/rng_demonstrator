import random
import struct
import sys

# =====================================================
# base algorithm for xorshift for generatin 32-bit number


def xorshift(seed):
    seed ^= seed << 6  # 13
    seed ^= seed >> 21  # 17
    seed ^= seed << 7  # 5
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
    for _ in range(10000000):  # 1 mio
        seed = xorshift(seed)

        sys.stdout.buffer.write(struct.pack('>I', seed))

# =====================================================
# =====================================================
# functions for testing dieharder
# with raw unsigned 32 integer input
# and non changing seed


def rawInputStaticSeed():
    seed = 134515345
    while True:
        seed = xorshift(seed)
        seed %= int("ffffffff", 16)
        sys.stdout.buffer.write(struct.pack('>I', seed))

def period():
    number = xorshift(1)
    counter = 1
    while number != 1:
        counter += 1
        number = xorshift(number)
    print(counter)


# def rawInputStaticSeed():
#     # seed = 134515345
#     while True:
#         seed = random.randint(0, 2**30)
#         for _ in range(2**32):
#             seed = xorshift(seed)
#             seed %= int("ffffffff", 16)
#             sys.stdout.buffer.write(struct.pack('>I', seed))

# =====================================================
# =====================================================
# main


def main():
    period()
    # rawInputChangingSeed()


if __name__ == '__main__':
    main()

# =====================================================
