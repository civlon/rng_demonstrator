

import struct
import sys


p = 2**63 - 25
a = 5520335699031059059
b = 2752743153957480735


# def icg(pair):
#     x, state = pair
#     if state == 0:
#         return (b/p, b)
#     else:
#         state = (a*pow(state, -1, p) + b) % p
#     return (state/p, state)


T = 2**32
m = p - p % T


def icg32(pair):
    x, state = pair
    if state == 0:
        return (b % T, b)
    state = (a*pow(state, -1, p) + b) % p
    while state > m:  # rare
        state = (a*pow(state, -1, p) + b) % p
    return (state % T, state)


x, state = 1, 1
while True:
    (x, state) = icg32((x, state))
    sys.stdout.buffer.write(struct.pack('>I', x))
