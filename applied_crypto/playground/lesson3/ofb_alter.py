from Crypto.Cipher import AES



plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
key = b"andy love simone"
iv = b"Not very random."
expect = "4e6f7420766572792072616e646f6d2e91de0aa207cf9f7d0f3cdf245e88f281248b5a2d4cb1b3afefac7bd25c1bc90a177fb88bea185fe13e766cd60a011c20e108f6a8693c756a70da283af3604fb3"
plainb = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
aes = AES.new(key, AES.MODE_OFB, iv=iv)

ciphertext = aes.encrypt(plainb).hex()

print(ciphertext == expect[-128:])
aesd = AES.new(key, AES.MODE_OFB, iv=iv)
print(aesd.decrypt(bytes.fromhex(ciphertext)))

# BY HAND

aesb = AES.new(key, AES.MODE_ECB)

inpt = iv
plain1 = plain[:16].encode()
plain2 = plain[16:32].encode()
plain3 = plain[32:48].encode()
plain4 = plain[48:64].encode()

out1 = aesb.encrypt(inpt)

cipher1 = (int.from_bytes(plain1, byteorder="big") ^ int.from_bytes(out1, byteorder="big")).to_bytes(16, byteorder="big").hex()

out2 = aesb.encrypt(out1)

cipher2 = (int.from_bytes(plain2, byteorder="big") ^ int.from_bytes(out2, byteorder="big")).to_bytes(16, byteorder="big").hex()

out3 = aesb.encrypt(out2)

cipher3 = (int.from_bytes(plain3, byteorder="big") ^ int.from_bytes(out3, byteorder="big")).to_bytes(16, byteorder="big").hex()

out4 = aesb.encrypt(out3)

cipher4 = (int.from_bytes(plain4, byteorder="big") ^ int.from_bytes(out4, byteorder="big")).to_bytes(16, byteorder="big").hex()

ciphertxt = cipher1 + cipher2 + cipher3 + cipher4

print(ciphertext)