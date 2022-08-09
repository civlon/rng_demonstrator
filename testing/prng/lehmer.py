import random
import struct
from sys import stdout
import sys
import time


class LcgPRNG():
    def __init__(self, mode):
        self.mode = mode
        self.startSeed = 6700417
        self.a = 213253412
        self.m = (2**32) + 1
        self.periodCounter = 0
        self.startLcg()

    def startLcg(self):
        self.z = ((self.a * int(self.startSeed))) % self.m
        return

    def lcg(self):
        self.z = ((self.a * int(self.z))) % self.m
        return

    def period(self):
        seen = []
        number = self.startSeed
        counter = 0
        while number not in seen:
            counter += 1
            seen.append(number)
            self.lcg()
            number = self.z
        print(counter)

    def periodRun(self):
        while True:
            number = self.startSeed
            if(self.mode == 'changing'):
                self.startSeed = random.randint(0, 2**32)
            for _ in range(640):
                self.lcg()
                number = self.z
                sys.stdout.buffer.write(struct.pack('>I', number))

    def next(self):
        if(self.periodCounter >= 640):
            if(self.mode == 'changing'):
                self.startSeed = random.randint(0, 2**32)
            self.startLcg()
            self.periodCounter = 0
        self.lcg()
        self.periodCounter += 1
        number = self.z
        # number %= int("ffffffff", 16)
        return number

rng = LcgPRNG('static')
rng.period()