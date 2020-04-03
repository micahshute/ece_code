import os
import math
from Crypto.PublicKey import RSA 
import random

class RSAManager:

    @classmethod
    def generate(cls,*,e=65537, bits=2048):
        nk = RSA.generate(bits, e=e)
        return cls.new_from_rsa(nk)

    @classmethod
    def new_from_pem(cls, pem):
        nk = RSA.importKey(pem)
        return cls.new_from_rsa(nk)

    @classmethod
    def new_from_rsa(cls, nk):
        return RSAManager(n=nk.n, p=nk.p, q=nk.q, d=nk.d, e=nk.e, keyobj=nk)

    @classmethod
    def exp_mod(cls, msg, exp, mod):
        return pow(msg, exp, mod)

    @classmethod
    def bf_key(cls, public, mod):
        p,q = cls.factor(mod)
        phi = (p-1) * (q-1)
        private = cls.inv_mod(public, phi)
        return private

    @classmethod
    def raw_to_int(cls, str):
        hx = cls.format_hex(str)
        return int(hx, 16)

    @classmethod
    def format_hex(cls, str):
        return str.replace(":", "")

    @classmethod
    def factor(cls, n):
        for i in range(math.ceil(math.sqrt(n)), 1, -1):
            if n % i == 0:
                return (i, n // i)
    
    @classmethod
    def padhex(self, h):
        return '0' * (len(h) % 2) + h

    @classmethod
    def verify_signature(cls, *, pubkey, sig, tostr=True, verification=None):
        ret = cls.encrypt_int(sig, e=pubkey['e'], n=pubkey['n'])
        if tostr:
            h = format(ret, 'x')
            ret = bytes.fromhex(cls.padhex(h)).decode()
        if verification is not None:
            return ret == verification
        return ret

    @classmethod
    def encrypt_int(cls, msg, *, e=None, n=None, tohex=False):
        cipher = cls.exp_mod(msg, e, n)
        if tohex:
            cipher = format(cipher, 'x')
        return cipher

    @classmethod
    def inv_mod(cls,a,b):
        r, rm1 = b, a
        s, sm1 = 0, 1
        t, tm1 = 1, 0
        while r != 0:
            q = rm1 // r
            rm1, r = r, rm1 % r
            sm1, s = s, sm1 - q * s
            tm1, t = t, tm1 - q * t
        d = sm1 * a + tm1 * b
        # return d, sm1, tm1
        return sm1

    # n = mod
    # p * q = n
    # phi = (p-1) * (q-1)
    # d = public
    # e  = private
    def __init__(self, *, n, p, q, d, e, keyobj=None):
        self.n, self.p, self.q, self.d, self.e = n,p,q,d,e
        self.keyobj = keyobj

    @property
    def phin(self):
        return (self.p - 1) * (self.q - 1)

    def publickey(self):
        return {'n': self.n, 'e': self.e}


    def export_key(self, f="PEM"):
        if self.keyobj is not None:
            self.keyobj.exportKey(f)
        else:
            raise Exception("This functionality is not available")

    def export_pub_key(self, f="PEM"):
        if self.keyobj is not None:
            self.keyobj.publickey().exportKey(f)
        else:
            raise Exception("This functionality is not available")

    def sign(self, msg):
        return self.create_signature(msg)

    def create_signature(self, msg):
        if type(msg) == int:
            i = msg
        elif type(msg) == str:
            i = int(msg.encode().hex(), 16)
        elif type(msg) == bytes:
            i = int(msg.hex(), 16)
        else:
            raise Exception(f"Unsupported type of msg: {type(msg)}")
        return self.decrypt_int(i)


    def encrypt_str(self, msg,*, key=None, mod=None, tohex=False):
        num = int(msg.encode().hex(), 16)
        return RSAManager.encrypt_int(num, e=key, n=mod, tohex=tohex)


    def decrypt_hex(self, msg, tostr=True):
        num = int(msg, 16)
        dnum = self.decrypt_int(num)
        if tostr:
            return bytes.fromhex(format(dnum, 'x')).decode()
        else:
            return dnum


    def decrypt_int(self, msg):
        return RSAManager.exp_mod(msg, self.d, self.n)



rsa = RSAManager.generate()
msg = "I solemnly swear to learn applied cryptography. Even though there are not enough graded assignments to incentivize the needed hours I will: 1) work problems 2) ask questions 3) ponder start-ups 4) think in a paranoid fashion 5) get it done without excuse"

sig = rsa.create_signature(msg)
print(f"Digital Signature: {sig}")
print(f"Assocaiated Public Key: {rsa.publickey()}")
res = RSAManager.verify_signature(sig=sig, pubkey=rsa.publickey(), verification=msg)
print(f"Signature passed verification: {res}")


# sig = 4377422687926411849499596957591617625758091221351147791767421440128652653604872273015931268629919888009531490009081766030799861613950550872197224046322574878310357395118958541513339491233097071233878099737894932293874710142076043262559277840155669214722224450272427630377855801439714892571436022329811572034433713222247260008612179701813382797989239134680601085451250048902504908887666029430401851506093454631936844185404849290865335013520045652237309343579638339787410678821981854963417030369345647970398734853094314504849693524278177920444692016019102757213923378100402056308932861168981461259616674487451337996190
# n = 20458140578971540545302477912993200186837262400900314199659784061507340424175109920971250526747069966943441828410075612143073747201475180065792714238721550017733046324462565309974712992566487388224670123739431339187259896197245206218405733387316747769565525789525738005451553011714557003144656094247689894277149619900498218991105955000821842207995457185064013511071581254001090543514237841490071120609078149390182171550333765991510203311487036339279658649145532345025500909796268758535390150472575671015476306081526663420262615919669352372153228948143090694310008569845279699540354867310162328870266365123867762896939
# e = 65537
# pubkey = {'n': n, 'e': e}
# verified = RSAManager.verify_signature(sig=sig, pubkey=pubkey, verification=msg)
# print(verified)

### TRICK INTO SIGNING VALID MESSAGE
pubkey = rsa.publickey()
fakesig = random.randint(2, rsa.n)
fakemsg = pow(fakesig, pubkey['e'], pubkey['n'])
print(f"Fake msg: {fakemsg}")
faketest = RSAManager.verify_signature(pubkey=pubkey, sig=fakesig, tostr=False, verification=fakemsg)
print(faketest)

trick_msg = "I, the undersigned, do solemnly swear to pick boogers, eat them, and wipe any excess on my shirt."
trick_int = int(trick_msg.encode().hex(), 16)

fake_noise = (RSAManager.inv_mod(fakemsg, pubkey['n']) * trick_int) % pubkey['n']

print(f"Fake Noise: {fake_noise}")


#Trick them into signing the fake noise: 
fake_noise_sig = rsa.sign(fake_noise)

reconstructed_msg_int = fake_noise * fakemsg % pubkey['n']
reconstructed_msg_hex = format(reconstructed_msg_int, 'x')
reconstructed_msg_str = bytes.fromhex(RSAManager.padhex(reconstructed_msg_hex)).decode()
print(f"The msg can be reconstructed to the orginal: {reconstructed_msg_str}")

trick_constructed_sig = fake_noise_sig * fakesig % pubkey['n']

trickres = RSAManager.verify_signature(pubkey=pubkey, sig=trick_constructed_sig, verification=reconstructed_msg_str)
print(f"The forged verified signing has been confirmed: {trickres}")






# faketxt = bytes.fromhex(RSAManager.padhex(format(fakemsg, 'x'))).decode()

# nraw = "00:c6:23:41:bb:52:10:0d:66:b1:52:0c:d8:af:c5:4d:70:a1:e2:7b:52:aa:45:fd:23:0a:d9:47"
# eraw = "24:50:d9:ff:67:6f:21:c5:ac:c2:89:30:3e:22:0d:10:00:e2:fa:a6:84:15:e9:62:1e:07:41"
# praw = "0f:e2:2d:e9:21:0c:aa:bd:49:72:72:73:4f:09"
# qraw = "0c:79:74:09:ee:f6:ef:8f:a1:77:2a:d9:a9:cf"



# n = RSAManager.raw_to_int(nraw)
# d = RSAManager.raw_to_int(eraw)
# p = RSAManager.raw_to_int(praw)
# q = RSAManager.raw_to_int(qraw)
# e = 65537

# rsa = RSAManager(n=n, e=e, p=p, q=q, d=d)



# n2raw = '00:d9:91:de:97:7a:93:15:29:87:23:ba:e8:61:c3:78:7d:34:4f:21:53:a0:c2:81:d0:71:28:9d'
# e2raw = '4e:4e:b6:33:07:27:11:22:d5:45:02:ec:c8:d8:93:f9:e0:36:bf:1d:85:d9:8f:c7:cc:6f:f1'
# p2raw = '0f:8c:52:37:bd:3b:9a:f3:8b:da:a8:21:14:17'
# q2raw = '0d:fe:49:97:05:d0:7d:73:ca:1b:02:53:35:6b'


# n = RSAManager.raw_to_int(n2raw)
# d = RSAManager.raw_to_int(e2raw)
# p = RSAManager.raw_to_int(p2raw)
# q = RSAManager.raw_to_int(q2raw)
# e = 65537

# rsa2 = RSAManger(n=n, e=e, p=p, q=q, d=d)

# rsapub = (rsa.e, rsa.n)
# rsa2pub = (rsa2.e, rsa2.n)

# rsa_2_rsa2_msg = "Hello from 1 to 2"
# rsa_2_rsa2_cipher = rsa.encrypt_str(rsa_2_rsa2_msg, key=rsa2pub[0], mod=rsa2pub[1], tohex=True)

# print(rsa_2_rsa2_cipher)

# decrypted = rsa2.decrypt_hex(rsa_2_rsa2_cipher)
# print(decrypted)

# calc_rsa2_private = RSAManager.bf_key(rsa2pub[0], rsa2pub[1])
# print(calc_rsa2_private)
# print(rsa2.e)

# tocrack_int = int(rsa_2_rsa2_cipher, 16)
# cracked = pow(tocrack_int, calc_rsa2_private, rsa2pub[1])
# print("CRACKED???")
# print(cracked)