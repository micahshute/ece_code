

def ms_rand(seed):
    sq = seed ** 2
    strsq = str(sq)
    if len(strsq) < 12:
        for _ in range(12 - len(strsq)):
            strsq = "0" + strsq
    mdl = len(strsq) // 2
    return strsq[mdl - 3 : mdl + 3]

def ms_rand_gen(seed):
    nxtSeed = seed
    while True:
        nxtval = ms_rand(int(nxtSeed))
        yield nxtval
        nxtSeed = nxtval


gen = ms_rand_gen(123456)

vals = [next(gen) for _ in range(10)]
print(vals)