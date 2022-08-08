import struct
import sys
import sympy

# super secret large numbers
x = 3*10**200
y = 4*10**200
seed = 5*10**300


def next_usable_prime(x):
    # Find the next prime congruent to 3 mod 4 following x.
    p = sympy.nextprime(x)
    while (p % 4 != 3):
        p = sympy.nextprime(p)
    return p


p = next_usable_prime(x)
q = next_usable_prime(y)
M = p*q

assert(1 < seed < M)
assert(seed % p != 0)
assert(seed % q != 0)

# Number of random numbers to generate
N = 10

x = seed
# bit_string = ""
# for _ in range(N):
#     x = x*x % M
#     x %= int("ffffffff", 16)
#     sys.stdout.buffer.write(struct.pack('>I', x))
#     print(x)
#     b = x % 2
#     bit_string += str(b)
#     print(bit_string)

while True:
    x = x*x % M
    x %= int("ffffffff", 16)
    # sys.stdout.buffer.write(struct.pack('>I', x))
    print(x)
