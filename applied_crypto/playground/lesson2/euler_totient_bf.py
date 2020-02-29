from python_resources.functions import *


def etbf(num):
    return sum([1 for n in range(1, num) if gcd(n, num) == 1])

et6 = etbf(6)
et10 = etbf(10)
eta = etbf(16254)
etb = etbf(53)

print((5 ** et6) % 6 )
print(7 ** etbf(10) % 10)
print(5 ** etbf(16254) % 16254 )
print(50 ** etbf(53) % 53)