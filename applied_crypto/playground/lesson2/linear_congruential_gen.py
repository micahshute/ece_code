from python_resources.functions import *

def lcg(seed):
    r = seed
    m = 2 ** 31
    a = 1103515245
    c = 12345
    while True:
        rn = (a * r + c) % m
        yield rn
        r = rn 

# rand = lcg(3)
# for _ in range(5):
#     print( next(rand) )
a = 1103515245
m = 2 ** 31
c = 12345
_, imod, _ = inv_mod(a,m) 

iimod = imod % m
print(iimod)

r1 = 300562173
# r1 = a * r + c % m
# r1 - c = a * r % m
# 1 = (a * iimod) % m
# (r1-c) = a * iimod * (r1 - c) % m
# r = (iimod * (r1 - c))

seed = iimod * (r1 - c) % m
print(seed)

rand = lcg(seed)
for _ in range(5):
    print( next(rand))