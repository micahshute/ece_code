import math
import os
import subprocess
import random
import hashlib
from Crypto.Cipher import AES

class EllipticCurve:

    @classmethod
    def bf_inv_mod(cls, a, m): 
        a = a % m
        for x in range(1, m): 
            if ((a * x) % m == 1): 
                return x 
        return 1

    @classmethod
    def gcd_inv_mod(cls,a,b):
        r, rm1 = b, a
        s, sm1 = 0, 1
        t, tm1 = 1, 0
        while r != 0:
            q = rm1 // r
            rm1, r = r, rm1 % r
            sm1, s = s, sm1 - q * s
            tm1, t = t, tm1 - q * t
        d = sm1 * a + tm1 * b
        return d, sm1, tm1
        
    @classmethod
    def inv_mod(cls, a,b):
        gim = cls.gcd_inv_mod(a,b)
        if gim[0] == 1:
            return gim[1]
        return cls.bf_inv_mod(a,b)

    @classmethod
    def generate(cls, *, name='brainpoolP512t1', filename='ecc.pem'):
        os.system(f'openssl ecparam -name {name} -out {filename} -param_enc explicit')
        ecdata = cls.read_data_from_file(filename)
        ecdata = ecdata.decode().replace(' ', '').split("\n")
        data_dict = {}
        is_hash = lambda s: s.count(':') > 1
        format_key = lambda ks: ks.split(':')[0].lower().split('(')[0]
        curr_hash = ''
        curr_key = ''
        # print(ecdata)
        for el in ecdata:
            if not is_hash(el):
                if not curr_key == '':
                    if 'gen' in curr_key or 'pub' in curr_key:
                        data_dict[curr_key] = cls.gen2i(curr_hash)
                    else:
                        data_dict[curr_key] = cls.h2i(curr_hash)
                curr_hash = ''
                curr_key = format_key(el)
            else: 
                curr_hash += el
        
        if 'gen' in curr_key or 'pub' in curr_key:
            data_dict[curr_key] = cls.gen2i(curr_hash)
        else:
            data_dict[curr_key] = cls.h2i(curr_hash)
        if 'prime' not in data_dict:
            data_dict['prime'] = data_dict['polynomial']
        # print(data_dict)
        return cls(p=data_dict['prime'], a=data_dict['a'], b=data_dict['b'], gen=data_dict['generator'], order=data_dict['order'])

    @classmethod
    def gen2i(cls, gen):
        genh = gen.replace(' ', '').replace(':', '')[2:]
        l = len(genh)
        return (int(genh[:l//2], 16), int(genh[l//2:], 16))



    @classmethod
    def h2i(cls, hexLines):
        if hexLines == '':
            return 0
        return int(hexLines.replace(':',''), 16)

    @classmethod
    def read_data_from_file(cls, filename):
        return subprocess.run(['openssl', 'ecparam', '-in', filename, '-text', '-noout'], stdout=subprocess.PIPE).stdout

    @classmethod
    def openssl_to_int(cls, str):
        return int(cls.format_hex(str), 16)

    @classmethod
    def format_hex(cls, str):
        return str.replace(":", "")

    @classmethod
    def new_from_data(cls, data):
        return cls(p=data['p'], a=data['a'], b=data['b'], gen=data['gen'], order=data['order'])

    def __init__(self, *, p,a,b, gen=None, order=None):
        self.p, self.a, self.b, self.order = p, a, b, order
        if gen is not None:
            self.gen = self.get_point(x=gen[0], y=gen[1])
        else:
            self.gen = None

    def __eq__(self, ec):
        return self.p == ec.p and self.a == ec.a and self.b == ec.b

    def get_point(self,x, y):
        point = EllipticCurve.Point(x=x, y=y, curve=self)
        if not point.is_on_curve(): 
            raise Exception(f"That point is not on the curve with a={self.a}, b={self.b}, p={self.p}")
        return point

    def random_secret(self):
        return random.randint(2, self.order - 1)

    def curve_data(self):
        return {
            'p': self.p,
            'a': self.a,
            'b': self.b,
            'gen': (self.gen.x, self.gen.y),
            'order': self.order
        }

    class Point:

        def __init__(self, *, x,y, curve):
            self.x, self.y, self.curve = x, y, curve

        def __add__(self, ec):
            if (type(ec) == EllipticCurve.Point):
                if ec.curve != self.curve:
                    raise Exception()
                else:
                    curve = ec.curve
            elif type(ec) == tuple:
                curve = self.curve
            if self.is_inf_pt():
                print("SELF WAS INF")
                return ec
            elif ec.is_inf_pt():
                # print("EC WAS INF")
                return self
            if self == ec:
                # print("SAME PT")
                s = (((3 * (self.x ** 2)) + curve.a )  * (EllipticCurve.inv_mod(( 2 * self.y), curve.p))) % curve.p
                
            else:
                try:
                    # s = ((ec.y - self.y) % curve.p / (ec.x - self.x) % curve.p) % curve.p
                    if (ec.x - self.x) == 0: raise ZeroDivisionError()
                    s = ((ec.y - self.y) *  EllipticCurve.inv_mod(ec.x - self.x, curve.p) % curve.p) % curve.p
                    # print(f's = {s} = ({ec.y} - {self.y}) / ({ec.x} - {self.x}) % {curve.p}')
                except ZeroDivisionError:
                    # print("DBZ ERR")
                    return EllipticCurve.Point(x=0,y=0, curve=curve)
            # print(f"s = {s}")
            x = ((s ** 2) - self.x - ec.x) % curve.p
            y = ((s * (self.x - x)) - self.y) % curve.p
            return EllipticCurve.Point(x=x,y=y, curve=curve)

        def __eq__(self, pt):
            return self.x == pt.x and self.y == pt.y and self.curve == pt.curve

        def __mul__(self, num):
            tot_sum = None
            multiplier = num
            val = self
            valnum = 1
            while multiplier > 1:
                if multiplier % 2 == 1:
                    if tot_sum is None:
                        tot_sum = val
                    else:
                        tot_sum += val
                multiplier = multiplier // 2
                val = val + val
                valnum = valnum + valnum
            # print(valnum)
            if tot_sum is None: 
                tot_sum = val
            else:
                tot_sum += val
            return tot_sum

        def __str__(self):
            return f'x: {self.x}, y: {self.y}'


        @property
        def coord(self):
            return (self.x, self.y)

        def is_inf_pt(self):
            return self.x == 0 and self.y == 0

        def is_on_curve(self):
            return ((self.y ** 2) % self.curve.p) == ((self.x ** 3) + (self.curve.a * self.x) + self.curve.b) % self.curve.p

        def to_tuple(self):
            return self.coord

# p = 101
# a = -1
# b = 1
# # p = 7
# # a = 3
# # b = 4
# ec = EllipticCurve(p=p, a=a, b=b)
# # p1 = EllipticCurve.Point(x=1, y=1, curve=ec)
# # p2 = EllipticCurve.Point(x=1, y=1, curve=ec)
# p1 = ec.get_point(1,1)
# p2 = ec.get_point(0,1)
# a = p1 + p1 + p1 + p1 + p1 + p1 + p1 + p1 + p1 + p1 + p1 + p1 + p1 + p1
# print('--------------')
# b = p1 * 14
# print('-----')
# # print(p1 + p1 + p1 + p1)
# print('----')
# print(a)
# print(b)
# print(a.is_on_curve())
# print(p1 * 4)
# print(p1)
# print(p1 * 4 + p1)
# print(p1 + p1 * 4)
# a = p1 + p2
# print(a)
# print(p1.is_on_curve())
# print(p2.is_on_curve())
# print(a.is_on_curve())

# ap1p2 = a + p1 + p2 + p1 + p1 + p1 
# print(ap1p2.is_on_curve())
# print(p1)
# print(ap1p2)
# print(ap1p2 + p1)
### TEST 2

class ECCDHEParty:
    
    def __init__(self,*, curve_data=None, EC=EllipticCurve, curve_name=None):
        if curve_data is None:
            if curve_name is None: 
                self.ec = EC.generate()
            else:
                self.ec = EC.generate(name=curve_name)
        else:
            self.ec = EC.new_from_data(curve_data)
        self.secret = self.ec.random_secret()
        self.public = self.ec.gen * self.secret

    def publish_curve(self):
        return self.ec.curve_data()

    def publish_public(self):
        return self.public.to_tuple()

    def calc_shared(self, partner_public):
        if type(partner_public) == tuple:
            partner_public = EllipticCurve.Point(x=partner_public[0], y=partner_public[1], curve=self.ec)
        self.shared = partner_public * self.secret
        sharedx_hex = self.padhex(format(self.shared.x, 'x'))
        sharedx_bytes = bytes.fromhex(sharedx_hex)
        self.aes_key = hashlib.sha256(sharedx_bytes).digest()
    
    def padhex(self, h):
        return '0' * (len(h) % 2) + h

    def padbytes(self, msg, s=16):
        return msg + b"\x00" * (s - (len(msg) % s))

    def encrypt(self, msg, *, mode=AES.MODE_CBC):
        if type(msg) == str:
            msg = msg.encode()
        pmsg = self.padbytes(msg)
        iv = os.urandom(16)
        aes = AES.new(self.aes_key, mode, iv=iv)
        cout = aes.encrypt(pmsg).hex()
        ivh = iv.hex()
        return ivh + cout

    def decrypt(self, ctxt, *, mode=AES.MODE_CBC):
        iv = bytes.fromhex(ctxt[:32])
        cmsg = bytes.fromhex(ctxt[32:])
        baes = AES.new(self.aes_key, mode, iv=iv)
        return baes.decrypt(cmsg).decode()




# Tested and works with name=secp521r1
# Without name defaults to brainpoolP512t1 which according to 
# the IETF complies with NIST standards



alice = ECCDHEParty(curve_name="secp521r1")
curve_data_to_bob = alice.publish_curve()

bob = ECCDHEParty(curve_data=curve_data_to_bob)

bob_public = bob.publish_public()
alice_public = alice.publish_public()

alice.calc_shared(bob_public)
bob.calc_shared(alice_public)

print(f"Alice and Bob have calculated the same shared secret: {alice.shared == bob.shared}")

smsg = "I am alice and I am sending secrets to bob!"
print(f"Alice wants to send the message: {smsg}")
cmsg = alice.encrypt(smsg)
print(f"Alice sends the iv|ciphertext: {cmsg}")

bmsg = bob.decrypt(cmsg)
print(f'Bob decrypts the plaintext: {bmsg}')





# ec = EllipticCurve.generate(name='secp521r1')

# print(ec.gen.is_on_curve())
# print(f'Generator X: {ec.gen.x}\nGenerator Y: {ec.gen.y}')

# alice_secret = ec.random_secret()
# print(f"Alice Secret: {alice_secret}")
# alice_public = ec.gen * alice_secret
# print(f"Alice Public: {alice_public}")
# curve_export_data = ec.curve_data()


# bob_ec = EllipticCurve.new_from_data(curve_export_data)
# bob_secret = bob_ec.random_secret()
# print(f"Bob Secret: {bob_secret}")
# bob_public = bob_ec.gen * bob_secret
# print(f"Bob Public: {bob_public}")

# alice_shared = bob_public * alice_secret

# bob_shared = alice_public * bob_secret
# print(f"Alice's shared Secret: {alice_shared}")
# print(f"Alice and Bob's shared secret is identical: {alice_shared == bob_shared}")
# # print(format(alice_shared.x, 'x'))
# # print(len(format(alice_shared.x, 'x')))
# def padhex(h):
#     return '0' * (len(h) % 2) + h

# ahex = format(alice_shared.x, 'x')
# bhex = format(bob_shared.x, 'x')

# axcoordbytes = bytes.fromhex(padhex(ahex))
# bxcoordbytes = bytes.fromhex(padhex(bhex))
# ashared_aes = hashlib.sha256(axcoordbytes).digest()
# bshared_aes = hashlib.sha256(bxcoordbytes).digest()

# print(f"Hashed AES keys identical: {ashared_aes == bshared_aes}")

# def pad(msg, s=16):
#     return msg + b"\x00" * (len(msg) % s)

# iv = os.urandom(16)
# key = ashared_aes

# aes = AES.new(key, AES.MODE_CBC, iv=iv)
# msg = 'This is a secret message'
# pmsg = pad(msg.encode())
# print("\n\n\n\n")
# print(f"Alice wants to decrypt and send: {msg}")
# out = aes.encrypt(pmsg).hex()

# ivhex = iv.hex()

# a2b = ivhex + out
# print(f"The encrypted IV and msg sent to Bob is: {a2b}")

# bob_iv = bytes.fromhex(a2b[:32])
# bob_cipher = bytes.fromhex(a2b[32:])
# baes = AES.new(bshared_aes, AES.MODE_CBC, iv=bob_iv)
# omsg = baes.decrypt(bob_cipher).decode()

# print(f"Bob has decrypted and received the msg: {omsg}")

# print(f"The message sent by Alice matches the message received by Bob: {msg in omsg}")

