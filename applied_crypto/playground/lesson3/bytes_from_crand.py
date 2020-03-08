from python_resources.functions import crand
import random
mod = 2 ** 8
# temp = 2158094741372
# randseed = random.randint(1000,100000)
gen = crand(1983)
temp = next(gen)
num1 = temp % mod
num2 = (temp >> 8) % mod
num3 = (temp >> 16) % mod

print(f"{num1};{num2};{num3}")


htemp = format(temp, 'x')
print(htemp)
hnum1 = htemp[-2:]
hnum2 = htemp[-4:-2]
hnum3 = htemp[-6:-4]
print(f"{hnum1};{hnum2};{hnum3}")
print(f"{int(hnum1, 16)};{int(hnum2, 16)};{int(hnum3, 16)}")

temp1 = temp
temp2 = next(gen)
temp3 = next(gen)
temp4 = next(gen)

print([temp1, temp2, temp3, temp4])