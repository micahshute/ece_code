
def inv_mod_iterative2(a,b):
    rm1, rm2 = b, a
    sm1, sm2 = 0, 1
    tm1, tm2 = 1, 0
    
    while rm1 != 0:
        r = rm2 % rm1
        q = int(rm2 / rm1)
        s = sm2 - q * sm1
        t = tm2 - q * tm1
        rm1, rm2 = r, rm1
        sm1, sm2 = s, sm1
        tm1, tm2 = t, tm1
    d = sm1 * a + tm1 * b
    return d, sm2, tm2


def inv_mod_iterative(a,b):
    r, rm1 = b, a
    s, sm1 = 0, 1
    t, tm1 = 1, 0
    while r != 0:
        q = int(rm1 / r)
        rm1, r = r, rm1 % r
        sm1, s = s, sm1 - q * s
        tm1, t = t, tm1 - q * t
    d = sm1 * a + tm1 * b
    return d, sm1, tm1


    
    
        

a = 1103515245
b = 2 ** 31

d, s, t = inv_mod_iterative(a,b)


print(d)
print(s)
print(t)
print((a*s) % b)
print((b*t) % a)
print((s * a + t * b) )