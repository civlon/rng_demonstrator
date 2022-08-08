import random
import struct
from sys import stdout
import sys
import time


class LcgPRNG():
    def __init__(self, mode):
        self.mode = mode
        self.startSeed = 1
        self.a = 75
        self.m = 2**16
        self.c = 74
        self.startLcg()

    def startLcg(self):
        self.z = ((self.a * int(self.startSeed)) + self.c) % self.m
        return

    def lcg(self):
        self.z = ((self.a * int(self.z)) + self.c) % self.m
        return

    def gen(self):
        while True:
            self.startSeed = random.randint(0, 2**32)
            self.startLcg()
            for _ in range(2**16 - 1):
                self.lcg()
                number = self.z
                sys.stdout.buffer.write(struct.pack('>I', number))

    def next(self):
        if(self.periodCounter >= 100000):
            if(self.mode == 'changing'):
                self.startSeed = random.randint(0, 2**32)
            self.startLcg()
            self.periodCounter = 0
        self.lcg()
        self.periodCounter += 1
        number = self.z
        number %= int("ffffffff", 16)
        return number


rng = LcgPRNG('egal')
rng.gen()
