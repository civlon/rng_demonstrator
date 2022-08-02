import random


class LcgPRNG():
    def __init__(self, mode):
        self.mode = mode
        self.startSeed = 1
        # POSIX constants
        self.a = 25214903917
        self.m = 2**48
        self.c = 11
        self.periodCounter = 0
        # initialize first number in sequence
        self.startLcg()

    def startLcg(self):
        self.z = ((25214903917 * int(self.startSeed)) + 11) % 2**48
        return

    def lcg(self):
        self.z = ((25214903917 * int(self.z)) + 11) % 2**48
        return

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
