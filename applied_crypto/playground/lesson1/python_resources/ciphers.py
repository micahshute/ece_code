
def encrypt_cc(key, msg):
    return "".join([chr(65 + (ord(c) - 65 + key) % 26) for c in msg.upper() if ord(c) >= 65 and ord(c) <= 90])


def decrypt_cc(key, msg):
    return encrypt_cc(26 - key, msg)


def bf_decrypt_cc(msg):
    return [ (key, decrypt_cc(key, msg)) for key in range(26) ]

def encrypt_vc(key, msg):
    return "".join([encrypt_cc(key[i % len(key)], char) for i, char in enumerate(msg)])

def decrypt_vc(key, msg):
    return key, encrypt_vc([ 26 - k for k in key], msg)