import random
import struct
from sys import stdout
import sys
import time

# Source:
# Link: https://www.johndcook.com/blog/2017/07/05/simple-random-number-generator/

# constants for LCG
z = 10  # 20170705   # seed
a = 1103515245  # 62089911  # 742938285  # multiplier
e = 31
m = 2**e - 1    # modulus
c = 12345
N = 1000000000  # 1.000.000.000

# =====================================================
# base LCG function


def lcg(z):
    global a
    global e
    global m
    global c
    return ((a * z) + c) % m

# =====================================================
# functions for testing dieharder
# with raw unsigned 32 integer input
# and changing seed


def rawInputChangingSeed():
    seed = random.randint(0, 2**30)
    for _ in range(10000):
        generate_numbers(seed)


def generate_numbers(seed):
    for _ in range(100000):  # 1 mio
        seed = lcg(seed)
        sys.stdout.buffer.write(struct.pack('>I', seed))

# =====================================================
# =====================================================
# functions for testing dieharder
# with raw unsigned 32 integer input
# and non changing seed


def rawInputStaticSeed():
    # global z
    # while True:
    #     z = lcg(z)
    #     sys.stdout.buffer.write(struct.pack('>I', z))
    while True:
        random.randint(0, 2**30)

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
        print(_)
        z = lcg(z)
        stdout.write(str(z) + '\n')

# =====================================================
# =====================================================
# main


def main():
    while True:
        seed = int(random.random() * 2**30)
        sys.stdout.buffer.write(struct.pack('>I', seed))
    # rawInputStaticSeed()
    # rawInputChangingSeed()
    # txtFileInput()


if __name__ == '__main__':
    main()

# =====================================================
