import random
import urllib2

f=file('quotes.txt','r')
quotes = [l.strip() for l in f]
f.close()
quotes = [w + chr(random.randint(ord('A'),ord('Z'))) if len(w) % 2 == 1 else w for w in quotes]

res = urllib2.urlopen('https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english-usa.txt')
words = res.read().split()

random.shuffle(quotes)
random.shuffle(words)

def substitution(plaintext):
    letters = range(26)
    random.shuffle(letters)
    cipher = plaintext
    for i in range(26):
        pt = chr(65+i)
        cipher = cipher.replace(pt, chr(97+letters[i]))
    return cipher, letters

def shiftEnc(c, n):
    return chr(((ord(c) - ord('A') + n) % 26) + ord('a'))

def vigenere(raw):
    key = [random.randint(1,25) for i in range(random.randint(10,20))]
    secret = "".join([shiftEnc(raw[i], key[i % len(key)]) for i in range(len(raw))])
    return secret, key

def col_trans(plain):
    cols = random.randint(8,10)
    key = range(cols)
    random.shuffle(key)
    return "".join(plain[i::cols].lower() for i in key), key

def playfair_box_shift(i1, i2):
    r1 = i1/5
    r2 = i2/5
    c1 = i1 % 5
    c2 = i2 % 5
    out_r1 = r1
    out_c1 = c2
    out_r2 = r2
    out_c2 = c1
    if r1 == r2:
        out_c1 = (c1 + 1) % 5
        out_c2 = (c2 + 1) % 5
    elif c1 == c2:
        out_r1 = (r1 + 1) % 5
        out_r2 = (r2 + 1) % 5
    return out_r1*5 + out_c1, out_r2*5 + out_c2

def playfair_enc(plain):
    random.shuffle(words)
    seed = "".join(words[:10]).replace('j','i')
    alpha = 'abcdefghiklmnopqrstuvwxyz'
    suffix = "".join( sorted( list( set(alpha) - set(seed) ) ) )
    seed_set = set()
    prefix = ""
    for letter in seed:
        if not letter in seed_set:
            seed_set.add(letter)
            prefix += letter
    key = prefix + suffix
    secret = ""
    for i in range(0,len(plain),2):
        chr1 = plain[i]
        chr2 = plain[i+1]
        if chr1 == chr2:
            chr2 = 'X'
        i1 = key.find(chr1.lower())
        i2 = key.find(chr2.lower())
        ci1, ci2 = playfair_box_shift(i1, i2)
        secret += key[ci1] + key[ci2]
    return secret, key

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
    while not found:
        a,b,c,d = [random.randint(0,25) for i in range(4)]
        det = (a*d - b*c) % 26
        det2 = ((a-1)*d - b*(c-1)) % 26
        if (det % 2 != 0 )and (det % 13 != 0) and (det2 % 26 != 0):
            found = True
    secret = ''
    for i in range(0, len(plain), 2):
        i1 = c2i(plain[i])
        i2 = c2i(plain[i+1])
        c1 = (i1*a + i2*b) % 26
        c2 = (i1*c + i2*d) % 26
        secret += i2c(c1) + i2c(c2)
    return secret, [a,b,c,d]