from Crypto.Cipher import AES
import binascii

key = bytes.fromhex('000102030405060708090a0b0c0d0e0f')
plain = bytes.fromhex('00112233445566778899aabbccddeeff')

aes = AES.new(key, AES.MODE_ECB)
hdig = aes.encrypt(plain).hex()

print(hdig)

key192 = bytes.fromhex('000102030405060708090a0b0c0d0e0f1011121314151617')
plain192 = bytes.fromhex('00112233445566778899aabbccddeeff')
expect192 = 'dda97ca4864cdfe06eaf70a0ec0d7191'
aes192 = AES.new(key192, AES.MODE_ECB)
hdig192 = aes192.encrypt(plain192).hex()
print(hdig192 == expect192)

key256 = bytes.fromhex('000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f')
plain256 = bytes.fromhex('00112233445566778899aabbccddeeff')
expect256 = '8ea2b7ca516745bfeafc49904b496089'
aes256 = AES.new(key256, AES.MODE_ECB)
hdig256 = aes256.encrypt(plain256).hex()
print(hdig256 == expect256)
