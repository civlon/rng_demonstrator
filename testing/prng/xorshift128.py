import struct
import sys


class R2:
    def __init__(self):
        self.x = x = 123456789
        self.y = 362436069
        self.z = 521288629
        self.w = 88675123

    def next(self):
        t = self.x ^ (self.x << 11) & 0xffffffff
        self.x = self.y
        self.y = self.z
        self.z = self.w
        w = self.w
        self.w = w ^ (w >> 19) ^ (t ^ (t >> 8)) & 0xffffffff
        return self.w


r = R2()
while True:
    sys.stdout.buffer.write(struct.pack('>I', r.next()))
