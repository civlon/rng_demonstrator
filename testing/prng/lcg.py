import random
import struct
from sys import stdout
import sys
import time

        # POSIX constants
        # self.a = 25214903917
        # self.m = 2**48
        # self.c = 11
        # period 100000

class LcgPRNG():
    def __init__(self, mode):
        self.mode = mode
        self.startSeed = 123456
        self.a = 25214903917
        self.m = 2**48
        self.c = 11
        self.periodCounter = 0
        self.startLcg()
        self.z = 1
        #0xffffffffffff

    def startLcg(self):
        self.z = ((12 * self.startSeed)) % 281474976710655
        return

    def lcg(self):
        self.z = ((25214903912 * self.z)) % 281474976710655
        return

    def next(self):
        if(self.periodCounter >= 26800):
            if(self.mode == 'changing'):
                self.startSeed = random.randint(0, 2**32)
            self.startLcg()
            self.periodCounter = 0
        self.lcg()
        self.periodCounter += 1
        number = self.z
        number %= int("ffffffff", 16)
        return number

    def periodRun(self):
        while True:
            self.z = 1
            if(self.mode == 'changing'):
                self.z = random.randint(0, 2**32)
            for _ in range(26880):
                self.lcg()
                number = self.z
                number %= int("ffffffff", 16)
                sys.stdout.buffer.write(struct.pack('>I', number))

    def period(self):
        counter = 0
        number = 0
        while number != 1:
            counter += 1
            self.lcg()
            number = self.z
            #print(number)
        print(counter)

rng = LcgPRNG('changing')
rng.period()
print(0xffffffffffff)

    #def startLcg(self):
        #self.z = (25214903912 * self.startSeed) % 0xffffffffffff
        #return

    #def lcg(self):
        #self.z = (25214903912 * self.z) % 0xffffffffffff
        #return


# # Source:
# # Link: https://www.johndcook.com/blog/2017/07/05/simple-random-number-generator/

# # constants for LCG
# z = 10  # 20170705   # seed
# a = 65539  # 62089911  # 742938285  # multiplier
# e = 31
# m = 2**e - 1    # modulus
# c = 12345
# N = 1000000000  # 1.000.000.000

# # =====================================================
# # base LCG function


# def lcg(z):
#     global a
#     global e
#     global m
#     global c
#     return ((a * z) + c) % m

# # =====================================================
# # functions for testing dieharder
# # with raw unsigned 32 integer input
# # and changing seed


# def rawInputChangingSeed():
#     seed = random.randint(0, 2**30)
#     while True:
#         generate_numbers(seed)


# def generate_numbers(seed):
#     for _ in range(10000000):  # 1 mio
#         seed = lcg(seed)
#         sys.stdout.buffer.write(struct.pack('>I', seed))

# # =====================================================
# # =====================================================
# # functions for testing dieharder
# # with raw unsigned 32 integer input
# # and non changing seed


# def rawInputStaticSeed():
#     global z
#     while True:
#         z = lcg(z)
#         sys.stdout.buffer.write(struct.pack('>I', z))


# # =====================================================
# # =====================================================
# # functions to tes dieharder with .txt file


# def txtFileInput():
#     global z
#     stdout.write('# lcg' + '\n')
#     stdout.write('# seed: ' + str(z) + '\n')
#     stdout.write('type: d \n')
#     stdout.write('count: ' + str(N) + '\n')
#     stdout.write('numbit: 32' + '\n')

#     for _ in range(N):
#         print(_)
#         z = lcg(z)
#         stdout.write(str(z) + '\n')

# =====================================================
# =====================================================
# main


#def main():
    # while True:
    #     seed = int(random.random() * 2**30)
    #     sys.stdout.buffer.write(struct.pack('>I', seed))
    # rawInputStaticSeed()
    # rawInputChangingSeed()
    # txtFileInput()
    #rng = LcgPRNG('changing')
    # rng.next()
    #while True:
     #   sys.stdout.buffer.write(struct.pack('I', rng.next()))


#if __name__ == '__main__':
    #main()

# =====================================================
