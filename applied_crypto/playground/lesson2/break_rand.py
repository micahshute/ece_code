from random import *
from python_resources.rand_breaker import *

def crand(seed):
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
    while True:
        next = r[len(r)-31]+r[len(r)-3] % 2**32
        r.append(next)
        yield (next >> 1 if next < 2**32 else (next % 2**32) >> 1)

theseed = randint(1, 2**30)
skip = randint(10000, 200000)
skip = 23971
print(skip)
my_generator = crand(theseed)
for i in range(skip):
    temp = next(my_generator)

the_input = [next(my_generator) for i in range(93)]

the_output = [next(my_generator) for i in range(93)]


def your_code(theinput):
    rb = RandBreaker(theinput)
    # rb = RandBreaker.create_test()
    res = rb.crack()
    print()
    print(res)
    seed, ip31term = res
    starting_term = ip31term + 62
    cgen = crand(int(seed))
    out = []
    for i in range(starting_term):
        next(cgen)
    for i in range(93):
        out.append(next(cgen))
    return out

if your_code(the_input) == the_output:
    print("You win")
else:
    print("Try again")