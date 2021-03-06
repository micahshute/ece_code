from python_resources.functions import *
import code

class RandBreaker:

    #stole this from you
    @classmethod
    def crand(cls, seed):
        r=[]
        r.append(seed)
        for i in range(30):
            r.append((16807*r[-1]) % 2147483647)
            if r[-1] < 0:
                r[-1] += 2147483647
        for i in range(31, 34):
            r.append(r[len(r)-31])
        for i in range(34, 344):
            r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
            counter = 0
        while True:
            next = r[len(r)-31]+r[len(r)-3] % 2**32
            r.append(next)
            ## if counter >= 31 + 16 and counter < 62 + 16: print(next - 2 * (next // 2) )
            # if counter >= 31 and counter < 62: print(next >> 1 if next < 2**32 else (next % 2**32) >> 1) 
            counter += 1
            yield (next >> 1 if next < 2**32 else (next % 2**32) >> 1)


    @classmethod
    def test_crand(cls, seed):
        r=[]
        r.append(seed)
        for i in range(30):
            r.append((16807*r[-1]) % 2147483647)
            if r[-1] < 0:
                r[-1] += 2147483647
        for i in range(31, 34):
            r.append(r[len(r)-31])
        for i in range(34, 344):
            r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
            counter = 0
        while True:
            next = r[len(r)-31]+r[len(r)-3] % 2**32
            r.append(next)
            ## if counter >= 31 + 16 and counter < 62 + 16: print(next - 2 * (next // 2) )
            # if counter >= 31 and counter < 62: print(next >> 1 if next < 2**32 else (next % 2**32) >> 1) 
            counter += 1
            yield ((next >> 1 if next < 2**32 else (next % 2**32) >> 1), next - 2 * (next // 2))

    @classmethod
    def get_random_vals(cls, seed, starti, endi):
        gen = cls.crand(seed)
        vals = []

        for _ in range(starti):
            next(gen)
        
        for _ in range(endi - starti):
            vals.append(next(gen))
            if len(vals) == 0: print(vals[0])
        return vals


    @classmethod
    def create_test(cls, seed=888888):
        gen = cls.test_crand(seed)
        skip = 10001#breaks at 16
        for _ in range(skip):
            next(gen)
        bitstream_with_xis = [next(gen) for _ in range(93)]
        bitstream = [bwx[0] for bwx in bitstream_with_xis]
        xis = [bwx[1] for bwx in bitstream_with_xis]
        testrb = cls(bitstream)
        for xi in testrb.possible_xis:
            if xi == xis[31:62]: 
                print(True)
            # NOTE: NEED TO MAX XI LENGTH EQUAL XIS LEN. CURRENNTLY LEN XI IS 31, XI IS 93
                
        print('Done search')
        return testrb

    def __init__(self, bitstream):
        self.startbit = None
        self.bitstream = bitstream
        self.known_xis = self.get_xis()
        ## print(self.known_xis)
        self.possible_xis = self.xi_permutations()
        self.all_rip375s = []
        for xis in self.possible_xis:
            self.all_rip375s.append([(self.bitstream[i + self.startbit] * 2 + xis[i]) % 2 ** 32 for i in range(31)])
        # print(self.rip375s) # starting output number = i + 31, rnum = i + 375
        self.lincombos = {}



    def xi_permutations(self):
        needed_nums = sum([1 for i in self.known_xis if i is None])
        if needed_nums == 0:
            return [self.known_xis]
        xiperms = []
        # open_slots = [i + self.startbit for i in range(len(self.known_xis)) if self.known_xis[i] is None]
        # print(open_slots)
        for i in range(2 ** (needed_nums + 1)):
            perm = list(self.known_xis)
            nums_to_insert = to_bin_arr(i, len(bin(2 ** needed_nums)[2:]))
            # print(nums_to_insert)
            for i in range(len(perm)):
                if perm[i] is None:
                    perm[i] = nums_to_insert.pop(0)
            
            xiperms.append(perm)
        return xiperms

    def get_xis(self):
        rrems = [None for _ in range(len(self.bitstream))]
        res = [(self.bitstream[i] - self.bitstream[i - 3] - self.bitstream[i - 31]) % 2 ** 31  for i in range(31, len(self.bitstream))]
        # return [0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1]
        for i in range(31, len(self.bitstream)):
            if res[i - 31] == 1:
                rrems[i - 31] = 1
                rrems[i - 3] = 1
                rrems[i] = 0
        for i in range(31, len(self.bitstream)):
            if res[i-31] == 0:
                if rrems[i-31] == 1:
                    rrems[i-3] = 0
                elif rrems[i-3] == 1:
                    rrems[i-31] = 0
        updating = True
        count = 0
        changes = 0

        while updating:
            # print(f"updating count: {count}")
            updating = False
            for i in range(31, len(rrems)):
                if rrems[i] == 1:
                    if rrems[i-3] is None:
                        if rrems[i-31] == 1:
                            rrems[i-3] = 0
                            updating = True
                        elif rrems[i-31] == 0:
                            rrems[i-3] = 1
                            updating = True
                    elif rrems[i-31] is None:
                        if rrems[i-3] == 1:
                            rrems[i-31] = 0
                            updating = True
                        elif rrems[i-3] == 0:
                            rrems[i-31] = 1
                            updating = True
                elif rrems[i] == 0:
                    if rrems[i-3] is None:
                        if rrems[i-31] == 1:
                            rrems[i-3] = 1
                            updating = True
                        elif rrems[i-31] == 0:
                            rrems[i-3] = 0
                            updating = True
                    elif rrems[i-31] is None:
                        if rrems[i-3] == 1:
                            rrems[i-31] = 1
                            updating = True
                        elif rrems[i-3] == 0:
                            rrems[i-31] = 0
                            updating = True
                elif rrems[i] is None:
                    if rrems[i-3] is not None and rrems[i-31] is not None:
                        rrems[i] = rrems[i-3] ^ rrems[i-31]
                        updating = True
                if res[i-31] == 0:
                    if rrems[i-31] == 1 and rrems[i-3] is None:
                        rrems[i-3] = 0
                        updating = True
                    elif rrems[i-3] == 1 and rrems[i-31] is None:
                        rrems[i-31] = 0
                        updating = True

            count += 1

        print(f"Known remainder values: \n{rrems}")
        popstart = self.most_populated_region(rrems)
        print(f"Largest run of known bits starts at: {popstart}")

        self.startbit = popstart
        return rrems[self.startbit: self.startbit + 31]


    def most_populated_region(self, lst):
        startindex = None
        maxval = float('-inf')
        for i in range(31, len(lst)):
            val = sum([1 for val in lst[i-31:i] if val is not None])
            if val > maxval:
                maxval = val
                startindex = i-31
        print(f"Brute force space: 2^{31 - maxval}")
        print(f"Will be slow for values > 2^5")
        return startindex

    def get_lincomb_for_term(self, term):
        if term in self.lincombos:
            return self.lincombos[term]
        elif term < 31:
            self.lincombos[term] = self.Equation(term, 1)
        elif term < 34:
            self.lincombos[term] = self.get_lincomb_for_term(term - 31)
        else:
            self.lincombos[term] = self.Equation.add(self.get_lincomb_for_term(term - 31), self.get_lincomb_for_term(term - 3))
        return self.lincombos[term]

    def crack(self):
        st = 31
        # st = 10030
        totseen = set()
        while True:
            
            eqns = [self.get_lincomb_for_term(i + 344) for i in range(st, st + 31)]
            
            coeff_lists = [list(eqn.to_coeff_list()) for eqn in eqns]
            
            
            mcl = smod_mat(coeff_lists, 2 ** 32)
            mclinv = sinv_mat(mcl)
            # print(mclinv)
            # seed_coeffs = mclinv.tolist()[0] 
            seed_coeffs = mclinv[0] 
            
            seen = set()
            for rip375s in self.all_rip375s:
                seed = 0
                for i in range(31):
                    seed += (seed_coeffs[i] * rip375s[i]) % 2 ** 32
                seedmod = seed % 2 ** 32
                if seedmod in seen: continue
                testvals = RandBreaker.get_random_vals(int(seedmod), st, st + 31)
                if testvals == self.bitstream[self.startbit: self.startbit + 31]:
                    return seedmod, st
                # if abs(seedmod - 888888) < 100: print(seedmod)
                # if abs(seedmod - 888888) < 100000: print(seedmod)
                # if seedmod in totseen: print("\nSEEN")
                # print(len(totseen))
                print(f"Check for bitnum {st}, seedmod {seedmod}", end="\r")
                seen.add(seedmod)
                
                totseen.add(seedmod)
            st += 1

    class Equation:

        @classmethod
        def add(cls, eq1, eq2):
            new_eqn = cls(None, None)
            new_eqn_coeffs = {k: v for k,v in eq1.coeffs.items()}
            for term, coeff in eq2.coeffs.items():
                if term in new_eqn_coeffs:
                    new_eqn_coeffs[term] = (new_eqn_coeffs[term] + coeff) #% 2 ** 32
                else:
                    new_eqn_coeffs[term] = coeff
            new_eqn.coeffs = new_eqn_coeffs
            return new_eqn

        def __init__(self, term, coefficient):
            self.coeffs = {term: coefficient}


        def to_coeff_list(self):
            coarr = [0 for _ in range(31)]
            for term, coeff in self.coeffs.items():
                #NOTE: ADDED MOD BELOW
                coarr[term] = coeff #% 2 ** 32
            return coarr

            