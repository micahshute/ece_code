from Crypto.PublicKey import RSA 
import random
import math
import os
import subprocess
import hashlib
from Crypto.Cipher import AES
from Crypto.Signature import pss
from Crypto.Hash import SHA256
import json


class CertificateError(Exception):
    pass

class JSONSerializerStrategy:

    @classmethod
    def stringify(cls, d):
        return json.dumps(d)

    @classmethod
    def parse(cls, str):
        return json.loads(str)

#NOT USED - INSECURE
class RSASignatureClassroomStrategy:

    @classmethod
    def sign(cls, msg, pkey):
        if type(msg) == int:
            i = msg
        elif type(msg) == str:
            i = int(msg.encode().hex(), 16)
        elif type(msg) == bytes:
            i = int(msg.hex(), 16)
        else:
            raise Exception(f"Unsupported type of msg: {type(msg)}")
        return pow(i, pkey.d, pkey.n)

    @classmethod
    def verify(cls, *, pubkey, sig, tostr=True, verification=None, prehashed=False):
        ret = pow(sig, pubkey['e'], pubkey['n'])
        if tostr:
            h = format(ret, 'x')
            ret = bytes.fromhex(cls.padhex(h)).decode()
        if verification is not None:
            return ret == verification
        return ret

    @classmethod
    def padhex(self, h):
        return '0' * (len(h) % 2) + h



# DEFAULT due to security + easy serialization
class RSASignatureHashingStrategy:
    @classmethod
    def sign(cls, msg, pkey):
        if type(msg) == int:
            h = cls.padhex(format(msg, 'x'))
            b = bytes.fromhex(h)
        elif type(msg) == str:
            b = msg.encode()
        elif type(msg) == bytes:
            b = msg
        else:
            raise Exception(f"Unsupported type of msg: {type(msg)}")
        dig = hashlib.sha256(b).digest()
        i = int(dig.hex(), 16)
        return pow(i, pkey.d, pkey.n)

    @classmethod
    def verify(cls, *, pubkey, sig, tostr=True, verification=None, prehashed=False):
        ret = pow(sig, pubkey['e'], pubkey['n'])
        if tostr:
            h = format(ret, 'x')
            ret = bytes.fromhex(cls.padhex(h))
        if verification is not None:
            if not prehashed:
                if type(verification) == int:
                    verification = bytes.fromhex(cls.padhex(format(verification,'x')))
                elif type(verification) == str:
                    verification = verification.encode()
                verification = hashlib.sha256(verification).digest()
            return ret == verification
        return ret

    @classmethod
    def padhex(cls, h):
        return '0' * (len(h) % 2) + h

    @classmethod
    def padmsg(cls, msg, s=16):
        if type(msg) == str:
            msg = msg.encode()
        return msg + b"\x00" * (s - (len(msg) % s))




# WORKS, and is most secure, but it hard to serialize the public key
# objects which are required. The answer would be to stringify them
# into PEM files and send those, but I'm already a week late on this
# project...
class RSASignaturePSSStrategy:

    @classmethod
    def sign(cls, msg, pkey):
        if type(msg) == int:
            h = SHA256.new(bytes.fromhex(cls.padhex(format(mgs, 'x'))))
        elif type(msg) == str:
            h = SHA256.new(msg.encode())
        elif type(msg) == bytes:
            h = SHA256.new(msg)
        else:
            raise Exception(f"Unsupported type of msg: {type(msg)}")
        return pss.new(pkey).sign(h)

    @classmethod
    def verify(cls, *, pubkey, sig, tostr=True, verification=None, prehashed=False):
        if type(sig) == int:
            sig = bytes.fromhex(cls.padhex(format(sig, 'x')))
        if type(pubkey) == dict:
            pubkey = RSASignaturePSSStrategy.FakeKey(e=pubkey['e'],  n=pubkey['n'])
        if not prehashed:
            if type(verification) == str:
                verification = verification.encode()
            verification = SHA256.new(verification)
        try:
            pss.new(pubkey).verify(verification, sig)
            return True
        except (ValueError, TypeError):
            return False

    @classmethod
    def padhex(self, h):
        return '0' * (len(h) % 2) + h

    class FakeKey:
        def __init__(self,*, e, n):
            self.e, self.n = e, n


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
    def verify_signature(cls, *, pubkey, sig, tostr=True, verification=None, strategy=RSASignatureHashingStrategy, prehashed=False):
        return strategy.verify(pubkey=pubkey, sig=sig, tostr=tostr, verification=verification, prehashed=prehashed)


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
    def __init__(self, *, n, p, q, d, e, keyobj=None, signing_strategy=RSASignatureHashingStrategy):
        self.n, self.p, self.q, self.d, self.e = n,p,q,d,e
        self.keyobj = keyobj
        self.signing_strategy = signing_strategy

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
        return self.signing_strategy.sign(msg, self.keyobj)

    def publish_key(self):
        return self.keyobj.publickey()

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
                    raise Exception('The curves are not equal')
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
        self.shared = None

    def publish_curve(self):
        return self.ec.curve_data()

    def publish_public(self):
        return self.public.to_tuple()

    def calc_shared(self, partner_public):
        if type(partner_public) == tuple or type(partner_public) == list:
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
        plain = baes.decrypt(cmsg).decode()
        return plain.replace("\x00", "")





