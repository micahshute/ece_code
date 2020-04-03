from Crypto.Util.number import *

class DiffieHelman:

    @classmethod
    def find_coprime(cls, p):
        a = getRandomRange(2, p-1)
        while GCD(a, p) != 1:
            a = getRandomRange(2, p-1)
        return a


    class Alice:
        def __init__(self, *, primelen=512, base=2):
            self.base = base
            self.mod = getStrongPrime(primelen)
            self.private = DiffieHelman.find_coprime(self.mod - 1)
            self.public = pow(self.base, self.private, self.mod)

        def public_key(self):
            return (self.mod, self.base, self.public)

        def calc_shared_secret(self, bob_public):
            self.shared_secret = pow(bob_public, self.private, self.mod)

    class Bob:
        def __init__(self, alice_tuple):
            self.base = alice_tuple[1]
            self.mod = alice_tuple[0]
            self.alice_public = alice_tuple[2]
            self.private = DiffieHelman.find_coprime(self.mod - 1)
            self.public = pow(self.base, self.private, self.mod)
            self.shared_secret = pow(alice_tuple[2], self.private, self.mod)


        def public_key(self):
            return self.public

        #NOTE: Below methods not needed for DHKE
        def inv_mod_k(self):
            return self.inv_mod(self.shared_secret, self.mod)[1]

        def kinv(self):
            return pow(self.shared_secret, self.mod - 2, self.mod)

        def nkinv(self):
            return pow(self.alice_public, self.mod - 1 - self.private, self.mod)

        def inv_mod(self,a,b):
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



alice = DiffieHelman.Alice()
alice_public = alice.public_key()
print(alice_public)
bob = DiffieHelman.Bob(alice_public)
print(bob.public_key())
alice.calc_shared_secret(bob.public_key())

print(alice.shared_secret == bob.shared_secret)

base, p, A, b, B, K = (2, 10687697916839423481635652118834007146946191294923255999661800948347650137507026580619063362540990142707750877588667878612127060085500161314697355403684817, 2928243870826960095527291341465041733378889438215298802243486942058641990714876730583731143393190263600568508345339395159154963799337791343494391943691343, 3145210314820064242923507206669481373441142139974754058098783378176549671945497998282927729775598688573873767902141750162553709308511659052840059727418475, 243091867572058234977747830694512875533111671243488638254559652058902886471446388452939490802580633118475567282374030327794613305260510150217941576250986, 10641194206677418802665706883329799029279202711791423315137652972422041285490884720641376996879901644227818499713135456300204394885953287489010786875194858)
 
bob = DiffieHelman.Bob((p, base, A))
bob.private = b
bob.public = B
bob.shared_secret = K

ink = bob.inv_mod_k()
kin = bob.kinv()
nkin = bob.nkinv()
print(ink * K % p)
print(kin * K % p)
print(nkin * K % p)