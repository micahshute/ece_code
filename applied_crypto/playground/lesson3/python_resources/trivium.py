from python_resources.register import *

class Trivium:

    def __init__(self, key, iv):
        self.key = key
        self.iv = iv
        padded_key = str(key) + '0' * 13
        padded_iv = str(iv) + '0' * 4
        key_arr = [int(b) for b in padded_key]
        iv_arr = [int(b) for b in padded_iv]
        reg3 = [0 for _ in range(111)]
        reg3[110], reg3[109], reg3[108] = 1,1,1
        self.reg1 = Register(key_arr)
        self.reg2 = Register(iv_arr)
        self.reg3 = Register(reg3)
        # print(self.reg1.state)
        # print(len(self.reg1.state))
        # print(self.reg2.state)
        # print(len(self.reg2.state))
        # print(self.reg3.state)
        # print(len(self.reg3.state))
        # print('------------')

    def reg1_out(self):
        b66 = self.bit(66)
        return lambda out: out ^ b66

    def reg2_out(self):
        b162 = self.bit(162)
        return lambda out: out ^ b162

    def reg3_out(self):
        b243 = self.bit(243)
        return lambda out: out ^ b243

    def reg1_in(self):
        reg3_out = self.reg3_out()
        bwand3 = self.bwand(286,287)
        b69 = self.bit(69)
        return lambda r3out: reg3_out(r3out) ^ bwand3 ^ b69

    def reg2_in(self):
        reg1_out = self.reg1_out()
        bwand1 = self.bwand(91,92)
        b171 = self.bit(171)
        return lambda r1out: reg1_out(r1out) ^ bwand1 ^ b171

    def reg3_in(self):
        reg2_out = self.reg2_out()
        bwand2 = self.bwand(175, 176)
        b264 = self.bit(264)
        return lambda r2out: reg2_out(r2out) ^ bwand2 ^ b264

    def warmup(self):
        for _ in range(4 * 288):
            self.shift()

    def shift(self):
        r1out = self.reg1_out()
        r2out = self.reg2_out()
        r3out = self.reg3_out()
        r1in = self.reg1_in()
        r2in = self.reg2_in()
        r3in = self.reg3_in()
        r1do, r1update = self.reg1.shift()
        r2do, r2update = self.reg2.shift()
        r3do, r3update = self.reg3.shift()
        totout = r1out(r1do) ^ r2out(r2do) ^ r3out(r3do)
        r1update(r1in(r3do))
        r2update(r2in(r1do))
        r3update(r3in(r2do))
        # print(self.reg1.state)
        # print(len(self.reg1.state))
        # print(self.reg2.state)
        # print(len(self.reg2.state))
        # print(self.reg3.state)
        # print(len(self.reg3.state))
        # print(totout)
        # print('------------')
        
        return totout

    def bit(self, b):
        if b < 94:
            return self.reg1.state[b - 1]
        elif b < 178:
            return self.reg2.state[b -94]
        elif b < 289:
            return self.reg3.state[b - 178]

    def bwand(self, b1, b2):
        return self.bit(b1) * self.bit(b2)

    def xor(self, b1, b2):
        return self.bit(b1) ^ self.bit(b2)