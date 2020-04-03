from Crypto.Cipher import AES

iv = b"\x00"*16
key = b"andy love simone"
msg = b"andy love simoneandy love simone"
expected = "d6fdc5d5596e6ff6c3039cfbb5d9216f"
h = AES.new(key, AES.MODE_CBC, iv=iv).encrypt(msg)
hd = h.hex()
print(hd)
print(hd[-32:])
print(expected)
print(hd[-32:] == expected)

def XOR(b1, b2):
    return bytes.fromhex(format(int(b1.hex(), 16) ^ int(b2.hex(), 16), 'x'))


wmsg = "andy love simoneandy love simone" 
pt1 = wmsg[:16].encode()
pt2 = wmsg[-16:].encode()
ecb = AES.new(key, AES.MODE_ECB)
in1 = XOR(iv, pt1)
out1 = ecb.encrypt(in1)
in2 = XOR(pt2, out1)
out2 = ecb.encrypt(in2)

print(out2.hex())
print(out2.hex() == expected)

