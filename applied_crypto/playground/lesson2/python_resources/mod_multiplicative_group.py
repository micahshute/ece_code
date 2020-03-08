from python_resources.group import *

class ModMultiplicativeGroup(Group):

    def __init__(self, mod):
        if self.is_prime(mod):
            super().__init__(list(range(1, mod)), lambda a,b: (a * b) % mod)
            self.mod = mod
        else:
            self.mod = mod
            self.binop = lambda a,b: (a * b) % mod
            raise Exception(f"{mod} is not prime, but try (generator, inverse, group) {[(gen, grp.e, grp.values) for gen, grp in self.try_gens()]} ")

    def generators(self, altvals=None):
        subsets = []
        for num in self.values:
            if num == 1: continue
            cset = {num}
            cnum = self.binop(num, num)
            while cnum != num:
                cset.add(cnum)
                cnum = self.binop(cnum, num)
            subsets.append((num, Group(cset, self.binop)))
        return subsets 

    def try_gens(self):
        vals = list(range(1, self.mod))
        subsets = []
        for num in vals:
            if num == 1: continue
            cset = {num}
            cnum = self.binop(num, num)
            while cnum != num:
                cset.add(cnum)
                cnum = self.binop(cnum, num)
            try:
                subsets.append((num, Group(cset, self.binop)))
            except Exception:
                pass
        return subsets 

    def is_prime(self, num):
        if num > 1:
            for i in range(2, num // 2):
                if num % i == 0:
                    return False
            return True
        else:
            return False


    