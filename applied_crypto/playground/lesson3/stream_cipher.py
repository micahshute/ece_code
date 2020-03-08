from python_resources.functions import *
import binascii


mygen = crand(1983)
rands = [next(mygen) for i in range(4)]
plaintext = "andy rules!!"

hexplain = binascii.hexlify(plaintext.encode())
hexkey = "".join(map(lambda x: format(x, 'x')[-6:], rands))

cipher_as_int = int(hexplain, 16) ^ int(hexkey, 16)
cipher_as_hex = format(cipher_as_int, 'x')
newgen = crand(1983)
print(cipher_as_hex)
tst = stream_cipher(newgen, plaintext, decode=False)
print(tst)

newgen = crand(1983)
msghex = stream_cipher(newgen, tst, decode=True)
msg = hex2str(msghex)
print(msg)
