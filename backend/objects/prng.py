from math import ceil
import struct
from objects.trng import Trng

PERIOD_LENGTH = 196416
CHANGING_SEED_MODE = 'changing'
# Determinates when the dice dattern will be repeated
# With 32736 the pattern will repeat itself after 6 throws
DICE_ROLL_LENGTH = 32736

class PRNG():
    def __init__(self, mode, trng: Trng):
        self.mode = mode
        self.trng = trng
        self.currentNumber = 1
        self.periodCounter = 0

    def generateNumberSequence(self):
        # start seed for static mode
        currentNumber = 1
        if(self.mode == CHANGING_SEED_MODE):
            currentNumber = self.trng.next()
        randomNumbers = []
        for _ in range(PERIOD_LENGTH):
            number = currentNumber = (2521490392 * currentNumber) % 0xfffffffffff
            number &= 0xffffffff
            randomNumbers += (struct.pack('I', number)),
        return randomNumbers

    def getNumbersForDiceRoll(self):
        if(self.mode == CHANGING_SEED_MODE):
            self.currentNumber = self.trng.next()
        if(self.periodCounter == PERIOD_LENGTH):
            if(self.mode == CHANGING_SEED_MODE):
                self.currentNumber = self.trng.next()
            else: 
                self.currentNumber = 1
            self.periodCounter = 0
        for _ in range(DICE_ROLL_LENGTH):
            self.currentNumber = (2521490392 * self.currentNumber) % 0xfffffffffff
        self.periodCounter += DICE_ROLL_LENGTH

    def rollDice(self):
        self.getNumbersForDiceRoll()
        return str(ceil(((self.currentNumber + 1)  / (0xfffffffffff-1))* 6))

    # Testfunction to calculate periodlength of PRNG
    def period(self):
        counter = 0
        number = 1
        number = (2521490392 * number) % 0xfffffffffff
        while number != 1:
            counter += 1
            number = (2521490392 * number) % 0xfffffffffff
        print(counter)
        
