from python_resources.lfsr import *

# m = matrix([[0,0,1,1,0],[1,0,0,1,1],[1,1,0,0,1],[0,1,1,0,0],[0,0,1,1,0]])
# print(m)
# print(m.det())
bitstream = "00100001000001000111010001001110010100"
# bitstream = "1110110010011101000111010001001110010100"
coeff = LFSR.crack(19, [int(bit) for bit in bitstream])
print(coeff)

# lfsr = LFSR([int(c) for c in "0001011100100110111"],[0,1,1,0,1,1,0,1,1,0,0,1,1,0,1,0,0,0,1])
# bits = []

# for i in range(38):
#     bits.append(next(lfsr.stream))

# print(bits)


# lfsr1 = LFSR([0,0,1,1,0], [0,1,1,0,1])
# lfsr2 = LFSR([0,0,1,1,0], [1,0,0,1,1])

# bits1 = []
# bits2 = []

# for i in range(10):
#     bits1.append(next(lfsr1.stream))
#     bits2.append(next(lfsr2.stream))

# print(bits1)
# print(bits2)