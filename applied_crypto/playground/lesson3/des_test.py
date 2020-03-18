from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
# key = (87654321).to_bytes(8, byteorder="big")
key= b'smnsdddy'
scheme = DES.new(key, DES.MODE_ECB)
ciphertext = scheme.encrypt(pad(b'micahrulz', 16))
print(ciphertext)
out = scheme.decrypt(ciphertext)
print(unpad(out, 16).decode())


out = bytes.fromhex('7a689d7aa98bd217')
print(scheme.decrypt(out).decode())