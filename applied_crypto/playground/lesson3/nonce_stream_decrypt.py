from python_resources.functions import *

key = 61983
msg = "3e08816f1377f89f1c596fc197dd52946c92577bfd7c25c3"
# Given the first 6 bytes of the ciphertext is NONCE, use it to create a new key
nonce = msg[:12]
nkey = nonce_key(nonce, key)
gen = crand(nkey)


#Given first 6 bytes are nonce bytes, remove the first 12 letters of the msg
clear_msg = msg[12:]

res = stream_cipher(gen, clear_msg, decode=True)
print(res)
pmsg = hex2str(res)
print(pmsg)