class TLSConnection:

    @classmethod
    def begin(cls, id):
        return cls(id)


    def __init__(self, id, *, curve="brainpoolP512t1", certificate_strategy=RSAManager):
        self.certificate_strategy = certificate_strategy
        alice = TLSConnection.TLSParty(id, curve=curve, connection=self, certificate_strategy=certificate_strategy)
        self.connections = {}
        self.connections[id] = alice
    
    def join(self, id):
        if id == list(self.connections.keys())[0]:
            raise Exception("You must provide a unique id")
        if len(self.connections) == 1:
            alice = list(self.connections.items())[0][1]
            connection_dict = {
                "id": alice.id, 
                "certificate_pubkey": alice.certificate_manager.publickey()
            }
            bob = TLSConnection.TLSParty(id, connection=self, certificate_strategy=self.certificate_strategy, connected_to=connection_dict)
            self.connections[bob.id] = bob
            alice.commence_handshake(bob.id, bob.certificate_manager.publickey())
            return (alice, bob)
        else:
            raise Exception("This connection is not joinable")


    def send(self, data, *, to):
        self.connections[to].receive(data)



    class TLSParty:

        def __init__(self, id, *, connection, curve=None, certificate_strategy, connected_to=None, serializer_strategy = JSONSerializerStrategy):
            self.id = id
            self.serializer_strategy = serializer_strategy
            self.buffer = []
            self.connection = connection
            self.certificate_manager = certificate_strategy.generate()
            if connected_to is None:
                self.encryption_party = ECCDHEParty(curve_name=curve)
                self.handshake_data = self.encryption_party.publish_curve()
                self.connected_to = {}
            else:
                self.encryption_party = None
                self.connected_to = connected_to

        @property
        def partner_id(self):
            return self.connected_to["id"]

        @property
        def partner_sigkey(self):
            return self.connected_to["certificate_pubkey"]
        
        @property
        def connection_established(self):
            return self.encryption_party is not None and self.encryption_party.shared is not None

        def serialize_and_sign(self, msg):
            print(f"-------Sender: {self.id}--------")
            if "types" in msg:
                print(f"Handshake message, sending: {msg['types']}")
            else:
                print("Not a handshake")
            ## ENCRYPT THEN SIGN
            strmsg = self.serializer_strategy.stringify(msg)
            if self.connection_established:
                print("Ecnrcypting message before sign")
                strmsg = self.encryption_party.encrypt(strmsg)
            else:
                print("No encryption set up, not encrypting msg")
            
            # Note that depending on the strategy inthe certificate strategy,
            # this signed RSA certificate is most likely based on a SHA256 hash
            # of the msg
            sig = self.certificate_manager.sign(strmsg)
            # signature is an int, but if you try to change it at all
            # you will see that it will not pass upon receipt
            package = {
                "body": strmsg,
                "signature": sig
            }
            return self.serializer_strategy.stringify(package)


        def commence_handshake(self, recipient_id, certificate_pubkey):
            self.connected_to = { "id": recipient_id, "certificate_pubkey": certificate_pubkey }
            curvedata = self.encryption_party.publish_curve()
            pubkey = self.encryption_party.publish_public()

            data = {
                "data": {
                    "curve": curvedata,
                    "pubkey": pubkey
                },
                "types": ["curve", "pubkey"]
            }
            self.send(data)


        def receive_curve(self, curvedata):
            self.encryption_party = ECCDHEParty(curve_data=curvedata)
            pubkey = self.encryption_party.publish_public()
            msg = {
                "data": {
                    "pubkey": pubkey
                },
                "types": ["pubkey"]
            }
            self.send(msg)

        def receive_publickey(self, pkdata):
            self.encryption_party.calc_shared(pkdata)
            print('------------------------')
            print(f"{self.id} has established a connection: {self.connection_established}")
            print('------------------------')

        def send(self, msg):
            body = self.serialize_and_sign(msg)
            self.connection.send(body, to=self.connected_to["id"])

        def verify_signature(self, sig, verification, pubkey):
            if not self.certificate_manager.verify_signature(sig=sig, pubkey=pubkey, verification=verification):
                raise CertificateError("The Signature was bad!")

        def receive(self, res):
            print(f"Visible Message across internet: {res}")
            pubkey = self.partner_sigkey
            print(f"------Receiver: {self.id}-----")
            try:
                pres = self.serializer_strategy.parse(res)
                serialized_data = pres["body"]
                self.verify_signature(pres["signature"], serialized_data, pubkey)
                print("Signature Passes")

                if self.connection_established:
                    # print(f"Decrypting incoming data...{serialized_data}")
                    print('Decrypting incoming data...')
                    serialized_data = self.encryption_party.decrypt(serialized_data)
                else:
                    print('Data is not encrypted...')

                parsed_data = self.serializer_strategy.parse(serialized_data)

                if "types" in parsed_data:
                    if "curve" in parsed_data["types"]:
                        print(f"{self.id} is receiving curve data")
                        self.receive_curve(parsed_data["data"]["curve"])
                    if "pubkey" in parsed_data["types"]:
                        print(f"{self.id} is receiving encryption publickey")
                        self.receive_publickey(parsed_data["data"]["pubkey"])
                else:
                    print("Saving message...")
                    self.buffer.append(parsed_data)
            except CertificateError:
                print("Discarded packet due to bad signature")


