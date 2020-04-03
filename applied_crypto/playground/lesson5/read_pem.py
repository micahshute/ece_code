import sage.all as sage
import base64
import re

# RUN WITH sage --pyton3 read_pem.py

f = open('dh1024.pem', 'r')

data = f.read()


print(data)
rdata = re.split(r'-+\W+-+', data)
print('--')
raw = rdata[2].strip()
print(raw)
print('--')
bytes = base64.standard_b64decode(raw)

pbytes = bytes[6:6 + 129]

print(pbytes.hex())
phex = pbytes.hex()
print('--')
print(phex)
print('--')
p = int(phex, 16)
print(p)
print("IS PRIME?")
print(sage.is_prime(p))
pm1d2 = (p - 1) // 2
print(sage.is_prime(pm1d2))

gen = bytes[-1]
print(gen)


