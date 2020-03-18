from python_resources.functions import nonce_key
key = 54321
nonce = "cc4304c09aee"

noncekey = nonce_key(nonce, key)
print(noncekey)