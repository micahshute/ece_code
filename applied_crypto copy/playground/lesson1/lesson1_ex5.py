import hashlib
import binascii

phrase = "it is not the critic who counts".encode('utf-8')

hexdigest = hashlib.sha256(phrase).hexdigest()
digest = hashlib.sha256(phrase).digest()
converted_digest = binascii.a2b_hex(hexdigest)
reconverted_ascii = binascii.b2a_hex(converted_digest)

print(hexdigest)
print(digest)
print(converted_digest)
print(reconverted_ascii)