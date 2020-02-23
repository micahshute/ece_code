from python_resources.frequency_analysis import *
import math

def construct_key(keyphrase):
    alph = [char for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ"]
    seen_letters = set()
    klst = [char for char in FrequencyAnalysis(keyphrase).ciphertext]
    # [seen_letters.add(char) for char in klst]
    fbf = [[[],[],[],[],[]] for _ in range(5) ]
    adds = 0
    ltrsource = klst
    while adds < 25:
        col = adds % 5
        row = math.floor(adds / 5)
        ltr = ltrsource.pop(0)
        if ltr not in seen_letters:
            fbf[row][col] = ltr
            seen_letters.add(ltr)
            adds += 1
        if ltrsource == klst and len(klst) <= 0:
            ltrsource = alph
    return fbf


def key2hash(key):
    keyhash = {}
    for row in range(len(key)):
        for col in range(len(key[row])):
            keyhash[key[row][col]] = (row, col)
    return keyhash

def cipher_line(rc1, rc2, rc):
    return f"{rc[(rc1 + 1) % 5]}{rc[(rc2 + 1) % 5]}"


def cipher_box(r1, c1, r2, c2, k):
    return f"{k[r1][c2]}{k[r2][c1]}"

def cipher_pair(key, kh, wordpair):
    if wordpair[0] == wordpair[1]:
        wordpair = f"{wordpair[0]}X"
    row1, col1 = kh[wordpair[0]]
    row2, col2 = kh[wordpair[1]]
    if row1 == row2:
        return cipher_line(col1, col2, key[row1])
    elif col1 == col2:
        return cipher_line(row1, row2, [row[col1] for row in key])
    else:
        return cipher_box(row1, col1, row2, col2, key)

def cipher(key, phrase):
    kh = key2hash(key)
    res = ""
    for i in range(1, len(phrase), 2):
        res += cipher_pair(key, kh, f"{phrase[i-1]}{phrase[i]}")
    return res

def decipher_pair(key, kh, wordpair):
    row1, col1 = kh[wordpair[0]]
    row2, col2 = kh[wordpair[1]]
    if row1 == row2:
        return cipher_line(col1 - 2, col2 - 2, key[row1])
    elif col1 == col2:
        return cipher_line(row1 - 2, row2 - 2, [row[col1] for row in key])
    else:
        return cipher_box(row1, col1, row2, col2, key)

def decipher(key, phrase):
    kh = key2hash(key)
    res = ""
    for i in range(1, len(phrase), 2):
        res += decipher_pair(key, kh, f"{phrase[i-1]}{phrase[i]}")
    return res


phrase = "It's all about the money"
phrase2 = "playfair example"
key = construct_key(phrase)
# keyhash = key2hash(key)
# print(cipher_pair(key, keyhash, "W"))
ciphertext = cipher(key, "ANDYHOWWOULD")
print(ciphertext)
plaintext = decipher(key, ciphertext)
print(plaintext)



# NHADNEDNOBLEAJDUSTMENTOTFHINGSTHAWTHILETHERIESINFECTINOINDISEASAENDSORROWHTEREISNOTIHNGINTHEWROLDSOIRREISSTIBLYCOTNAGIOUSA
