
def permutations(arr):
    if len(arr) == 0:
        return [[None]]
    if len(arr) == 1:
        return [arr]
    if len(arr) == 2:
        return [arr, [arr[1], arr[0]]]
    all_perms = []
    for num in range(len(arr)):
        res_num = arr[num]
        remaining = arr[0:num] + arr[num+1:]
        nested = permutations(remaining)
        all_perms += [[res_num] + p for p in nested]
    return all_perms

# lam -> return true if first arg > second arg
def max_i_el(arr, lam=lambda a,b: a > b):
    max_i = 0
    max_el = arr[0]
    for i in range(1, len(arr)):
        if(lam(arr[i], max_el)):
            max_i = i
            max_el = arr[i]
    return max_i, max_el

def evenpad(hx):
    return ('0' * (len(hx) % 2)) + hx

def int2hex(num):
    return evenpad(hex(num)[2:])

def hex2int(hx):
    if isinstance(hx, str):
        return int(hx, 16)
    elif(isinstance(hx, bytes)):
        return int(hx.decode(), 16)
    else:
        raise ValueError(f"must be a str or bytes, not a {type(hx)}")

def str2hex(strg):
    return strg.encode().hex()

def hex2str(hx):
    return bytearray.fromhex(hx).decode()

def str2int(string):
    return hex2int(str2hex(string))

def int2str(num):
    return hex2str(int2hex(num))


def to_hex(obj):
    if(isinstance(obj, int)):
        return int2hex(obj)
    elif(isinstance(obj, str)):
        return str2hex(obj)
    elif(isinstance(obj, bytes)):
        return str2hex(obj.hex())
    else:
        raise ValueError('must be an int, str, or bytes')

def to_int(obj):
    if(isinstance(obj, str)):
        return hex2int(obj)
    elif(isinstance(obj, bytes)):
        return hex2int(obj.hex())
    elif(isinstance(obj, int)):
        return obj
    else:
        raise ValueError('must be an int or string')

def to_str(obj):
    if(isinstance(obj, str)):
        return hex2str(obj)
    elif(isinstance(obj, int)):
        return int2str(obj)
    else:
        raise ValueError('must be an int or string')
