import random
import struct
from sys import stdout
import sys
import time

# Source:
# Link: https://www.johndcook.com/blog/2017/07/05/simple-random-number-generator/

# constants for LCG
z = 56784654897435  # 20170705   # seed
a = 13235981548769  # 742938285  # multiplier
e = 31
m = 2**e - 1    # modulus
N = 1000000000  # 1.000.000.000

# =====================================================
# base LCG function


def lcg(z):
    global a
    global e
    global m
    return a * z % m

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
        seed = lcg(seed)
        sys.stdout.buffer.write(struct.pack('>I', seed))

# =====================================================
# =====================================================
# functions for testing dieharder
# with raw unsigned 32 integer input
# and non changing seed


def rawInputStaticSeed():
    global z
    while True:
        z = lcg(z)
        sys.stdout.buffer.write(struct.pack('>I', z))

# =====================================================
# =====================================================
# functions to tes dieharder with .txt file


def txtFileInput():
    global z
    stdout.write('# lcg' + '\n')
    stdout.write('# seed: ' + str(z) + '\n')
    stdout.write('type: d \n')
    stdout.write('count: ' + str(N) + '\n')
    stdout.write('numbit: 32' + '\n')

    for _ in range(N):
        z = lcg(z)
        stdout.write(str(z) + '\n')

# =====================================================
# =====================================================
# main


def main():
    # rawInputStaticSeed()
    rawInputChangingSeed()


if __name__ == '__main__':
    main()

# =====================================================
