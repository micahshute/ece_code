import os, math, binascii
from Crypto.Cipher import AES

def XOR_hex(h1, h2):
    ans_hex = hex(int(h1, 16) ^ int(h2, 16))[2:]
    if (ans_hex[-1] == "L"):
        ans_hex = ans_hex[:-1]
    return ans_hex.zfill(len(h1))

def XOR_raw(r1, r2):
    return binascii.unhexlify(XOR_hex(binascii.hexlify(r1), binascii.hexlify(r2)))

class ChainedCBC:
    def __init__(self, key):
        IV = os.urandom(16)
        self.IV = IV
        self.F_k = AES.new(key, AES.MODE_ECB)
        self.first_message = True
    def encrypt(self, pt):
        lpt = len(pt)
        if lpt % 16 > 0:
            padding = (16 - (lpt % 16))*"x"
        else:
            padding = ""
        padded_pt = pt + padding
        ciphertext = ""
        if self.first_message:
            self.first_message = False
            ciphertext += self.IV.hex()
        for i in range(len(padded_pt)//16):
            inputi = XOR_raw(self.IV, padded_pt[i:i+16].encode())
            self.IV = self.F_k.encrypt(inputi)
            ciphertext += self.IV.hex()
        return ciphertext

import random

class ChallengeProblem:
    def __init__(self):
        self.messages = ["The 1st message.", "The 2nd message."]
    def beginChallenge(self):
        self.cipher = ChainedCBC(os.urandom(16))
        self.__secret_index = ord(os.urandom(1)) % 2
        return self.encrypt(self.messages[self.__secret_index])
    def encrypt(self, pt):
        return self.cipher.encrypt(pt)
    def isTheSecret(self, guessed_index):
        # your goal is to have this function return true
        # more than 50% of the time
        return guessed_index == self.__secret_index


#sample challenge

class Encodable:

    def __init__(self, bytes):
        self.bytes = bytes

    def __add__(self, string):
        return self

    def __len__(self):
        return 16

    def __getitem__(self,x):
        return self

    def encode(self):
        return self.bytes


mychallenge = ChallengeProblem()
ciphertext = mychallenge.beginChallenge()
iv = ciphertext[:32]
civ = ciphertext[32:]
iiv = int(iv, 16)
iciv = int(civ, 16)

msg1 = "The 1st message."
msg1int = int(msg1.encode().hex(), 16)


p2 = iiv ^ iciv ^ msg1int
p2bytes = p2.to_bytes(16, byteorder="big")
inp = Encodable(p2bytes)

cout = mychallenge.encrypt(inp)
# print(ciphertext)
# print(cout)


    
#do work on the cipher text here to figure out message one or message two

myguess = 0
if cout not in ciphertext: myguess = 1
if mychallenge.isTheSecret(myguess):
    print("I was right!")
else:
    print("I was wrong")