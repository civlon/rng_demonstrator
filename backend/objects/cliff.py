import enum
import random
from numpy import log
from scipy.optimize import bisect

# Source-Link: https://www.johndcook.com/blog/2019/08/11/cliff-dieharder/


class CliffPRNG():
    def __init__(self, mode):
        self.mode = mode
        self.seed = 0.1
        self.initializeNumber()
        self.periodCounter = 0
        pass

    def cliff(self):
        self.randomNumber = abs(-100*log(self.randomNumber)) % 1
        return

    def next(self):
        if(self.periodCounter >= 1000000):
            if(self.mode == 'changing'):
                self.seed = random.uniform(0.1, 0.8)
            self.initializeNumber()
            self.periodCounter = 0
        self.cliff()
        self.periodCounter += 1
        return int(self.randomNumber * 2**32)

    def initializeNumber(self):
        self.randomNumber = bisect(
            lambda x: -100*log(x) - x - 20, self.seed, 0.999)
