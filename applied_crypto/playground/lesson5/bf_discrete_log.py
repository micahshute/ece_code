

def findx(a,g,p):
    x = 1
    while True:
        testa = g ** x % p
        if testa == a: break
        x += 1
    return x


print(findx(22,3,31))
