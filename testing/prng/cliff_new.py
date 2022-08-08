import enum
import multiprocessing
import random
import struct
import sys
import time
from numpy import log
from scipy.optimize import bisect

# Source-Link: https://www.johndcook.com/blog/2019/08/11/cliff-dieharder/


class CliffPRNG():
    def __init__(self, mode):
        self.mode = mode
        self.seed = 0.1
        self.initializeNumber()
        self.periodCounter = 0
        self.randomNumberList = []
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

    def runPrng(self):
        t_end = time.time() + 60 * 3
        while time.time() < t_end:
            self.randomNumberList.append(self.next())
        return self.randomNumberList

    # def generateNumbers(self):
    #     t_end = time.time() + 60 * 15
    #     while time.time() < t_end:
    #         self.queue.put(self.next())
    #     self.queue.close()


# N = 100000000
# cliff = CliffPRNG('changing')
# sys.stdout.write('# cliff' + '\n')
# sys.stdout.write('# seed: ' + str(cliff.randomNumber) + '\n')
# sys.stdout.write('type: d \n')
# sys.stdout.write('count: ' + str(N) + '\n')
# sys.stdout.write('numbit: 32' + '\n')
# for _ in range(N):
#     sys.stdout.write(str(cliff.next()) + '\n')

# while True:
#     sys.stdout.buffer.write(struct.pack('>I', cliff.next()))
