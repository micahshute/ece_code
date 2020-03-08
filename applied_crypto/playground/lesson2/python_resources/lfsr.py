from python_resources.functions import *

class LFSR:
    @classmethod
    def crack(cls, size, outbits):
        if len(outbits) < 2 * size: raise Exception('Not enough bits to decode!')
        a, b = [], []
        for i in range(size, size * 2):
            b.append([outbits[i]])
            a.append([outbits[j] for j in range(i - size, i)])
        am = matrix(a)
        bm = matrix(b)
        aminv = inv_mod_matrix(am, 2)
        return aminv * bm % 2

    def __init__(self, state, coefficients):
        if len(state) != len(coefficients):
            raise AttributeError
        self.state = state
        self.c = coefficients
        self.stream = self.generator()

    def generator(self):
        while True: 
            sum = 0
            for i in range(len(self.state) - 1, -1, -1):
                sum = sum ^ (self.c[i] * self.state[i])
            self.state.insert(0, sum)
            yield self.state.pop()


    