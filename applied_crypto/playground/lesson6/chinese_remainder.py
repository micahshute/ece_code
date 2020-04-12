import math
from functools import reduce
import numpy as np
class ModRemRing:

    class NotCoprimeError(Exception):
        pass
    
    #Mirror's sage's CRT; perform the chinese remainder theorem
    # by providing an array of residues and an array of mods
    @classmethod
    def crt(cls,remarr, modarr):
        if len(remarr) != len(modarr):
            raise Exception() 
        rings = [ cls(modarr[i], remarr[i]) for i in range(len(remarr)) ]
        return cls.chinese_remainder(rings)


    @classmethod
    def invmod(cls,a,b):
        r, rm1 = b, a
        s, sm1 = 0, 1
        t, tm1 = 1, 0
        while r != 0:
            q = rm1 // r
            rm1, r = r, rm1 % r
            sm1, s = s, sm1 - q * s
            tm1, t = t, tm1 - q * t
        d = sm1 * a + tm1 * b
        return d, sm1, tm1

    @classmethod
    def is_coprime(cls,a,b):
        return cls.invmod(a,b)[0] == 1

    @classmethod
    def is_pairwise_coprime(cls,rings):
        for i in range(0,(len(rings) - 1)):
            for j in range((i+1), len(rings)):
                if not cls.is_coprime(rings[i].mod, rings[j].mod):
                    raise cls.NotCoprimeError("Modulos must be pairwise coprime!")

    @classmethod
    def chinese_remainder(cls, *rings):
        if type(rings[0]) == list:
            rings = rings[0] 
        cls.is_pairwise_coprime(rings)
        n = np.prod([r.mod for r in rings])
        x = sum([cls.map_ring_to_val(r, n) for r in rings])
        return cls(n, x % n)

    @classmethod
    def map_ring_to_val(cls, ring, n):
        ai = ring.remainder
        non = n / ring.mod
        si = cls.invmod(non, ring.mod)[1]
        return ai * si * non


    def __init__(self,mod, remainder):
        self.mod, self.remainder = mod, remainder
        
    @property
    def nums(self):
        start = self.remainder % self.mod
        while(True):
            yield start
            start += self.mod

    def include(self,num):
        num % self.mod == self.remainder

    def __str__(self):
        return f"{self.remainder} (mod {self.mod})"
    

r = ModRemRing.crt([3,8,6,36],[9,13,25,121])
print(r)
gen = r.nums
print(next(gen))
print(next(gen))



