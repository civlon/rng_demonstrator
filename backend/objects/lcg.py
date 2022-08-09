import struct

from objects.trng import Trng

PERIOD_LENGTH = 26880
CHANGING_SEED_MODE = 'changing'

class LcgPRNG():
    def __init__(self, mode, trng: Trng):
        self.mode = mode
        self.trng = trng

    def generateNumberSequence(self):
        # start seed for static mode
        currentNumber = 1
        if(self.mode == CHANGING_SEED_MODE):
            currentNumber = self.trng.next()
        randomNumbers = []
        for _ in range(PERIOD_LENGTH):
            number = currentNumber = (25214903912 * currentNumber) % 0xffffffffffff
            number %= 0xffffffff
            randomNumbers += (struct.pack('I', number)),
        return randomNumbers

    def period(self):
        counter = 0
        number = 1
        number = (25214903912 * number) % 0xffffffffffff
        while number != 1:
            counter += 1
            number = (25214903912 * number) % 0xffffffffffff
        print(counter)