#########################################################################
#########################################################################
#########################################################################
###################### TEST ABOVE CODE: DIY TLS #########################
#########################################################################
#########################################################################
#########################################################################


# The below code conductions a handshake, calculates a shared secret,
# encrypts with AES all comms and signs a hashed version 
# of the messagewith an RSA private key.

conn = TLSConnection.begin("Thor")
thor, tony = conn.join("Stark")

tony.send("Can you hear me")
thor.send("I am a god")
tony.send("ok...")
thor.send("you people are so petty, and tiny")
tony.send("Shakespeare in the park? Doth mother know you weareth her drapes?")
thor.send("Fortunately, I am mighty!")
tony.send("worst conversationalist ever")
long_text_test = "So what does it mean to be a greedy algorithm? It means that we make decisions based on the best choice at the time. This isn’t always the best thing to do — for example, if you were implementing a chess bot, you wouldn’t want to take the other player’s queen if it opened you up for a checkmate the next move! For situations like this, something like minimax would work better. In our case today, this greedy approach is the best thing to do and it drastically reduces the number of checks I have to do without losing accuracy. How?? Well, let’s say I am at my source node. I will assume an initial provisional distance from the source node to each other node in the graph is infinity (until I check them later). I know that by default the source node’s distance to the source node is minium (0) since there cannot be negative edge lengths. My source node looks at all of its neighbors and updates their provisional distance from the source node to be the edge length from the source node to that particular neighbor (plus 0). Note that you HAVE to check every immediate neighbor; there is no way around that. Next, my algorithm makes the greedy choice to next evaluate the node which has the shortest provisional distance to the source node. I mark my source node as visited so I don’t return to it and move to my next node. Now let’s consider where we are logically because it is an important realization. The node I am currently evaluating (the closest one to the source node) will NEVER be re-evaluated for its shortest path from the source node. Its provisional distance has now morphed into a definite distance. Even though there very well could be paths from the source node to this node through other avenues, I am certain that they will have a higher cost than the node’s current path because I chose this node because it was the shortest distance from the source node than any other node connected to the source node. So any other path to this mode must be longer than the current source-node-distance for this node. Using our example graph, if we set our source node as A, we would set provisional distances for nodes B, C, and E. Because Ehad the shortest distance from A, we then visited node E. Now, even though there are multiple other ways to get from Ato E, I know they have higher weights than my current A→ E distance because those other routes must go through Bor C, which I have verified to be farther from A than E is from A. My greedy choice was made which limits the total number of checks I have to do, and I don’t lose accuracy! Pretty cool."
thor.send(long_text_test)
tony.send('whoever wrote that is a goddamn genius')

print('---------------------------------------------------')
print('---------------------------------------------------')
print("---------  RECEIVED UNENCRYPTED MESSAGES ----------")
print('---------------------------------------------------')
print('---------------------------------------------------')
print("Thor's received messages:")
print(thor.buffer)
print('-----------')
print('-----------')
print("Tony's received messages:")
print(tony.buffer)
