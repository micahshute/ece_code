from python_resources.hill_cipher_cracker import * 
import numpy as np
from python_resources.frequency_analysis import * 


def c2i(character):
    return ord(character)-ord('A')

def i2c(encoded):
    return chr(ord('a') + encoded)

def hill_enc(plain):
    found = False
    a=1
    b=1
    c=1
    d=1
    a,b,c,d = [17, 25, 19, 2]
    # a,b,c,d = [19,19,20,3]
    # a,b,c,d = [3,3,2,5]
    secret = ''
    for i in range(0, len(plain) - 1, 2):
        i1 = c2i(plain[i])
        i2 = c2i(plain[i+1])
        c1 = (i1*a + i2*b) % 26
        c2 = (i1*c + i2*d) % 26
        secret += i2c(c1) + i2c(c2)
    return secret, [a,b,c,d]


key = np.matrix([[17,25], [19,2]])
# key = np.matrix([[19,19], [20,3]])
# key = np.matrix([[3,3], [2,5]])

teststr = "The basic Hill cipher is vulnerable to a known-plaintext attack because it is completely linear. An opponent who intercepts {\displaystyle n}n plaintext/ciphertext character pairs can set up a linear system which can (usually) be easily solved; if it happens that this system is indeterminate, it is only necessary to add a few more plaintext/ciphertext pairs. Calculating this solution by standard linear algebra algorithms then takes very little time. While matrix multiplication alone does not result in a secure cipher it is still a useful step when combined with other non-linear operations, because matrix multiplication can provide diffusion. For example, an appropriately chosen matrix can guarantee that small differences before the matrix multiplication will result in large differences after the matrix multiplication. Indeed, some modern ciphers use a matrix multiplication step to provide diffusion. For example, the MixColumns step in AES is a matrix multiplication. The function g in Twofish is a combination of non-linear S-boxes with a carefully chosen matrix multiplication (MDS)."
# teststr = "help"

fa2 = FrequencyAnalysis(teststr)
secret, k = hill_enc(fa2.ciphertext)
print(f"SECRET: \n{secret}\n-------")
print(f"KEY: \n{key}\n---------")
fatest = FrequencyAnalysis(secret)
hcracker = Hill2x2CipherCracker(fatest)
# txt = hcracker.decrypt2txt(key)
txt = hcracker.crack()
print(txt)

# fa3 = FrequencyAnalysis(teststr)
# print(fa3.ciphertext_bigram_frequencies)
# fa1 = FrequencyAnalysis("DNZGHFHMELIMRG")
# # fa1 = FrequencyAnalysis("MRBVEHZP")
# hcracker = Hill2x2CipherCracker(fa1)
# txt = hcracker.decrypt2txt(key)
# print(txt)



