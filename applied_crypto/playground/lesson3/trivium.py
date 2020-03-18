from python_resources.trivium import *
from random import *
# key = '1' * 80
# iv = '1' * 80

# key = "".join([str(randint(0,1)) for _ in range(80)])
# iv = "".join([str(randint(0,1)) for _ in range(80)])

key = "10100111011011010101100011010101001001010101111101000011010010101111010100100111"
iv = "00001001011100100101010100110000100000001100001101010000001100000011110010111100"
print(key)
print(iv)

trivium = Trivium(key, iv)
trivium.warmup
next_160_outs = [trivium.shift() for _ in range(160)]
print(next_160_outs)