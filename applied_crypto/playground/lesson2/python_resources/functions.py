

def gcd(a,b):
    if b == 0:
        return a
    else: 
        return gcd(b, a % b)


def inv_mod(a,b):
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