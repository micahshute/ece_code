import hashlib

class FeistelNetwork:


    def __init__(self,*, iters=5000, hashing_algorithm=hashlib.pbkdf2_hmac, hashtype="sha256"):
        self.iters = iters
        self.hashing_algorithm = hashing_algorithm
        self.hashtype = hashtype

    def bxor(self, n1, n2):
        int1 = int.from_bytes(n1, byteorder="big")
        int2 = int.from_bytes(n2, byteorder="big")
        res = int1 ^ int2
        return res.to_bytes(64, byteorder="big")

    def decrypt(self, msg, salt):
        return self.encrypt(msg, salt)

    def encrypt(self, msg, salt):
        if type(salt) == str: salt = salt.encode()
        r = msg[len(msg) // 2 :]
        l = msg[: len(msg) // 2]
        for _ in range(4): 
            temp = self.bxor(l, self.hashing_algorithm(self.hashtype, r, salt, self.iters))
            l = r
            r = temp
            
        return bytes.fromhex(r.hex() + l.hex())


fn = FeistelNetwork()

phrase = b'hello this is a message which im not entirely sure how big it shhello this is a message which im not entirely sure how big it sh'
salt = b'this is a salt with 64 characters in itasdfghjklpoiuytrewqzxcvbn'

res = fn.encrypt(phrase, salt)
print(res) 
print(len(res))
print(len(phrase))
print(len(salt))
res2 = fn.decrypt(res, salt)
print(res2)




