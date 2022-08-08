import random
import struct


class LcgPRNG():
    def __init__(self, mode):
        self.mode = mode
        self.startSeed = 1
        # POSIX constants
        # self.a = 25214903917
        # self.m = 2**48
        # self.c = 11
        self.periodCounter = 0
        # initialize first number in sequence
        self.startLcg()

    def startLcg(self):
        self.z = ((25214903917 * self.startSeed) + 11) & 0xffffffffffff
        return

    def lcg(self):
        self.z = ((25214903917 * self.z) + 11) & 0xffffffffffff
        return

    def next(self):
        if(self.periodCounter >= 100000):
            if(self.mode == 'changing'):
                self.startSeed = random.randint(0, 2**32)
            self.startLcg()
            self.periodCounter = 0
        self.lcg()
        number = self.z
        self.periodCounter += 1
        return (number % 0xffffffff)

    def nextLines(self):
        numbers = []
        for i in range(10000):
            numbers.append(struct.pack('I', self.next()))
        return numbers
