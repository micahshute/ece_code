import binascii, hashlib

k = "secretkey"
msg = "forge this punks"

kplus = k + "\x00"*(64-len(k))
ipad = "\x36"*64
opad = "\x5C"*64

def XOR(raw1, raw2):
  return binascii.unhexlify(format(int(binascii.hexlify(raw1), 16) ^ int(binascii.hexlify(raw2), 16), 'x'))

tag = hashlib.sha256(XOR(kplus, opad) + hashlib.sha256(XOR(kplus, ipad) + msg).digest()).digest()

print binascii.hexlify(tag)