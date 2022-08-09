import timeit
import struct


print(timeit.timeit("25214903912 % 281474976710655", number=1000000))
print(timeit.timeit("25214903912 % 0xffffffffffff", number=1000000))

print(timeit.timeit("x.append(123462546)", "x = []", number=1000000))
print(timeit.timeit("x += 123462546,", "x = []", number=1000000))