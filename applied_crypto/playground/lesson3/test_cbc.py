from Crypto.Cipher import AES
from python_resources.functions import *

key = b'andy love simone'
ivdig = "000102030405060708090a0b0c0d0e0f"
iv = bytes.fromhex(ivdig)
expect = "87dd2acb714db44393d8b4b71bdbad7720fbf40d2e34a03a93324cb9c4b97a08"
plain = b'abcdefghijklmnopqrstuvwxyzabcdef'
aes = AES.new(key, AES.MODE_CBC, iv=iv)

out = aes.encrypt(plain).hex()
print(out == expect)

#"By Hnad"

plainstr = 'abcdefghijklmnopqrstuvwxyzabcdef'
plain1str = plainstr[:16]
plain2str = plainstr[16:]
plain1 = plain1str.encode()
plain2 = plain2str.encode()

aesin1 = int.from_bytes(plain1, byteorder="big") ^ int.from_bytes(iv, byteorder="big")

aes1 = AES.new(key, AES.MODE_ECB)
aesout1 = aes1.encrypt(aesin1.to_bytes(16, byteorder="big"))

aesin2 = int.from_bytes(plain2, byteorder="big") ^ int.from_bytes(aesout1, byteorder="big")
aesout2 = aes1.encrypt(aesin2.to_bytes(16, byteorder="big"))
out2 = aesout1.hex() + aesout2.hex()
print(out2 == expect)

### DECRYPT

outfirst = out2[:32]
outsecond = out2[32:]

aesout2 = aes1.decrypt(bytes.fromhex(outsecond))
aesout1 = aes1.decrypt(bytes.fromhex(outfirst))

plain1 = int.from_bytes(aesout2, byteorder="big") ^ int.from_bytes(bytes.fromhex(outfirst), byteorder="big")
plain1b = plain1.to_bytes(16, byteorder="big")
plain1t = plain1b.decode()

plain2 = int.from_bytes(aesout1, byteorder="big") ^ int.from_bytes(iv, byteorder="big")
plain2b = plain2.to_bytes(16, byteorder="big")
plain2t = plain2b.decode()

plain = plain2t + plain1t
print(plain)

aes = AES.new(key, AES.MODE_CBC, iv=iv)
plain = aes.decrypt(bytes.fromhex(out2)).decode()

print(plain)