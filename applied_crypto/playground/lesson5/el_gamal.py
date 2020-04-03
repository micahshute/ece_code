from Crypto.Util.number import *

class DiffieHelman:

    @classmethod
    def find_coprime(cls, p):
        a = getRandomRange(2, p-1)
        while GCD(a, p) != 1:
            a = getRandomRange(2, p-1)
        return a


    class Alice:
        def __init__(self, *, primelen=512, base=2, mod=None):
            self.base = base
            if mod is None:
                self.mod = getStrongPrime(primelen)
            else:
                self.mod = mod
            self.private = DiffieHelman.find_coprime(self.mod - 1)
            self.public = pow(self.base, self.private, self.mod)
            self.bob_public = None

        @property
        def public_key(self):
            return (self.mod, self.base, self.public)

        def calc_shared_secret(self, bob_public):
            self.bob_public = bob_public
            self.shared_secret = pow(self.bob_public, self.private, self.mod)

        @property
        def partner_public(self):
            return self.bob_public

    class Bob:
        def __init__(self, alice_tuple):
            self.base = alice_tuple[1]
            self.mod = alice_tuple[0]
            self.alice_public = alice_tuple[2]
            self.private = DiffieHelman.find_coprime(self.mod - 1)
            self.public = pow(self.base, self.private, self.mod)
            self.shared_secret = pow(alice_tuple[2], self.private, self.mod)

        @property
        def public_key(self):
            return self.public

        @property
        def partner_public(self):
            return self.alice_public

        
class ElGamal(DiffieHelman):

    @classmethod
    def modinv(cls, partner_public, mod, my_private):
        return pow(partner_public, mod - 1 - my_private, mod)

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
            return d, sm1, tm1


    class AssymetricPartner:

        @property
        def kinv(self):
            return ElGamal.modinv(self.partner_public, self.mod, self.private)


        def encrypt_str(self, msg, *,tohex=False):
            if type(msg) == str: msg = msg.encode()
            cipher = self.encrypt(int(msg.hex(), 16))
            if tohex:
                cipher = format(cipher, 'x')
            return cipher

        def decrypt(self, msg, *, tostr=False, tohex=False, isint=False):
            plain = None
            if isint:
                plain = self.decrypt_int(msg)
            else:
                plain = self.decrypt_int(int(msg, 16))
            if tohex or tostr:
                plain = format(plain, 'x')
            if tostr:
                plain = bytes.fromhex(plain).decode()
            return plain

        def encrypt(self, msg):
            return msg * self.shared_secret % self.mod

        def decrypt_int(self, cipher):
            return cipher * self.kinv % self.mod

        
    class Alice(DiffieHelman.Alice, AssymetricPartner):
        pass
        
    class Bob(DiffieHelman.Bob, AssymetricPartner):
        pass


p = int("E912ECF78A51FC5BBFA26A00E07A0CEC5ECEB897891643DD7DDD8056A51C71124258D52DAEF464B929F6397101F00C67CFC09B3D068B522E1C8B566431936C3A606A47928582F0D8D6B23F9019FF06A900CD5AD97E02CD3DEAA0495C968A2345858C6556623A61124C711DC0708999C08D5A349592F37DFE07A49C0D82241403", 16)
g = 2
# A = 74408461136476320040192012135939914206055185388982528814699228607013251386391305269826054254891759379863863350759949854053136667839141533267044866287518881777090596009115974238701991862409036124157408378577307084001963882534383746663373531423044012469587476373606501927304895322027352383290037195042880235768
# bob = ElGamal.Bob((p,g,A))
# print("PUBLIC KEY:")
# print(bob.public_key)
# print("PRIVATE KEY:")
# print(bob.private)
# print("SHARED SECRET:")
# print(bob.shared_secret)
# print("CIPHERTEXT:")
# print(bob.encrypt_str("i dont have a good secret"))
# C = 24508988142979968191529732374203129360472121173722855942277614720103918910024688717989884146360064764739922248503642710514953769038209360195792726366125058725111625764198665038975940123218925398254512513492948219834589408185426576334115927553355618459852285083075582713761455909960836542572377139059864249378



# alice = ElGamal.Alice(mod=p, base=g)
# alice_public = alice.public_key
# print(alice_public)
# print(alice.private)


# bob = ElGamal.Bob(alice_public)
# alice.calc_shared_secret(bob.public_key)

# msg = 'I dont have a good secret'
# cipher = alice.encrypt_str(msg)
# cipherhex = alice.encrypt_str(msg, tohex=True)
# print(cipher)
# print(cipherhex)

# orig = bob.decrypt(cipherhex, tostr=True)
# print(orig)



### Mod 5 Lesson 2

c1 = 18424891061981125566079466891923819180189054061023814911996244968757009636277781996991198589205553366877632626019687233233562516536979650853205499214249094240900255342184044396745719365913308597675593979310737613720122429835760055805218845303574586686599271581737663333099357124617446774817423136689946166367

c2 = 147916986843316695573527469896022062497486746186799547986333428947128110557487364196308461373471989565404856104071324637254647685467504146965165326708794537673201648748801360926219432677374843811543425663953769549430785910736947688203941658591437841781348072102214897713002887676885484302975358896835374731746

# c1 = m1 * k % p
m1 = int(b'andy love simone'.hex(), 16)

invm1 = ElGamal.inv_mod(m1, p)[1]
print('------m^-1-------')
print(invm1)
k = c1 * invm1 % p
print('----K----')
print(k)
invk = ElGamal.inv_mod(k, p)[1]

msg2int = c2 * invk % p
msg2bytes = bytes.fromhex(format(msg2int, 'x'))
msg2 = msg2bytes.decode()
print(msg2)