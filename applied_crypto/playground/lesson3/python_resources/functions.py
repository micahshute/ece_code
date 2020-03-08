import math
import binascii
import hashlib

def crand(seed):
    r=[]
    r.append(seed)
    for i in range(30):
        r.append((16807*r[-1]) % 2147483647)
        if r[-1] < 0:
            r[-1] += 2147483647
    for i in range(31, 34):
        r.append(r[len(r)-31])
    for i in range(34, 344):
        r.append((r[len(r)-31] + r[len(r)-3]) % 2**32)
    while True:
        next = r[len(r)-31]+r[len(r)-3] % 2**32
        r.append(next)
        yield (next >> 1 if next < 2**32 else (next % 2**32) >> 1)

def retreive_hbytes(num, bytecount):
    hnum = format(num, 'x')
    nums = [hnum[((i+1) * -2) + len(hnum): (i * -2) + len(hnum) ] for i in range(bytecount)]
    return nums

def stream_cipher(gen, msg, *, decode):
    bytes_needed = 0
    if decode:
        bytes_needed = len(msg) / 2
    else:
        bytes_needed = len(msg)
    nums_needed = math.ceil(bytes_needed / 3)
    nums = [next(gen) for _ in range(nums_needed)]
    # print([format(num, 'x')for num in nums])
    hbytes_list = []
    for num in nums:
        bytes = retreive_hbytes(num, 3)
        bytes = [bytes[len(bytes) - 1 - i] for i in range(len(bytes))]
        for byte in bytes:
            if len(hbytes_list) == nums_needed * 3: break
            hbytes_list.append(byte)
    # print(hbytes_list)
    hmsg = ''
    if decode:
        hmsg = int(msg, 16)
    else:
        hmsg = int(binascii.hexlify(msg.encode()), 16)
    hbytes = int("".join(hbytes_list), 16)
    return format(hmsg ^ hbytes, 'x')

def hex2str(hx):
    return bytearray.fromhex(hx).decode()

def digest_to_hex(dig):
    return binascii.unhexlify(dig)

def nonce_key(nonce, key):
    hexnonce = nonce.hex()
    keyhex = format(key, 'x')
    concathex = hexnonce + keyhex
    even_len = concathex.rjust(len(concathex) + len(concathex) % 2, '0')
    hexhash = hashlib.sha256(bytes.fromhex(even_len)).hexdigest()
    return int(hexhash, 16) % 2**32