import os, hashlib, binascii
from python_resources.functions import nonce_key
nonce = os.urandom(6)
print(nonce)
# hexnonce = binascii.hexlify(nonce)
hexnonce = nonce.hex()
print(hexnonce)
oursecret = 54321
secrethex = format(oursecret, 'x')
print(secrethex)
concatenated_hex = hexnonce + secrethex
print(concatenated_hex)
even_length = concatenated_hex.rjust(len(concatenated_hex) + len(concatenated_hex) % 2, '0')
print(even_length)
hexhash = hashlib.sha256(binascii.unhexlify(even_length)).hexdigest()
print(hexhash)
# OR DO THIS
hexhash = hashlib.sha256(bytes.fromhex(even_length)).hexdigest()
print(hexhash)

newseed = (int(hexhash, 16)) % 2**32
print(newseed)
print(nonce_key(nonce, oursecret))

