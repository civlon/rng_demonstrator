import struct
import sys
import numpy as np


class LCG(object):

    UZERO: np.uint32 = np.uint32(0)
    UONE: np.uint32 = np.uint32(1)

    def __init__(self, seed: np.uint32, a: np.uint32, c: np.uint32) -> None:
        self._seed: np.uint32 = np.uint32(seed)
        self._a: np.uint32 = np.uint32(a)
        self._c: np.uint32 = np.uint32(c)

    def next(self) -> np.uint32:
        self._seed = self._a * self._seed + self._c
        return self._seed

    def seed(self) -> np.uint32:
        return self._seed

    def set_seed(self, seed: np.uint32) -> np.uint32:
        self._seed = seed

    def skip(self, ns: np.int32) -> None:
        """
        Signed argument - skip forward as well as backward

        The algorithm here to determine the parameters used to skip ahead is
        described in the paper F. Brown, "Random Number Generation with Arbitrary Stride,"
        Trans. Am. Nucl. Soc. (Nov. 1994). This algorithm is able to skip ahead in
        O(log2(N)) operations instead of O(N). It computes parameters
        A and C which can then be used to find x_N = A*x_0 + C mod 2^M.
        """

        nskip: np.uint32 = np.uint32(ns)

        a: np.uint32 = self._a
        c: np.uint32 = self._c

        a_next: np.uint32 = LCG.UONE
        c_next: np.uint32 = LCG.UZERO

        while nskip > LCG.UZERO:
            if (nskip & LCG.UONE) != LCG.UZERO:
                a_next = a_next * a
                c_next = c_next * a + c

            c = (a + LCG.UONE) * c
            a = a * a

            nskip = nskip >> LCG.UONE

        self._seed = a_next * self._seed + c_next


# %%
np.seterr(over='ignore')

a = np.uint32(1664525)
c = np.uint32(1013904223)
seed = np.uint32(1)

rng = LCG(seed, a, c)

while True:
    sys.stdout.buffer.write(struct.pack('>I', rng.next()))
